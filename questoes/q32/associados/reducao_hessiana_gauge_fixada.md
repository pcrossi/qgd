# Q32 — Redução gauge-fixada da Hessiana e origem do propagador modificado

## 1. Objetivo

Este adendo fixa a forma tecnicamente correta da resposta à Questão 32:

\[
G_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}(L_{\rm GDQ}^{(2)})^{-1}.
\]

O fator \(e^{-p_E^2/\Lambda^2}\) não é um regulador inserido manualmente. Ele é
o limite plano do semigrupo de calor gerado pelo operador quadrático normalizado
da ação GDQ.

---

## 2. Separação essencial: Hessiana e gerador de calor

A expansão quadrática da ação oficial em torno de um fundo estável
\((g_0,f_0,\bar f_0)\) tem a forma:

\[
\mathcal S_{\rm GDQ}^{(2)}
=
\frac12
\langle \Phi,\mathcal O_{\rm Hess}^{(2)}\Phi\rangle_{0}.
\]

Como a ação oficial contém o fator de fluxo \(\tau\), a Hessiana contém
tipicamente um fator global de \(\tau\):

\[
\mathcal O_{\rm Hess}^{(2)}
=
\tau\,L_{\rm GDQ}^{(2)}.
\]

O gerador do núcleo de calor não é a Hessiana com esse prefator repetido, mas:

\[
\boxed{
L_{\rm GDQ}^{(2)}
:=
\tau^{-1}\mathcal O_{\rm Hess}^{(2)}.
}
\]

Assim:

\[
e^{-\tau L_{\rm GDQ}^{(2)}}\to e^{-\tau p_E^2},
\qquad
\Lambda=\tau^{-1/2}.
\]

Isso remove a dupla contagem que produziria erroneamente
\(e^{-\tau^2p_E^2}\).

---

## 3. Setor escalar reduzido

Para o setor reduzido

\[
S[f]=\tau\int (R_0+|\nabla f|^2)e^{-f}dV,
\qquad
f=f_0+\varphi,
\]

a forma quadrática escalar é:

\[
S_{\varphi}^{(2)}
=
\tau\int e^{-f_0}
\left[
|\nabla\varphi|^2
-2\varphi\nabla f_0\cdot\nabla\varphi
+\frac12(R_0+|\nabla f_0|^2)\varphi^2
\right]dV.
\]

Após integração por partes no espaço ponderado:

\[
\boxed{
\mathcal O_{\rm Hess,\varphi}^{(2)}
=
2\tau
\left[
-\Delta_{f_0}
+\Delta f_0
+\frac12R_0
-\frac12|\nabla f_0|^2
\right].
}
\]

Logo:

\[
\boxed{
L_\varphi
=
2
\left[
-\Delta_{f_0}
+\Delta f_0
+\frac12R_0
-\frac12|\nabla f_0|^2
\right].
}
\]

Na ação oficial completa, a medida

\[
\mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
\]

e o fator

\[
\frac{f+\bar f}{2}-n
\]

adicionam termos de potencial e acoplamentos mistos. Portanto a expressão acima
é a redução escalar local, não a Hessiana total.

---

## 4. Setor métrico Hermitiano

No setor métrico, o símbolo principal esperado é o operador de
Lichnerowicz com drift:

\[
\boxed{
(L_h h)_{\mu\bar\nu}
=
-\Delta_{f_0}h_{\mu\bar\nu}
-2R_{\mu\bar\alpha\nu\bar\beta}h^{\alpha\bar\beta}
+{\rm Ric}_{\mu\bar\alpha}h^\alpha{}_{\bar\nu}
+{\rm Ric}_{\alpha\bar\nu}h_\mu{}^{\bar\alpha}
+V_{\mu\bar\nu}^{\alpha\bar\beta}h_{\alpha\bar\beta}.
}
\]

A fixação natural é o gauge Hermitiano-DeTurck ponderado:

\[
\boxed{
\mathcal F_\nu(h)
=
\nabla^\mu h_{\mu\bar\nu}
-\frac12\nabla_{\bar\nu}{\rm tr}_g h
-h_{\mu\bar\nu}\nabla^\mu f_0
=0.
}
\]

Com o termo:

\[
S_{\rm DT}
=
\frac{1}{2\xi}
\int |\mathcal F(h)|_{g_0}^2\,d\mu_{f_0},
\]

os modos de difeomorfismo são separados do setor físico. O operador físico é
obtido pela projeção:

\[
\boxed{
L_{h,{\rm phys}}
=
\Pi_{\rm phys}L_h\Pi_{\rm phys}.
}
\]

---

## 5. Setor misto \(g\)-\(f\)

A Hessiana completa contém acoplamentos entre flutuações escalares e métricas:

\[
\mathcal S_{gs}^{(2)}
=
\int d\mu_{f_0}
\left[
h^{\mu\bar\nu}\nabla_\mu f_0\nabla_{\bar\nu}\varphi
+\varphi\,\delta R[h]
+\varphi\,h^{\mu\bar\nu}T_{\mu\bar\nu}(f_0)
+\cdots
\right].
\]

Esses termos não alteram o símbolo principal elíptico quando o fundo é estável,
mas deslocam massas efetivas e misturas. A forma compacta correta é:

\[
\boxed{
L_{\rm GDQ}^{(2)}
=
\begin{pmatrix}
L_\varphi & L_{\varphi h}\\
L_{h\varphi} & L_{h,{\rm phys}}
\end{pmatrix}.
}
\]

O núcleo de calor completo é, portanto:

\[
\boxed{
K_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}.
}
\]

---

## 6. Polos e fantasmas

O propagador efetivo espectral é:

\[
\boxed{
G_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}(L_{\rm GDQ}^{(2)})^{-1}.
}
\]

Se:

\[
L_{\rm GDQ}^{(2)}\psi_n=\lambda_n\psi_n,
\]

então:

\[
G_\tau\psi_n=\frac{e^{-\tau\lambda_n}}{\lambda_n}\psi_n.
\]

O fator exponencial é função inteira sem zeros:

\[
e^{-z}\neq0.
\]

Logo:

\[
\boxed{
\text{o semigrupo de calor não cria polos adicionais.}
}
\]

Os polos físicos continuam determinados por:

\[
\lambda_n=0
\]

ou, no limite plano:

\[
p_E^2+m^2=0.
\]

Assim, não há fantasmas novos introduzidos pelo amortecimento gaussiano. A
ausência completa de fantasmas do setor métrico/gauge exige ainda a projeção
física, positividade OS e identidades de calibre.

---

## 7. Causalidade lorentziana

Não se deve continuar ingenuamente:

\[
e^{-p_E^2/\Lambda^2}
\mapsto
e^{+p_h^2/\Lambda^2}.
\]

A rota correta é:

\[
\boxed{
\text{fluxo euclidiano}
\rightarrow
\text{Schwinger functions refletidamente positivas}
\rightarrow
\text{reconstrução OS/Sudarshan}
\rightarrow
G_{\rm ret}.
}
\]

A condição causal final é:

\[
\boxed{
{\rm supp}\,G_{\rm ret}
\subseteq
J_h^+.
}
\]

Essa condição fica como critério formal de reconstrução; ela não decorre de
uma substituição algébrica em \(p^2\).

---

## 8. Veredito técnico da Q32

\[
\boxed{
\text{Q32 fica fechada estruturalmente.}
}
\]

O que foi estabelecido:

1. o gaussiano vem do semigrupo de calor;
2. o gerador correto é a Hessiana normalizada por \(\tau\);
3. no limite plano surge \(e^{-p_E^2/\Lambda^2}\);
4. não há novos polos;
5. o fator inteiro não introduz fantasmas;
6. a causalidade deve ser reconstruída por OS/Sudarshan, não por continuação
   ingênua.

O que fica para cálculo posterior:

1. coeficientes completos dos blocos mistos em fundo geral;
2. prova completa de reflexão positiva para todos os setores;
3. reconstrução explícita de \(G_{\rm ret}\) em fundo não plano;
4. checagem das identidades de Ward/Slavnov--Taylor no setor gauge efetivo.
