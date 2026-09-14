# Hiver AI Support Agent – Evaluation Report

## Dataset

Brand selected: AppleSupport  
Evaluation examples: 200  
Evaluation method: sampled customer-support messages  

## Results

Keyword classifier accuracy: **0.995**

## Baselines

- **Trivial baseline:** always predicts the most frequent intent.
- **Simple baseline:** keyword-based intent classifier.
- **Proposed pipeline:** intent classification + retrieval of historical AppleSupport replies + escalation decision.

## What is misleading about my headline number?

The headline accuracy is measured on a sampled evaluation set and the current labels were generated using an initial rule-based labeling process. Therefore, the number should not be interpreted as production-level accuracy. A manually verified golden set is required for the final evaluation.

## Top Failure Modes

1. Overlapping keywords can cause incorrect intent assignment.
2. Messages with very little context are difficult to classify.
3. Multiple issues in one customer message may belong to different intents.
4. Generic words such as 'app' can create false matches.
5. Unseen or unusual support issues fall into the general-support category.

## What I would do with one more week

1. Manually verify the 200-example golden evaluation set.
2. Replace keyword classification with a stronger ML/LLM classifier.
3. Improve retrieval using TF-IDF or embedding-based similarity.
4. Add an LLM-as-judge evaluation for reply quality.
5. Reconstruct more complete multi-turn support conversations.
