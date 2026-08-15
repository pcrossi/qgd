---
title: "Scripts — Chapter 27"
---

# Scripts — Chapter 27

Protocol scripts to standardize new GDQ calculations.

| Script | Output | Function |
|---|---|---|
| `generate_example_manifest.py` | `output_generate_example_manifest.md` | minimal manifest example |
| `classify_result.py` | `output_classify_result.md` | simple numerical status classifier |
| `numerical_status_table.py` | `output_numerical_status_table.md` | status of the main numerical blocks |
| `hessian_block_projector_schur.py` | `output_hessian_block_projector_schur.md` | self-contained example of physical projector and Schur complement |
| `gdq_reduced.py` | importable module | reduced library for DtN/Schur/response/coherence |
| `verify_gdq_reduced.py` | `output_verify_gdq_reduced.md` | self-contained test of the reduced blocks |

## Execution

```bash
python3 manuscript/27_numeric_experimental_program/scripts/generate_example_manifest.py
python3 manuscript/27_numeric_experimental_program/scripts/classify_result.py
python3 manuscript/27_numeric_experimental_program/scripts/numerical_status_table.py
python3 manuscript/27_numeric_experimental_program/scripts/hessian_block_projector_schur.py
python3 manuscript/27_numeric_experimental_program/scripts/verify_gdq_reduced.py
```
