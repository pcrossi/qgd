# Q38 — critério de resíduo do contorno oficial

## 1. Extração sem alterar a ação

O setor de curvatura da ação oficial é

\[
\mathcal S_R
=\frac{\hbar}{\Lambda_C^2}
\int_\gamma\frac{d\tau}{\tau}
\int_{\mathcal M_{\mathbb C}}
\tau\mathcal R\,\mathcal U\,dV_g.
\]

Após a decomposição gravitacional, defina

\[
F_R(\tau)
:=\int_K\eta_R e^{2A(y,\tau)}
\mathcal U(y,\tau)\,dV_{q(\tau)}.
\]

O fator \(\tau\) cancela exatamente a medida logarítmica, de modo que

\[
\boxed{
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\int_\gamma F_R(\tau)\,d\tau .}
\]

## 2. Lema de anulação steady

Se \(\gamma\) é fechado e \(F_R\) é holomorfa no domínio limitado por
\(\gamma\), então Cauchy implica

\[
\oint_\gamma F_R(\tau)d\tau=0.
\]

Em particular, no background steady homogêneo, sem warp e com medida interna
normalizada,

\[
F_R(\tau)=\eta_R\int_K\mathcal U_*dV_K=\eta_R,
\]

e portanto

\[
\boxed{C_R^{\rm steady,hom}=0.}
\]

O cancelamento não é uma aproximação numérica: decorre da forma da ação e do
fechamento de \(\gamma\).

Embora \(\mathcal U\) contenha explicitamente
\((4\pi z_\tau)^{-n}\), esse denominador não constitui, por si só, um polo
gravitacional depois que se impõe
\(\int_K\mathcal U dV_K=1\) folha a folha. A normalização força a parte
espacialmente constante de \(\sigma\) a compensá-lo. Contar simultaneamente o
denominador e a medida normalizada duplicaria o mesmo fator.

## 3. Condição necessária para gravidade não nula

Para obter \(C_R^{\rm GDQ}\ne0\), o modo projetado \(F_R\) deve possuir uma
singularidade ou monodromia física dentro do contorno. No caso meromorfo,

\[
\oint_\gamma F_R(\tau)d\tau
=2\pi i\sum_{\tau_k\in\operatorname{Int}\gamma}
\operatorname{Res}_{\tau_k}F_R.
\]

Logo,

\[
\boxed{
C_R^{\rm GDQ}
=\frac{2\pi\hbar}{\Lambda_C^2}
\operatorname{Re}\!\left[
i\sum_k\operatorname{Res}_{\tau_k}F_R
\right].}
\]

Esta é a forma dedutiva correta da afirmação de que a gravidade deve vir do
contorno causal. O resíduo relevante precisa ser obtido da solução GDQ; não
pode ser fixado por \(G\) observado.

## 4. Condição de realidade e sinal

Com a convenção da ação escrita, um resíduo puramente real produz uma integral
puramente imaginária e desaparece após \(\operatorname{Re}\). Para
\(C_R>0\), a soma dos resíduos deve ter a fase compatível com a orientação de
\(\gamma\), ou a prescrição causal deve conter explicitamente o fator usual
\(1/(2\pi i)\). Como esse fator não aparece na ação oficial exibida, não deve
ser inserido silenciosamente.

## 5. Relação com o background Hopf--Bismut

O background

\[
(S^3_R\times S^1_R)\times T^4,
\qquad
H=\frac2R\operatorname{vol}_{S^3},
\]

satisfaz condicionalmente o balanço steady generalizado

\[
R_{ij}-\frac14H_{ik\ell}H_j{}^{k\ell}
+\nabla_i\nabla_j f=0,
\qquad d_f^\dagger H=0,
\]

quando \(\mathcal R\) da ação é interpretada constitutivamente como
\(R_{LC}-|H|^2/12\), com \(H=d^c\omega(g,J)\). Ele é um background interno
regular, mas seu modo homogêneo não produz o coeficiente de Einstein--Hilbert
porque é analítico e constante no contorno.

## 6. Problema reduzido que realmente resta

Não resta procurar um número em um determinante de Yang--Mills nem ajustar um
warp compacto shrinking. Resta resolver, a partir das equações GDQ e da
prescrição causal, um modo \(F_R(\tau)\) com estrutura analítica não trivial e
calcular seu resíduo. A condição quantitativa é

\[
\operatorname{Re}\left[2\pi i\sum_k\operatorname{Res}_{\tau_k}F_R\right]
=\frac{c^4\Lambda_C^2}{16\pi\hbar G}.
\]

Esta igualdade é um alvo de verificação, não uma definição do resíduo.

## 7. Veredito

1. a sela shrinking em \(T^5\times S^3\) está topologicamente excluída;
2. a sela steady homogênea de Hopf--Bismut tem integral gravitacional nula;
3. um \(G\ne0\) requer estrutura singular/monodrômica em \(\tau\);
4. a ação atual não fornece ainda o perfil causal necessário.

Assim, a Q38 está encerrada quanto às rotas produto, warp shrinking e steady
homogênea. Sua previsão numérica reduz-se de maneira precisa ao cálculo de um
resíduo causal GDQ ainda não derivado.

## 8. Avaliação pela dinâmica causal existente

A equação do calor conjugada e a normalização permitem avaliar esse resíduo.
Para inserção geométrica suave,

\[
F_R(z)=\langle e^{zL}\Phi_R,\mathcal U_0\rangle
=a_0+a_1z+a_2z^2+\cdots,
\]

logo \(\operatorname{Res}F_R=0\). A demonstração completa está em
questoes/q38/associados/derivacao_causal_residuo_q38.md. Portanto, não resta apenas um cálculo
numérico: existe um teorema de anulação no setor suave normalizado. Um valor
não nulo requer que a GDQ identifique e derive um defeito, salto ou monodromia
causal ausente da ação atualmente escrita.
