# Saída — cálculo direto do Schur de superfície Q48

Classificação: cálculo direto do bloco reduzido de superfície Q40.
Este cálculo não substitui a Hessiana completa do próton; ele testa o
bloco coletivo já derivado.

## Dados

- r_p = 0.840778765450 fm
- Lambda_E = sqrt(12)/r_p = 4.120110732439 fm^-1
- j = [1.712091781054, 1.341454657186, 1.063840998206]

## Resultado por escala

| escala | q (fm^-1) | x | J0 | J1 | J2 | min eig K | max eig K | R=-J^T K^-1 J |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| hiperfina 1s: q~1/aB* | 1.888697509086e-05 | 2.101391825245e-11 | 3.597775672775e-11 | 2.818921850547e-11 | 1.024795667724e-16 | 1.000000000021e+00 | 1.000000000042e+00 | -2.089031019060e-21 |
| Lamb 2s: q~1/(2aB*) | 9.443487545431e-06 | 5.253479563111e-12 | 8.994439181938e-12 | 7.047304626367e-12 | 1.280994584655e-17 | 1.000000000005e+00 | 1.000000000011e+00 | -1.305644386936e-22 |
| hadrônica: q~1/rp | 1.189373520232e+00 | 8.333333333333e-02 | 1.426743150878e-01 | 1.117878880988e-01 | 2.559203694538e-02 | 1.083333333333e+00 | 1.173611111111e+00 | -2.999611553485e-02 |
| Q40 espalhamento baixo: q=0.25 fm^-1 | 2.500000000000e-01 | 3.681817356415e-03 | 6.303609235260e-03 | 4.938991039671e-03 | 2.376676566494e-04 | 1.003681817356e+00 | 1.007377190492e+00 | -6.386079337265e-05 |
| Q40 espalhamento médio: q=1.0 fm^-1 | 1.000000000000e+00 | 5.890907770264e-02 | 1.008577477642e-01 | 7.902385663473e-02 | 1.521073002556e-02 | 1.058909077703e+00 | 1.121288434841e+00 | -1.538200245154e-02 |

## Conclusão

Na escala atômica, o bloco de superfície Q40 é suprimido por x^2.
Isso confirma diretamente que ele não pode fornecer o resíduo hiperfino
de ordem 10^-5 nem o Lamb shift de ordem GHz. Ele é o bloco correto para
espalhamento/fatores de forma em q hadrônico/intermediário.

$$
\boxed{
\text{no-go setorial: o Schur coletivo }q^4\text{ não fecha a metrologia atômica.}
}
$$
