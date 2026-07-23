# Saída — Q76 avaliador de protótipo de qubit

Classificação: comparação fenomenológica / protocolo de fechamento.

Os cenários são fixos. Em uma aplicação GDQ real, `J/Delta`, `T1`, `T2`,
`f_gap`, erro de eixo e readout devem vir de `K_phys` e `R_app`.

| cenário | leak | T1 | T2 | nonad | eixo | readout | erro total | fidelidade |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline_convencional_bom | 1.000e-04 | 1.000e-04 | 1.667e-04 | 1.013e-05 | 1.667e-05 | 1.000e-03 | 1.393e-03 | 0.998606553 |
| gdq_gap_contorno_moderado | 9.000e-06 | 1.000e-05 | 1.667e-05 | 2.533e-06 | 4.167e-06 | 2.000e-04 | 2.424e-04 | 0.999757634 |
| gdq_meta_forte | 2.500e-07 | 1.667e-07 | 2.500e-07 | 1.013e-07 | 1.067e-07 | 2.000e-07 | 1.075e-06 | 0.999998925 |

## Leitura

O caso `baseline_convencional_bom` ilustra um qubit bom, mas ainda com
readout e coerência limitantes. O caso `gdq_gap_contorno_moderado` mostra
que reduzir `J/Delta` e aumentar coerência já empurra a fidelidade para
a faixa `99.96%`. O caso `gdq_meta_forte` mostra o regime que seria
compatível com erro `~1e-6` por porta.

$$
\boxed{
\text{o fechamento real exige substituir esses números pela Hessiana e pelo contorno calculados.}
}
$$
