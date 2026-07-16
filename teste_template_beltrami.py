#!/usr/bin/env python3
"""Garante que o template Beltrami não inventa dinâmica default."""
import numpy as np
from ponte_global_local_solver_extensivel import BeltramiCanonicalModelTemplate

model=BeltramiCanonicalModelTemplate("harmonico-fixo-a-derivar")
assert model.parameter_count==15
assert model.beltrami_real_state_dimension==4
assert model.beltrami_matching_dimension==4
try:
    model.initial(np.zeros(15),"L")
except NotImplementedError as error:
    assert "condição regular" in str(error)
else:
    raise AssertionError("o template não pode fornecer dinâmica default")
print("BELTRAMI_TEMPLATE_BLOCKED_UNTIL_DERIVATION = PASS")
