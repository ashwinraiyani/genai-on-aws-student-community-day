import boto3

client = boto3.client("bedrock-runtime", region_name="us-east-1")

response = client.converse(
    modelId="amazon.nova-lite-v1:0",
    messages=[{
        "role": "user",
        "content": [{"text": "Explain cloud computing to a first-year student in 3 lines."}],
    }],
    inferenceConfig={"maxTokens": 200, "temperature": 0.5},
)
print(response["output"]["message"]["content"][0]["text"])
