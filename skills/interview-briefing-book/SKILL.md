---
name: interview-briefing-book
description: Prepares someone for an upcoming job interview conversation, like a recruiter or phone screen, a hiring-manager intro, a first Zoom or video call, or a founder chat. It builds an interview briefing book, one self-contained HTML page to keep open during the call, with a 30-second intro, their real stories in glanceable beats, honest framing for gaps and career changes, sourced questions to ask and a company brief. Use this whenever someone mentions an interview, screen or intro call coming up and wants help preparing, knowing what to say, talking points, a cheat sheet, a prep doc or a "battle plan", especially if they share a job posting, a recruiter message, a resume or a candidate-profile.md, even if they never say "briefing book". Load it before asking for materials or reading their files, because its intake step says what to look for and what to ask. Not for coding or system-design rounds, take-home assignments, mock-interview practice, resume rewriting, offer negotiation, or interviewing other people.
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

### 1. Intake: gather real material before drafting

The most common failure in a briefing book is the agent filling silence with plausible reasons and story details. Intake fixes the cause: real material from the candidate. Read `references/intake.md`. In short:

- **Look before you ask.** Gather what already exists: the posting, the message that set up the call (it often says what caught their eye; that's gold), the resume, earlier prep notes or briefing books, and **`candidate-profile.md`** if there is one. A profile holds the candidate's verified stories and real motivations from earlier interviews, so it's the best raw material available. Confirm anything older than about three months.
- **Ask the must-ask batch**, in one message, skipping anything already answered: the call details, **why they're looking, why this company**, two or three stories with what *they* did, how it ended and why they did it that way, constraints (location, visa, comp floor), and what they're worried about. These are precisely the things agents otherwise make up.
- **Don't block on it.** Research while you wait if you can. If the candidate wants to skip intake, build with highlighted gaps and put the questions in the handoff. Skipping intake means more gaps, never more fiction.

### 2. Research the company and the role

Read `references/research.md` before researching. In short:

- **Primary sources first:** official docs, changelog or release notes, the company blog, the careers page, funding announcements. Use whatever web tools your harness has.
- **Record the source of every fact the candidate might say out loud:** source type (docs, blog, changelog, press, the candidate's own test), URL, and the date you checked. Candidates get asked "where did you read that?", and "a blog post" is a weaker answer than "your docs". When a blog and the docs disagree, the docs win, and the disagreement itself may make a good question.
- **Hands-on beats reading.** If the product has a free tier, a public API or a demo, suggest one or two cheap, safe checks the candidate can run (or you can run with their permission). A first-hand observation makes the strongest question in the book.
- **Mark company claims** ("1M users", "fastest") as company-stated, and **take funding and other fast-moving facts from the company's own newsroom or blog**, not search summaries, which often lag by a round or two.

### 3. Mine the candidate's real stories

The book is only as good as the true stories in it. Read `references/answer-shapes.md`, then:

- Map each stated requirement in the posting to concrete evidence from the candidate's history.
- Pick 4–7 stories that cover the likely questions. For each one, **ask the candidate for the details that make it land**: numbers, durations, who was involved, what happened afterward. A story with "fixed in three hours, no other customers affected" beats "it got fixed."
- **Never invent anything about the candidate.** That covers experience, numbers and outcomes, and just as much **motivations, reasons, feelings and the "why" behind a story**: why they built something, why they're leaving, what they loved, what they were tired of, who their customers were. Those are exactly what interviewers probe ("What made you build that?"), and a reason the candidate didn't give is one they can't defend. It's the easiest thing to invent by accident, because it makes a script flow.
  - Anything you don't know goes in a highlighted gap, written as a prompt: `<span class="fill">[why you built it, in your words]</span>`. Plausible fiction is worse than a gap.
  - If a suggestion would help, put it in the card's note as options for the candidate to choose from ("Possible reasons, pick the true one: …"), never in the spoken sentence.
  - A note saying "say only if true" doesn't make an invented sentence OK. If the line is in the script, it reads as fact under pressure.
- After drafting, ask **targeted questions about the remaining gaps**, quoting the beat each one belongs to, most important first. When the candidate supplies a detail, update the story and remove the gap.

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
- **At least three questions to ask are grounded in something specific** (their docs, changelog, release notes, a launch post, the posting's own wording, or a hands-on test) **and cite it** in a source line. Grounded questions are what make a candidate memorable, so even with thin inputs, go find the material: release notes and help-center pages almost always exist. Standard questions (next steps, what great looks like at six months) need no source line; leave it off rather than writing filler.
- **Technical facts that could change carry a source line** and are marked "verify" when they come from docs that move.
- **Card kinds:** `say` (use with confidence), `frame` (a weak spot, framed honestly), `ask` (a question for them), `avoid` (a trap).

### 5. Review pass: the source check first

Drafting drifts. A script reads better with a reason or a habit in it, so they creep in even when you know the rule. Catch them with a **source check** before anything else:

- Go through **every first-person sentence and cue** in the book ("I…", "my…", "what drew me…"). For each one, name its source: a resume line, a message, the candidate's intake answer, or the profile.
- Anything without a source gets one of three treatments: **cut it**, **turn it into a highlighted gap** written as a prompt, or **reframe it as an approach** rather than a claim about the past ("Here's how I'd handle that: …" instead of "I always…").
- Watch especially for habits and self-assessments ("I do this day to day", "the thing I do best"), feelings and reasons ("what I loved", "because I wanted"), and inflated scope ("my whole department" when the resume says "the department").

Then run the rest of `references/quality-checklist.md`: no leftover `{{placeholders}}`, at least three grounded questions, every spoken answer in beats, nothing generic.

### 6. Deliver

- Save one `.html` file with a clear name (e.g. `acme-hiring-manager-briefing-book.html`). It works offline and needs no install.
- **Keep it private by default.** It contains the candidate's history, comp expectations and sometimes contact details. Don't publish it to a public URL unless the candidate asks. Mask any secrets (API keys, tokens) that turn up while researching or testing.
- Tell the candidate in three lines how to use it: practice from the full sentences, switch on **Cues only** for the call, and use the **Jump to** index or the **↑ Index** button to find answers.
- List the highlighted gaps they still need to fill, as targeted questions.
- **Offer to save new material to `candidate-profile.md`** (start from `assets/candidate-profile-template.md` if there isn't one): only what the candidate actually said, dated. Ask before writing personal data to disk. The next book then starts from verified material instead of from zero.
- If the candidate has no prep folder, offer the layout in `references/intake.md`, in a private location they choose.

### 7. After the call

Offer to help with:

- **A short thank-you** that mentions one specific thing the interviewer said. If the candidate said something wrong on the call (a misremembered source or number), a brief, confident correction in the thank-you turns a slip into a strength.
- **Updating the book** with what was learned (questions asked, concerns raised), **saving new facts to the profile**, and **carrying the best material into the next stage's book**.

## Reference files

| File | Read it when |
|---|---|
| `references/definition.md` | You need the full spec of what a briefing book is and isn't |
| `references/intake.md` | At the start: what to look for, the must-ask questions, the candidate profile, folder layout |
| `references/research.md` | Before researching the company (source hierarchy, hands-on checks, citing) |
| `references/answer-shapes.md` | Before writing any spoken answer (shapes, beats, examples, panic lines) |
| `references/quality-checklist.md` | Before delivering the book |
| `assets/template.html` | When building the book (copy it) |
| `assets/candidate-profile-template.md` | When starting a candidate's reusable profile |
| `examples/example-book.html` | To see a finished book for a fictional candidate |
