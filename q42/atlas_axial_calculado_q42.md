# Q42 — Cálculo do atlas axial e do pullback na Hessiana

## 1. Duas cartas do fibrado de Hopf

Na carta norte, com coordenada \(w\in\mathbb C\), escolha

\[
 u_N(w)=\frac{(1,w)^T}{\sqrt{1+|w|^2}}.
\]

Na carta sul, com \(w'=1/w\), escolha

\[
 u_S(w')=\frac{(w',1)^T}{\sqrt{1+|w'|^2}}.
\]

No overlap,

\[
 u_S=e^{-i\arg w}u_N.
\]

Logo a função de transição é

\[
 g_{NS}=e^{-i\arg w},
\]

com grau \(-1\) nesta convenção; a orientação conjugada fornece grau \(+1\).
O projetor

\[
 P=uu^\dagger
\]

é idêntico nas duas cartas.

As conexões locais

\[
 \mathcal A_N=-iu_N^\dagger du_N,
 \qquad
 \mathcal A_S=-iu_S^\dagger du_S
\]

satisfazem

\[
 \mathcal A_S=\mathcal A_N-d\arg w.
\]

Sua curvatura é

\[
 \mathcal F=d\mathcal A
 =-i\frac{d\bar w\wedge dw}{(1+|w|^2)^2},
\]

e

\[
 \frac1{2\pi}\int_{S^2}\mathcal F=\pm1
\]

conforme a orientação.

## 2. Métrica de Fubini--Study induzida

Uma diferenciação direta fornece

\[
 \operatorname{Tr}(dP,dP)
 =\frac{2\,dw\,d\bar w}{(1+|w|^2)^2}.
\]

Portanto o atlas produz corretamente a métrica de Fubini--Study e fixa a
normalização geométrica de \(P\).

## 3. Inserção no background cilíndrico

O \(S^3\) redondo pode ser escrito localmente como fibrado de Hopf:

\[
 ds_{S^3_a}^2
 =a^2\left[(d\psi+\mathcal A)^2
 +ds_{\rm FS}^2\right],
\]

com uma redistribuição convencional dos fatores entre \(\psi\),
\(\mathcal A\) e \(ds_{\rm FS}^2\). A colagem

\[
 \mathcal A_S=\mathcal A_N-d\chi,
 \qquad
 \psi_S=\psi_N+\chi
\]

mantém \(d\psi+\mathcal A\) global.

Uma orientação global \(U\in SU(2)\) atua por isometria:

\[
 P\mapsto UPU^\dagger,
 \qquad
 g\mapsto U^*g=g,
 \qquad
 F\mapsto F.
\]

Assim, para o mapa de campos fundamentais,

\[
 \Phi(P)=(g(P),F(P),\bar F(P)),
\]

a derivada de uma orientação global é

\[
 T_A=(\mathcal L_{X_A}g,\mathcal L_{X_A}F,
 \mathcal L_{X_A}\bar F).
\]

Como \(X_A\) é Killing no cilindro redondo e \(F=F(r)\),

\[
 \mathcal L_{X_A}g=0,
 \qquad
 \mathcal L_{X_A}F=0.
\]

Consequentemente,

\[
 \boxed{T_A=0}
\]

para a orientação global. Mesmo para uma representação por difeomorfismo
não-Killing, a projeção Hermitiano--DeTurck remove
\(T_A=\mathcal L_X\Phi\) do subespaço físico.

## 4. Resultado do pullback

O pullback pedido é

\[
 Z_{\rm bulk}G^{\rm FS}_{AB}
 =\langle T_A,
 \Pi_{\rm phys}\mathbb H_{\rm GDQ}\Pi_{\rm phys}T_B\rangle.
\]

Com o atlas acima e apenas os campos fundamentais da ação oficial,

\[
 \boxed{Z_{\rm bulk}^{\rm orientação\ global}=0.}
\]

Este é um resultado, não uma ausência de cálculo. A topologia de Hopf existe
e o setor \(c_1=\pm1\) está correto, mas a posição do projetor dentro de uma
órbita de isometrias não é uma deformação energética do background livre.

## 5. Por que \(V_H\) não contradiz \(Z_{\rm bulk}=0\)

O valor

\[
 V_H=2/\tau
\]

é o autovalor angular de uma **textura não homogênea** de grau \(l=2\) no
\(S^3\). Já \(Z_{\rm bulk}=0\) acima refere-se à rotação global homogênea.
Uma textura espacial tem energia; uma rotação global do background isotrópico
não tem.

## 6. Consequência para Stern--Gerlach

O campo do aparelho quebra a isometria e produz uma resposta localizada
\(\delta\Phi_P\) pela equação

\[
 \mathbb H_R\delta\Phi_P=J_{\rm SG}[P,B].
\]

Portanto, a rigidez relevante ao experimento é a já derivada

\[
 \kappa_H^{\rm SG}
 =\frac12(G_{\rm FS})^{AB}
 \sum_\nu\frac{Z_\nu}{\lambda_\nu^2}
 j_{\nu A}^*j_{\nu B},
\]

e não uma constante intrínseca positiva da orientação livre. Ela se anula
quando \(B\to0\), como deve ocorrer por simetria.

Assim, a tentativa de obter um \(Z_{\rm bulk}>0\) universal para a rotação
global estava mal formulada. O atlas fecha a topologia; o aparelho fornece a
rigidez da textura física.

