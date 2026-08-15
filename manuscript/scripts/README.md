---
title: "Transversal Scripts of the Manuscript"
---

# Transversal Scripts of the Manuscript

## Transversal Audit

The script `auditoria_transversal.py` verifies:

- the 28 chapters, their indexes, and checklists;
- Wiki links and local Markdown links;
- Quartz mathematical conventions;
- dependencies on historical files;
- suspicious constitutive signs;
- literal preservation of the official action;
- syntax of Python scripts;
- bibliographical coverage;
- nominal citation of scripts in their chapters.

Execution:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 manuscript/scripts/transversal_audit.py
```

Output:

- [`final_transversal_audit.md`](../notes/editorial/final_transversal_audit.md)

The checker certifies document and syntactic integrity. It does not decide the physical validity of the hypotheses or the correctness of an analytical proof.
