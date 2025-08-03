import subprocess
from datetime import datetime

FILENAME = "daily.js"

# Append a comment with timestamp as "commit made on YYYY-MM-DDTHH:MM:SSZ"
with open(FILENAME, "a") as f:
    f.write(f"// Commit made on {datetime.utcnow().isoformat()} UTC\n")

subprocess.run(["git", "config", "--global", "user.name", "github-actions[bot]"])
subprocess.run(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
subprocess.run(["git", "add", FILENAME])
subprocess.run(["git", "commit", "-m", f"Daily commit: {datetime.utcnow().isoformat()}"], check=False)
subprocess.run(["git", "push"])
