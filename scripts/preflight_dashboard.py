import os
import sys
from datetime import datetime

sql_files = []

# Get SQL files from command line or default folder
if len(sys.argv) > 1:
    sql_files = sys.argv[1:]
else:
    for root, dirs, files in os.walk("sal/deployment"):
        for file in files:
            if file.endswith(".sql"):
                sql_files.append(os.path.join(root, file))

results = []

for file in sql_files:
    status = "SUCCESS"
    reason = ""
    filename = os.path.basename(file)

    # Path validation
    if not file.startswith("sal/deployment/SCT-") or not file.endswith(".sql"):
        status = "FAILED"
        reason = f"Invalid path: {file}"

    # Filename date + version validation
    elif not os.path.basename(file).split("_")[-1].startswith("v"):
        status = "FAILED"
        reason = f"Invalid filename format: {filename}"
    else:
        try:
            date_part = "_".join(filename.split("_")[-4:-1])
            datetime.strptime(date_part, "%Y_%m_%d")
        except:
            status = "FAILED"
            reason = f"Invalid date in filename: {filename}"

    results.append({
        "deployment_id": file.split("/")[2],
        "file_name": file,
        "status": status,
        "reason": reason,
        "timestamp": datetime.utcnow().isoformat()
    })

# Print Phase 4 style dashboard
print("\n=== REAL-TIME SQL PRE-FLIGHT DASHBOARD ===")
print("Deployment | File | Status | Reason")
for r in results:
    print(f"{r['deployment_id']} | {r['file_name']} | {r['status']} | {r['reason']}")
