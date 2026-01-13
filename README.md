# EdTech Support Chatbot — 3 Approaches (Rules • Intent Classifier • LLM)

A portfolio project that explores **three chatbot architectures** for common EdTech / student-support questions (e.g., admissions, enrollment, fees, campus services), and compares their tradeoffs in **speed, maintainability, accuracy, and conversational quality**.

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
