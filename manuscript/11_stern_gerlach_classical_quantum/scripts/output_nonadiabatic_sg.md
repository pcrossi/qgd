# Non-adiabatic regime — Chapter 11

Hamiltonian: `H(t)=(v t sigma_z + Delta sigma_x)/2`, with `Delta=1` and `hbar=1`.

| v | numerical P_exc | Landau–Zener | absolute error |
|---:|---:|---:|---:|
| 0.200 | 0.000387351 | 0.000388203 | 8.521e-07 |
| 0.400 | 0.019708490 | 0.019702873 | 5.617e-06 |
| 0.800 | 0.140436139 | 0.140366923 | 6.922e-05 |
| 1.600 | 0.374824101 | 0.374655739 | 1.684e-04 |
| 3.200 | 0.612383265 | 0.612091283 | 2.920e-04 |

- largest numerical/asymptotic error: `2.920e-04`;
- norm of `[H,P_z+]` in the test: `0.707106781`;
- instantaneous drift `dp_z/dt` in the test state: `0.500000000`.

## Interpretation

The probability of channel swapping increases with the sweep speed. Thus, the immediate identification of channels with instantaneous projectors requires the adiabatic condition.

When `[H,P_n] != 0`, `p_n=Tr(P_n rho)` receives the drift `-i Tr(P_n[H,rho]) dt` and ceases to be a martingale. Therefore, the first-passage proof of the Born rule remains valid in the documented adiabatic/QND measurement sector, but cannot be transferred without modification to an apparatus whose direction varies rapidly.

This test validates the reduced two-level dynamics. It does not yet fix `Delta` or `v` in physical units from the GDQ background.
