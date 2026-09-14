# Decision Log – Hiver AI Support Agent

## 1. Brand Selection
Selected AppleSupport as the target brand because it had a sufficiently large set of customer-support interactions and clear support patterns.

## 2. Dataset
Used the Customer Support on Twitter dataset because it contains real-world customer-support conversations.

## 3. Customer Message Filtering
Filtered inbound messages that explicitly mention @AppleSupport to create a focused customer-message dataset.

## 4. Golden Set Size
Created a 200-example evaluation set, which is within the required 150–250 range.

## 5. Intent Taxonomy
Defined a small set of support intents from recurring themes observed in the AppleSupport data.

## 6. Manual Labeling
Used manual review for the golden evaluation set instead of relying only on automatic keyword labels.

## 7. Trivial Baseline
Used majority-class prediction as the trivial baseline.

## 8. Simple Baseline
Used a keyword-based classifier as the simple baseline because it is transparent and easy to reproduce.

## 9. Historical Knowledge Base
Used historical AppleSupport responses as the basis for retrieval and response grounding.

## 10. Retrieval
Used lexical word-overlap similarity as an initial lightweight retrieval method.

## 11. Escalation
Escalated account-specific and unclear issues because they are less suitable for automatic handling.

## 12. Sampling
Used a fixed random seed when sampling the golden set so that the evaluation set can be reproduced.

## 13. Scope
Focused on one brand rather than attempting to build a universal customer-support agent.

## 14. Deployment
Did not deploy the application because the assignment requires a runnable pipeline and GitHub repository, not a production deployment.

## 15. AI/LLM Scope
Kept the initial implementation lightweight and reproducible, while identifying stronger ML/LLM classification and semantic retrieval as next-step improvements.