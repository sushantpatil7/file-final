import json
import boto3
import os
from datetime import datetime

dynamodb = boto3.resource(
    "dynamodb",
    region_name=os.environ["AWS_REGION"]
)

table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])


def lambda_handler(event, context):
    print("🚀 SAL SQL DEPLOYMENT – PHASE 6")
    print("📥 EVENT RECEIVED FROM GITHUB:")
    print(json.dumps(event, indent=2))

    deployment_id = event.get("deployment_id", "UNKNOWN")
    pr_number = event.get("pr_number", "NA")
    sql_files = event.get("changed_sql_files", [])

    results = []

    print("📄 SQL FILES TO PROCESS:")
    for file in sql_files:
        print(f"- {file}")

        try:
            # 🔁 MOCK LOGIC (Phase 5)
            if "vX" in file:
                raise Exception("Invalid version format")

            status = "SUCCESS"
            reason = "Mock validation passed"

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

        results.append({
            "file": file,
            "status": status
        })

    print("🏁 FINAL RESULT:")
    print(json.dumps(results, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Phase 6 execution completed",
            "results": results
        })
    }
