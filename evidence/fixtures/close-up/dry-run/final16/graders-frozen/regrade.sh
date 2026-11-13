#!/bin/bash
# usage: bash graders/regrade.sh RUN_DIR [SKILL_PATH]
#
# Grades saved transcripts again with the checkers of the grade16.sh in this same folder, and no save step, so
# anyone can recount a run from the files alone. RUN_DIR holds the saved transcripts (C01.md, C02.md, ...).
# SKILL_PATH is the close-up package folder, the one that holds SKILL.md. It defaults to ../../../../skills/close-up
# from this folder (the layout of the private repo).
#
# The checker list is read from grade16.sh itself: every line after the save step, each "python3 -I ... | filter"
# turned into a call that keeps the checker's exit code. So regrade.sh can never run a different set of checks than
# grade16.sh, and a copy of an older graders folder regrades its own run with its own checks.
#
# Prints one line per case (PASS, or FAIL with the checkers that printed FAIL), then the totals. A check that runs
# and fails is a result. A checker that cannot run (exit code above 1, or a Python traceback) is an error: the
# script still grades every case, then exits 1. Exit 0 means every checker ran on every case. Checker runs that
# printed nothing (check_preview_save.py on a run with no save, for example) are listed, not counted as errors.
G="$(cd "$(dirname "$0")" && pwd)"
[ -n "$1" ] || { echo "usage: bash graders/regrade.sh RUN_DIR [SKILL_PATH]"; exit 2; }
RUN="$(cd "$1" && pwd)" || { echo "no such folder: $1"; exit 2; }
PKG="$(cd "${2:-$G/../../../../skills/close-up}" && pwd)" || { echo "no such folder: ${2:-the default package path}"; exit 2; }
[ -f "$PKG/SKILL.md" ] || { echo "no SKILL.md in $PKG"; exit 2; }
[ -f "$G/grade16.sh" ] || { echo "no grade16.sh in $G"; exit 2; }
cd "$G/.." || exit 2
[ -d cases ] || { echo "no cases folder next to graders"; exit 2; }
# transcripts are named by a path relative to this folder, as in grade16.sh, so the "| cut" filters keep the verdict
REL="$(python3 -I -c 'import os, sys; print(os.path.relpath(sys.argv[1], sys.argv[2]))' "$RUN" "$PWD")" || exit 2
TMP="$(mktemp -d)" || exit 2

# grade16.sh after its save step, with each checker call rewritten to: run <filter> <checker.py> <args...>
sed -n '/^f="\$out\/\$c.md"$/,$p' "$G/grade16.sh" | sed '1d' > "$TMP/body.raw"
[ -s "$TMP/body.raw" ] || { echo "could not find the save step in grade16.sh"; exit 2; }
sed -E \
  -e 's#"\$SP/\.\./\.\./\.\./\.\./skills/close-up"#"$PKG"#g' \
  -e 's#python3 -I "\$SP"/([a-z0-9_]+\.py)([^|;]*) \| cut -c1-([0-9]+)#run cut\3 \1\2#g' \
  -e 's#python3 -I "\$SP"/([a-z0-9_]+\.py)([^|;]*) \| tail -([0-9]+)#run tail\3 \1\2#g' \
  -e 's#python3 -I "\$SP"/([a-z0-9_]+\.py)([^|;]*) \| head -([0-9]+)#run head\3 \1\2#g' \
  -e 's#python3 -I "\$SP"/([a-z0-9_]+\.py)([^|;]*)#run all \1\2#g' \
  "$TMP/body.raw" > "$TMP/body.sh"
if grep -q "python3" "$TMP/body.sh"; then
  echo "grade16.sh has a checker call regrade.sh cannot rewrite:"; grep -n "python3" "$TMP/body.sh"; exit 2
fi
nchecks=$(grep -o "run [a-z]*[0-9]* [a-z0-9_]*\.py" "$TMP/body.sh" | sort -u | wc -l | tr -d ' ')
[ "$nchecks" -gt 0 ] || { echo "no checker calls found in grade16.sh"; exit 2; }

SP="$G"
SKILL="$PKG/SKILL.md"
errors=0
ncase=0
nruns=0

# run <filter> <checker.py> <args...>: prints the checker's stdout through the grade16.sh filter, and adds one row
# to the tally (case, checker, exit code, FAIL lines in the filtered output)
run() {
  local filt=$1 py=$2; shift 2
  python3 -I "$G/$py" "$@" > "$TMP/o" 2> "$TMP/e"
  local e=$?
  case "$filt" in
    all) cat "$TMP/o" > "$TMP/f";;
    cut*) cut -c1-"${filt#cut}" "$TMP/o" > "$TMP/f";;
    tail*) tail -"${filt#tail}" "$TMP/o" > "$TMP/f";;
    head*) head -"${filt#head}" "$TMP/o" > "$TMP/f";;
  esac
  cat "$TMP/f"
  [ -s "$TMP/o" ] || echo "$c $py" >> "$TMP/silent.txt"
  if [ $e -gt 1 ] || grep -q "Traceback" "$TMP/e"; then
    echo "RUN ERROR $py on $c: exit $e $(head -c 300 "$TMP/e")" >&2
    errors=$((errors + 1))
  fi
  nruns=$((nruns + 1))
  printf '%s\t%s\t%s\t%s\n' "$c" "$py" "$e" "$(grep -cw "FAIL" "$TMP/f")" >> "$TMP/tally.tsv"
}

for f in "$REL"/C[0-9][0-9].md; do
  [ -f "$f" ] || continue
  c=$(basename "$f" .md)
  [ -f "cases/$c.md" ] || { echo "RUN ERROR no case file cases/$c.md" >&2; errors=$((errors + 1)); continue; }
  ncase=$((ncase + 1))
  { . "$TMP/body.sh"; } > "$TMP/$c.log"
done
[ "$ncase" -gt 0 ] || { echo "RUN ERROR no transcripts named Cxx.md in $RUN"; exit 1; }

cat > "$TMP/tally.py" <<'EOF'
import collections, os, re, sys
tmp = sys.argv[1]
rows = [l.rstrip("\n").split("\t") for l in open(os.path.join(tmp, "tally.tsv"), encoding="utf-8")]
NAME = {"check_g31.py": "G31", "check_g32.py": "G32Q", "check_m36_37.py": "G28/G29", "check_c35.py": "M35",
        "grade_general.py": "general", "check_e1.py": "G16/G21", "check_police_line.py": "G33Q", "check_provenance.py": "G34"}
NEWER = ("G31", "G32Q", "G33Q", "G34", "check_c37", "check_c38", "check_c01_20")
fails, cases = collections.defaultdict(list), []
for c, py, e, nf in rows:
    if c not in cases:
        cases.append(c)
    if int(nf) > 0:
        fails[c].append(NAME.get(py, py.replace(".py", "")))
same = diff = 0
g30 = collections.Counter()
g33 = collections.Counter()
for c in cases:
    log = open(os.path.join(tmp, c + ".log"), encoding="utf-8").read()
    same += len(re.findall(r" SAME save-only", log))
    diff += len(re.findall(r" DIFF save-only", log))
    for k in ("PASS", "n/a", "FAIL"):
        g30[k] += len(re.findall(r" G30 %s" % re.escape(k), log))
    for k in ("exact", "differs"):
        g33[k] += len(re.findall(r"^G33 REPORT %s " % k, log, re.M))
for c in cases:
    print("%s %s" % (c, ("FAIL " + ", ".join(fails[c])) if fails[c] else "PASS"))
strict = [c for c in cases if fails[c]]
older = [c for c in cases if [x for x in fails[c] if x not in NEWER]]
emerg = [c for c in cases if c in ("C08", "C16", "C17", "C19", "C30", "C34")]
print("TOTAL cases %d | strict pass %d of %d | strict fails: %s | apart from G31, G32Q, G33Q, G34, check_c37, check_c38 and check_c01_20: %s | "
      "G31 fails: %s | G32Q fails: %s | G33Q fails: %s | G33 pages exact: %d of %d | saves equal to the preview %d of %d | emergency cases failing G16/G21 (D27) "
      "%d of %d | G30 pass %d, n/a %d, fail %d" % (
          len(cases), len(cases) - len(strict), len(cases), ", ".join(strict) or "none", ", ".join(older) or "none",
          ", ".join(c for c in cases if "G31" in fails[c]) or "none",
          ", ".join(c for c in cases if "G32Q" in fails[c]) or "none",
          ", ".join(c for c in cases if "G33Q" in fails[c]) or "none", g33["exact"], g33["exact"] + g33["differs"],
          same, same + diff, len([c for c in emerg if "G16/G21" in fails[c]]), len(emerg),
          g30["PASS"], g30["n/a"], g30["FAIL"]))
EOF
python3 -I "$TMP/tally.py" "$TMP"
t=$?
[ $t -eq 0 ] || { echo "RUN ERROR the tally did not run (exit $t)"; errors=$((errors + 1)); }
nsilent=0; [ -f "$TMP/silent.txt" ] && nsilent=$(wc -l < "$TMP/silent.txt" | tr -d ' ')
echo "checkers in grade16.sh: $nchecks | checker runs: $nruns | runs that printed nothing: $nsilent | run errors: $errors | logs: $TMP | package: $PKG"
[ "$nsilent" -eq 0 ] || echo "printed nothing: $(tr '\n' ',' < "$TMP/silent.txt")"
[ "$errors" -eq 0 ] || exit 1
exit 0
