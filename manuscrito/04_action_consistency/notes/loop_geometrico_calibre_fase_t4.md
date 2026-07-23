---
title: "Loop geométrico de calibre pela fase toroidal"
---

# Loop geométrico de calibre pela fase toroidal

Esta nota registra o teste mínimo de preservação de calibre em loops derivado
diretamente da ação oficial da GDQ. O objetivo é evitar a rota incorreta em
que um loop fermiônico externo é tratado como fundamental. O campo usado aqui
é a fase do próprio campo $f$.

## 1. Background e flutuação

No bulk local oficial:

$$
M=\mathbb R^4\times T^4,
$$

escrevemos, ao redor de um fundo real constante:

$$
f=f_\ast+i\chi,
\qquad
\bar f=f_\ast-i\chi.
$$

Então:

$$
\frac{f+\bar f}{2}=f_\ast,
$$

e a medida não varia no setor de fase:

$$
\mathcal U=\mathcal U_\ast.
$$

O termo cinético da ação oficial dá:

$$
g^{MN}\partial_Mf\partial_N\bar f
=
g^{MN}\partial_M\chi\partial_N\chi.
$$

Logo a segunda variação no setor de fase tem a forma:

$$
S_\chi^{(2)}
=
\frac{Z_\chi}{2}
\int_M
g^{MN}\partial_M\chi\partial_N\chi\,dV_g,
$$

com $Z_\chi>0$. Esse fator global não afeta a identidade de Ward, pois
$\operatorname{Tr}\log Z_\chi$ é independente da conexão efetiva.

## 2. Conexão como componente métrica

Escolha um ciclo $S^1\subset T^4$ com coordenada periódica $y\sim y+2\pi$.
A métrica fibrada é:

$$
ds^2
=
h_{\mu\nu}dx^\mu dx^\nu
+R^2(dy+\kappa A_\mu dx^\mu)^2
+ds_{T^3}^2.
$$

Aqui $A_\mu$ não foi adicionado como campo fundamental. Ele é a componente de
fibração métrica do ciclo toroidal.

Expanda a fase:

$$
\chi(x,y)
=
\sum_{n\in\mathbb Z}
\chi_n(x)e^{iny},
\qquad
\chi_{-n}=\bar\chi_n.
$$

A derivada horizontal atua no modo $n$ como:

$$
D_\mu^{(n)}
=
\partial_\mu-iq_nA_\mu,
\qquad
q_n=n\kappa.
$$

O autovalor interno é:

$$
m_n^2
=
\frac{n^2}{R^2}
+\lambda_\perp.
$$

Para o modo fundamental isolado, pode-se tomar $\lambda_\perp=0$.

## 3. Hessiana física reduzida

O par real de modos $n,-n$ equivale a um modo complexo carregado. A Hessiana
reduzida é:

$$
H_n[A]
=
-
(D^{(n)})^2
+m_n^2.
$$

A integral gaussiana desse par de modos reais produz:

$$
\Gamma_n^{(1)}[A]
=
\operatorname{Tr}\log H_n[A].
$$

Portanto a cadeia de uma volta é:

$$
\mathcal S_{\rm GDQ}
\longrightarrow
S_\chi^{(2)}
\longrightarrow
H_n[A]
\longrightarrow
\Gamma_n^{(1)}[A].
$$

## 4. Tempo próprio e covariância

Com resolução espectral $s_0>0$:

$$
\Gamma_{n,s_0}^{(1)}[A]
=
-
\operatorname{Tr}
\int_{s_0}^{\infty}
\frac{ds}{s}
e^{-sH_n[A]}.
$$

Sob transformação abeliana de calibre:

$$
A\mapsto A+\partial\lambda,
$$

o operador transforma por conjugação:

$$
H_n[A+\partial\lambda]
=
e^{iq_n\lambda}
H_n[A]
e^{-iq_n\lambda}.
$$

Logo:

$$
\operatorname{Tr}F(H_n[A+\partial\lambda])
=
\operatorname{Tr}F(H_n[A])
$$

para qualquer função espectral admissível $F$. Assim:

$$
\partial_\mu
\frac{\delta\Gamma_{n,s_0}^{(1)}}{\delta A_\mu}
=0.
$$

Essa é a identidade de Ward na forma geométrica.

## 5. Polarização

A expansão de $|D\chi_n|^2$ contém dois vértices lineares
$A\chi\partial\chi$ e um vértice quadrático de contato $A^2|\chi|^2$. O termo
de contato é obrigatório: ele completa a transversalidade.

Defina:

$$
u=x(1-x),
\qquad
\eta_n=s_0m_n^2.
$$

Depois da subtração infravermelha $\Pi_n(0)=0$, a função escalar é:

$$
\Pi_{n,s_0}(Q^2)
=
\frac{q_n^2}{16\pi^2}
\int_0^1dx\,
(1-2x)^2
\left[
E_1(\eta_n)
-
E_1\left(s_0[m_n^2+uQ^2]\right)
\right].
$$

O tensor completo é:

$$
\Pi_{\mu\nu}^{(n)}(Q)
=
(Q_\mu Q_\nu-Q^2\delta_{\mu\nu})
\Pi_{n,s_0}(Q^2).
$$

Portanto:

$$
Q^\mu\Pi_{\mu\nu}^{(n)}(Q)=0.
$$

## 6. Limites

Na janela $m_n^2\ll Q^2\ll s_0^{-1}$:

$$
\Pi_n(Q^2)
\simeq
\frac{q_n^2}{48\pi^2}
\log\frac{Q^2}{m_n^2}
+\text{constante}.
$$

No ultravioleta geométrico:

$$
\Pi_{n,s_0}(\infty)
=
\frac{q_n^2}{48\pi^2}
E_1(\eta_n)
<
\infty.
$$

Isso demonstra simultaneamente:

1. um loop completo derivado da ação oficial;
2. preservação de Ward no setor declarado;
3. saturação ultravioleta;
4. ausência de massa de gauge gerada por loop, pois $\Pi_n(0)=0$.

## 7. Interpretação dos fantasmas

Neste teste abeliano, o determinante de Faddeev--Popov é:

$$
\Delta_{\rm FP}^{U(1)}
=
\det(-\partial^2),
$$

independente de $A$. Ele não participa dinamicamente da polarização.
Fantasmas podem representar esse jacobiano em linguagem externa, mas não são
campos ontológicos da GDQ.

## 8. Extensão não abeliana

No setor não abeliano, a condição suficiente é preservar a covariância
espectral:

$$
L_{A^g}
=
g^{-1}L_Ag.
$$

Então:

$$
\operatorname{Tr}F_\tau(L_{A^g})
=
\operatorname{Tr}F_\tau(L_A),
$$

e a identidade funcional resultante é:

$$
\mathcal S(\Gamma_\tau)=0.
$$

Essa é a forma geométrica de Slavnov--Taylor. O jacobiano de gauge continua
sendo parte do quociente; sua representação por fantasmas é opcional.

## 9. Status

O teste mínimo de calibre em loops está fechado no setor geométrico declarado.
O que permanece como refinamento posterior é calcular coeficientes locais
completos em fundos não abelianos, torsionais e topologicamente não triviais.

