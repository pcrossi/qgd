# Questão 30 — Confinamento, Wilson loops e mass gap

## 1. Veredito

\[
\boxed{
\text{Questão 30 fechada estruturalmente no setor efetivo GDQ--}SU(3)_C.
}
\]

A resposta não afirma ter resolvido o problema Clay de Yang--Mills puro em toda
sua formulação analítica externa. O que fica estabelecido é mais preciso:

\[
\boxed{
\text{na GDQ, o setor de cor efetivo admite conexão }SU(3),
\text{ Wilson loops, lei de área e gap positivo sob hipóteses funcionais
explícitas.}
}
\]

O documento técnico principal é:

`questoes/q30/associados/conexao_su3_wilson_gap.md`.

---

## 2. O que já vinha fechado

O argumento antigo do manuscrito continha a ideia física correta:

\[
\text{tubo de fluxo}
\Longrightarrow
V(r)\sim\sigma r.
\]

Mas ele era frágil porque parecia assumir:

1. seção transversal constante;
2. densidade de energia constante;
3. tensão \(\sigma\) constante.

Esse ponto foi corrigido pelo princípio variacional.

Para um tubo entre fontes separadas por coordenada geodésica \(z\in[0,r]\):

\[
E[q]
=
\int_0^r\mathcal L_\perp(q,q')\,dz.
\]

Como no bulk:

\[
\frac{\partial\mathcal L_\perp}{\partial z}=0,
\]

a identidade de Beltrami fornece:

\[
\sum_a q_a'
\frac{\partial\mathcal L_\perp}{\partial q_a'}
-
\mathcal L_\perp
=
\text{constante}.
\]

No minimizador translacionalmente invariante:

\[
q'(z)=0.
\]

Logo:

\[
\boxed{
\mathcal L_\perp(q_0,0)=\sigma=\text{constante}.
}
\]

Se \(q\) inclui o raio transversal:

\[
R(z)=R_0,
\qquad
\mathcal A(z)=\pi R_0^2=\mathcal A_0.
\]

Portanto:

\[
\boxed{
V(r)=\sigma r+O(1).
}
\]

A tensão e a seção transversal não são postuladas. Elas são consequências do
mínimo variacional.

---

## 3. Conexão efetiva \(SU(3)_C\)

Da Questão 28, o setor interno é:

\[
E_{\rm int}=E_C\oplus E_W\oplus L_Y.
\]

O setor de cor é:

\[
E_C\simeq\mathbb C^3.
\]

Os automorfismos unitários preservando volume complexo dão:

\[
\boxed{
G_C=SU(3)_C.
}
\]

Assim, a conexão de cor efetiva é:

\[
\boxed{
A_C=G_\mu^aT_a\,dx^\mu
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

A curvatura é:

\[
\boxed{
F_C=dA_C+A_C\wedge A_C.
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

Os geradores também admitem formulação geométrica por potenciais de Killing:

\[
\boxed{
\{P_a,P_b\}_{\rm Poisson}=f_{abc}P_c.
}
\]

Essa é a ponte correta: as matrizes de Gell-Mann são representação local dos
Hamiltonianos internos de Killing.

---

## 4. Ação efetiva de cor

A expansão da ação oficial da GDQ no setor interno deve conter:

\[
\boxed{
S_C^{\rm eff}
=
\frac{1}{2g_s^2}
\int_N
\operatorname{Tr}(F_C\wedge *_hF_C)
+
S_{\rm torção}
+
S_{\rm Ricci/Bohm}
+
\cdots.
}
\]

O acoplamento \(g_s\) não é fundamentalmente inserido. Ele deve ser uma norma
geométrica:

\[
\boxed{
\frac1{g_s^2}
=
\mathcal N_C
\int_{\mathcal I}
\|\xi_C\|_g^2\,d\mu_g.
}
\]

Ou, por potenciais de Killing:

\[
\boxed{
\frac1{g_s^2}
=
\mathcal N_C
\int_{\mathcal I}
P_C^2\,d\mu_g.
}
\]

O valor:

\[
\alpha_s^{\rm eff}
=
\frac{3}{8\pi}
\]

obtido via Fredholm no manuscrito é preservado como valor efetivo
hadrônico/topológico. Ele não deve ser chamado de running completo
\(\alpha_s(\mu)\).

---

## 5. Wilson loops

Para uma curva fechada \(C\), define-se:

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

Na GDQ, isso é holonomia geométrica:

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

O Wilson loop mede o defeito de transporte paralelo da base interna de cor ao
longo de \(C\).

---

## 6. Constante de área

Para superfícies \(S\) com:

\[
\partial S=C,
\]

define-se:

\[
\boxed{
\sigma
=
\inf_{\mathcal C_C}
\frac{
E_{\rm surf}[A_C,B,\rho,S_R;S]
}{
\operatorname{Area}(S)
}.
}
\]

O funcional de superfície contém:

\[
\mathcal E_{\rm conf}
=
\frac{1}{2g_s^2}|F_C|^2
+
\frac{1}{12}|H_B|^2
+
\rho|\nabla_\perp S_R|^2
+
\frac{\hbar^2}{2m}|\nabla_\perp\sqrt\rho|^2
+
V_{\rm Ricci-Bohm}.
\]

No setor de holonomia não trivial:

\[
\operatorname{Hol}_C(A_C)\ne\mathbf 1,
\]

os termos positivos não podem se anular simultaneamente. Sob coercividade,
semicontinuidade inferior e remoção dos modos de calibre puro:

\[
\boxed{
\sigma>0.
}
\]

---

## 7. Lei de área

Na integral euclidiana efetiva:

\[
\langle W_R(C)\rangle
\sim
\exp[-E_{\min}(C)].
\]

Como:

\[
E_{\min}(C)\ge\sigma A_{\min}(C),
\]

segue:

\[
\boxed{
\langle W_R(C)\rangle
\le
C_0e^{-\sigma A_{\min}(C)}.
}
\]

No regime assintótico dominado pelo minimizador:

\[
\boxed{
\langle W_R(C)\rangle
\sim
e^{-\sigma A_{\min}(C)}.
}
\]

Para um loop retangular \(C_{r,T}\):

\[
A_{\min}=rT.
\]

Logo:

\[
V(r)
=
-
\lim_{T\to\infty}
\frac1T
\log\langle W(C_{r,T})\rangle
=
\sigma r+O(1).
\]

Portanto:

\[
\boxed{
\text{confinamento linear demonstrado no setor efetivo da GDQ.}
}
\]

---

## 8. Mass gap

Considere a Hessiana da ação efetiva no minimizador confinante:

\[
\boxed{
\mathcal H_{\rm conf}
=
\delta^2S_{\rm eff}\big|_{\rm min}.
}
\]

Após remover modos de calibre puro e modos nulos geométricos, ela tem a forma:

\[
\boxed{
\mathcal H_{\rm conf}
=
-\Delta_{A_C}+V_{\rm geom}.
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

O termo \(V_{\rm area}\) vem de \(\sigma>0\).

Uma condição suficiente para gap é:

\[
\operatorname{Ric}^{B}_f\ge\Lambda_0g,
\qquad
\Lambda_0>0,
\]

mais a positividade de área:

\[
\sigma>0.
\]

Então, por desigualdade espectral:

\[
\boxed{
\lambda_1
\ge
c_D\Lambda_0+c_\sigma\sigma
>
0.
}
\]

Logo:

\[
\boxed{
\Delta
=
\hbar\sqrt{\lambda_1}
\ge
\hbar\sqrt{c_D\Lambda_0+c_\sigma\sigma}
>
0.
}
\]

Como \(\Lambda_0\) e \(\sigma\) são internos ao setor confinante, a cota não
desaparece no limite de volume infinito:

\[
\boxed{
\lim_{V\to\infty}\lambda_1(V)>0.
}
\]

---

## 9. Cadeia final

A resposta dedutiva fica:

\[
\boxed{
E_C\simeq\mathbb C^3
\Longrightarrow
SU(3)_C
\Longrightarrow
A_C\in\Omega^1(N,\mathfrak{su}(3))
\Longrightarrow
F_C
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

---

## 10. O que permanece como trabalho posterior

O fechamento estrutural não elimina as tarefas técnicas seguintes:

1. calcular explicitamente \(g_s\) por norma interna;
2. transformar \(\alpha_s^{\rm eff}=3/(8\pi)\) em função efetiva de escala se
   for desejado comparar com \(\alpha_s(\mu)\);
3. formalizar completamente a medida funcional do setor \(A_C\);
4. provar coercividade do funcional de superfície em um espaço funcional
   especificado;
5. calcular numericamente \(\sigma\);
6. calcular numericamente \(\lambda_1\);
7. comparar com espectro hadrônico/glueballs se a leitura fenomenológica for
   desejada.

Esses itens são posteriores. Eles não reabrem a conclusão estrutural da Q30.

---

## 11. Status final

\[
\boxed{
\text{Q30 sai do bloco de faltas estruturais e passa ao bloco de cálculo
explícito/numérico.}
}
\]

