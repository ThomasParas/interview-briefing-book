# Quality checklist

Run this before handing the book over. Fix what fails; don't just report it.

## Truth

- [ ] **Source check done:** every first-person sentence and cue points to a resume line, a message, an intake answer or the profile. Anything else was cut, made a highlighted gap, or reframed as an approach ("Here's how I'd handle it").
- [ ] No habit or self-assessment claims the candidate didn't make ("day to day", "the thing I do best"), and no inflated scope ("my whole department").
- [ ] Every claim about the candidate comes from their resume, their messages, or their answers to you. Nothing invented: no made-up numbers, durations, outcomes, tools or titles.
- [ ] **No invented motivations or reasons.** Reread every first-person line that says why: "because…", "I was tired of…", "what I loved…", "so that…", "I wanted…". Each one comes from the candidate, or it's a highlighted prompt for their real reason.
- [ ] Every unknown the candidate must supply is a highlighted `<span class="fill">[…]</span>` gap, not plausible filler.
- [ ] Conflicting versions of a story are resolved with the candidate, or the uncertain beats are marked `opt`.
- [ ] Company claims (user counts, "fastest", growth) are marked company-stated.
- [ ] At least three questions to ask are grounded in something specific and cite it in a `<p class="src">` line (source type, URL, date checked). Standard questions have no source line.
- [ ] Every technical fact that could change has a source line.
- [ ] Where a blog and the docs disagree, the book says so and favors the docs.

## Usable under stress

- [ ] Every spoken answer is in beats with bold cues of 3–8 words. No answer is a paragraph.
- [ ] Every likely question, story and gap card has `data-q="…"` so it appears in the index.
- [ ] Each answer fits in about 90 seconds at the default depth.
- [ ] The Under pressure panel is intact.
- [ ] Nothing important is buried in a note. Notes are prep guidance; they hide in Cues only mode.

## Specific to this interview

- [ ] The 30-second intro ends pointing at this role.
- [ ] Every story has a Bridge beat tied to this company.
- [ ] Gaps that the posting or the candidate's background make obvious are named on Frame cards before the interviewer raises them.
- [ ] Questions to ask are grounded in something specific (a doc, a launch, a hands-on test), not generic ("What's the culture like?").
- [ ] Generic interview advice that would fit any company has been cut or made specific.

## Technical

- [ ] No `{{PLACEHOLDER}}` text or `REPLACE` comments left. Search the file for `{{` before delivering.
- [ ] `data-book-id` on `<body>` is a unique slug.
- [ ] The template's CSS and `<script>` are unchanged.
- [ ] The file opens offline in a browser with no console errors (if you can check).
- [ ] No secrets (API keys, tokens, passwords) anywhere in the file.

## Handoff message

- [ ] Where the file is.
- [ ] How to use it: practice from the full sentences, switch on Cues only for the call, use the index.
- [ ] The list of highlighted gaps the candidate still needs to fill.
- [ ] Anything to do before the call (a reply to send, a hands-on check to run).
