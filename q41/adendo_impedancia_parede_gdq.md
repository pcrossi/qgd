# Q41 — Impedância variacional de uma parede física

## 1. Objetivo e alcance

Este adendo completa o elo formal que faltava no tratamento do poço: obter a
condição de Robin como resposta de uma parede, e não introduzi-la diretamente
como condição arbitrária.

O resultado não fornece uma constante universal para qualquer parede. Ele
fornece o mapa que transforma o background GDQ estacionário de um material em
sua impedância espectral de contorno:

\[
\boxed{
(g_*,f_*,B_*)_{\rm parede}
\longrightarrow
K_{\rm parede}
\longrightarrow
\Lambda_{\rm DN}(E,q)
\longrightarrow
E_n.
}
\]

A ação oficial permanece inalterada. A parede é um background externo e sua
Hessiana é a segunda variação da ação oficial, restrita ao domínio material.

## 2. Domínio e dados variacionais

Considere o poço em

\[
\Omega_{\rm p}=(0,L)
\]

e uma parede direita de espessura \(d\),

\[
\Omega_{\rm w}=(L,L+d).
\]

Seja \(R\) o modo reduzido no poço e \(U\) o vetor dos modos físicos da
parede obtidos da flutuação

\[
(\delta g,\delta f,\delta\bar f,\delta B)
\]

em torno de um background estacionário admissível

\[
(g_*,f_*,B_*).
\]

Depois da projeção sobre o setor que se acopla ao modo do poço, a segunda
variação tem a forma

\[
I^{(2)}
=
\frac12\langle R,K_{\rm p}R\rangle_{\Omega_{\rm p}}
+\frac12\langle U,K_{\rm w}U\rangle_{\Omega_{\rm w}}
+\langle U,J_\partial R_\partial\rangle
+\frac12\langle R_\partial,\lambda_{\rm bare}R_\partial\rangle,
\]

onde \(R_\partial=R(L)\). Aqui \(K_{\rm w}\) é a Hessiana física da parede,
depois da remoção dos modos de gauge e da imposição de seu domínio
auto-adjunto. A estabilidade material exige

\[
K_{\rm w}>0
\]

no subespaço físico, admitindo inversa primada quando houver modos zero
protegidos.

## 3. Modos relaxáveis: complemento de Schur

A equação linear da parede é

\[
K_{\rm w}U+J_\partial R_\partial=0.
\]

Logo,

\[
U_{\rm cl}=-K_{\rm w}^{-1}J_\partial R_\partial.
\]

Substituindo a solução na ação quadrática, obtém-se

\[
I_{\partial,\rm eff}^{(2)}
=
\frac12\langle R_\partial,\lambda_\partial R_\partial\rangle,
\]

com

\[
\boxed{
\lambda_\partial(E,q)
=
\lambda_{\rm bare}
-J_\partial^\dagger(E,q)K_{\rm w}^{-1}(E,q)J_\partial(E,q).
}
\]

Essa fórmula vale quando \(U\) representa modos auxiliares ou relaxáveis
acoplados a um grau de liberdade de contorno já existente.

## 4. Continuação do campo: mapa Dirichlet–Neumann

Quando o campo do poço continua diretamente para dentro da parede, não se deve
adicionar novamente o complemento de Schur anterior. Nesse caso, fixa-se

\[
U(L)=R(L)
\]

e resolve-se o problema elíptico da parede. A ação da solução, avaliada na
casca, é

\[
I_{\rm w,on-shell}^{(2)}
=
\frac12\langle R_\partial,\Lambda_{\rm DN}R_\partial\rangle.
\]

O operador

\[
\boxed{
\Lambda_{\rm DN}
=
-A\frac{\nabla_nU_{\rm cl}}{U_{\rm cl}}\bigg|_{L}
}
\]

é o mapa Dirichlet–Neumann da Hessiana da parede. A condição natural do poço
torna-se

\[
\boxed{
R'(L)=-\lambda_L(E,q)R(L),
\qquad
\lambda_L=\Lambda_{\rm DN}.
}
\]

Na parede esquerda, a orientação oposta da normal fornece

\[
R'(0)=\lambda_0(E,q)R(0).
\]

## 5. Parede homogênea de espessura finita

No setor escalar homogêneo mínimo, a Hessiana projetada pode ser escrita como

\[
K_{\rm w}
=
-A_\partial\frac{d^2}{dy^2}+M_\partial^2(E,q),
\qquad 0<y<d,
\]

onde \(y=x-L\). Defina

\[
\Omega^2(E,q)=A_\partial^{-1}M_\partial^2(E,q).
\]

Na face externa da parede, imponha

\[
U'(d)+\eta U(d)=0.
\]

A solução com valor prescrito \(U(0)=R(L)\) produz

\[
\boxed{
\lambda_L(E,q)
=
A_\partial\Omega
\frac{\Omega\sinh(\Omega d)+\eta\cosh(\Omega d)}
{\Omega\cosh(\Omega d)+\eta\sinh(\Omega d)}.
}
\]

Casos importantes:

1. face externa de Dirichlet, \(\eta\to\infty\):

   \[
   \lambda_L=A_\partial\Omega\coth(\Omega d);
   \]

2. face externa de Neumann, \(\eta=0\):

   \[
   \lambda_L=A_\partial\Omega\tanh(\Omega d);
   \]

3. parede semi-infinita, \(d\to\infty\):

   \[
   \boxed{
   \lambda_L=A_\partial\Omega;
   }
   \]

4. parede rígida, \(A_\partial\Omega\to\infty\):

   \[
   R(L)\to0.
   \]

Assim, Dirichlet é o limite de impedância infinita de uma parede estável.

## 6. Conferência pelo limite de barreira usual

Tome

\[
A_\partial=1,
\qquad
M_\partial^2(E)=\frac{2m}{\hbar^2}(V_0-E).
\]

Então

\[
\Omega(E)=\kappa(E)
=
\frac{\sqrt{2m(V_0-E)}}{\hbar}.
\]

Para uma parede semi-infinita,

\[
\lambda_\partial(E)=\kappa(E),
\]

recuperando exatamente a impedância de uma barreira finita. Isso é teste de
correspondência. O conteúdo propriamente GDQ aparece quando \(A_\partial\) e
\(M_\partial^2\) são calculados da Hessiana do background
\((g_*,f_*,B_*)\).

## 7. Espectro resultante

No interior,

\[
R(x)=A\cos(kx)+B\sin(kx),
\qquad
E=\frac{\hbar^2k^2}{2m}.
\]

Com impedâncias \(\lambda_0(E)\) e \(\lambda_L(E)\), o espectro é determinado
por

\[
\boxed{
F(E)
=
[\lambda_0(E)\lambda_L(E)-k^2(E)]\sin[k(E)L]
+k(E)[\lambda_0(E)+\lambda_L(E)]\cos[k(E)L]
=0.
}
\]

Para paredes simétricas quase rígidas,

\[
E_n
=
\frac{\hbar^2\pi^2n^2}{2mL^2}
\left[
1-\frac{4}{\lambda_\partial(E_n)L}
+O((\lambda_\partial L)^{-2})
\right].
\]

Se a dependência em \(E\) for relevante, \(F(E)=0\) deve ser resolvida
autoconsistentemente, sem substituir \(\lambda_\partial\) por um número
ajustado após a comparação.

## 8. Critério de estabilidade e fechamento

Uma parede GDQ admissível deve satisfazer:

1. o background resolve a primeira variação da ação oficial no material;
2. a Hessiana física \(K_{\rm w}\) é auto-adjunta no domínio declarado;
3. seus modos não protegidos têm espectro não negativo;
4. \(\Lambda_{\rm DN}(E,q)\) é real abaixo do limiar de propagação;
5. o fluxo normal total é conservado na interface;
6. o limite rígido recupera Dirichlet;
7. os parâmetros materiais são fixados antes do confronto espectral.

Com isso, a pendência formal do poço fica encerrada:

\[
\boxed{
\text{a impedância Robin é o mapa Dirichlet--Neumann da Hessiana física da
parede, ou o complemento de Schur quando há modos auxiliares de superfície.}
}
\]

O que resta para cada experimento é avaliar \(K_{\rm w}\) no background
material específico.
