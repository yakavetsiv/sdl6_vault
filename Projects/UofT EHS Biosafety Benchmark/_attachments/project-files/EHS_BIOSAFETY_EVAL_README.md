# UofT EHS Biosafety QA Eval Loop

This folder contains a reproducible loop for creating source-specific biosafety questions from the local Obsidian EHS Wiki, testing GPT-5.5 without retrieval, and refilling the dataset around model blind spots.

## Files

- `build_ehs_biosafety_qa_dataset.py` builds QA items from `EHS Wiki/Pages` and `EHS Wiki/PDF Notes`.
- `ehs_biosafety_qa_seed_1000.jsonl` is the first 1,000-item seed dataset.
- `run_gpt55_ehs_eval.py` calls GPT-5.5 without retrieval and labels answers with a heuristic overlap score.
- `refill_ehs_biosafety_questions.py` keeps missed/partial items and fills the next round with nearby unseen questions.
- `iterate_ehs_biosafety_benchmark.py` runs eval/refill rounds in sequence and keeps prior questions out of the filler pool.

## Run

```bash
python3 build_ehs_biosafety_qa_dataset.py --limit 1000 --out ehs_biosafety_qa_seed_1000.jsonl
export OPENAI_API_KEY="..."
python3 run_gpt55_ehs_eval.py --input ehs_biosafety_qa_seed_1000.jsonl --output ehs_biosafety_gpt55_eval_round1.jsonl --model gpt-5.5
python3 refill_ehs_biosafety_questions.py --base ehs_biosafety_qa_seed_1000.jsonl --eval ehs_biosafety_gpt55_eval_round1.jsonl --out ehs_biosafety_qa_round2.jsonl
python3 run_gpt55_ehs_eval.py --input ehs_biosafety_qa_round2.jsonl --output ehs_biosafety_gpt55_eval_round2.jsonl --model gpt-5.5
```

Or run the loop directly:

```bash
export OPENAI_API_KEY="..."
python3 iterate_ehs_biosafety_benchmark.py --rounds 3 --model gpt-5.5
```

For a smoke test:

```bash
python3 iterate_ehs_biosafety_benchmark.py --rounds 1 --model gpt-5.5 --limit 5
```

## Notes

The eval label is heuristic, not a perfect judge. Use it to triage likely-correct answers away from likely-missed source-specific questions, then manually inspect samples or add an LLM judge later.

`gpt-5.5` currently rejects explicit `temperature=0`, so the evaluator leaves temperature at the model default.
