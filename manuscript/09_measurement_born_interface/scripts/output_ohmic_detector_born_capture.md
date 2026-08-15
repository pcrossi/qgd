# Output — ohmic detector and Born capture

Classification: consistency test with dimensionless parameters.

## Diagnostic parameters

| parameter | value |
|---|---:|
| zeta_A | 1.700000000000 |
| c_A | 2.300000000000 |
| gamma_A | 0.739130434783 |
| mobility | 1.352941176471 |
| k_pointer | 4.000000000000 |
| g_X | 1.000000000000 |
| kBT | 0.500000000000 |
| Gamma_info | 0.338235294118 |
| tau_relax | 0.184782608696 |
| p0 | 0.370000000000 |
| trajectories | 100000.000000000000 |
| final time | 4.000000000000 |

## Convergence of the retarded DtN

| h | relative error |
|---:|---:|
| 0.200000 | 4.255868489493e-03 |
| 0.100000 | 1.064668462629e-03 |
| 0.050000 | 2.662109650198e-04 |
| 0.025000 | 6.655548208398e-05 |

## Martingale and conditioned separation

| t | E[p_t] | E[p_t|+] | E[p_t|-] |
|---:|---:|---:|---:|
| 1.0000 | 0.370684229390 | 0.771387782955 | 0.132704422422 |
| 2.0000 | 0.371300912096 | 0.902914630966 | 0.055572915493 |
| 3.0000 | 0.372164716145 | 0.956798344440 | 0.024947935133 |
| 4.0000 | 0.372457279754 | 0.980403329639 | 0.011395137151 |

## Final result

| quantity | value |
|---|---:|
| information | 1.352941176471 |
| empirical_error | 0.009560000000 |
| analytic_error_prior | 0.009607130572 |
| analytic_error_equal | 0.010000743136 |
| empirical_true_plus | 0.372610000000 |
| empirical_plus_record | 0.371950000000 |
| mean_final_p | 0.372457279754 |
| mean_x_plus | 0.248668407318 |
| x_eq_plus | 0.250000000000 |
| mean_x_minus | -0.250546856931 |
| x_eq_minus | -0.250000000000 |

## Verifications

| test | value |
|---|---:|
| martingale error | 2.457279754300e-03 |
| binomial standard error | 1.526761278000e-03 |
| martingale error in standard deviations | 1.609472148468 |
| MC vs analytical error difference | 4.713057238513e-05 |

## Verdict

The test confirms the ohmic DtN, the martingale property, the conditioned asymptotic capture, and the relaxation of the pointer in the reduced model. It does not calculate parameters of a real material.
