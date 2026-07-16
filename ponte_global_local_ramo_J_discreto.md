# Ponte global--local — ramo integrável discreto de $J$

## 1. Ramo e condição

O único ramo diferente da estrutura original encontrado pelo tensor de
Nijenhuis é

$$
\chi=\frac\pi2\pmod\pi
$$

com

$$
\boxed{
\mathcal F_I
=\frac{\dot a}{a}-\frac{\dot c}{c}-\frac2c+rac{2c}{a^2}=0.
}
$$

Ele é uma componente discreta do espaço de estruturas complexas. Não existe
$p_\chi$ nem uma velocidade $\dot\chi$.

## 2. Torção e ação oficial

Defina

$$
k_0=2\left(\frac{\dot a}{a}-\frac{c}{a^2}\right),
\qquad
k_1=\frac2c+\frac{\dot a}{a}+\frac{\dot c}{c}.
$$

No ramo original, $|H|^2=6k_0^2$; no ramo discreto,

$$
\boxed{|H|^2=6k_1^2.}
$$

Logo a redução causal oficial é

$$
I_{\pi/2}=\int ds\,N\mathscr V
\left[\tau(\mathcal K_C+\Delta\mathcal K_{\pi/2})+u-4-\lambda_N\right],
$$

onde

$$
\boxed{
\Delta\mathcal K_{\pi/2}
=-\frac12(k_1^2-k_0^2).
}
$$

Essa substituição vem apenas de $H=d_J^c\omega$.

## 3. Imposição variacional da integrabilidade

A variação deve permanecer no subespaço $\mathcal F_I=0$. Uma representação
local implementável usa um multiplicador auxiliar $\ell(s)$:

$$
I_{\rm restr}=I_{\pi/2}+\int ds\,N\ell\mathcal F_I.
$$

$\ell$ não é campo físico nem termo novo da ação; ele implementa o domínio
integrável, como um multiplicador de coordenadas. A variação em $\ell$ devolve
$\mathcal F_I=0$.

Pode-se alternativamente eliminar $\dot c$:

$$
\boxed{
\dot c=\frac ca\dot a-2+\frac{2c^2}{a^2}.
}
$$

Sobre essa restrição,

$$
k_1=2\frac{\dot a}{a}+2\frac c{a^2},
$$

e

$$
\boxed{
\Delta\mathcal K_{\pi/2}ig|_{\mathcal F_I=0}
=-8\frac{c\dot a}{a^3}.
}
$$

O termo torna-se linear em velocidade, mas não deve ser descartado antes de
considerar a medida $\mathscr V$.

## 4. Momentos e lapse

Relativamente ao ramo original,

$$
\boxed{
\Delta p_a
=\frac{\tau\mathscr V}{a}(-k_1+2k_0)+\frac\ell a,
}
$$

$$
\boxed{
\Delta p_c
=-\frac{\tau\mathscr V}{c}k_1-\frac\ell c.
}
$$

Os demais momentos oficiais mantêm suas expressões, embora a solução acoplada
mude. A correção exata à restrição do lapse é

$$
\boxed{
\Delta\mathcal C_N
=\tau\mathscr V\left[
\Delta\mathcal K
-\dot a\,\partial_{\dot a}\Delta\mathcal K
-\dot c\,\partial_{\dot c}\Delta\mathcal K
\right]
+\ell\left(-\frac2c+\frac{2c}{a^2}\right).
}
$$

## 5. Sistema diferencial restrito

Se $q=(a,c,u,v,x_0,x_s)$, as equações são

$$
\frac d{ds}\frac{\partial L_{\rm restr}}{\partial\dot q^A}
-\frac{\partial L_{\rm restr}}{\partial q^A}=0,
$$

juntamente com

$$
\mathcal F_I=0,
\qquad
\mathcal C_N^{(0)}+\Delta\mathcal C_N=0.
$$

Em primeira ordem, use os momentos causais antigos acrescidos dos dois shifts
acima. A equação $\mathcal F_I=0$ fornece $\dot c$. A derivada
$d\mathcal F_I/ds=0$, combinada às equações de Euler--Lagrange, determina
$\dot\ell$. Assim a condição não precisa ser reprojetada depois de cada passo.

## 6. Regularidade do DAE

No setor interno $(a,c,u)$, a Hessiana cinética do ramo restrito possui

$$
\det M=\frac{32}{a^2c^2}\neq0.
$$

O covetor da restrição nas velocidades é

$$
l=\left(\frac1a,-\frac1c,0\right).
$$

Um cálculo exato dá

$$
l^TM^{-1}l=-\frac58,
$$

e a matriz bordada satisfaz

$$
\boxed{
\det\begin{pmatrix}M&l\\l^T&0\end{pmatrix}
=\frac{20}{a^2c^2}\neq0.
}
$$

Portanto o sistema diferencial--algébrico é localmente regular para $a,c>0$:
$d\mathcal F_I/ds=0$ determina unicamente o multiplicador e preserva a
integrabilidade durante a evolução. Não há no-go dinâmico local.

## 7. Garganta refletida

Na seção mínima,

$$
\dot a(0)=\dot c(0)=0.
$$

A condição $\mathcal F_I(0)=0$ implica

$$
\boxed{a_0=c_0.}
$$

Derivando a restrição e usando a paridade,

$$
\boxed{\ddot a(0)=\ddot c(0).}
$$

Essas são condições geométricas, não Robin. Os valores de $u_0,v_0$ e os
momentos restantes continuam sujeitos ao lapse, carga e fluxo oficiais.

## 8. Matching

Os traços de $a,c,u,v$ permanecem contínuos. Os momentos a colar são os
momentos aumentados pelo multiplicador de integrabilidade:

$$
\Pi_a^{I}=\Pi_a^{S}+\Delta p_a,
\qquad
\Pi_c^{I}=\Pi_c^{S}+\Delta p_c.
$$

Sem fonte externa,

$$
\boxed{
\Pi_{A,-}^{I}+\Pi_{A,+}^{I}=0.
}
$$

O lado direito é zero. O multiplicador não é um salto material; ele garante
que ambos os lados variem dentro da classe complexa integrável.

## 9. Veredito

O ramo $\chi=\pi/2$ é dinamicamente admissível como sistema restrito local:
a matriz bordada é não singular e a condição de Nijenhuis é preservável. Ele
é, porém, mais restritivo que o ramo original e não acrescenta parâmetro de
tiro. Se ajuda o tripleto residual é uma questão numérica da nova sela, não
uma consequência da contagem de dimensões.

`ponte_global_local_ramo_J_discreto.py` implementa torção, restrição,
momentos e lapse; o teste associado verifica as identidades variacionais.

