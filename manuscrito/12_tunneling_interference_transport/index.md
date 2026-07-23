---
title: "12. Tunelamento, dupla fenda, escolha retardada e transporte"
---

# 12. Tunelamento, dupla fenda, escolha retardada e transporte

Este capítulo trata fenômenos que parecem paradoxais quando são descritos
como partículas pontuais atravessando um espaço rígido: tunelamento, dupla
fenda, perda de franjas por detector e escolha retardada.

Na GDQ, a leitura correta é por densidade, fase, contorno e transporte. A
ação oficial não é alterada. Barreiras, fendas, detectores e recombinadores
entram como dados externos do aparelho:

$$
J_{\rm app}^{\rm classico}
\to
\delta\Phi_{\rm app}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
\mathsf R_{\rm app}
\to
\text{resposta de transporte}
\to
\text{registro}.
$$

## Roteiro

- [[12.1 - Tunelamento e o paradoxo de Hartman]]
- [[12.2 - Modelo geométrico reduzido da barreira]]
- [[12.3 - Dupla fenda como problema de contorno]]
- [[12.4 - Densidade, fase e pressão de Bohm nas franjas]]
- [[12.5 - Detector como impedância de interface]]
- [[12.6 - Perda de visibilidade por complemento de Schur]]
- [[12.7 - Escolha retardada sem sinal para o passado]]
- [[12.8 - O que foi demonstrado e o que é metrologia de aparelho]]

## Resultado central

A densidade reduzida de duas fendas com detector pode ser escrita como:

$$
\rho_{\rm det}
=
I_1+I_2
+
2e^{-\Gamma_{\rm det}}
\sqrt{I_1I_2}
\cos\Delta\phi.
$$

O fator de coerência não é postulado:

$$
\mathcal C_{\rm det}=e^{-\Gamma_{\rm det}}.
$$

Ele vem da impedância de contorno do detector:

$$
\Gamma_{\rm det}
=
\frac12
\left\langle
\Delta\Phi_\partial,
\mathsf R_{\rm det}
\Delta\Phi_\partial
\right\rangle,
$$

com:

$$
\mathsf R_{\rm det}
=
K_{\partial\partial}
-
K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Para escolha retardada, o que muda é:

$$
\mathsf R_{\rm old}\to\mathsf R_{\rm new}.
$$

Não há sinal físico para o passado. Há mudança de contorno efetivamente
realizado antes do registro final.

## Estatuto do resultado

| Bloco | Status | Observação |
|---|---|---|
| Hartman por distância própria saturada | Teorema reduzido condicional | $g_{xx}\propto\rho$ vale no canal evanescente declarado, não universalmente. |
| Dupla fenda sem detector | Fechada no setor Madelung plano | Recupera interferência operacional conhecida. |
| Nós como barreira de Bohm | Redução efetiva | Manifestação geométrica dos zeros de $\rho$. |
| Detector linear | Fechado estruturalmente | DtN/Schur em canal reduzido. |
| Perda de visibilidade | Fechada condicionalmente | $\exp(-\Gamma_{\rm det})$. |
| Escolha retardada | Fechada estruturalmente | Contorno/transporte, sem retrocausalidade física. |
| Detector real completo | Programa metrológico | Exige material, geometria e Hessiana completa. |

No caso reduzido validado para dupla fenda com detector:

$$
\lambda_{\rm det}=1.1,
\qquad
L=1,
\qquad
\mathsf R_{\rm det}=1.37414284103,
$$

e a coerência decai de $1$ para $0.013647535$ quando
$\zeta_{\rm det}$ vai de $0$ a $2.5$.

## Controle editorial

- [[checklist_operacional|Checklist operacional do capítulo]]
- [[notes/provas_lemas_definicoes|Provas, lemas e definições associados]]
- [[notes/construcao_gdq_transporte_interferencia|Construção GDQ do transporte e da interferência]]
- [[notes/hartman_ansatz_conformal_unidimensional|Hartman como ansatz conformal unidimensional]]
- [[notes/detector_DtN_Schur_visibilidade|Detector DtN/Schur e visibilidade]]
- [[notes/interferometro_eo_mzi_escolha_retardada|Interferômetro EO-MZI e escolha retardada]]
- [[notes/escolha_retardada_contorno_nao_retrocausal|Escolha retardada como contorno]]
- [[scripts/README|Scripts do Capítulo 12]]

[[../index|← Home]] | [[12.1 - Tunelamento e o paradoxo de Hartman|Next →]]
