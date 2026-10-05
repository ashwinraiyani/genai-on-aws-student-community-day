"""Ask a question against a Bedrock Knowledge Base (RAG).

Usage:
  export KB_ID=XXXXXXXXXX
  export MODEL_ID=amazon.nova-lite-v1:0
  python demo/rag/ask.py "What is the attendance policy?"
"""
import os
import sys
import boto3

REGION = os.environ.get("AWS_REGION", "us-east-1")
KB_ID = os.environ["KB_ID"]
MODEL_ID = os.environ.get("MODEL_ID", "amazon.nova-lite-v1:0")


def ask(question: str) -> dict:
    client = boto3.client("bedrock-agent-runtime", region_name=REGION)
    model_arn = f"arn:aws:bedrock:{REGION}::foundation-model/{MODEL_ID}"
    return client.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": KB_ID,
                "modelArn": model_arn,
            },
        },
    )


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "What is this document about?"
    res = ask(q)
    print("Answer:\n", res["output"]["text"])
    print("\nSources:")
    for c in res.get("citations", []):
        for ref in c.get("retrievedReferences", []):
            loc = ref.get("location", {}).get("s3Location", {}).get("uri")
            print(" -", loc)
