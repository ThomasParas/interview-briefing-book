# Interview Briefing Book

An Agent Skill that turns a job posting, a recruiter message and your background into an **interview briefing book**: a single HTML page that prepares you for **one specific interview conversation** and stays open while you're on the call.

Interview prep usually ends up as a wall of notes. When the call starts and your heart is racing, you can't read paragraphs. A briefing book is built for that moment:

- **Answers in beats, not paragraphs.** Each answer is a short stack of color-coded beats (Open → Build → Prove → Land), each with 3–8 bold cue words you can read at a glance.
- **Cues only mode.** One click hides everything except the cue words.
- **A clickable index on every tab**, built automatically, plus an "↑ Index" button.
- **An "Under pressure" panel** with lines for when you blank, ramble or don't know.
- **Honest by design.** It never invents your experience. Anything it doesn't know becomes a highlighted gap for you to fill.
- **Sourced.** Every question you might ask and every technical fact carries its source and the date it was checked, so you can answer "where did you read that?"

See [`examples/example-book.html`](skills/interview-briefing-book/examples/example-book.html) for a complete book for a fictional candidate (download it and open it in a browser).

## What's in a book

| Tab | Contents |
|---|---|
| **Battle plan** | Your 30-second intro, the one idea to land, your proof mapped to their requirements, gaps named before they ask, questions to ask (with sources), traps, comp, close |
| **Call drills** | Likely behavioral and scenario questions as stories in beats, plus the awkward ones (layoffs, gaps, title mismatches) |
| **What they want** | What this call is screening for, each item labeled stated, likely or guess |
| **Domain primer** | The problems their customers hit, from public docs, with your angle on each (named for the role: ticket map, product primer, glossary…) |
| **Company** | What they do, numbers (company claims marked), funding, people, values, sources |
| **Before the call** | Any reply to send first, homework in order, day-of steps (checklist saves in your browser) |

It's built for **early conversational stages**: recruiter screens, hiring-manager intros, first video calls, founder chats. It isn't for live coding, system design or take-homes.

## Install

The skill is the folder [`skills/interview-briefing-book/`](skills/interview-briefing-book). It follows the Agent Skills format (a folder with a `SKILL.md`), so any harness that supports skills can use it. Copy or symlink that folder into your harness's skills directory.

**Claude Code** (personal skills, available in every project):

```bash
git clone https://github.com/ThomasParas/interview-briefing-book.git
mkdir -p ~/.claude/skills
cp -r interview-briefing-book/skills/interview-briefing-book ~/.claude/skills/
```

**Other harnesses:** copy `skills/interview-briefing-book/` wherever your tool loads skills from. Check its docs for the location.

**Claude.ai:** zip the `interview-briefing-book` folder and upload it as a skill in your settings.

## Use

Give your agent what you have and ask for a briefing book:

> I have a 30-minute Zoom with the hiring manager at Acme on Thursday for their Solutions Engineer role. Here's the posting, the recruiter's email and my resume. Can you build me a briefing book?

The agent will ask you a short batch of questions first: why you're looking, why this company, and the details of your best stories. Those are exactly what interviewers probe, and only you know them. Then it researches the company, builds the page, and asks about any gaps left. Then:

1. **Before the call:** practice out loud from the full sentences. Fill the highlighted gaps.
2. **During the call:** turn on **Cues only** and use the **Jump to** index.
3. **After the call:** ask the agent for a thank-you note, and to update the book for the next round.

### Reuse your material across interviews

The skill can keep a **`candidate-profile.md`**: your verified facts, stories and real motivations, in your own words. It reads it at the start of every new book and offers to update it as you answer questions, so your second interview starts from tested material instead of from zero. A suggested private folder layout:

```
interview-prep/                 ← private, never a public repo
  candidate-profile.md          ← reused across interviews
  resume.pdf
  acme-hiring-manager/          ← one folder per conversation
    posting.md  messages.md  notes.md
    acme-hiring-manager-briefing-book.html
```

Books and profiles contain your history and comp expectations, so they're private by default. Keep them that way.

## A note on fairness

This is a tool for **preparing your own notes**, the same as a page of talking points. It isn't live AI assistance during the interview. Some companies don't allow AI help during interviews; check the company's rules.

## How it compares

Several good projects focus on **coaching** (mock interviews, answer scoring, story banks across a whole job search), for example [interview-coach-skill](https://github.com/noamseg/interview-coach-skill), [ai-job-search](https://github.com/MadsLorentzen/ai-job-search) and [career-ops](https://github.com/career-ops-hq/career-ops). This skill does one narrower thing: the page you keep open during one specific call. They work well together: practice with a coach, keep a briefing book open on the call.

## Repository layout

```
skills/interview-briefing-book/
  SKILL.md                       workflow and rules the agent follows
  references/definition.md       what a briefing book is and isn't
  references/intake.md           the must-ask questions, the candidate profile, folder layout
  references/research.md         source hierarchy, hands-on checks, citing
  references/answer-shapes.md    the six answer shapes and how beats work
  references/quality-checklist.md  the review pass before delivery
  assets/template.html           the page shell: styles, tabs, index, Cues only
  assets/candidate-profile-template.md  a starting point for your reusable profile
  examples/example-book.html     a finished book for a fictional candidate
```

## License

MIT. See [LICENSE](LICENSE).
