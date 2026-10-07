# Answer shapes and beats

Interviews go wrong when the candidate invents the structure and recalls the details at the same time. Give every answer a **shape** in advance, and under pressure only the details are left to remember.

## Contents
- Beats: the building block
- The six shapes
- Writing good cue words
- Mining a story from the candidate
- Rules for every answer
- Panic lines
- Worked example

## Beats: the building block

Every spoken answer is a short stack of beats. Each beat has a **kind** (its color in the book), a **label**, a **cue** and a **full sentence**.

| Kind | Color | What it does |
|---|---|---|
| `open` | orange | The answer, in one line. The interviewer knows where you're going before you go there. |
| `build` | blue | Only the context needed to follow. Two sentences at most. |
| `prove` | green | What the candidate did, the evidence, the decisions and why. **Most of the time goes here.** |
| `land` | purple | The result (a number if there is one) and the bridge to this company. |

Markup:

```html
<li class="beat prove"><span class="lab">What I did</span><div>
  <b class="cue">Followed the data past my layer → enrichment rule</b>
  <span class="full">Instead I followed the data past our layer, into the platform's enrichment rules…</span>
</div></li>
```

## The six shapes

Pick the shape the moment the question is asked.

| Shape | Use for | Beats (approximate timing) |
|---|---|---|
| **Story** | "Tell me about a time…", hardest problem, a mistake, a conflict, an improvement | Headline (open, 5s) → Setup (build, 15s) → What I did (prove, 40s) → Result (land, 15s) → Bridge (land, 10s) |
| **Process** | "How do you…", "What would you do if…", scenarios | Principle (open) → Steps (prove) → Real example (build) → Judgment: where you'd stop or hand off (land) |
| **Motivation** | Why this company, why this role, why leaving, why you stayed | Claim (open) → Two reasons, not five (build) → One proving fact (prove) → Bridge to this job (land) |
| **Gap** | Missing skills, "have you done X?", weaknesses | Name it first (open) → Closest evidence (prove) → Plan (build) → End on confidence, not apology (land) |
| **Opinion** | How you use AI, what good looks like, your philosophy | Position (open) → Reason (build) → Example (prove) → What it means for this job (land) |
| **Explain** | "Tell me about yourself", "What do you know about us?", explaining a concept | One-liner (open) → How it works (build) → Why it matters / proof (prove) → Where I fit (land) |

Put the shape in the card's chip: `Say · Story`, `Frame · Gap`, and so on.

## Writing good cue words

The cue is what the candidate reads mid-sentence, so it has to work at a glance.

- **3–8 words.** Fragments are fine. Arrows are fine: "Followed the data → wrong enrichment rule".
- **Content, not instructions.** "Three tools stuck in the backlog for years", not "Talk about the tools".
- **Distinctive.** Each cue should trigger one memory. Names, numbers and odd details work best: "Friday Python bump broke PDF parsing".
- **The full sentence is for practice.** Write it in the candidate's voice, plain and spoken. No buzzwords.

## Mining a story from the candidate

Resumes say what happened; stories need the details that make them believable. For each story, ask the candidate a short batch of questions:

- What was the situation, in one sentence? What made it hard or unusual?
- What exactly did *you* do (not the team)? What did you try first, and what did you rule out?
- How did it end? Any number: time to fix, how many affected, before and after?
- Who else was involved, and how did you work with them?
- What changed afterward so it didn't happen again?

Anything still unknown becomes a highlighted gap in the book: `<span class="fill">[how long the fix took]</span>`. Never fill it with something plausible. A gap is honest; a guess is a liability under follow-up.

When two of the candidate's sources tell a story differently (an old prep doc and a new message), ask which version is true rather than merging them. Until they answer, mark the uncertain beats optional:

```html
<li class="beat prove opt"> … <b class="cue">…</b><span class="optag">optional · confirm</span> …</li>
```

## Rules for every answer

- **First sentence answers the question.**
- **"I", not "we",** for the parts the candidate did. Credit others by name.
- **Land it, then stop.** Silence after a good answer is fine.
- **Three depths per story:** 30 seconds (headline only), 90 seconds (the default), 5 minutes (only if they keep pulling).
- **End on the company.** The bridge beat ties the story to this role in one sentence.
- **Lead with the problem, not the build.** Especially for builder-types: what was costing people time, then what you did about it.

## Panic lines

These live in the book's "Under pressure" panel. Keep them as they are.

| Situation | Line |
|---|---|
| You blank | "Let me pick the best example for that. Give me a second." |
| You're rambling | "The short version is…" Then the headline, and stop. |
| You don't know | "I haven't done that exactly. The closest thing I've done is…" |
| Question is fuzzy | "Do you mean the technical side, or how I handled the people?" |
| You lost the thread | "I went a bit wide. Did that answer what you were asking?" |

## Worked example (Story shape)

From the example book (`examples/example-book.html`). The candidate is fictional.

Question: *"Tell me about a tricky issue you took to the root cause."*

| Beat | Cue | Full sentence |
|---|---|---|
| open · Headline | Shipments "delivered" before pickup | One carrier's shipments started showing as delivered before they'd been picked up. |
| build · Setup | Messages valid; billing on hold | Every message passed validation, nothing in our parser had changed, and billing had frozen 140 loads because the timeline made no sense. |
| prove · What I did | Lined up raw timestamps → offset missing | I lined up the raw messages against our parsed events and saw the carrier had dropped the time zone offset after an upgrade. We were reading Pacific times as UTC. |
| prove · The choice | Patched them, then guarded everyone | I patched that carrier's mapping the same day, then added a check that flags any carrier whose events arrive out of order. |
| land · Result | Billing unfrozen same day; check caught 2 more | Billing released the loads that afternoon, and the check caught two other carriers with the same problem within a quarter. |
| land · Bridge | What changed isn't always what broke | Nothing on our side had changed. The seam had. That's the first question I'd ask on a broken integration here. |

Notice: the story is specific (140 loads, a six-hour offset, two more carriers), the "I" is clear, the fix covers everyone and not just one customer, and the bridge turns a past story into a skill for this job.
