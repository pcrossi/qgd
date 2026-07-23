# Saída — Q76 requisitos para vantagem GDQ

Classificação: ferramenta de engenharia reduzida / requisitos de fechamento.

Orçamento de erro usado:

| canal | peso |
|---|---:|
| vazamento | 0.20 |
| T1 | 0.15 |
| T2 | 0.20 |
| não adiabático | 0.15 |
| eixo/contorno | 0.10 |
| readout | 0.20 |

## Requisitos

| alvo | gate ns | erro alvo | max J/Delta | min T1 | min T2 | min f_gap | max eixo mrad | max readout |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| NISQ_bom_99p9 | 50 | 1.0e-03 | 1.414e-02 | 333.333 us | 250.000 us | 0.260 GHz | 24.495 | 2.000e-04 |
| fault_tolerance_99p99 | 50 | 1.0e-04 | 4.472e-03 | 3333.333 us | 2500.000 us | 0.822 GHz | 7.746 | 2.000e-05 |
| alto_99p999 | 50 | 1.0e-05 | 1.414e-03 | 33333.333 us | 25000.000 us | 2.599 GHz | 2.449 | 2.000e-06 |
| ultra_99p9999 | 50 | 1.0e-06 | 4.472e-04 | 333333.333 us | 250000.000 us | 8.219 GHz | 0.775 | 2.000e-07 |
| porta_rapida_99p99 | 5 | 1.0e-04 | 4.472e-03 | 333.333 us | 250.000 us | 8.219 GHz | 7.746 | 2.000e-05 |

## Leitura GDQ

Esses requisitos são os alvos que a construção GDQ precisa atingir pela
Hessiana e pelo contorno:

$$
K_{\rm phys}
\to
\Delta_{\rm gap},
\qquad
P_\perp\delta K P_Q
\to
J,
\qquad
\mathsf R_{\rm app}
\to
p_{\rm read}.
$$

Se a GDQ reduzir $J/\Delta$ e melhorar $T_1,T_2$ sem piorar readout, ela
pode reduzir overhead. Se não conseguir, fica apenas como reinterpretação
geométrica do qubit operacional.

$$
\boxed{
\text{a próxima prova física da Q76 é calcular esses requisitos, não postulá-los.}
}
$$
