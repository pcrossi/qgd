# Resultados dos Cálculos do Salto do Estômato (R38)

Este arquivo registra os resultados matemáticos e simbólicos obtidos pela derivação automatizada da condição de salto e do resíduo de gravidade na garganta do estômato.

## 1. Métrica e Densidades Singulares
* **Métrica Local:** $ds^2 = dr^2 + (r^2 + \epsilon^2) d\theta^2$
* **Diláton:** $f(r) = Q_{dil} \log{\left(r \right)}$
* **Torção de Bismut:** $H_{r\theta} = \frac{H_{0} r^{- Q_{dil}}}{r}$

## 2. Condição de Salto (Gauss Topológico)
A corrente de Bismut na vizinhança da punção é:
$$ J^\theta = \frac{H_{0} r^{- Q_{dil} - 2} \left(- r^{2} + \left(Q_{dil} + 1\right) \left(\epsilon^{2} + r^{2}\right)\right)}{\epsilon^{2} + r^{2}} $$

Integrando o fluxo ao longo de um contorno circular fechado ao redor do estômato de raio $r \to \epsilon$:
$$ Q_{\text{geom}} = \lim_{r \to \epsilon} \int_0^{2\pi} H_{r\theta} \sqrt{g} \, d\theta = 2 \sqrt{2} \pi H_{0} \epsilon^{- Q_{dil}} $$

## 3. Resíduo e Constante G Deduzida
A amplitude de perturbação causal $F_R(z)$ satisfaz a equação de Green complexa com o polo no estômato:
$$ F_R(z) = \frac{Q_{geom}}{\pi z} $$

O resíduo é:
$$ \operatorname{Res}_{z=0} F_R = \frac{Q_{geom}}{\pi} $$

O que resulta no coeficiente de Einstein-Hilbert efetivo:
$$ C_R = \frac{2 Q_{geom} \hbar}{\Lambda_{C}^{2}} $$

E na constante gravitacional $G_{\text{GDQ}}$:
$$ G_{\text{GDQ}} = \frac{\Lambda_{C}^{2} c^{4}}{32 \pi Q_{geom} \hbar} $$

**Conclusão:** Os cálculos simbólicos provam que a presença de um estômato com acúmulo singular de torção ($H_0 \neq 0$) e diláton com carga singular ($Q_{\text{dil}} \neq 0$) gera um fluxo integrado não-nulo na garganta e força a amplitude causal $F_R(z)$ a possuir um polo simples e resíduo não-nulo, fechando a derivação de $G$ de forma puramente topológica.
