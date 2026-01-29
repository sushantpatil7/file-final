import json
import boto3
import os
from datetime import datetime

# ✅ Read table and region from Lambda env
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE", "SQLDeploymentStatus")
AWS_REGION = os.environ.get("AWS_REGION", "eu-north-1")

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
table = dynamodb.Table(DYNAMODB_TABLE)

def lambda_handler(event, context):
    print("🚀 SAL SQL DEPLOYMENT – PHASE 6")
    print("📥 EVENT RECEIVED FROM GITHUB:")
    print(json.dumps(event, indent=2))

    deployment_id = event.get("deployment_id", "UNKNOWN")
    pr_number = event.get("pr_number", "NA")
    sql_files = event.get("changed_sql_files", [])

    results = []

    if not sql_files:
        print("⚠️ No SQL files found in PR.")
        return {"statusCode": 400, "body": json.dumps({"message": "No SQL files"})}

    print("📄 SQL FILES TO PROCESS:")
    for file in sql_files:
        print(f"- {file}")

        try:
            # 🔁 MOCK VALIDATION
            if "_v" not in file or not file.endswith(".sql"):
                raise Exception("Invalid file name format")

            status = "SUCCESS"
            reason = "Validation passed"

        except Exception as e:
            status = "FAILED"
            reason = str(e)

        item = {
            "deployment_id": deployment_id,
            "file_name": file,
            "status": status,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat(),
            "pr_number": str(pr_number)
        }

        print("📝 Writing to DynamoDB:")
        print(json.dumps(item, indent=2))
        table.put_item(Item=item)
        print("✅ DynamoDB write successful")

        results.append({"file": file, "status": status})

    print("🏁 FINAL RESULT:")
    print(json.dumps(results, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Phase 6 execution completed",
            "results": results
        })
    }
