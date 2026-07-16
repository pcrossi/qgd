# Q38 — Auditoria da extração dos operadores a partir da ação oficial

## 1. Resultado da auditoria

A ação oficial usada nos documentos é

\[
\mathcal S_{\rm GDQ}
=\int_\gamma\frac{d\tau}{\tau}
\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau(\mathcal R+|\nabla f|^2)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z.
\]

As variáveis explicitamente variáveis nessa expressão são \(g\), \(f\) e
\(\bar f\). A conexão de Bismut, sua torção \(H\), o termo topológico
\(\operatorname{tr}(\mathcal F_B\wedge\mathcal F_B)\) e uma ação de fronteira
Robin não aparecem como termos independentes na fórmula escrita.

Consequentemente, a ação oficial permite definir rigorosamente a Hessiana
\(g\)-\(f\), mas ainda não permite calcular numericamente, sem uma definição
constitutiva adicional, a Hessiana independente de \(\mathcal A_B\) usada no
argumento instantônico.

Este ponto não invalida o representante topológico local. Ele delimita seu
status: o perfil BPST--Bismut representa a classe relativa assumida, mas ainda
não foi demonstrado como solução de Euler--Lagrange da ação oficial tal como
ela está escrita.

## 2. Extração correta por projetores

Seja \(L_{\rm GDQ}^{(2)}\) o operador gauge-fixado já estruturado na Q32:

\[
L_{\rm GDQ}^{(2)}
=\begin{pmatrix}
L_{ff}&L_{fg}\\
L_{gf}&L_{gg}^{\rm phys}
\end{pmatrix}.
\]

Definam-se os projetores ortogonais, na medida estacionária de Perelman,

\[
P_H:\mathscr H\to\mathscr H_H,
\qquad
P_T:\mathscr H\to\mathscr H_T,
\qquad
P_HP_T=0.
\]

Então os blocos não precisam ser postulados separadamente. Eles são

\[
\boxed{
K_H=P_HL_{\rm GDQ}^{(2)}P_H,
\quad
K_T=P_TL_{\rm GDQ}^{(2)}P_T,
\quad
J=P_HL_{\rm GDQ}^{(2)}P_T.
}
\]

O operador físico reduzido é

\[
\boxed{
K_{\rm eff}
=P_HL P_H
-P_HL P_T(P_TLP_T)^{-1}P_TLP_H.
}
\]

Essa fórmula é uma consequência direta da Hessiana oficial. Para avaliá-la,
porém, são necessários:

1. o background estacionário explícito \((g_*,f_*)\);
2. as três autofunções Hopf que definem \(P_H\);
3. as cinco autofunções toroidais que definem \(P_T\);
4. os elementos de matriz mistos de \(L_{fg}\) e \(L_{gf}\);
5. a projeção física completa de \(L_{gg}\).

Os documentos atuais fornecem a forma variacional desses blocos, mas não os
cinco itens como funções normalizadas prontas para integração.

## 3. Condição de contorno que realmente segue da ação

Ao integrar por partes o termo cinético ponderado, surge a forma de fronteira

\[
\mathfrak b(\phi,\psi)
=\int_{\partial\mathcal M}
e^{-\sigma_*}
\left(\bar\phi\,\nabla_n\psi
-(\nabla_n\bar\phi)\psi\right)d\Sigma.
\]

Sem ação adicional de borda, as extensões naturais são Dirichlet ou Neumann
ponderada. Uma condição Robin

\[
(\nabla_n+Z_T^{\rm Rob})\psi|_\partial=0
\]

com \(Z_T^{\rm Rob}\neq0\) requer que a variação da ação produza o termo
quadrático

\[
\frac12\int_{\partial\mathcal M}
Z_T^{\rm Rob}|\psi|^2d\Sigma.
\]

Esse termo pode emergir de transgressão/cola torsional, mas seu coeficiente
não está presente explicitamente na ação oficial exibida. Portanto,
\(Z_T^{\rm Rob}\) ainda não pode ser escolhido numericamente como se já fosse
uma saída variacional.

## 4. Correção da contagem de \(\alpha^4\)

Há duas afirmações diferentes nos documentos:

1. a teoria global usa dimensão complexa quatro;
2. o Apêndice 2 e o Capítulo 22 atribuem \(\alpha^4\) a uma subvariedade de
   dimensão complexa dois e à estrutura \((2,2)\).

Elas não são a mesma derivação. Em geral, se

\[
g_{a\bar b}^{(*)}=D_a{}^c\widehat g_{c\bar b},
\]

então o fator de volume é

\[
\boxed{J_g=\det_{\mathbb C}D.}
\]

Assim:

- em dimensão complexa quatro, \(D=\alpha I_4\) produz \(J_g=\alpha^4\);
- em dimensão complexa dois, \(D=\alpha I_2\) produz apenas
  \(J_g=\alpha^2\);
- em dimensão complexa dois, obter \(\alpha^4\) pelo determinante exige
  \(D=\alpha^2I_2\), cuja origem variacional precisa ser demonstrada.

Logo, a afirmação correta é condicional:

\[
\boxed{
\alpha^4=\det_{\mathbb C}D
\quad\text{se e somente se o mapa estacionário }D
\text{ tiver determinante }\alpha^4.
}
\]

A simples menção a uma forma \((2,2)\) não basta para fixar essa potência.

## 5. Determinante de flutuações

Uma vez fornecidos os projetores e o termo de borda, o cálculo sem pós-ajuste
é

\[
\log\mathcal P_{\rm GDQ}
=-\frac12
\left[
\log\det{}'K_{\rm eff}^{\rm inst}
-\log\det K_{\rm eff}^{(0)}
\right]
+\log J_{\rm orb},
\]

onde \(J_{\rm orb}\) é o jacobiano da redução à órbita física. Na formulação
sem fantasmas, \(J_{\rm orb}\) continua necessário como jacobiano da mudança
de variáveis, mesmo que não seja representado por campos fantasmas.

O número \(1.00267505\) permanece somente como comparação final. Ele não fixa
\(Z_T^{\rm Rob}\), os elementos de \(J\), massas efetivas ou o jacobiano.

## 6. Próxima derivação necessária

Existem duas rotas consistentes:

### Rota A — Bismut constitutivo

Definir \(H=H[g,J,\omega]\) como funcional determinado da estrutura
Hermitiana. Substituí-lo em \(\mathcal R_B(g,H[g])\) antes de variar. Nesse
caso toda a Hessiana continua sendo uma Hessiana de \(g\) e \(f\), e os modos
Hopf/toro são projeções de \(L_{gg}^{\rm phys}\).

### Rota B — Bismut dinâmico

Escrever explicitamente na ação oficial o setor de \(H\), sua normalização e
o termo de transgressão. Isso amplia o conjunto de variáveis e modifica a
Hessiana oficial; não pode ser feito silenciosamente num adendo.

Como o usuário determinou que a ação oficial não deve ser alterada, a rota
compatível é a **Rota A**. A relação constitutiva e sua linearização foram
encontradas no próprio manuscrito e desenvolvidas em
`q38/linearizacao_bismut_e_jacobiano_q38.md`:

\[
H=d^c\omega,
\qquad
\delta H_h=d^c[h(J\cdot,\cdot)].
\]

## 7. Veredito atualizado

O complemento de Schur está formalmente definido por projeção da Hessiana
oficial, mas ainda não está numericamente calculável. As duas pendências
irredutíveis são:

1. avaliar os perfis \(g_*\), \(f_*\), \(H_*\) e as bases de projeção;
2. demonstrar no background que o tensor quadrático normalizado da conexão
   satisfaz \(\widehat{\mathcal Q}_{a\bar b}=\widehat g_{a\bar b}\).

Foi também reconciliada a contagem dimensional: a GDQ global é complexa 4,
enquanto a fibra interna após a projeção 4D é complexa 2. Nessa fibra,
\(\alpha^4\) surge condicionalmente como
\(\det_{\mathbb C}(\alpha^2I_2)\), pois o canal responde quadraticamente à
conexão. Avaliar os dois pontos acima precede o prefator espectral.
