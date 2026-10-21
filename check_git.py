import subprocess
import os

out = []
for cmd in ["git --version", "git config user.name", "git config user.email", "gh --version", "git remote -v"]:
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5)
        out.append(f"[{cmd}]\nstdout: {res.stdout.strip()}\nstderr: {res.stderr.strip()}\nrc: {res.returncode}")
    except Exception as e:
        out.append(f"[{cmd}] err: {e}")

out.append(f"cwd: {os.getcwd()}")
out.append(f"OmniAI .git exists: {os.path.exists('.git')}")
out.append(f"Parent .git exists: {os.path.exists('..\\.git')}")

with open("D:\\LOYHA\\OmniAI\\git_info.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(out))
