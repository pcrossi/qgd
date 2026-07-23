---
title: "Checklist operacional — Capítulo 7"
---

# Checklist operacional — Capítulo 7

Este checklist registra o estado do Capítulo 7, dedicado ao limite clássico e
ao princípio da correspondência na GDQ.

O capítulo deve permanecer didático, mas sem vender o limite clássico como uma
substituição formal $\hbar\to0$. A constante $\hbar$ não desaparece. O que se
torna pequeno é uma razão adimensional entre o comprimento de de Broglie
reduzido e a escala de variação da densidade.

## 1. Enunciado do capítulo

No setor regular de Madelung selecionado nos Capítulos 5 e 6, com

$$
p_\rho=0,
\qquad
\Pi_{S_R}=\sqrt h\,\rho,
$$

define-se

$$
\varepsilon_{\rm cl}
=\frac{\hbar}{pL_\rho}.
$$

Quando $\varepsilon_{\rm cl}\ll1$, longe de nós, bordos abruptos e cáusticas,
o termo de Bohm é subdominante:

$$
\frac{|Q_B|}{T_{\rm cl}}
=O(\varepsilon_{\rm cl}^2).
$$

Assim, Hamilton--Jacobi--Bohm reduz-se a Hamilton--Jacobi clássica; suas
características dão Hamilton/Newton; a continuidade induz Liouville no
ensemble monocinético.

## 2. Status lógico

| Bloco | Status | Observação |
|---|---|---|
| Limite Hamilton--Jacobi | Fechado condicionalmente | Vale no setor regular de Madelung com $\varepsilon_{\rm cl}\ll1$. |
| Características Hamilton/Newton | Demonstrado no setor | Segue da equação Hamilton--Jacobi limite. |
| Liouville | Demonstrado antes de cáusticas | Após cáusticas exige múltiplos ramos ou medida geral. |
| WKB/fase estacionária | Correspondência efetiva | Confere a forma usual, mas não substitui a derivação GDQ. |
| Cotangente $\to$ Kepler | Demonstrado como limite local | Normalização do acoplamento continua setorial. |
| Noether clássico | Demonstrado condicionalmente | Conserva se redução e bordo preservam a simetria. |
| Maxwell macroscópico | Fechado condicionalmente | Forma $F=dA$ e equação fonte vêm do setor $U(1)_Q$ efetivo. |
| Einstein/Newton macroscópico | Fechado condicionalmente | Forma métrica clássica exige média torsional e fechamento hidrodinâmico. |

## 3. Cadeia dedutiva escalar

A cadeia escalar do capítulo é:

$$
\mathcal S_{\rm GDQ}
\to
\text{setor Madelung}
\to
(\rho,S_R)
\to
\text{Hamilton--Jacobi--Bohm}
\to
\varepsilon_{\rm cl}\ll1
\to
\text{Hamilton--Jacobi}
\to
\text{Hamilton/Newton}
\to
\text{Liouville}.
$$

O capítulo não prova novamente a polarização de Madelung. Essa seleção pertence
aos Capítulos 5 e 6.

## 4. Pontos que precisam permanecer explícitos

- O limite clássico não é $\hbar=0$.
- A GDQ não é reduzida ontologicamente à mecânica quântica usual.
- A forma de Schrödinger/WKB é uma representação efetiva do setor de
  Madelung.
- A trajetória clássica única exige localização adicional em fase; o limite
  natural é primeiro um ensemble.
- Nós, bordos abruptos, cáusticas, núcleos de estômato e regiões torsionais
  podem invalidar o limite escalar simples.
- Torção não precisa desaparecer em experimentos sensíveis a spin,
  polarização, vorticidade ou contorno.
- Maxwell e Einstein aparecem como correspondências macroscópicas setoriais,
  não como novas ações fundamentais.

## 5. Conteúdo histórico incorporado

O mapa de preservação registra a incorporação do material histórico:

[[preservation_map|Mapa de preservação do Capítulo 7]]

Foram preservados e corrigidos:

- desaparecimento relativo do termo de Bohm;
- Hamilton--Jacobi e Newton;
- Liouville e ensemble;
- WKB e fase estacionária;
- potencial cotangente global e limite local de Kepler;
- Noether clássico;
- correspondência de Maxwell;
- correspondência métrica Einstein/Newton;
- ressalva sobre $g-2$ e mésons como fenomenologia futura, não prova do
  limite clássico.

## 6. Notas e cálculos longos

O corpo principal deve permanecer educativo. Provas longas podem ficar nas
notas:

- [[../notes/classical/Tensor energia-momento via Hessiana de f]];
- [[../notes/classical/Analise dimensional do acoplamento gravitacional]].

Essas notas preservam contas longas sem inflar a linha didática principal.

## 7. Scripts opcionais recomendados

Os scripts do capítulo devem ser autocontidos e classificados como
verificações didáticas. Eles não calculam novas constantes fundamentais.

Recomenda-se a pasta:

`manuscrito/07_classical_limit/scripts/`

com:

| Script | Função |
|---|---|
| `verificar_bohm_epsilon_cl.py` | Mostra numericamente $|Q_B|/T_{\rm cl}\sim\varepsilon_{\rm cl}^2$. |
| `verificar_hamilton_newton.py` | Verifica que as características de Hamilton reproduzem Newton para um potencial teste. |
| `verificar_liouville_monocinetico.py` | Verifica a conservação de uma densidade transportada antes de cáusticas. |
| `verificar_cotangente_kepler.py` | Mostra o limite local do potencial cotangente para $1/r$. |
| `verificar_noether_classico.py` | Testa conservação de energia e momento angular em sistemas com simetrias preservadas. |

## 8. Extensões que não reabrem o capítulo

Não são lacunas internas do Capítulo 7:

- derivação metrológica de $\alpha$;
- derivação final de $G$;
- resposta de aparelhos reais;
- Lamb shift, hiperfina ou anomalias magnéticas;
- setor completo de partículas;
- prova de todos os backgrounds admissíveis.

Esses problemas usam correspondências clássicas ou macroscópicas, mas
pertencem a capítulos e apêndices setoriais próprios.

## 9. Critério de fechamento

O Capítulo 7 está pronto quando:

1. o limite escalar estiver formulado por $\varepsilon_{\rm cl}$;
2. as hipóteses de regularidade e domínio estiverem próximas das equações;
3. Hamilton/Newton e Liouville forem apresentados como consequências;
4. WKB for tratado como verificação efetiva, não fundamento;
5. Maxwell e Einstein forem apresentados como correspondências setoriais;
6. normalizações contínuas forem separadas das formas clássicas;
7. o material histórico for preservado sem reintroduzir afirmações não demonstradas.

## Revisão didática de 2026-07-19

O Capítulo 7 foi conferido na fase de revisão científica/didática. O corpo
principal foi limpo de linguagem histórica desnecessária: as seções de
correspondência vetorial e métrica agora apresentam as construções de forma
positiva e autocontida, sem depender do leitor conhecer versões anteriores do
texto.

Os scripts do capítulo devem permanecer como verificações didáticas: escala do
termo de Bohm, Hamilton--Newton, Liouville monocinético, potencial
cotangente--Kepler e Noether clássico. Eles verificam passos de
correspondência e não são previsões metrológicas.
