---
title: "Checklist operacional — Capítulo 16"
---

# Checklist operacional — Capítulo 16

## 1. Enunciado

Construir, em linguagem GDQ, a constante de estrutura fina herdada, o efeito
Zeeman, o termo mínimo $g=2$, o termo líder $\alpha/(2\pi)$ e o operador
Hessiano que define a anomalia magnética.

## 2. Cadeia construtiva

$$
J_{\rm app}^{\rm clássico}
\to
\delta\Phi_{\rm app}
\to
K_{\rm phys}
\to
\mathsf R_{\rm app}
\to
\Delta E_{\rm Zeeman}
\to
a_\ell.
$$

## 3. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| $\alpha$ | fechado condicionalmente | média de Einstein e ponte global--local |
| Zeeman | fechado estruturalmente | Noether, isotropia e fonte externa |
| $g=2$ | teorema condicional no setor mínimo | Noether conserva a circulação; o mapa mínimo fixa $\gamma_0=q/(mc)$ |
| $\alpha/(2\pi)$ | fechado no canal líder reduzido | norma harmônica exata; identificação modal declarada |
| Hessiana operacional | construída e corrigida | o multiplicador conserva a circulação sem projetar fora $c_\ell$ |
| resíduos metrológicos | abertos | exigem canais superiores de $H_{C,\ell}$ |

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `calcular_alpha_media_einstein.py` | Avaliação direta da média geométrica herdada. |
| `calcular_projetor_iso_hessiana.py` | Avaliação direta do projetor isotrópico da Hessiana média. |
| `teste_schur_dtn_alpha.py` | Diagnóstico Schur/DtN sem ajuste da impedância redonda. |
| `zeeman_resposta_linear.py` | Verificação simbólico-numérica da resposta Zeeman. |
| `gmenos2_termo_lider.py` | Avaliação direta de $a^{(1)}=\alpha/(2\pi)$. |
| `avaliar_hessiana_anomalia.py` | Teste de consistência do bloco Hessiano líder. |
| `teste_hierarquia_nao_substitui_gmenos2.py` | Diagnóstico que separa a hierarquia leptônica de o setor Zeeman/g-2. |

## 5. Pontos preservados

- O campo magnético é fonte/contorno de aparelho, não novo termo fundamental.
- $g=2$ não é importado de Dirac.
- $\alpha/(2\pi)$ não é chamado de loop ontológico.
- Noether não é usado sozinho para determinar o coeficiente da fonte externa.
- $P_{\rm phys}$ não elimina o modo $c_\ell$ antes da resposta do multiplicador.
- a hierarquia leptônica fornece background leptônico, não resposta magnética completa.
- Blocos `required` históricos de o setor Zeeman/g-2 não são migrados como previsão.
- Fórmulas fenomenológicas de $g_\mu-2$ ficam como programa futuro até a Hessiana superior.
