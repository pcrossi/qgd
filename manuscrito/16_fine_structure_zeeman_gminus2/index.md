---
title: "16. Estrutura fina, Zeeman e g-2"
---

# 16. Estrutura fina, Zeeman e $g-2$

Este capítulo trata a resposta magnética como GDQ, não como uma importação da
teoria de Dirac ou da QED. O campo magnético é um dado clássico do aparelho:
fonte, contorno ou vínculo externo. A partícula já possui circulação, carga e
rigidez geométrica antes da medição.

A cadeia de construção usada aqui é:

$$
J_{\rm app}^{\rm clássico}
\to
\delta\Phi_{\rm app}
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\text{resposta magnética}
\to
\text{registro}.
$$

No setor fraco e quase uniforme, essa cadeia reduz a três resultados:

1. a constante de estrutura fina entra como normalização herdada da ponte
   global--local;
2. o efeito Zeeman vem da seleção de eixo por Noether e isotropia;
3. o termo mínimo $g=2$ e a correção líder $\alpha/(2\pi)$ são respostas
   geométricas, enquanto os resíduos metrológicos de $g-2$ exigem canais
   superiores da Hessiana.

O objetivo não é afirmar que todo $g-2$ já está numericamente fechado. O
objetivo é mostrar o operador correto que deve substituir, na GDQ, a linguagem
operacional de vértices:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,K_{\ell,\rm phys}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,K_{\ell,\rm phys}^{+}c_\ell\rangle
}.
$$

## Seções

- [[16.1 - A constante de estrutura fina herdada]]
- [[16.2 - Circulação, carga e momento magnético]]
- [[16.3 - Campo magnético como fonte e contorno]]
- [[16.4 - Efeito Zeeman por Noether e isotropia]]
- [[16.5 - Por que o termo mínimo é g igual a 2]]
- [[16.6 - O fator alpha sobre 2pi]]
- [[16.7 - O operador Hessiano da anomalia]]
- [[16.8 - Relação com a hierarquia leptônica]]
- [[16.9 - Comparação, limites e programa metrológico]]

## Notas chamadas

- [[notes/electromagnetism/alpha_media_einstein|Alpha como média de Einstein]]
- [[notes/electromagnetism/zeeman_noether_isotropia|Zeeman por Noether e isotropia]]
- [[notes/electromagnetism/acoplamento_1forma_2forma_zeeman|Acoplamento por 1-forma e 2-forma]]
- [[notes/electromagnetism/g2_protecao_noether|Proteção de Noether de g igual a 2]]
- [[notes/electromagnetism/fator_1_sobre_2pi_circulacao|Fator 1 sobre 2 pi]]
- [[notes/electromagnetism/gmenos2_hessiana_transversal|Hessiana transversal de g-2]]
- [[notes/electromagnetism/canais_superiores_gmenos2|Canais superiores de g-2]]
- [[notes/electromagnetism/auditoria_gmu2_pendente|Auditoria pendente de g-2]]
- [[notes/electromagnetism/provas_formais_resposta_magnetica|Provas formais da resposta magnética]]

## Scripts e verificações

- [[scripts/README|Scripts do Capítulo 16]]

## Status

| Bloco | Status | Observação |
|---|---|---|
| $\alpha$ | fechado condicionalmente | média isotrópica de Einstein e ponte global--local |
| Zeeman | fechado estruturalmente | fonte externa, Noether e isotropia |
| $g=2$ | teorema condicional no setor mínimo | circulação conservada e mapa magnético $\gamma_0=q/(mc)$ |
| $\alpha/(2\pi)$ | fechado no canal líder reduzido | norma harmônica exata e identificação do canal transversal primitivo |
| canal superior direto uniforme | fechado negativamente | regra de Hodge dá $\mu_{2,\ell}^{\rm direto}=0$ |
| rota superior | fechada como programa preciso | mistura Hessiana mediada por densidade |
| $g_e$ completo | aberto metrologicamente | requer sela 8D física e contração superior |
| $g_\mu-2$ completo | aberto metrologicamente | não deve ser obtido por ajuste posterior |

Formalização Lean:
[MagneticResponse.lean](../../formal/GDQ/MagneticResponse.lean).

[[../15_leptonic_hierarchy_masses/index|← Previous chapter]] | [[../17_baryonic_structure/index|Next chapter →]]
