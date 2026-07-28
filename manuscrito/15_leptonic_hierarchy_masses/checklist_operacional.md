---
title: "Checklist operacional — Capítulo 15"
---

# Checklist operacional — Capítulo 15

## 1. Enunciado

Derivar razões leptônicas como rigidezes geométricas adimensionais da GDQ,
sem confundir calibração de unidade, benchmark espectral auxiliar ou fórmula
empírica com fundamento ontológico.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Massa como custo geométrico | Estrutural | Energia de sustentação do defeito. |
| Escala absoluta | Metrológica | MeV exige padrão externo de unidade. |
| Rosen--Morse | Benchmark auxiliar | Não identifica gerações. |
| Múon | Teorema condicional no modelo reduzido intrínseco | $\frac32\alpha^{-1}+\frac65+2\alpha$ dados os três coeficientes geométricos reduzidos. |
| Tau | Candidato por saturação geométrica condicional | Koide produz dois ramos; a seleção pesada exige Hessiana física. |
| Quarta direção primitiva | Excluída no suporte reduzido | Não há quatro direções independentes em $\mathbb R^3$; isso não é no-go global de todos os estados. |
| Redução Perelman 3D/8D | Teorema condicional fechado | Perelman atua no fator curvo $B_3$, não no 8D geral. |
| Background 8D produto | Fechado | $a_W=a_f=a_H=\varepsilon=0$ e $\Delta_{\rm Schur}=0$. |
| Hessiana 8D produto | Fechada | $J=0$, Schur preserva razões. |
| Warped/misto | Condicional | Critério $j_{\rm mix}^2/m_\perp^2<\lambda_B^{\rm gap}$. |

## 3. Cadeia construtiva

$$
\mathcal S_{\rm GDQ}
\to
\Phi_\ell
\to
K_{\rm phys}^{\ell}
\to
P_k
\to
R_\mu
\to
Q=\frac23
\to
R_\tau
\to
H_B-JH_\perp^{-1}J^\dagger.
$$

## 4. Scripts finais/reduzidos

| Script | Classificação |
|---|---|
| `tensao_intrinseca_mu_tau.py` | Avaliação direta da rota GDQ intrínseca. |
| `derivacao_simbolica_hierarquia_leptonica.py` | Derivação simbólica das fórmulas reduzidas. |
| `koide_saturacao.py` | Verificação da saturação geométrica e dois ramos. |
| `perelman_reducao_3d_bulk8.py` | Verificação simbólico-numérica da redução 3D no bulk 8D fatorado. |
| `background_8d_estacionario.py` | Avaliação direta dos parâmetros $a_W,a_f,a_H,\varepsilon,\lambda_B^{\rm gap}$. |
| `hessiana_8d_schur.py` | Teste de Schur produto/warped-misto reduzido. |
| `criterio_warped_misto.py` | Teste do critério subcrítico para backgrounds mistos. |
| `hierarquia_8d_schur_resposta.py` | Resposta 8D das razões sob complemento de Schur. |
| `rosen_morse_benchmark.py` | Benchmark auxiliar, não ontologia. |
| `verificar_calibracao_metrologica.py` | Verificação simbólico-numérica da calibração metrológica. |

## 5. Pontos que não podem ser esquecidos

- Não declarar massa absoluta sem calibração.
- Não confundir $\Lambda_C$, $\widehat\Lambda_\tau$, massas setoriais e
  escala metrológica $E_0$.
- Não usar Rosen--Morse como geração física.
- Não usar Koide como entrada empírica.
- Não chamar correções de renormalização fundamental.
- Não omitir Hessiana/Schur na elevação 8D.
- Não promover ramo leve de Koide sem Hessiana própria.
- Não chamar o ramo pesado de estável apenas porque satisfaz a saturação.
- Não transportar $3\sqrt2/5$ para backgrounds mistos sem recalcular o DtN.
- Não carregar tentativas infrutíferas para a narrativa principal.
