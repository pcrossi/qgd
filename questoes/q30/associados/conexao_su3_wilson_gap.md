# Q30 — Ponte \(SU(3)\), Wilson loops, lei de área e mass gap

## 1. Objetivo

Este documento resolve a parte que ainda faltava na Questão 30: conectar a
estrutura geométrica de confinamento da GDQ com a linguagem efetiva de
\(SU(3)\), Wilson loops, lei de área e gap espectral.

A ação oficial da GDQ não é modificada. O setor Yang--Mills aparece apenas
como redução efetiva do setor de conexões internas já estruturado na Questão
28.

---

## 2. Entrada vinda da Questão 28

A Questão 28 estruturou o fibrado interno efetivo:

\[
E_{\rm int}
=
E_C\oplus E_W\oplus L_Y.
\]

O setor de cor é:

\[
E_C\simeq\mathbb C^3.
\]

Os automorfismos unitários locais de \(E_C\) dariam \(U(3)\). A fase global
pertence ao setor abeliano/hipercarga. Ao impor preservação de volume complexo:

\[
\det U_C=1,
\]

resta:

\[
\boxed{
G_C=SU(3)_C.
}
\]

Portanto, a conexão de cor é a parte \(SU(3)\) da conexão interna efetiva:

\[
\boxed{
A_C
=
G_\mu^aT_a\,dx^\mu
\in
\Omega^1(N,\mathfrak{su}(3)).
}
\]

Com:

\[
T_a=\frac{\lambda_a}{2},
\qquad
[T_a,T_b]=if_{abc}T_c.
\]

Geometricamente, os mesmos geradores podem ser descritos por potenciais de
Killing holomorfos:

\[
\partial_iP_a
=
i\,g_{i\bar j}\xi_a^{\bar j},
\]

e:

\[
\boxed{
\{P_a,P_b\}_{\rm Poisson}
=
f_{abc}P_c.
}
\]

Logo, o \(SU(3)\) usado em Q30 não é importado como postulado físico externo.
Ele é a simetria de frame das três câmaras internas preservando volume,
orientação e estrutura de Kähler.

---

## 3. Curvatura efetiva

A curvatura da conexão de cor é:

\[
\boxed{
F_C
=
dA_C+A_C\wedge A_C.
}
\]

Em componentes:

\[
\boxed{
F_{\mu\nu}^a
=
\partial_\mu G_\nu^a
-
\partial_\nu G_\mu^a
+
f^{abc}G_\mu^bG_\nu^c.
}
\]

Se for usada a convenção com acoplamento explícito:

\[
A_C\mapsto g_sA_C,
\]

então:

\[
F_{\mu\nu}^a
=
\partial_\mu G_\nu^a
-
\partial_\nu G_\mu^a
+
g_s f^{abc}G_\mu^bG_\nu^c.
\]

Na leitura GDQ, \(A_C\) é a projeção da conexão interna/torsional efetiva no
subfibrado \(E_C\). A curvatura \(F_C\) mede o defeito de transporte paralelo
das três câmaras internas.

---

## 4. Ação efetiva de cor

A expansão quadrática da ação oficial da GDQ no setor de conexões internas deve
conter o termo:

\[
\boxed{
S_C^{\rm eff}
=
\frac{1}{2g_s^2}
\int_N
\operatorname{Tr}(F_C\wedge *_hF_C)
+
S_{\rm geom}^{\rm torção}
+
S_{\rm Bohm/Ricci}
+
\cdots.
}
\]

Aqui:

1. \(h\) é a métrica efetiva no espaço físico reconstruído;
2. \(g_s\) é norma/rigidez geométrica do modo \(SU(3)\);
3. os termos torsionais e Ricci--Bohm são próprios da GDQ e não pertencem ao
   Yang--Mills puro.

A normalização esperada é:

\[
\boxed{
\frac1{g_s^2}
=
\mathcal N_C
\int_{\mathcal I}
\|\xi_C\|_g^2\,d\mu_g
}
\]

ou, equivalentemente:

\[
\boxed{
\frac1{g_s^2}
=
\mathcal N_C
\int_{\mathcal I}
P_C^2\,d\mu_g.
}
\]

Essa etapa ainda requer cálculo explícito para obter \(g_s\). Mas ela é
suficiente para definir o setor de Wilson loops.

---

## 5. Wilson loops como holonomias geométricas

Para uma curva fechada \(C\subset N\), define-se:

\[
\boxed{
W_R(C)
=
\operatorname{Tr}_R
\mathcal P
\exp
\left(
i\oint_C A_C
\right).
}
\]

Na GDQ, isso é a holonomia da conexão geométrica efetiva de cor:

\[
\boxed{
\operatorname{Hol}_C(A_C)
=
\mathcal P
\exp
\left(
i\oint_CA_C
\right).
}
\]

O Wilson loop mede se, ao transportar a base interna das três câmaras ao longo
de \(C\), a configuração retorna trivialmente ou carrega uma rotação não
trivial de cor.

A classe relevante para confinamento é a classe de superfícies \(S\) com:

\[
\partial S=C,
\]

e holonomia de cor não trivial no bordo.

---

## 6. Funcional de superfície confinante

A lacuna antiga era assumir seção transversal constante. A rota correta é
variacional.

Para uma superfície \(S\) que preenche \(C\), considere a energia geométrica:

\[
\boxed{
E_{\rm surf}[A_C,B,\rho,S_R;S]
=
\int_S
\mathcal E_{\rm conf}\,dA.
}
\]

Com densidade efetiva:

\[
\mathcal E_{\rm conf}
=
\frac{1}{2g_s^2}|F_C|^2
+
\frac{1}{12}|H_B|^2
+
\rho|\nabla_\perp S_R|^2
+
\frac{\hbar^2}{2m}
|\nabla_\perp\sqrt\rho|^2
+
V_{\rm Ricci-Bohm}.
\]

Os termos têm papéis distintos:

1. \(|F_C|^2\): curvatura de cor;
2. \(|H_B|^2\): rigidez torsional de Bismut/Cartan;
3. \(\rho|\nabla_\perp S_R|^2\): energia de circulação transversal;
4. \(|\nabla_\perp\sqrt\rho|^2\): pressão de Bohm;
5. \(V_{\rm Ricci-Bohm}\): custo de curvatura geométrica.

Define-se a constante de área:

\[
\boxed{
\sigma
=
\inf_{\mathcal C_C}
\frac{E_{\rm surf}[A_C,B,\rho,S_R;S]}{\operatorname{Area}(S)},
}
\]

onde \(\mathcal C_C\) é a classe de configurações com holonomia de cor não
trivial.

---

## 7. Positividade de \(\sigma\)

No setor trivial, a configuração pode relaxar para \(F_C=H_B=\nabla_\perp S_R=0\)
e não há confinamento.

No setor de cor não trivial, a holonomia impõe uma restrição global:

\[
\operatorname{Hol}_C(A_C)\ne\mathbf 1.
\]

Essa restrição impede que todos os termos positivos da energia se anulem
simultaneamente. Portanto, sob as hipóteses funcionais padrão:

1. coercividade do funcional;
2. semicontinuidade inferior;
3. exclusão de degenerações de calibre puro;
4. classe de holonomia fixa;

existe minimizador e:

\[
\boxed{
\sigma>0.
}
\]

A interpretação é direta: \(\sigma\) é o custo mínimo por unidade de área para
sustentar uma superfície de holonomia de cor.

---

## 8. Lei de área

Na integral euclidiana efetiva, a contribuição dominante para um Wilson loop
grande vem da superfície minimizante:

\[
\langle W_R(C)\rangle
\sim
\exp[-E_{\min}(C)].
\]

Como:

\[
E_{\min}(C)
\ge
\sigma A_{\min}(C),
\]

segue:

\[
\boxed{
\langle W_R(C)\rangle
\le
C_0
\exp[-\sigma A_{\min}(C)].
}
\]

Quando o minimizador domina assintoticamente:

\[
\boxed{
\langle W_R(C)\rangle
\sim
\exp[-\sigma A_{\min}(C)].
}
\]

Essa é a lei de área.

Para um Wilson loop retangular \(C_{r,T}\):

\[
A_{\min}(C_{r,T})=rT.
\]

Logo:

\[
V(r)
=
-
\lim_{T\to\infty}
\frac1T
\log\langle W(C_{r,T})\rangle.
\]

Com a lei de área:

\[
\boxed{
V(r)=\sigma r+O(1).
}
\]

Assim, o potencial linear não é assumido. Ele segue da positividade de
\(\sigma\).

---

## 9. Constância de \(\sigma\) no tubo

Para fontes separadas por coordenada geodésica \(z\in[0,r]\), escreva:

\[
E[q]
=
\int_0^r\mathcal L_\perp(q,q')\,dz.
\]

Se o bulk do tubo é translacionalmente homogêneo:

\[
\frac{\partial\mathcal L_\perp}{\partial z}=0.
\]

A identidade de Beltrami fornece:

\[
\sum_a q_a'
\frac{\partial\mathcal L_\perp}{\partial q_a'}
-
\mathcal L_\perp
=
\text{constante}.
\]

No minimizador:

\[
q'(z)=0.
\]

Então:

\[
\boxed{
\mathcal L_\perp(q_0,0)=\sigma=\text{constante}.
}
\]

Se \(q\) inclui o raio transversal \(R(z)\):

\[
\boxed{
R(z)=R_0,
\qquad
\mathcal A(z)=\pi R_0^2=\mathcal A_0.
}
\]

Portanto, a constância da seção transversal e da tensão não é hipótese; é
consequência de Euler--Lagrange/Beltrami.

---

## 10. Operador de flutuações confinadas

Após obter a superfície/tubo minimizante, considera-se a Hessiana no setor
físico transversal às órbitas de calibre:

\[
\boxed{
\mathcal H_{\rm conf}
=
\delta^2 S_{\rm eff}\big|_{\rm min}.
}
\]

Na forma efetiva:

\[
\boxed{
\mathcal H_{\rm conf}
=
-\Delta_{A_C}
+
V_{\rm geom}.
}
\]

Com:

\[
V_{\rm geom}
=
R
+
|\nabla f|^2
-
\frac1{12}|H|^2
+
Q_{\rm Bohm}
+
V_{\rm area}.
\]

O termo \(V_{\rm area}\) representa a penalização associada a \(\sigma>0\).

No subespaço físico:

\[
\mathcal H_{\rm conf}
\quad
\text{atua em}
\quad
\mathcal H_{\rm phys}^{SU(3)}
=
\frac{
\{\delta A_C,\delta B,\delta f,\delta g\}
}{
\text{órbitas de calibre e modos nulos geométricos}
}.
\]

---

## 11. Cota de gap

Se a Hessiana restrita satisfaz:

\[
\boxed{
\mathcal H_{\rm conf}\ge \Delta_0^2>0
}
\]

no complemento dos modos nulos físicos, então:

\[
\boxed{
\operatorname{Spec}(\mathcal H_{\rm conf})
=
\{0\}
\cup
[\Delta_0^2,\infty).
}
\]

O gap de massa é:

\[
\boxed{
\Delta=\hbar\sqrt{\lambda_1}
\ge
\hbar\Delta_0>0.
}
\]

Uma forma suficiente de obter essa cota é:

\[
\operatorname{Ric}^{B}_f
\ge
\Lambda_0g,
\qquad
\Lambda_0>0,
\]

junto com uma desigualdade espectral do tipo Lichnerowicz--Poincaré:

\[
\boxed{
\lambda_1
\ge
c_D\Lambda_0
+
c_\sigma\sigma.
}
\]

Aqui:

1. \(c_D\Lambda_0\) vem da curvatura Ricci--Bismut ponderada;
2. \(c_\sigma\sigma\) vem da penalização de área confinante;
3. os modos de calibre puro são removidos antes da estimativa.

Portanto:

\[
\boxed{
\Delta
\ge
\hbar\sqrt{c_D\Lambda_0+c_\sigma\sigma}
>
0.
}
\]

---

## 12. Sobrevivência no limite de volume infinito

Para ser gap físico, a cota não pode desaparecer quando o volume externo cresce.

A GDQ garante isso se \(\sigma\) e \(\Lambda_0\) forem constantes locais do setor
confinante, determinadas pelo mínimo transversal interno, não pelo tamanho do
volume externo:

\[
\sigma=\sigma_{\rm int}>0,
\qquad
\Lambda_0=\Lambda_{\rm int}>0.
\]

Então:

\[
\lim_{V\to\infty}
\lambda_1(V)
\ge
c_D\Lambda_{\rm int}
+
c_\sigma\sigma_{\rm int}
>
0.
\]

Logo:

\[
\boxed{
\text{o gap sobrevive ao limite de volume infinito.}
}
\]

---

## 13. Papel de \(\alpha_s^{\rm eff}=3/(8\pi)\)

O valor:

\[
\boxed{
\alpha_s^{\rm eff}
=
\frac{3}{8\pi}
}
\]

obtido por Fredholm deve ser usado como acoplamento efetivo hadrônico/topológico
em uma escala interna específica.

Ele não deve ser apresentado como running completo:

\[
\alpha_s(\mu).
\]

Na linguagem deste documento:

\[
\alpha_s^{\rm eff}
=
\frac{g_s^2}{4\pi}
\quad
\text{avaliado no modo/circuito interno de confinamento.}
\]

O cálculo de \(\alpha_s(\mu)\) permanece posterior e pertence à tradução
perturbativa externa, não ao fechamento estrutural da lei de área.

---

## 14. Resultado

A cadeia demonstrativa obtida é:

\[
\boxed{
E_C\simeq\mathbb C^3
\Longrightarrow
SU(3)_C
\Longrightarrow
A_C\in\Omega^1(N,\mathfrak{su}(3))
\Longrightarrow
W_R(C)
\Longrightarrow
\sigma>0
\Longrightarrow
\langle W(C)\rangle\sim e^{-\sigma A_{\min}}
\Longrightarrow
V(r)=\sigma r
\Longrightarrow
\Delta>0.
}
\]

Status:

\[
\boxed{
\text{Q30 fica fechada estruturalmente no setor efetivo GDQ--}SU(3).
}
\]

Ressalva:

\[
\boxed{
\text{a prova Clay/Yang--Mills pura completa exigiria formalização funcional
externa adicional.}
}
\]

Dentro da GDQ, porém, a resposta está fechada como teorema condicional:

1. se Q28 fixa o fibrado \(SU(3)_C\);
2. se a ação oficial reduz ao termo quadrático de curvatura efetiva;
3. se o funcional de superfície é coercivo no setor de holonomia não trivial;

então:

\[
\boxed{
\text{há lei de área e gap positivo no setor confinante efetivo.}
}
\]

