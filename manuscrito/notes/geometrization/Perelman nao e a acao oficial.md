---
title: "Perelman não é a ação oficial"
---

# Perelman não é a ação oficial

## Enunciado

O funcional de Perelman é usado na GDQ como matriz geométrica auxiliar para
organizar medida ponderada, entropia geométrica, fluxo e estabilidade. Ele não
substitui a ação física oficial.

## Ação oficial

A ação física fundamental permanece:

$$
\mathcal S_{\rm GDQ}
=
\int_\gamma
\left[
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left(
\tau\left(
\mathcal R
+g^{\mu\bar\nu}\partial_\mu f\,\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right)
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]
\frac{d\tau}{\tau}.
$$

Aqui $\Lambda_C$ é o número de corte adimensional nas coordenadas normalizadas
pela escala de Cartan, e a restauração de unidades físicas usa escalas
separadas, como $k_C=\ell_C^{-1}$ e $E_C=\hbar c k_C$.

## Funcional auxiliar de Perelman

O funcional de Perelman, em sua forma geométrica usual, organiza expressões do
tipo:

$$
\mathcal F(g,\sigma)
=
\int_M
\left(
R+|\nabla\sigma|^2
\right)e^{-\sigma}\,dV_g.
$$

Ele também aparece em versões entrópicas ponderadas por $\tau$. A semelhança
formal com o integrando interno da GDQ é deliberada: ambas as estruturas medem
curvatura, gradiente logarítmico de densidade e peso entrópico.

Mas a GDQ contém dados adicionais que não são meros detalhes:

1. o campo complexo $f$;
2. a densidade constitutiva $\rho=e^{-(f+\bar f)/2}$;
3. a fase real $S_R=\hbar(f-\bar f)/(2i)$;
4. a medida $\mathcal U=\rho/(4\pi z_\tau)^n$;
5. o contorno causal $\gamma$;
6. a conexão Hermitiana/Bismut quando $H\neq0$;
7. os vínculos físicos e condições de contorno do estômato.

Portanto, Perelman fornece a gramática geométrica do fluxo, mas não é a ação
física.

## Uso correto

É correto usar Perelman para:

- identificar monotonicidade geométrica;
- estudar estabilidade de sólitons;
- organizar a medida ponderada;
- interpretar fluxos de calor conjugados;
- construir funcionais auxiliares de Lyapunov;
- comparar singularidades e cirurgias em setores tridimensionais fatorados.

Não é correto usar Perelman para:

- mudar a ação oficial;
- apagar a fase $S_R$;
- substituir a Hessiana física da GDQ;
- declarar automaticamente a existência de backgrounds materiais;
- transportar teoremas tridimensionais para todo bulk 8D sem hipótese de
  fatoração setorial.

## Consequência para a escrita do manuscrito

Quando o texto disser que “Perelman entra”, deve-se ler:

> a estrutura entrópica de Perelman fornece a matriz geométrica auxiliar da
> GDQ.

Não se deve ler:

> a ação física da GDQ foi trocada pelo funcional de Perelman.

Essa distinção preserva a identidade da teoria e evita misturar uma ferramenta
geométrica com o princípio variacional fundamental.

