# GenAI on AWS: AWS Student Community Day

Resources for the 40-minute session **"From Zero to GenAI on AWS: Build Your First AI App"**.

## Contents
- `slides/slide-outline.md`: slide-by-slide content
- `slides/speaker-notes.md`: full speaker notes with timings
- `demo/bedrock_demo.py`: first Bedrock call
- `demo/rag/`: mini RAG chatbot using Bedrock Knowledge Bases
- `demo/rag/template.yaml`: optional SAM template (Lambda + API Gateway)

## Prerequisites
- AWS account (Free Tier / AWS Educate credits)
- Python 3.10+, `pip install boto3`
- AWS CLI configured (`aws configure`) with an IAM user/role (never use root keys)
- Model access enabled in the Bedrock console (Amazon Nova, Titan Embeddings; Claude optional)
- A **budget alert** set in AWS Billing

## Quick start
```bash
pip install -r demo/requirements.txt
python demo/bedrock_demo.py
```

## RAG demo steps
1. Create an S3 bucket and upload a PDF (e.g. college handbook).
2. Bedrock console > Knowledge bases > Create. Choose the S3 bucket, Titan Text Embeddings v2, and the quick-create vector store.
3. Sync the data source.
4. Copy the Knowledge Base ID, then run:
```bash
export KB_ID=XXXXXXXXXX
export MODEL_ID=amazon.nova-lite-v1:0
python demo/rag/ask.py "What is the attendance policy?"
```
5. Optional: deploy `demo/rag/lambda_function.py` behind API Gateway with `sam deploy --guided`.

## Cleanup (important, avoids charges)
Delete the Knowledge Base, the OpenSearch Serverless collection it created, the S3 bucket, and any Lambda/API Gateway stack.

## Student resources
- AWS Educate, AWS Skill Builder, PartyRock (partyrock.aws)
- Certifications: Cloud Practitioner, AI Practitioner
- AWS Community Builders and local user groups

## Notes
Model IDs and regional availability change. Verify in the Bedrock console before the session.
