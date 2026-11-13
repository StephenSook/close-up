#!/bin/bash
# usage: bash graders/grade16.sh <agent-id> <case> <package-sha> <out-dir>   (run from fixtures/close-up/dry-run, with CLOSEUP_TASKS set to the folder that holds the runners' <agent-id>.output files)
SP="$(cd "$(dirname "$0")" && pwd)"
SKILL=""$SP"/../../../../skills/close-up/SKILL.md"
a=$1; c=$2; sha=$3; out=$4
python3 -I "$SP"/save_run.py "$a" "$c" "$sha" "$out" || { echo "SAVE FAILED"; exit 1; }
f="$out/$c.md"
python3 -I "$SP"/grade_general.py "$c" "$f" | cut -c1-230
s=$(grep -- "--target knowledge-agent" "$f" | head -1)
echo "changed line: $(echo "$s" | grep -o 'Changed since your last page[^\\]*' | head -1 | cut -c1-110)"
echo "photo change listed: $(echo "$s" | grep -c 'Photo: was')"
python3 -I "$SP"/check_preview_save.py "$f"
case "$c" in C08|C16|C17|C19|C30|C34) python3 -I "$SP"/check_e1.py "cases/$c.md" "$f"; python3 -I "$SP"/e4_fidelity.py "cases/$c.md" "$f" | head -3;; esac
python3 -I "$SP"/check_new_fields.py "$c" "$f" | cut -c1-260
case "$c" in C20|C21|C22|C23|C26|C27|C30|C31) python3 -I "$SP"/check_labels.py "$c" "$f";; esac
case "$c" in C24|C25|C32) python3 -I "$SP"/check_readback.py "$c" "$f";; esac
python3 -I "$SP"/check_g22.py "$f" | tail -1
python3 -I "$SP"/check_templates.py "$SKILL" "$f" | tail -1
python3 -I "$SP"/check_paths.py "$c" "$f" | cut -c1-260
python3 -I "$SP"/check_m34.py "$f" | tail -1
python3 -I "$SP"/check_g27.py "$f" | tail -1
case "$c" in C33|C34) python3 -I "$SP"/check_c33_34.py "$c" "$f";; esac
python3 -I "$SP"/check_c35.py "$c" "$f" | cut -c1-300
python3 -I "$SP"/check_m36_37.py "$f" | cut -c1-200
python3 -I "$SP"/check_g30.py "$f" | cut -c1-120
case "$c" in C01) python3 -I "$SP"/check_c01_20.py "$f" | cut -c1-200;; esac
case "$c" in C37) python3 -I "$SP"/check_c37.py "$f" | cut -c1-300;; esac
case "$c" in C38) python3 -I "$SP"/check_c38.py "$f" | cut -c1-300;; esac
python3 -I "$SP"/check_g31.py "cases/$c.md" "$f" | cut -c1-220
python3 -I "$SP"/check_police_line.py "$f" | cut -c1-260
python3 -I "$SP"/check_provenance.py "$f" | cut -c1-260
# G32 is reported, not a gate: its lines start with "G32 REPORT" or an item kind and carry no pass or fail word
python3 -I "$SP"/check_g32.py "$SP/../../../../skills/close-up" "$f" | cut -c1-220
