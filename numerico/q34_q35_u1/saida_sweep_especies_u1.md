# Varredura multiespécie $U(1)$ — Q34/Q35

## Classificação

**Avaliação direta e teste de consistência.** A fronteira calculada não
prediz $\Lambda_{\rm EM}$; informa apenas que condição uma derivação
geométrica posterior precisa satisfazer.

## Fórmula

$$
\Pi_{\rm EM}(\infty)=\frac{\alpha_0}{3\pi}
\sum_f N_c^{(f)}Q_f^2
E_1\!\left(\frac{m_f^2}{\Lambda_{\rm EM}^2}\right).
$$

A fronteira é definida por $\Pi_{\rm EM}(\infty)=1$.

## Resultados

| cenário | espécies | $\sum N_cQ^2$ | $\log_{10}(\Lambda_{\rm crit}/m_e)$ | $\Pi$ na raiz |
|:---|---:|---:|---:|---:|
| léptons GDQ | 3 | 3.000000 | 95.561913582 | 1.000000000000 |
| férmions carregados — benchmark | 9 | 8.000000 | 37.803035603 | 1.000000000000 |

Uma década abaixo e acima da raiz:

| cenário | $\Pi(\Lambda_{\rm crit}/10)$ | $\Pi(10\Lambda_{\rm crit})$ | monotônica |
|:---|---:|---:|:---:|
| léptons GDQ | 0.989303021 | 1.010696979 | True |
| férmions carregados — benchmark | 0.971474723 | 1.028525277 | True |

## Espectro: léptons GDQ

| espécie | $m_f/m_e$ | $Q_f$ | $N_c$ | peso | proveniência |
|:---|---:|---:|---:|---:|:---|
| e | 1 | -1 | 1 | 1 | unidade metrológica |
| mu | 206.767399 | -1 | 1 | 1 | razão espectral Q39 |
| tau | 3477.13178 | -1 | 1 | 1 | razão espectral Q39 |

## Espectro: férmions carregados — benchmark

| espécie | $m_f/m_e$ | $Q_f$ | $N_c$ | peso | proveniência |
|:---|---:|---:|---:|---:|:---|
| e | 1 | -1 | 1 | 1 | referência externa |
| mu | 206.768283 | -1 | 1 | 1 | referência externa |
| tau | 3477.22828 | -1 | 1 | 1 | referência externa |
| u | 4.22701456 | 0.666667 | 3 | 1.33333 | massa de quark dependente de esquema |
| d | 9.13896203 | -0.333333 | 3 | 0.333333 | massa de quark dependente de esquema |
| s | 181.99646 | -0.333333 | 3 | 0.333333 | massa de quark dependente de esquema |
| c | 2485.328 | 0.666667 | 3 | 1.33333 | massa de quark dependente de esquema |
| b | 8180.05595 | -0.333333 | 3 | 0.333333 | massa de quark dependente de esquema |
| t | 338082.886 | 0.666667 | 3 | 1.33333 | massa de quark dependente de esquema |

## Limitações

- O cenário léptons GDQ usa as razões espectrais registradas na Q39.
- O cenário com quarks é benchmark externo: massas de quarks dependem de
  esquema e escala e não foram derivadas neste cálculo.
- A raiz extremamente alta é consequência matemática da extrapolação
  efetiva; não deve ser chamada de escala GDQ prevista.
- A próxima etapa estrutural continua sendo obter $\Lambda_{\rm EM}$ da
  Hessiana e do espectro eletromagnético.
