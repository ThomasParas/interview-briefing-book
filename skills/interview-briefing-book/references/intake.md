# Intake: gathering real material before drafting

A briefing book is only as honest as its raw material. When the agent lacks the candidate's real reasons and story details, it fills the silence with plausible ones, and those are exactly what interviewers probe ("What made you build that?"). Intake prevents that. It takes the candidate 5–10 minutes and saves them from defending sentences that aren't theirs.

## Contents
- Order of operations
- Look before you ask
- The must-ask batch
- After the draft: targeted gap questions
- The skip path
- The candidate profile
- Folder layout

## Order of operations

1. **Look** at everything already available: messages, attachments, the working folder, and a `candidate-profile.md` if one exists.
2. **Ask the must-ask batch**, skipping anything already answered. One message, numbered, so the candidate can reply inline.
3. **Research and draft** while waiting if your harness allows it. Otherwise draft once they reply.
4. **Ask targeted gap questions** about whatever is still highlighted in the draft.
5. **Save what you learned** to the candidate profile (with their permission) so the next book starts from it.

## Look before you ask

Don't ask for anything you can find. Check:

- The chat and any attached files (resume, posting, recruiter or interviewer message, earlier prep notes).
- The working folder, if your harness has file access, especially `candidate-profile.md`, earlier `*-briefing-book.html` files and notes folders. Earlier books often hold better-tested stories than a fresh draft.
- Public pages the candidate pointed to (their portfolio, GitHub, a project site).

If you find a profile, use it, and **confirm anything older than about three months** ("Your profile says you're leaving because of X. Still true?").

## The must-ask batch

These are the questions agents otherwise answer for the candidate. Ask only what's missing, and keep it to one message of about 6–10 questions. Adapt the wording to the person.

**About this call**
1. Who is it with (name, role), when (with time zone), and how long? Video or phone?
2. Did the interviewer or recruiter ask you anything in advance, or say what caught their eye?

**Your real reasons** (the most important part: these get probed, and only you know them)
3. Why are you looking right now? One or two honest sentences; I'll help with the framing.
4. Why this company and this role, in your own words? What would make you excited to take it?

**Your best stories** (pick two or three things you're proud of)
5. For each one: what was the situation, what did *you* do (not the team), and how did it end? Any number helps: time saved, how many people affected, before and after.
6. Why did you do it that way, or why did you start it at all?

**Constraints**
7. Anything to settle on the call: location, on-site days, visa, start date, notice period?
8. Your comp floor, if you want help framing that conversation (optional; it stays in your private book).

**Gaps**
9. Is there anything in your background you're worried they'll ask about?

If the candidate gives short answers, that's fine. Use exactly what they said and highlight the rest.

## After the draft: targeted gap questions

Once the draft exists, the remaining highlighted gaps show precisely what's missing. Ask about them directly, quoting the beat, for example:

> In the "time-traveling shipments" story, the Result beat says "[how many loads were affected]". Do you remember roughly?

Group these into one message, most important first (anything in the 30-second intro or the first story beats a minor detail). When the candidate answers, update the beats and remove the highlights.

## The skip path

If the candidate says "just build it", or there's no time, build the book with highlighted gaps and put the must-ask questions in the handoff message. Never treat "skip intake" as permission to invent. It means more gaps, not more fiction.

## The candidate profile

`candidate-profile.md` is a plain Markdown file the candidate owns, holding **verified** material in their own words: facts, stories with details, and real motivations. Start it from `assets/candidate-profile-template.md`.

- **Read it at the start** of every new book. It's the best raw material available.
- **Offer to update it** when the candidate gives you new facts or story details. Don't silently write personal data to disk; ask once ("Want me to save these to your profile for next time?").
- **Only write what the candidate said.** The profile is a source of truth for future books, so anything inferred would compound. Mark anything uncertain `(unconfirmed)`.
- **Date each section** (`updated: YYYY-MM-DD`) so staleness is visible.
- **Keep it private.** It's personal data. Never commit it to a public repository.

## Folder layout

A suggested convention. It still works fine if everything arrives in chat.

```
interview-prep/                     ← private, never a public repo
  candidate-profile.md              ← reused across interviews
  resume.pdf
  acme-hiring-manager/              ← one folder per conversation
    posting.md
    messages.md                     ← recruiter or interviewer messages
    notes.md                        ← your notes, after-call debrief
    acme-hiring-manager-briefing-book.html
```

If the candidate has no folder, offer to create this structure in a location they choose. Don't assume.
