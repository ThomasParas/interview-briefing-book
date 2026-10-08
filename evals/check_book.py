"""Programmatic checks for an interview briefing book run.

Usage: python3 evals/check_book.py <run_dir> <eval_name>
Reads <run_dir>/outputs/, writes <run_dir>/grading.json (fields: text, passed, evidence).
The "no invented candidate facts" check needs human/LLM judgment and is merged in separately.
"""
import glob, json, os, re, sys

run_dir, eval_name = sys.argv[1], sys.argv[2]
out = os.path.join(run_dir, "outputs")
htmls = [p for p in glob.glob(os.path.join(out, "*.html"))]
html = open(htmls[0], encoding="utf-8").read() if htmls else ""
text = re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S))
if not html:  # no HTML book: judge content checks on the main Markdown prep doc instead
    mds = [p for p in glob.glob(os.path.join(out, "*.md")) if os.path.basename(p) not in ("handoff.md", "questions_for_candidate.md")]
    text = " ".join(open(p, encoding="utf-8").read() for p in mds)
low = text.lower()
results = []


def check(name, passed, evidence):
    results.append({"text": name, "passed": bool(passed), "evidence": evidence})


check("Produces exactly one self-contained HTML book",
      len(htmls) == 1 and "<script src=" not in html,
      f"{len(htmls)} .html file(s): {[os.path.basename(h) for h in htmls]}")
check("No leftover template placeholders",
      bool(html) and "{{" not in html,
      f"'{{{{' occurrences: {html.count('{{')}" if html else "no html")
beats = len(re.findall(r'class="beat (open|build|prove|land)', html))
cues = html.count('class="cue"')
check("Spoken answers are in beats with bold cues (>= 15 beats)",
      beats >= 15 and cues >= beats * 0.9, f"{beats} beats, {cues} cue elements")
check("Has Cues only toggle and auto index",
      'id="cueBtn"' in html and "body.cues" in html and 'data-auto' in html,
      f"cueBtn={'id=\"cueBtn\"' in html}, cues css={'body.cues' in html}, auto index={'data-auto' in html}")
asks = re.findall(r'<div class="card ask".*?</div>\s*(?=<div class="card|<h2|</section)', html, flags=re.S)
sourced = [a for a in asks if 'class="src"' in a and "http" in a]
check("At least 3 questions to ask are grounded in a cited source URL",
      len(sourced) >= 3, f"{len(sourced)} of {len(asks)} ask cards have a source line with a URL")
fills = html.count('class="fill"')
check("Unknown candidate details are marked as highlighted gaps",
      fills >= 1, f"{fills} highlighted gap(s)")
qf = os.path.join(out, "questions_for_candidate.md")
qtext = open(qf).read() if os.path.exists(qf) else ""
nq = len(re.findall(r"^\s*(?:[-*]|\d+[.)])\s+", qtext, flags=re.M))
check("Writes down questions for the candidate (>= 3)", nq >= 3, f"{nq} list items in questions_for_candidate.md" if qtext else "file missing")

if eval_name.startswith("support-engineer"):
    check("Settles the US-Eastern overlap requirement",
          "overlap" in low or "eastern" in low, "found" if ("overlap" in low or "eastern" in low) else "no mention of overlap/Eastern")
    frames = re.findall(r'<div class="card frame".*?</ol>', html, flags=re.S)
    ts = any("typescript" in f.lower() for f in frames)
    check("Frames the TypeScript gap honestly on a Frame card", ts, "Frame card mentions TypeScript" if ts else "no Frame card mentions TypeScript")
elif eval_name.startswith("cx-engineer"):
    used = bool(re.search(r"2\s?am|2\s?a\.m\.|paged", low)) and "60-day" in low or ("60 day" in low and "paged" in low)
    check("Uses the profile's real motivations and outcomes", used, "found 2am/paged and 60-day" if used else "missing 2am/paged or 60-day")
    frames = re.findall(r'<div class="card frame".*?</ol>', html, flags=re.S)
    gq = any("graphql" in f.lower() for f in frames)
    check("Frames the GraphQL gap on a Frame card", gq, "found" if gq else "no Frame card mentions GraphQL")
    check("Needs clearly fewer gaps when a profile exists (< 30; no-profile books had 35-46)", fills < 30, f"{fills} highlighted gaps")
    sal = bool(re.search(r"previous salary|current salary|last salary|salary history", low)) and not re.search(r"(never|don.t|do not|avoid)[^.]{0,60}(previous|current|last) salary", low)
    check("Never mentions previous salary", not sal, "no previous-salary disclosure" if not sal else "mentions previous salary")
else:
    frames = re.findall(r'<div class="card frame".*?</ol>', html, flags=re.S)
    cc = any(re.search(r"teach|classroom|career change|career-change|switch", f, re.I) for f in frames)
    check("Frames the career change honestly on a Frame card", cc, "found" if cc else "no Frame card about the career change")
    rs = "recruiter" in low
    check("Scoped to a recruiter screen", rs, "mentions recruiter" if rs else "no mention of recruiter")

json.dump({"expectations": results,
           "summary": {"passed": sum(r["passed"] for r in results), "total": len(results)}},
          open(os.path.join(run_dir, "grading.json"), "w"), indent=2)
print(f"{eval_name}: {sum(r['passed'] for r in results)}/{len(results)} passed")
