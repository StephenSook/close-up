import json, os, sys
task, case, sha, outdir = sys.argv[1:5]
tasks = os.environ.get("CLOSEUP_TASKS")
assert tasks, "set CLOSEUP_TASKS to the folder that holds the runners' .output files"
p = os.path.join(tasks, task + ".output")
files=set(); other=set(); msg=None; models=set()
for l in open(p,encoding="utf-8"):
    try: o=json.loads(l)
    except Exception: continue
    m=o.get("message",{})
    if m.get("role")!="assistant" or not isinstance(m.get("content"),list): continue
    if m.get("model"): models.add(m["model"])
    for c in m["content"]:
        if c.get("type")!="tool_use": continue
        if c["name"]=="Read": files.add(c["input"]["file_path"])
        elif c["name"]=="SubagentHandback": msg=c["input"]["message"]
        else: other.add(c["name"])
base = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..")) + "/"
allowed={base+"skills/close-up/SKILL.md", base+f"fixtures/close-up/dry-run/cases/{case}.md"}|{base+"skills/close-up/references/"+n for n in ["disclosures.md","first-run-questions.md","install-and-removal.md","limits.md","messages.md","page-format.md","sources.md","testing.md"]}
out=len(files-allowed)
print(case, "files", len(files), "outside", out, "other tools", sorted(other))
import re as _re
m0 = _re.search(r"^T\d+ ", msg or "", _re.M)
assert m0, "no numbered turn"
msg = msg[m0.start():]
hdr=f"# Dry run {case}, final pass on the final text, at {sha} (fixture test, not a device test)\n\nMADE-UP TEST DATA. Model: {", ".join(sorted(models)) or "not recorded"} (from the runner's task log), single pass, prompt as in RUNNER.md plus the eight reference file names and \"use no other tool\". Files read: {len(files)}, outside the allowed set: {out}. Other tool calls: {len(other)}.\n\n"
open(f"{outdir}/{case}.md","w",encoding="utf-8").write(hdr+msg.rstrip()+"\n"); print("saved")
