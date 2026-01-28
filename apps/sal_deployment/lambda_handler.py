import json
import boto3
import logging
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("SQLDeploymentStatus")

def lambda_handler(event, context):
    logger.info("🚀 SAL SQL DEPLOYMENT STARTED")
    logger.info("📥 EVENT: %s", json.dumps(event))

    deployment_id = str(event.get("deployment_id", "UNKNOWN"))
    sql_files = event.get("changed_sql_files", [])

    if not sql_files:
        logger.warning("❌ No SQL files provided")
        return {"statusCode": 400}

    for file in sql_files:
        if "_v" in file and file.endswith(".sql"):
            status = "SUCCESS"
            reason = "Validation passed"
        else:
            status = "FAILED"
            reason = "Invalid filename format"

        item = {
            "deployment_id": deployment_id,
            "file_name": file,
            "status": status,
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        }

        logger.info("📝 Writing to DynamoDB: %s", json.dumps(item))
        table.put_item(Item=item)

    logger.info("✅ Lambda execution completed")
    return {"statusCode": 200}
