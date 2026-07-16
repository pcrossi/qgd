# Determinação dos coeficientes da cirurgia do nêutron

## 1. Enunciado

Determinar, a partir da geometria de duas calotas e um colar, da ação oficial
e das conservações já demonstradas,

$$
\ell,
\quad w_R,
\quad w_V,
\quad A_2^{\rm cola},
\quad C_4^{\rm cola},
\quad G_{r,3}.
$$

## 2. Geometria geral do colar

Escreva a região de matching como um produto warped

$$
ds^2+ a(s)^2d\Omega_3^2,
\qquad 0\leq s\leq L,
$$

com $L=\ell r$. Para uma fibra $S^3$ unitária,

$$
\mathcal R
=6\frac{1-(a')^2}{a^2}-6\frac{a''}{a},
\qquad
dV=2\pi^2a^3ds.
$$

Se $a'=0$ nas duas extremidades, integração por partes fornece

$$
\boxed{
\int\mathcal R,dV
=12\pi^2\int_0^L a(s)\left[1+(a'(s))^2\right]ds.
}
$$

Para o cilindro exato $a(s)=r$,

$$
\int\mathcal R,dV=12\pi^2\ell r^2.
$$

O matching adiciona

$$
\boxed{
A_2^{\rm cola}
\propto12\pi^2
\int_{\rm transição}a(s)(a'(s))^2ds,
}
$$

além das respostas da medida e de $f$. O valor depende do perfil $a(s)$.

O volume da transição é

$$
\boxed{
V_{\text{cola}}=2\pi^2\int_{\text{transição}}a(s)^3ds,
}
$$

e contribui para $C_4^{\rm cola}$ de forma igualmente dependente do perfil.

## 3. O comprimento $\ell$ não é fixado pelo matching local

As condições de colagem no equador das calotas são

$$
a(0)=a(L)=r,
\qquad
a'(0)=a'(L)=0.
$$

Elas são satisfeitas por todo cilindro de comprimento $L>0$. Portanto,

$$
\boxed{\ell>0\text{ é um módulo global do ansatz.}}
$$

Homogeneidade e isotropia fixam a forma transversal $S^3$, mas não o
comprimento longitudinal do colar. A minimização apenas do custo de curvatura
leva ao ínfimo degenerado $\ell\to0$; um comprimento finito exige incluir a
energia torsional, o matching causal e as condições de saída.

## 4. Limite de colagem fraca

Se for admitida uma métrica apenas $C^1$ por partes, a calota encontra o
cilindro no equador com o mesmo primeiro jato. Não aparece curvatura delta, e
uma camada de suavização de largura tendendo a zero fornece formalmente

$$
A_2^{\rm cola}\to0,
\qquad
C_4^{\rm cola}\to0.
$$

Esses valores são o **limite fraco ideal**, não valores derivados para uma
cirurgia suave $C^2$. Para qualquer largura positiva, diferentes funções
$a(s)$ produzem custos diferentes preservando as mesmas cargas.

## 5. Pesos causais

Se $F_R(z)$ e $F_V(z)$ são os pullbacks completos dos blocos de curvatura e
potencial, então, para orientação positiva,

$$
\boxed{
w_R=\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}[z^3]F_R(z)
\right],
}
$$

$$
\boxed{
w_V=\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}[z^3]F_V(z)
\right].
}
$$

A normalização

$$
\int_M\mathcal U(z)dV_{g(z)}=1
$$

fornece uma equação por ordem em $z$. Ela determina o modo homogêneo de
$\sigma=\operatorname{Re}f$ em função do volume, mas não relaciona
unicamente os jatos de curvatura, potencial e Hessiana radial.

Com efeito, para números arbitrários $c_R,c_V$,

$$
F_R(z)=F_{R,0}+c_Rz^3,
\qquad
F_V(z)=F_{V,0}+c_Vz^3
$$

possuem os mesmos dados até segunda ordem e produzem pesos diferentes. A
normalização pode ser preservada ajustando o terceiro jato homogêneo de
$\sigma$. Logo, conservação da densidade não fixa separadamente $w_R,w_V$.

## 6. Inércia causal

Analogamente,

$$
\boxed{
M_r
=\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}\left[
\frac{2\pi i}{(4\pi)^4}G_{r,3}
\right].
}
$$

Para orientação positiva, positividade exige

$$
\operatorname{Im}G_{r,3}<0.
$$

Essa desigualdade fixa o sinal, não o módulo. A família

$$
G_{r,3}=-i\chi,
\qquad \chi>0,
$$

obedece à causalidade e à positividade para qualquer $\chi$. Portanto,
$G_{r,3}$ não é determinado pelas conservações.

## 7. Resultado de identificabilidade

As informações atuais determinam apenas

$$
\ell>0,
$$

$$
A_2^{\rm cola},C_4^{\rm cola}\to0
\quad\text{no limite fraco ideal},
$$

$$
A_2>0,
\qquad C_4>0,
\qquad \operatorname{Im}G_{r,3}<0,
$$

e a condição de bounce

$$
B_3^2>4A_2C_4.
$$

Não determinam valores únicos. Existem famílias contínuas de
$(\ell,a(s),F_R,F_V,G_{r,3})$ com as mesmas simetrias, densidade normalizada e
fluxo torsional conservado.

## 8. Teorema de não identificabilidade

> No ansatz de duas calotas e colar, homogeneidade, isotropia, normalização da
> densidade e conservação do fluxo torsional não determinam os seis
> coeficientes solicitados. O comprimento é um módulo global; os termos de
> cola dependem do perfil de suavização; e os três pesos físicos dependem dos
> terceiros jatos da família causal. Valores únicos exigem condições de
> contorno e uma solução das equações oficiais ao longo de $\gamma$.

Esse é um resultado negativo: exclui a possibilidade de obter uma meia-vida
única apenas escolhendo a geometria redonda e invocando conservações.

## 9. Problema mínimo que produziria os valores

É necessário fornecer ou resolver simultaneamente

$$
\delta\mathcal S_{\rm GDQ}=0,
$$

$$
\int H=2\tau_T,
\qquad
\int\mathcal U,dV=1,
$$

$$
(g,f,\bar f)|_{\gamma_-}=\Phi_n,
\qquad
(g,f,\bar f)|_{\gamma_+}=\Phi_{p+2}^{\rm APS},
$$

com regularidade no estrato de matching. Essa solução fixa $a(s)$, $L$ e os
terceiros jatos. O corpus ainda não contém esses dados de extremidade como
campos explícitos.

## 10. Verificação

O resíduo causal e o teste de perfis de matching estão em
`neutron/verificar_nao_identificabilidade_coeficientes.py`.
