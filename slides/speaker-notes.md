# Speaker notes (40 minutes)

## 0-3 min: Hook (slides 1-3)
- Greet, introduce yourself in 20 seconds.
- Show the chatbot answering a handbook question with citations. Say: "By the end you will know how to build this."
- Poll by show of hands: ChatGPT users? AWS users?
- Agenda in one breath.

## 3-8 min: GenAI basics (slides 4-6)
- GenAI creates new content; an LLM predicts the next token, like phone autocomplete trained on a huge library.
- Tokens: pieces of words; you pay per token.
- Prompt: your instruction. Better prompt, better answer.
- Embedding: a numeric "meaning fingerprint" so similar text sits close together.
- Hallucination: confident wrong answers. This is why RAG matters.
- Why cloud: training and hosting need costly GPUs; rent them per use.

## 8-13 min: AWS landscape (slides 7-8)
- Three layers. Top: Amazon Q (ready-made assistants). Middle: Bedrock, the one that matters for beginners. Bottom: SageMaker and custom chips for people training models.
- Bedrock: choose from many models via one API, no servers. Knowledge Bases = RAG, Agents = take actions, Guardrails = safety filters.

## 13-28 min: Live demo (slides 9-12)
- Keep a recorded backup open in another tab.
- PartyRock (3 min): type an idea, e.g. "study planner for exams". Show widgets and remix.
- Playground (4 min): same prompt to two models; compare quality, speed, cost.
- RAG (8 min): explain slide 11 first (60 seconds). Then show S3 bucket with PDF, Knowledge Base, sync, ask a question, show citations. Run `python demo/rag/ask.py` to show the same thing in code. Mention Lambda + API Gateway makes it a web API.
- If something fails: switch to the recording, do not debug live.

## 28-33 min: Best practices (slide 13)
- IAM least privilege; never commit keys; use roles.
- Budget alerts on day one; delete resources after (OpenSearch Serverless costs money while it exists).
- Guardrails; do not paste personal data; verify AI answers.
- Mention data privacy and bias briefly.

## 33-37 min: Opportunities (slide 14)
- Free Tier and credits, AWS Educate, Skill Builder free courses, PartyRock.
- Certs: Cloud Practitioner, then AI Practitioner.
- Join Community Builders and local user groups; build in public on GitHub.

## 37-40 min: Close (slide 15)
- Challenge: build one GenAI mini-project this month and share it.
- Show QR code to the repo. Take questions; repeat each question before answering.

## Pre-session checklist
- Bedrock model access enabled in your region.
- KB already created and synced (sync takes minutes).
- Budget alert set; recorded backup ready; slides and repo link tested.
