import json
import os
import boto3

REGION = os.environ.get("AWS_REGION", "us-east-1")
KB_ID = os.environ["KB_ID"]
MODEL_ID = os.environ.get("MODEL_ID", "amazon.nova-lite-v1:0")

client = boto3.client("bedrock-agent-runtime", region_name=REGION)


def handler(event, context):
    try:
        body = json.loads(event.get("body") or "{}")
        question = body.get("question", "").strip()
        if not question:
            return _resp(400, {"error": "question is required"})
        res = client.retrieve_and_generate(
            input={"text": question},
            retrieveAndGenerateConfiguration={
                "type": "KNOWLEDGE_BASE",
                "knowledgeBaseConfiguration": {
                    "knowledgeBaseId": KB_ID,
                    "modelArn": f"arn:aws:bedrock:{REGION}::foundation-model/{MODEL_ID}",
                },
            },
        )
        sources = [
            r.get("location", {}).get("s3Location", {}).get("uri")
            for c in res.get("citations", [])
            for r in c.get("retrievedReferences", [])
        ]
        return _resp(200, {"answer": res["output"]["text"], "sources": sources})
    except Exception as e:
        return _resp(500, {"error": str(e)})


def _resp(code, obj):
    return {
        "statusCode": code,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(obj),
    }
