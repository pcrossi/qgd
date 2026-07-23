# Q38 — derivação causal de \(F_R\) e cálculo do resíduo

## 1. Dados efetivamente fornecidos pela GDQ

A variável causal é

\[
z:=z_\tau=\tau+i\nu_0t,
\]

e a medida satisfaz a conservação conjugada, em notação de operador,

\[
\partial_z\mathcal U=L_z^*\mathcal U,
\qquad
\int_K\mathcal U(z,y)dV_{q(z)}=1.
\]

O sinal de \(L_z^*\) depende da orientação escolhida para o fluxo; isso não
afeta o argumento abaixo. A condição essencial é que \(L_z^*\) conserve a
massa. A combinação causal simétrica usa os valores retardado e avançado,

\[
\mathcal U_{\rm sym}
=\frac12(\mathcal U_{\rm ret}+\mathcal U_{\rm adv}).
\]

## 2. Perfil gravitacional projetado

Defina a inserção geométrica

\[
\Phi_R(z,y):=\eta_R e^{2A(z,y)}
\]

e

\[
\boxed{
F_R(z)=\int_K\Phi_R(z,y)\mathcal U(z,y)dV_{q(z)}.}
\]

Essa é a forma derivada diretamente da redução do termo \(\mathcal R\) da
ação oficial. Ela é uma esperança geométrica na medida normalizada, e não o
kernel de calor sem integração.

## 3. Solução causal por semigrupo

Em um background estacionário suave, escreva

\[
\mathcal U(z)=e^{zL^*}\mathcal U_0.
\]

Por dualidade,

\[
F_R(z)
=\langle \Phi_R(z),e^{zL^*}\mathcal U_0\rangle
=\langle e^{zL}\Phi_R(z),\mathcal U_0\rangle.
\]

Se \(\Phi_R\), os coeficientes de \(L\) e os dados iniciais são suaves, a
expansão local é

\[
F_R(z)
=\sum_{k=0}^{\infty}\frac{z^k}{k!}
\langle L^k\Phi_R(0),\mathcal U_0\rangle
+\text{termos das derivadas explícitas de }\Phi_R.
\]

Portanto,

\[
F_R(z)=a_0+a_1z+a_2z^2+\cdots.
\]

Não existe coeficiente de Laurent \(z^{-1}\).

## 4. Por que \((4\pi z)^{-n}\) não fornece o resíduo

Localmente, o kernel de calor possui a forma

\[
K(z;y,y_0)
\sim(4\pi z)^{-n}
e^{-d(y,y_0)^2/(4z)}
\sum_{j\ge0}u_j(y,y_0)z^j
\]

em dimensão real \(2n\). Contudo, a integração contra uma inserção suave dá

\[
\int_K\Phi_R(y)K(z;y,y_0)dV_y
\sim
\Phi_R(y_0)+zL\Phi_R(y_0)+O(z^2).
\]

O fator gaussiano fornece exatamente as potências positivas necessárias para
cancelar \(z^{-n}\). Em particular,

\[
\int_KK(z;y,y_0)dV_y=1.
\]

Usar apenas \((4\pi z)^{-n}\) e ignorar o restante do kernel criaria um polo
espúrio e violaria a normalização.

## 5. Setores retardado e avançado

Cada ramo possui expansão regular na sua região setorial. A média simétrica
tem

\[
F_R^{\rm sym}(z)
=\frac12\left(F_R^{\rm ret}(z)+F_R^{\rm adv}(z)\right)
=a_0+a_1^{\rm sym}z+a_2^{\rm sym}z^2+\cdots.
\]

A simetrização pode alterar fases e coeficientes regulares, mas não cria um
termo \(z^{-1}\) ausente nos dois ramos.

## 6. Cálculo do resíduo

Por definição,

\[
\operatorname{Res}_{z=0}F_R
=[z^{-1}]F_R(z).
\]

Da expansão acima,

\[
\boxed{\operatorname{Res}_{z=0}F_R=0.}
\]

O mesmo vale em qualquer ponto regular interno ao contorno. Assim,

\[
\boxed{
C_R^{\rm GDQ}
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\oint_\gamma F_R(z)dz
=0}
\]

para o setor suave, normalizado e sem defeitos do modelo atual.

## 7. Teorema de não geração no setor suave

**Teorema.** Seja \(K\) compacto, \(L_z^*\) um operador conservativo de calor
conjugado com coeficientes regulares, \(\mathcal U\) uma solução normalizada e
\(\Phi_R\) uma inserção geométrica suave e monovalorada. Então \(F_R\) não
possui resíduo isolado dentro de uma deformação causal que permaneça no
domínio de regularidade. Consequentemente, o termo de curvatura integrado no
contorno fechado não gera um coeficiente de Einstein--Hilbert não nulo.

## 8. Como um resíduo não nulo poderia aparecer

É necessário violar ao menos uma das hipóteses do teorema por uma estrutura
já definida fisicamente, por exemplo:

1. defeito geométrico no qual \(\Phi_R\) tenha comportamento \(1/z\);
2. condição de salto que produza monodromia não removível;
3. fonte singular na equação conjugada;
4. contorno aberto, relativo ou com termo explícito de transgressão;
5. coeficiente de curvatura com uma 1-forma causal, em vez de \(F_Rdz\)
   exata/holomorfa.

Nenhum desses dados está especificado na ação oficial exibida. Escolher um
deles e ajustar seu coeficiente para reproduzir \(G\) não seria uma derivação.

## 9. Veredito

A dinâmica causal atualmente definida determina

\[
\boxed{F_R(z)=a_0+a_1z+a_2z^2+\cdots,
\qquad \operatorname{Res}F_R=0.}
\]

Logo, a tentativa de derivar o valor observado de \(G\) desse setor falha por
um teorema de anulação. A Q38 não possui, na ação atual e sob regularidade, uma
previsão gravitacional não nula. Para avançar, o manuscrito precisa identificar
na própria geometria GDQ qual defeito causal legítimo quebra uma hipótese do
teorema e derivar sua intensidade independentemente de \(G\).
