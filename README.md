# EdTech Support Chatbot: Rules • Intent Classifier • LLMs

---

## Overview

A portfolio project that conceptualizes and develops **three chatbot architectures** from easy to advanced — rule-based, NLP intent classification, and LLM-based—to answer common EdTech questions for students and faculty, and compares tradeoffs in **speed, maintainability, accuracy, and conversational quality**.

This repo intentionally keeps the project **modular**:

- ✅ **Rule-based** chatbot (NLTK) — fast, deterministic baseline
- ✅ **Intent classifier** (Keras + NLP preprocessing) — scalable structured responses
- ✅ **LLM prototype** (Transformers) — natural language generation + QA-style answers

> Why this is useful: In real support systems, you rarely choose a single approach forever. A strong implementation starts with a reliable baseline, then evolves toward ML/LLM as requirements grow.

---

## Demo

- **Tkinter GUI** (local desktop app)
- Optional: notebooks / training / LLM experiments

> Add screenshots to `assets/screenshots/` and link them here once you have them.

---

## Project Highlights

- Built an intent-driven chatbot pipeline from scratch:
  `intents.json → preprocessing → (rules / classifier / LLM) → response`
- Implemented three architectures to compare practical tradeoffs:
  - Rules: lowest latency, highest control
  - Intent classifier: maintainable at scale, requires training + evaluation
  - LLM: most fluent, but heavier compute + requires safety/guardrails
- Documented engineering challenges (model loading, latency, environment constraints) and structured the repo to keep the “default run path” lightweight.

---

## Repository Structure

```text
data/
  intents.json                 # original intent dataset (patterns + responses)
  intents_edtech_clean.json    # (optional) cleaned, more general EdTech version

src/
  rule_based/                  # NLTK Chat (regex patterns) baseline
  intent_classifier/           # Keras training + inference (optional)
  llm/                         # GPT-2 generation + BERT QA prototypes (optional)
  ui/                          # Tkinter GUI (default entrypoint)
  common/                      # shared preprocessing / utils (optional)

notebooks/
  EdTech_Support_Chatbot_SuperComplete.ipynb

docs/
  EdTech_Chatbot_Presentation.pptx
```

---

## Quickstart (Rule-based + Tkinter GUI)

```bash
pip install -r requirements.txt
python -m src.ui.tkinter_app
```

---

## Data: intents.json

The dataset is organized by intents:

- tag: intent name (e.g., greeting, admission, placement)
- patterns: example user questions
- responses: candidate answers

Files:

- data/intents.json — original dataset
- data/intents_edtech_clean.json — (optional) cleaned, more general EdTech version

---

## Approach 1 — Rule-based (NLTK)

Best for: reliable FAQs, predictable flows, and strict control over answers.

How it works:

- Regex-like pattern matching using nltk.chat.util.Chat
- Fallback reply when no pattern matches

Tradeoffs:

- ✅ Fast, deterministic, easy to debug
- ❌ Limited generalization beyond defined patterns

Improvements:

- Add normalization (lowercasing, punctuation removal) before matching
- Expand pattern coverage for high-frequency queries
- Group patterns by topic (admissions / fees / campus services)

---

## Approach 2 — Intent Classifier (Keras + NLP Preprocessing)

Best for: scaling beyond handcrafted patterns with a maintainable, data-driven pipeline.

Typical flow:

- 1. Normalize + tokenize text
- 2. Vectorize (Bag-of-Words / TF-IDF / embeddings)
- 3. Train a multi-class classifier on patterns → tag 4. Select a response from the predicted intent’s responses

How to run:

```bash
python -m src.intent_classifier.train
python -m src.intent_classifier.infer
```

Tradeoffs:

- ✅ More scalable than rules; easier to maintain at larger intent sets
- ❌ Requires training + evaluation; sensitive to data quality

Improvements:

- Add evaluation: accuracy, confusion matrix, per-intent metrics
- Balance classes + deduplicate patterns in intents.json
- Upgrade classifier to a lightweight transformer encoder (sentence embeddings + classifier head)

---

## Approach 3 — LLM Prototype (Transformers)

Best for: natural responses and open-ended questions, with guardrails.

What was explored:

- GPT-2 style text generation
- BERT-style question answering (extractive QA)

Notes:

- Transformer models can be heavy (download size + memory). Running in Colab or a machine with sufficient RAM is recommended.
- LLMs may generate incorrect or inappropriate responses. Implementing safety checks and guardrails is crucial for production use.

How to run:

```bash
python -m src.llm.gpt2_generate
python -m src.llm.bert_qa
```

Modern upgrade path (2026-ready):

- Replace GPT-2 with a modern LLM (e.g., GPT-4/5-class or instruction-tuned open models)
- Add RAG over a vetted FAQ knowledge base (citations)
- Add safety filters + refusal policy for unsupported questions
- Add latency/cost controls (routing + caching + fallback to rules)

---

## Roadmap / Improvements

Short-term (portfolio polish)

- Add screenshots/GIF demo to assets/screenshots/
- Add intents_edtech_clean.json (remove placeholders, normalize categories)
- Add a simple evaluation script for the intent classifier
- Add CLI entrypoint (python -m src.rule_based.cli)

Engineering upgrades

- Streamlit web UI + deploy
- RAG over curated FAQ docs (vector store + citations)
- Better routing: rules → classifier → LLM fallback
- Observability: logs, analytics, and error tracking

---

## Notes on Responsible Use

This is a learning/portfolio project. For real student-support deployments:

- Avoid exposing private student data
- Restrict sensitive actions (account/financial operations) to verified channels
- Add security, audit logging, and human handoff for high-risk cases
