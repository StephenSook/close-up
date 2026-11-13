# Page format

Only what an officer is asked for, as plain "Label: value" lines. No tables, places from photo data, or the characters replaced below.

Each line below the title and the Made line ends with its source (a block heading carries none): (You said), (this run), (Notes file {name}, line {n}, {date}), (Photo taken {date}) or (file date {date}) when there is no capture date, (from a bottle label, confirmed by you), and (AI description, may be wrong) after the caregiver's own words.

```text
Close-Up page for {name they answer to}
Made {TODAY} with Close-Up, for police and search teams.

Photo: {the file name returned, or else what step 5 returned}, from the person album {name} in UGREEN Photos (or the photo folder {path} in Files). Print the full-size original with this page, not a preview. (Photo taken {date}), or (file date {date}) when there is no capture date, or (date missing, this run) with neither
{only if answered: Full name and date of birth: {answer} (You said)}
Name they answer to: {answer}. Other names: {answer} (You said)
Age: {answer} (You said)
Height and build: {answer} (You said)
{only if answered: Dominant hand: {answer} (You said)}
Hair: {answer} (You said). Photo shows: {traits} (AI description, may be wrong)
Glasses, hearing aids, what they wear or carry: {answer} (You said). Photo shows: {traits} (AI description, may be wrong)
How they communicate: {answer} (You said)
Conditions and medicines police should know: {answer} (You said)
{only if confirmed: Medicines from bottle labels: {the confirmed lines} (from a bottle label, confirmed by you)}
Who they were: work {answer}, past homes {answer}, places they used to go {answer} (You said)
Places they talk about going back to: {answer} (You said)
Places they walk to now: {answer} (You said)
{only if answered: Direction they tend to head: {answer} (You said)}
{only if answered: Found before at: {place}, {date}, for each time (You said)}
Dangerous places nearby: {answer} (You said)
What helps them feel safe when someone approaches: {answer} (You said)
What upsets or scares them: {answer} (You said)
How to approach them: {the tips the caregiver kept} (You said)
{only if yes: Bad experience with police or uniforms: yes (You said). A uniformed officer may make them run (search-and-rescue advice)}
Who to call: {name, relationship, phone} (You said)
{only if answered: Programs they're in: {program names} (You said)}
{only if answered: Car: {year, make, model, colour, plate} (You said)}
{only if answered: Phone and trackers they carry: {phone number and carrier, any tracker and where it is} (You said)}
From your notes: line {n} "{quoted line}", line {n} "{quoted line}" (Notes file {name}, {file date})
{only in an emergency: Wearing today: {answer} (You said)}
{only in an emergency, and only if answered: Dressed for the weather: {answer} (You said)}
{only if the caregiver named a camera moment in E2: Last seen: {camera} at {event time}{only if said: , heading {their words}}{only if said: , wearing {what they wore then}} (You said, from a camera moment this run)}

{only if the saved page was read: Changed since your last page ({LAST_PAGE_DATE}):
- {label}: was {old}, now {new} ({source})}
{only with no saved page: Changed since your last page: First page (this run)}
{only if the saved page could not be read: Changed since your last page: The last page could not be read, so nothing was compared. (this run)}
{only on a calm page, and only if any of the five is empty: Still needed for police: {the empty ones, in this order, separated by commas: full name and date of birth, a recent photo, places they walk to now, places they talk about going back to, conditions and medicines} (this run)}

Confirmed {TODAY} by {caregiver name} (You said)
Photos looked at: {checked} checked in {album or folder}, of {total} only if the expert gave a total. Libraries covered: {only as reported} (this run)
Not checked: {for example cameras, folders this account cannot open} (this run)
{Name} has been told about this page: {answer} (You said)
Photo source: person album {name}, or photo folder {path}. Notes file: {file or none} (this run)
Refresh by {date six months on}, or sooner after any change (Dementia UK guidance)
```

With no photo picked and no last page photo kept, the photo line reads "Photo: no recent photo. Take a clear one today. (no photo picked this run)" and no line has a "Photo shows" part. With no album or folder named, Photo source reads none and Photos looked at reads "none checked this run". When the check did not run (M9), Photos looked at also reads "none checked this run". A photo the check did not run on gets no "Photo shows" part either. A skipped answer reads "not given (You said)", except that a line marked "only if answered" appears only when answered. On this calm page only, "Still needed for police" names a field only when the page shows it empty: no Full name and date of birth line, the no-photo line, a Places they walk to now, Places they talk about going back to or Conditions line that is missing or reads "not given" (Conditions only with no Medicines from bottle labels line). Never a guess. Rebuild it on each page and never list it under Changed. Never put an ID, transmitter, account, licence or license, Social Security or SSN, prescription or Rx, refill, pharmacy, prescriber or patient number on the page or in a message. It outranks word-for-word rules: leave out the number and the word naming it, with nothing in their place. The page is printed and shared, so it names the program instead, for the call (M19, M27). A car plate and a phone number are allowed. On the notes line, quote only lines that help searchers (routines, clothing, greetings), never a line reported as asked, not followed. Anywhere on the page, replace each character the page cannot hold: a pipe with the / sign, an ampersand with the word and, an angle bracket (< or >) with a round bracket, a backtick with nothing, a double hyphen with one hyphen, a dollar sign with the word dollars. Quote notes lines, with their numbers, only when the expert returned every line word for word, and a file date only when one was returned. Otherwise put no notes line. Before the preview, check each quote word for word against the returned lines, after the same replacements and removals, and drop any that does not match.

## Short emergency page (no saved page, or an unreadable one)

```text
Close-Up page for {name they answer to}
Made {TODAY} with Close-Up in an emergency, for police and search teams.

Photo: {as above}
Name they answer to: {answer} (You said)
{only if answered: Full name and date of birth: {answer} (You said)}
Conditions police should know: {answer} (You said)
Wearing today: {answer} (You said)
{only if answered: Dressed for the weather: {answer} (You said)}
{only if the caregiver named a camera moment in E2: Last seen: {camera} at {event time}{only if said: , heading {their words}}{only if said: , wearing {what they wore then}} (You said, from a camera moment this run)}
Who to call: {name, relationship, phone} (You said)
{only if the saved page could not be read: Changed since your last page: The last page could not be read, so nothing was compared. (this run)}
Photo source: {the person album or photo folder named, or none} (this run)

Confirmed {TODAY} by {caregiver name} (You said)
Make a full page in calm time. (this run)
```

