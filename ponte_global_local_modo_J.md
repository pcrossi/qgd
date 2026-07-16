# Ponte global--local — extensão mínima intrínseca de $J$

## 1. Objetivo e classificação

A Porta B mostrou que o setor com estrutura complexa congelada não possui
graus de liberdade suficientes para liberar simultaneamente os momentos de
garganta necessários. Este documento introduz a menor extensão
cohomogeneidade--1 da própria estrutura hermitiana, sem alterar a ação e sem
tratar $H$ como campo independente.

O resultado é uma derivação reduzida quase-hermitiana. A auditoria posterior
em `ponte_global_local_integrabilidade_J.md` demonstra que a integrabilidade
elimina $\chi(s)$ como modo contínuo. Este arquivo deve ser preservado como
rota calculada e excluída, não usado pelo solver hermitiano.

## 2. Família ortogonal de estruturas quase complexas

No bloco ortonormal

$$
(e^5,e^6,e^7,e^8)
=(Nds,a\sigma_1,a\sigma_2,c\sigma_3),
$$

considere as duas formas fundamentais quaternionicamente compatíveis

$$
\Omega_0=e^{58}+e^{67},
\qquad
\Omega_1=e^{56}-e^{78}.
$$

A extensão mínima é

$$
\boxed{
\omega_\perp(\chi)
=\cos\chi\,\Omega_0+\sin\chi\,\Omega_1.
}
$$

Como $\Omega_0$ e $\Omega_1$ pertencem à esfera unitária das formas
fundamentais ortogonais em quatro dimensões, a estrutura $J_\chi$ definida por

$$
\omega_\perp(X,Y)=g(J_\chi X,Y)
$$

satisfaz exatamente

$$
J_\chi^2=-1,
\qquad
g(J_\chi X,J_\chi Y)=g(X,Y).
$$

Logo $\chi(s)$ é um candidato a modo de $J$, não um escalar acrescentado à
ação. A parte toroidal de $\omega$ permanece a do ansatz causal.

As duas identidades acima provam compatibilidade **quase-hermitiana**. Para
usar ``Bismut'' no sentido hermitiano estrito ainda se deve impor

$$
\boxed{N_{J_\chi}=0,}
$$

ou demonstrar que a classe geométrica oficial admite a conexão característica
quase-hermitiana correspondente. As fórmulas abaixo calculam a substituição
algébrica $d^c_{J_\chi}\omega$; elas não devem ser interpretadas como prova de
integrabilidade para $\chi$ arbitrário. A equação $N_{J_\chi}=0$ é uma
restrição diferencial adicional e pode reduzir ou até eliminar esse modo.

## 3. Torção constitutiva

Use

$$
d\sigma_1=2\sigma_2\wedge\sigma_3,
\quad
d\sigma_2=2\sigma_3\wedge\sigma_1,
\quad
d\sigma_3=2\sigma_1\wedge\sigma_2.
$$

Com derivadas próprias, defina

$$
k_0=2\left(\frac{\dot a}{a}-\frac{c}{a^2}\right),
\qquad
k_1=\frac2c+\frac{\dot a}{a}+\frac{\dot c}{c}.
$$

Um cálculo exterior direto fornece

$$
d\omega_\perp=Ae^{567}+Be^{578},
$$

onde

$$
\boxed{
A=\cos\chi\,k_0-\sin\chi\,\dot\chi,
}
$$

$$
\boxed{
B=-\sin\chi\,k_1-\cos\chi\,\dot\chi.
}
$$

Como $J_\chi$ é ortogonal, $H=d^c_{J_\chi}\omega$ possui a mesma norma:

$$
\boxed{
|H_\perp|^2=6(A^2+B^2).
}
$$

Para $\chi=\dot\chi=0$, recupera-se

$$
|H_\perp|^2=6k_0^2
$$

e, portanto, exatamente a torção Berger anterior. Esta verificação fixa a
normalização.

## 4. Ação reduzida

Se $\mathcal K_C$ é a densidade cinética--potencial causal já derivada e

$$
\mathscr V=A_0A_s^3a^2ce^{-u},
$$

a única mudança é a substituição constitutiva no termo torsional:

$$
I=\int ds\,N\mathscr V
\left[\tau(\mathcal K_C+\Delta\mathcal K_J)+u-4-\lambda_N\right],
$$

com

$$
\boxed{
\Delta\mathcal K_J
=-\frac12\left(A^2+B^2-k_0^2\right).
}
$$

Não foi adicionado termo fundamental. A expressão é apenas a diferença entre
$-|H(J_\chi)|^2/12$ e $-|H(J_0)|^2/12$.

## 5. Momentos

Os momentos causais antigos recebem somente as correções abaixo:

$$
\boxed{
\Delta p_a
=\frac{\tau\mathscr V}{a}
\left(-2A\cos\chi+B\sin\chi+2k_0\right),
}
$$

$$
\boxed{
\Delta p_c
=\tau\mathscr V\frac{B\sin\chi}{c},
}
$$

$$
\boxed{
p_\chi
=\tau\mathscr V
\left[sin\chi\cos\chi(k_0-k_1)-\dot\chi\right].
}
$$

Não há correção direta em $p_0,p_s,p_u,p_v$, embora suas velocidades possam
mudar depois da inversão do sistema acoplado. A nova velocidade é

$$
\boxed{
\dot\chi
=\sin\chi\cos\chi(k_0-k_1)
-\frac{p_\chi}{\tau\mathscr V}.
}
$$

Assim, o modo pode alterar $p_c$ sem transformar a torção em variável
independente. Isso mostra por que congelar $J$ escondia uma direção canônica.

## 6. Restrição do lapse

A forma exata, que evita separar incorretamente termos lineares e potenciais,
é

$$
\boxed{
\mathcal C_N^{(J)}
=\mathcal C_N^{(0)}
+\tau\left[
\Delta\mathcal K_J
-\dot a\frac{\partial\Delta\mathcal K_J}{\partial\dot a}
-\dot c\frac{\partial\Delta\mathcal K_J}{\partial\dot c}
-\dot\chi\frac{\partial\Delta\mathcal K_J}{\partial\dot\chi}
\right]=0.
}
$$

Essa expressão é precisamente $\partial(NL)/\partial N=0$ com todas as
derivadas próprias escaladas por $N^{-1}$.

## 7. Equação de $\chi$

Como a medida não depende de $\chi$, sua equação é

$$
\boxed{
\frac d{ds}p_\chi
=N\tau\mathscr V
\frac{\partial\Delta\mathcal K_J}{\partial\chi}.
}
$$

Ela deve ser integrada juntamente com as equações métricas e de $f$. Não há
uma carga adicional que autorize fixar $p_\chi$ arbitrariamente.

## 8. Regularidade de garganta

### 8.1 Colo excisado não degenerado

Na seção mínima refletida, todos os campos escalares invariantes são pares.
Logo a condição regular é

$$
\dot\chi(0)=0.
$$

Ela não implica em geral $p_\chi(0)=0$; pela fórmula canônica,

$$
p_\chi(0)=\tau\mathscr V_0\sin\chi_0\cos\chi_0
(k_{0,0}-k_{1,0}).
$$

Se a reflexão também preserva a estrutura complexa sem rotação entre as duas
folhas, então $\chi_0=0\pmod\pi$ e $p_\chi(0)=0$. Permitir
$\chi_0\neq0$ é precisamente a extensão geométrica a ser testada, não uma
condição Robin.

### 8.2 Centro suave

Para $a=c=s+O(s^3)$, tem-se $k_1=4/s+O(s)$. A suavidade na trivialização
complexa selecionada exige

$$
\chi(s)=O(s^2),
\qquad
\dot\chi(s)=O(s).
$$

Então $B=O(s)$ e $H$ permanece regular. Uma constante não nula de $\chi$ na
coframe de Maurer--Cartan produziria $B\sim-4\sin\chi/s$ e singularidade.
Esse centro suave continua incompatível com carga strong-KT relativa não nula;
o novo modo não remove o resultado topológico anterior.

## 9. O que foi e não foi demonstrado

Foi derivada a menor direção de $J$ que:

1. preserva exatamente $J^2=-1$;
2. preserva a métrica hermitiana;
3. modifica $H$ somente por $H=d_J^c\omega$;
4. recupera o setor anterior em $\chi=0$;
5. fornece um momento capaz de acoplar-se a $p_c$.

Ainda é necessário resolver a sela ampliada. Portanto não se afirma que a
extensão elimina o no-go; afirma-se que ela é a primeira extensão intrínseca
que deve ser testada antes de qualquer condição externa.

Há ainda uma porta anterior à solução: verificar $N_{J_\chi}=0$ com as
condições de garganta. Se a única solução regular for
$\chi=0\pmod\pi$, esta extensão fica excluída e o no-go da Porta B permanece.

## 10. Verificação computacional

`ponte_global_local_modo_J.py` implementa as fórmulas. O teste
`teste_ponte_global_local_modo_J.py` verifica por diferenças centrais os três
momentos, a inversão de $p_\chi$, o limite $\chi=0$ e a variação exata do lapse.
