# Questão 44

## Status vigente

Q44 está consolidada no manuscrito autocontido como fechamento condicional no
setor Madelung de fundo fixo com detector linear reduzido.

Destino consolidado:

- [Capítulo 12 — Tunelamento, dupla fenda, escolha retardada e transporte](../../manuscrito/12_tunneling_interference_transport/index.md)

Resultados preservados no manuscrito:

$$
\rho_{\rm det}
=
I_1+I_2
+
2e^{-\Gamma_{\rm det}}
\sqrt{I_1I_2}\cos\Delta\phi,
$$

com:

$$
\Gamma_{\rm det}
=
\frac12
\zeta_{\rm det}^2
C_{\rm path}
\lambda_{\rm det}\coth(\lambda_{\rm det}L).
$$

No teste reduzido:

$$
\lambda_{\rm det}=1.1,
\qquad
L=1,
\qquad
\mathsf R_{\rm det}=1.37414284103.
$$

Para $N=8000$:

| $\zeta_{\rm det}$ | $\Gamma_{\rm det}$ | $e^{-\Gamma_{\rm det}}$ |
|---:|---:|---:|
| $0$ | $0$ | $1$ |
| $0.5$ | $0.171767855$ | $0.842174657$ |
| $1.25$ | $1.073549095$ | $0.341793305$ |
| $2.5$ | $4.294196378$ | $0.013647535$ |

## Enunciado

- [44-0.md](44-0.md)

## Documento principal

- [questao_44.md](questao_44.md)

## Arquivos relacionados

- [Capítulo legado — Experimento da Dupla Fenda](../../pt-br/37%20-%20Experimento%20da%20Dupla%20Fenda.md)
- [Script legado de visualização](../../src/plot_dupla_fenda.py)
- [Figura legada](../../figs/dupla_fenda_comparacao.png)
- [Auditoria dos scripts](associados/auditoria_scripts_dupla_fenda_q44.md)
- [Plano para solução final completa](associados/plano_solucao_final_q44.md)
- [Derivação do detector por DtN/Schur](associados/derivacao_detector_dtn_q44.md)
- [Solver reduzido com detector](associados/resolver_dupla_fenda_detector_q44.py)
- [Saída do solver reduzido](associados/saida_solver_detector_q44.md)

## Status

Fechada condicionalmente no setor Madelung com detector linear reduzido. A
decoerência foi derivada por impedância DtN/Schur do aparelho. Permanece como
aplicação futura calcular os parâmetros microscópicos de um detector material
real.
