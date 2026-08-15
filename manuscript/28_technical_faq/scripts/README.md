---
title: "Scripts — Chapter 28"
---

# Scripts — Chapter 28

This chapter does not introduce a new physical solver. The scripts are self-contained editorial and conceptual checkers.

## Scripts

- `faq_status_matrix.py`: generates a matrix of objections, answers, status, and recommended action.
- `check_no_historical_refs.py`: verifies that the chapter does not reference historical files external to the manuscript.
- `check_overclaim_terms.py`: searches for expressions that could suggest undue closure or change of the official action.
- `faq_metrological_comparisons.py`: regenerates the short table of metrological comparisons preserved in this FAQ.

## How to run

```bash
python3 faq_status_matrix.py
python3 check_no_historical_refs.py
python3 check_overclaim_terms.py
python3 faq_metrological_comparisons.py
```

The Markdown outputs are saved in this same folder.
