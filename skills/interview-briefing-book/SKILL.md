---
name: interview-briefing-book
description: Build an interview briefing book, a single self-contained HTML page that prepares a candidate for one specific early-stage interview conversation (recruiter screen, hiring-manager intro, first Zoom or phone call) and stays open as a glanceable reference during the call. It holds a talk track, prepared answers in scannable beats, honest framing for gaps, questions to ask with sources, a company brief, and a pre-call checklist. Use this skill whenever someone has an upcoming interview or intro call and shares a job posting, a recruiter or hiring-manager message, a resume, or asks for help prepping talking points, a cheat sheet, a "battle plan", call notes, or what to say on the call, even if they don't say "briefing book". Not for live coding rounds, take-home assignments, or running mock-interview practice sessions.
---

# Interview briefing book

An interview briefing book is one HTML page built for **one specific interview conversation** and meant to be **kept open during it**. Think of the briefing book political staff prepare before a debate: the message to land, prepared answers, known weak spots and how to handle them, and questions to ask back, organized so anything can be found in seconds while the call is live.

The reader will be nervous. Their heart may be racing and they'll have a few seconds to glance between sentences. Every design decision in this skill follows from that: short bold cue words instead of paragraphs, a clickable index, a "Cues only" mode, and only material they'd actually use in that call.

Full definition (what it contains, what it isn't): `references/definition.md`.

## Scope

- **One book per conversation.** A recruiter screen and a hiring-manager call at the same company test different things, so they get different books.
- **Early conversational stages:** recruiter screens, hiring-manager intros, "get to know you" video calls, founder chats. For skills assessments (live coding, system design, take-homes), say this skill isn't built for that and offer only the conversational parts.
- **Prep notes, not live AI help.** The book is the candidate's own prepared notes. If the candidate seems to want an AI answering for them during the call, say plainly that this isn't that, and that some companies prohibit AI assistance in interviews.

## Workflow

### 1. Intake: gather what exists, ask only for what matters

Start from whatever the candidate already gave you. Look for:

- **The posting** (text or URL) and **the message that set up the call** (recruiter or interviewer note, scheduling email). The message often says what caught their eye; that's gold.
- **The candidate's resume or background**, and any **earlier prep notes or briefing books**. Earlier books often hold better-tested stories than a fresh draft. Reuse the best parts.
- **The call itself:** who (name, role), when (with time zone), how long, what format, which stage.
- **Constraints:** location or on-site requirements, comp band if posted, visa, start date.

Ask the candidate only for what you can't find or infer, in one batch, and then get started. Don't hold the whole book hostage to a missing detail; mark it as a gap and keep going.

### 2. Research the company and the role

Read `references/research.md` before researching. In short:

- **Primary sources first:** official docs, changelog or release notes, the company blog, the careers page, funding announcements. Use whatever web tools your harness has.
- **Record the source of every fact the candidate might say out loud:** source type (docs, blog, changelog, press, the candidate's own test), URL, and the date you checked. Candidates get asked "where did you read that?", and "a blog post" is a weaker answer than "your docs". When a blog and the docs disagree, the docs win, and the disagreement itself may make a good question.
- **Hands-on beats reading.** If the product has a free tier, a public API or a demo, suggest one or two cheap, safe checks the candidate can run (or you can run with their permission). A first-hand observation makes the strongest question in the book.
- **Mark company claims** ("1M users", "fastest") as company-stated.

### 3. Mine the candidate's real stories

The book is only as good as the true stories in it. Read `references/answer-shapes.md`, then:

- Map each stated requirement in the posting to concrete evidence from the candidate's history.
- Pick 4–7 stories that cover the likely questions. For each one, **ask the candidate for the details that make it land**: numbers, durations, who was involved, what happened afterward. A story with "fixed in three hours, no other customers affected" beats "it got fixed."
- **Never invent experience, numbers or outcomes.** Anything you don't know goes in a highlighted gap: `<span class="fill">[how long it took]</span>`. Plausible fiction is worse than a gap. The candidate can't defend it under follow-up, and it's dishonest.
- When the candidate supplies a detail later, update the story and remove the gap.

### 4. Build the book from the template

Copy `assets/template.html` and fill it in. Keep its CSS and script untouched; they provide the tabs, the auto-built index, Cues only mode, the saved checklist and copy buttons. `examples/example-book.html` shows a complete book for a fictional candidate. Look at it before writing to calibrate tone, density and markup.

The tabs, in order:

| Tab | What goes in it |
|---|---|
| **Battle plan** | Under pressure panel (keep as-is), anything to settle first (on-site, visa), the 30-second intro, the one idea to land, proof → their asks, gaps named honestly, questions to ask, traps, comp, close |
| **Call drills** | Story bank (likely behavioral and scenario questions), the awkward ones (why leaving, gaps, title mismatches) |
| **What they want** | What this call is screening for, each labeled stated / likely / guess, plus "Why us?" |
| **Domain primer** | Rename for the role: Ticket map (support), Product primer (PM), Customer problems (sales/CS), Glossary (new domain). The problems their customers hit, from public docs, with the candidate's angle on each |
| **Company** | One-liner, numbers (company-stated marked), funding and people, values in their words, sources |
| **Before the call** | Any reply that must go out first, homework in order, day-of steps |

How to write the content:

- **Every spoken answer is beats, not a paragraph.** Each beat has a bold cue (3–8 words, readable at a glance) and the full sentence underneath. Beat kinds: **Open** (the answer in one line), **Build** (context, two sentences max), **Prove** (what the candidate did; most of the time goes here), **Land** (the result, tied to this company). Shapes and examples are in `references/answer-shapes.md`.
- **Under 90 seconds per answer.** Answer, one concrete example, what changed afterward, stop.
- **Specific to this interview.** If a card would make sense for any company, cut it or make it specific. Generic interview advice doesn't belong.
- **Index what they'll hunt for.** Add `data-q="Short label"` to every question, story and gap card. The index builds itself.
- **Every Ask card has a source line**, and so does any technical fact that could change. Mark technical details "verify" when they come from docs that move.
- **Card kinds:** `say` (use with confidence), `frame` (a weak spot, framed honestly), `ask` (a question for them), `avoid` (a trap).

### 5. Review pass

Before handing it over, run `references/quality-checklist.md`. The checks that matter most: no invented facts about the candidate, no leftover `{{placeholders}}`, every Ask card sourced, every spoken answer in beats, and nothing generic.

### 6. Deliver

- Save one `.html` file with a clear name (e.g. `acme-hiring-manager-briefing-book.html`). It works offline and needs no install.
- **Keep it private by default.** It contains the candidate's history, comp expectations and sometimes contact details. Don't publish it to a public URL unless the candidate asks. Mask any secrets (API keys, tokens) that turn up while researching or testing.
- Tell the candidate in three lines how to use it: practice from the full sentences, switch on **Cues only** for the call, and use the **Jump to** index or the **↑ Index** button to find answers.
- List the highlighted gaps they still need to fill.

### 7. After the call

Offer to help with:

- **A short thank-you** that mentions one specific thing the interviewer said. If the candidate said something wrong on the call (a misremembered source or number), a brief, confident correction in the thank-you turns a slip into a strength.
- **Updating the book** with what was learned (questions asked, concerns raised) and **carrying the best material into the next stage's book**.

## Reference files

| File | Read it when |
|---|---|
| `references/definition.md` | You need the full spec of what a briefing book is and isn't |
| `references/research.md` | Before researching the company (source hierarchy, hands-on checks, citing) |
| `references/answer-shapes.md` | Before writing any spoken answer (shapes, beats, examples, panic lines) |
| `references/quality-checklist.md` | Before delivering the book |
| `assets/template.html` | When building the book (copy it) |
| `examples/example-book.html` | To see a finished book for a fictional candidate |
