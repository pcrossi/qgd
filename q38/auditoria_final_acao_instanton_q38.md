# Q38 — Auditoria final da ação e do setor instantônico

## 1. Ação oficial

\[
\mathcal S_{\rm GDQ}
=\int_\gamma\frac{d\tau}{\tau}
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[\tau(\mathcal R+|\nabla f|^2)+\frac{f+\bar f}{2}-n\right]
\mathcal U\sqrt{\det g}\,d^{2n}z.
\]

Mesmo interpretando \(\mathcal R\) como o escalar de Bismut
\(\mathcal R_B=R_{\rm LC}-|H|^2/12\), o integrando permanece linear na
curvatura escalar. Ele não contém explicitamente
\[
\operatorname{tr}(\mathcal F_B\wedge *\mathcal F_B)
\quad\text{nem}\quad
\operatorname{tr}(\mathcal F_B\wedge\mathcal F_B).
\]

## 2. Hipótese adicional identificada

Os adendos usaram
\[
\frac{S_E}{\hbar}
=\frac1{2\alpha}\|\mathcal F_B-*\mathcal F_B\|^2
+\frac{Q_{\rm rel}}{\alpha}.
\]
Esse completamento BPS pertence a um funcional quadrático de curvatura e não
decorre automaticamente do termo de Perelman/Einstein--Hilbert. Falta provar
\[
\boxed{
\mathcal S_{\rm GDQ}\big|_{\mathcal C_Q}
\equiv
\frac{\hbar}{2\alpha}\|\mathcal F_B-*\mathcal F_B\|^2
+\frac{\hbar Q_{\rm rel}}{\alpha}+S_{\rm estacionário}.
}
\]
Sem essa identidade, \(e^{-1/(2\alpha)}\) permanece uma hipótese efetiva.

## 3. Retroação e determinante

Como \(\mathcal A_B\) é constitutiva de \((g,J)\), a sela deve satisfazer
\[
\frac{\delta\mathcal S_{\rm GDQ}}{\delta g}=0,\qquad
\frac{\delta\mathcal S_{\rm GDQ}}{\delta f}=0,\qquad
Q_{\rm rel}(\nabla^B[g,J])=\frac12.
\]
O perfil BPST satisfaz \(F=*F\), mas isso não prova as duas primeiras
equações. Um determinante semiclassico só é físico quando calculado na
Hessiana da mesma ação em torno de um ponto crítico. Enquanto isso não for
demonstrado, \(\det{}'\mathbb L_{B,\rm inst}\) não é o determinante
gravitacional da GDQ.

## 4. Resultados preservados e condicionais

Permanecem válidos o background steady de Einstein--Bismut, o cancelamento
\(R_{ij}-H_{ikm}H_j{}^{km}/4=0\), a carga matemática
\(Q_{\rm rel}=1/2\), a transgressão e a auditoria numérica de \(\Pi_1\).

Permanecem condicionais:

1. \(S_{\rm inst}/\hbar=1/(2\alpha)\) como resultado da ação oficial;
2. \(\rho\) como modo zero da Hessiana oficial;
3. o determinante BPST como prefator gravitacional;
4. seu uso para remover o resíduo de \(0.2668\%\).

## 5. Rota sem alterar a ação

É necessário demonstrar uma identidade de Chern--Weil/transgressão interna ao
termo existente, reduzindo \(\int\mathcal R_B\mathcal U\,dV\) ao funcional
autodual quadrático mais o termo topológico. Como uma expressão é linear e a
outra quadrática em curvatura, essa identidade não é automática.

Se ela não existir, deve-se abandonar a origem instantônica proposta ou
alterar a ação oficial com um setor quadrático/topológico.

## 6. Veredito

\[
\boxed{\text{Com a ação atualmente escrita, Q38 não pode ser declarada fechada.}}
\]

O bloqueio é a derivação do funcional BPS a partir da ação oficial, não a
precisão numérica do solver.
