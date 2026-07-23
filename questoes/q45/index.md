# Questão 45 — Hartman

## Status vigente

Q45 está consolidada no manuscrito autocontido como teorema reduzido
condicional no setor evanescente unidimensional.

Destino consolidado:

- [Capítulo 12 — Tunelamento, dupla fenda, escolha retardada e transporte](../../manuscrito/12_tunneling_interference_transport/index.md)

Resultado central:

$$
\rho(x)=\rho_0e^{-2\kappa x}
\quad\Longrightarrow\quad
g_{xx}(x)=g_0\frac{\rho(x)}{\rho_0}
=
g_0e^{-2\kappa x},
$$

sob barreira estacionária, corrente real suprimida, transversais congeladas,
interface normalizada e calibre longitudinal.

Assim:

$$
D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right),
$$

e:

$$
\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Com $\kappa=g_0=v_0=1$, o teste reduzido dá:

| $L$ | $D_{\rm prop}(L)$ | fração do limite |
|---:|---:|---:|
| $0.1$ | $0.095162581964$ | $0.095162581964$ |
| $1.0$ | $0.632120558829$ | $0.632120558829$ |
| $4.0$ | $0.981684361111$ | $0.981684361111$ |
| $8.0$ | $0.999664537372$ | $0.999664537372$ |

Documento principal:

- [[questao_45]]

Enunciado preservado:

- [[45-0 1]]

Associados:

- [[associados/derivacao_reduzida_hartman_gdq]]
