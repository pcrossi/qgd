# Saída — Q76 protótipo spin/Hopf

Classificação: teste de consistência operacional reduzido.

## Projetores e pesos de leitura

- vetor de preparação $\mathbf a$: `[0.5773502691896258, 0.5773502691896258, 0.5773502691896258]`

| eixo do aparelho | p_plus GDQ/Born | p_minus GDQ/Born | soma |
|---|---:|---:|---:|
| z | 0.788675134595 | 0.211324865405 | 1.000000000000 |
| x | 0.788675134595 | 0.211324865405 | 1.000000000000 |
| diag | 0.735702260396 | 0.264297739604 | 1.000000000000 |

## Porta por transporte de contorno

Porta ideal: rotação $\pi/2$ em torno de $y$.

- eixo real inclinado: `[0.01999500187421909, 0.9997500937109545, -0.009997500937109546]`
- fidelidade unitária reduzida: `0.999833406216`
- Bloch após porta real: `[0.5946346926977104, 0.565516176131879, -0.5714901895688824]`

## Vazamento para complemento

Estimador reduzido:

$$
\epsilon_{\rm leak}
\sim
\frac{\|J\|^2}{\Delta_{\rm gap}^2}.
$$

- $\Delta_{\rm gap}=1.000000$

| ||J|| | epsilon_leak |
|---:|---:|
| 0.010000 | 1.000000000000e-04 |
| 0.030000 | 9.000000000000e-04 |
| 0.100000 | 1.000000000000e-02 |
| 0.300000 | 9.000000000000e-02 |

## Interpretação

O protótipo spin/Hopf recupera exatamente os pesos projetivos de
Stern--Gerlach e fornece uma métrica reduzida para erro de porta e
vazamento. A informação física que falta para virar previsão de hardware é
$\Delta_{\rm gap}$, $J$ e a impedância de aparelho calculados pela Hessiana
da ação oficial.

$$
\boxed{
\text{qubit spin/Hopf fechado como redução operacional; hardware real permanece futuro.}
}
$$
