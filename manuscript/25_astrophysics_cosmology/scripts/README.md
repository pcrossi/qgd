---
title: "Scripts — Chapter 25"
---

# Scripts — Chapter 25

The scripts in this folder are self-contained and serve to reproduce the numerical reductions preserved in the chapter.

| Script | Output | Classification |
|---|---|---|
| `reduced_black_hole.py` | `output_reduced_black_hole.md` | reduction consistency test |
| `reduced_black_hole_pipeline.py` | `output_reduced_black_hole_pipeline.md` | reduced evaluation / validation track |
| `gdq_cosmology_scales.py` | `output_gdq_cosmology_scales.md` | direct evaluation of structural formulas |
| `integrated_cosmology_contraction.py` | `output_integrated_cosmology_contraction.md` | structural verification of the unique cosmological solver contract |
| `global_electroweak_scale.py` | `output_global_electroweak_scale.md` | audit of $v_K$, calculation of $\beta_\ast$, $v_{\rm GDQ}$, and conditional W/Z |
| `electroweak_proton_radius.py` | `output_electroweak_proton_radius.md` | direct evaluation and phenomenological comparison |
| `surface_proton_radius.py` | `output_surface_proton_radius.md` | legacy arithmetic correction, calculation of $r_p^{\rm surf}$, and probe response |

## Execution

At the project root:

```bash
python3 manuscript/25_astrophysics_cosmology/scripts/reduced_black_hole.py
python3 manuscript/25_astrophysics_cosmology/scripts/reduced_black_hole_pipeline.py
python3 manuscript/25_astrophysics_cosmology/scripts/gdq_cosmology_scales.py
python3 manuscript/25_astrophysics_cosmology/scripts/integrated_cosmology_contraction.py
python3 manuscript/25_astrophysics_cosmology/scripts/global_electroweak_scale.py
python3 manuscript/25_astrophysics_cosmology/scripts/electroweak_proton_radius.py
python3 manuscript/25_astrophysics_cosmology/scripts/surface_proton_radius.py
```
