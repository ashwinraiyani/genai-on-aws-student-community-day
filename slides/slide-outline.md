# Slide-by-slide outline (about 15 slides)

1. **Title**: From Zero to GenAI on AWS. Name, role, social handles.
2. **Hook**: Screenshot/live demo of a chatbot answering from a college handbook. Poll: who has used ChatGPT? Who has used AWS?
3. **Agenda**: Basics > AWS stack > Demo > Best practices > Your next steps.
4. **What is GenAI?** Generates text, images, code. Analogy: very well-read autocomplete.
5. **Key terms**: LLM, token, prompt, embedding, hallucination (one line each).
6. **Why the cloud?** GPUs are expensive; pay-as-you-go; managed models.
7. **AWS GenAI stack**: Applications (Amazon Q), Models/tools (Bedrock), Infrastructure (SageMaker, Trainium/Inferentia, EC2 GPU).
8. **Amazon Bedrock**: One API, many models; Knowledge Bases, Agents, Guardrails.
9. **Demo 1: PartyRock** (no code).
10. **Demo 2: Bedrock Playground**: compare two models.
11. **RAG explained**: Question > embed > search docs > add context > LLM > cited answer.
12. **Demo 3: RAG chatbot** architecture: S3 > Knowledge Base > Bedrock model > (Lambda + API Gateway).
13. **Best practices**: IAM least privilege, no keys in code, budget alerts, Guardrails, responsible AI, cleanup.
14. **Student opportunities**: Free Tier, AWS Educate, Skill Builder, PartyRock, certifications, Community Builders.
15. **Challenge + Q&A**: Build one GenAI mini-project this month. QR code to this repo.
