#!/usr/bin/env python3
"""Verifica a convergência do traço pelo modelo de Weyl em d=4."""

import numpy as np

dimension = 4
tau = 0.05
max_n = 1_000_000
j = np.arange(1, max_n + 1, dtype=float)
eigenvalues = j ** (2.0 / dimension)
terms = np.exp(-tau * eigenvalues) / eigenvalues

cutoffs = [100, 1_000, 10_000, 100_000, 1_000_000]
partial = np.cumsum(terms)
limit_proxy = partial[-1]

print("N partial_trace tail_to_1e6")
previous_tail = float("inf")
for cutoff in cutoffs:
    value = partial[cutoff - 1]
    tail = limit_proxy - value
    print(f"{cutoff} {value:.12e} {tail:.12e}")
    if tail > previous_tail + 1e-12:
        raise SystemExit("A cauda não diminuiu.")
    previous_tail = tail

if terms[-1] > 1e-20:
    raise SystemExit("O último termo ainda é grande para o proxy escolhido.")
