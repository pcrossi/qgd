# Q35 — Espectro global EM no produto $S^3\times I$

## 1. Enunciado e domínio

Considera-se o modo eletromagnético que vem da conexão de um ciclo do $T^4$.
No produto global com o módulo estabilizado $S^3(R)$ e o colar compacto
$I=[0,L]$, sua amplitude interna é uma função escalar
$u(r,\Omega)$ multiplicando a 1-forma externa $A_\mu dx^\mu$.

Depois da projeção transversal externa, o operador interno mínimo é

$$
\boxed{
L_{\rm EM,int}
=-\partial_r^2+\Delta_{S^3(R)}^{(0)}.
}
$$

O domínio é $H^2(S^3\times I)$, com Neumann nas extremidades do colar. Não
se introduz massa fotônica, potencial ou impedância Robin.

## 2. Espectro separado

Os modos radiais são

$$
\lambda_n^{(I)}=\left(\frac{n\pi}{L}\right)^2,
\qquad n=0,1,\ldots
$$

e os harmônicos escalares da esfera tridimensional satisfazem

$$
\lambda_\ell^{(S^3)}=\frac{\ell(\ell+2)}{R^2},
\qquad \ell=0,1,\ldots
$$

Logo,

$$
\boxed{
\lambda_{n\ell}
=\left(\frac{n\pi}{L}\right)^2
+\frac{\ell(\ell+2)}{R^2}.
}
$$

O modo $(n,\ell)=(0,0)$ é o fóton sem massa. Ele é removido ao calcular o
primeiro autovalor positivo.

## 3. Dois setores físicos distintos

### Setor cosmológico homogêneo em $S^3$

Se o ansatz físico restringe $\ell=0$, então

$$
\lambda_{1,\rm hom}^{+}=\frac{\pi^2}{L^2}.
$$

Usando a colagem torsional

$$
\frac{L}{\ell_C}
=\pi\sqrt{\tau_{\rm EM}^{\rm dimless}},
$$

obtém-se exatamente

$$
\sqrt{\lambda_{1,\rm hom}^{+}}
=\widehat\Lambda_{\rm EM}
=1{,}90727017413475.
$$

### Domínio global completo

Se flutuações não homogêneas em $S^3$ pertencem ao espaço físico, o primeiro
candidato é o mínimo entre $(n,\ell)=(1,0)$ e $(0,1)$:

$$
\boxed{
\lambda_{1,\rm full}^{+}
=\min\left\{
\frac{\pi^2}{L^2},\frac{3}{R^2}
\right\}.
}
$$

Para $\alpha=1/137$ e $n_B=1$:

$$
\frac{\pi^2}{L^2}=3{,}63767951714400,
\qquad
\frac3{R^2}=2{,}78934007751156.
$$

Portanto,

$$
\boxed{
\sqrt{\lambda_{1,\rm full}^{+}}
=\frac{\sqrt3}{R}
=1{,}67013175453662.
}
$$

## 4. Resolução do domínio físico

A escolha do domínio não é livre. O campo EM da Q35 é o modo $U(1)$ que vem
da conexão de um ciclo de $T^4$ e é escalar sob as isometrias do $S^3$
cosmológico. Seja $P_0$ a média de Haar sobre $S^3$:

$$
(P_0u)(r)
=\frac1{\operatorname{Vol}(S^3)}\int_{S^3}u(r,\Omega)\,d\Omega.
$$

Como o background, $R$, $Z_{\rm EM}$ e as condições de colagem são
homogêneos,

$$
[P_0,L_{\rm EM,int}]=0.
$$

Além disso, produtos e contrações de campos invariantes continuam
invariantes. Portanto, restringir a ação e sua Hessiana a

$$
\mathcal H_{\rm EM}^{\rm inv}=P_0\mathcal H
$$

é uma truncagem consistente: a dinâmica do setor não sourceia modos
$\ell\ge1$.

Os harmônicos $\ell\ge1$ transformam não trivialmente sob as isometrias de
$S^3$ e constituem uma torre KK cosmológica adicional. Eles são estados
físicos possíveis do domínio global completo, mas não pertencem ao canal
$U(1)$ eletromagnético homogêneo definido na Q35. Seu autovalor
$3/R^2$ não deve ser usado para calibrar o semigrupo desse canal.

## 5. Veredito

No espaço físico correto da Q35,

$$
L_{\rm EM}^{(2)}ig|_{\mathcal H_{\rm EM}^{\rm inv}}
=-\partial_r^2,
$$

com kernel constante e Neumann. Depois de remover o kernel,

$$
\boxed{
\lambda_{1,\rm EM}^{+}
=\frac{\pi^2}{L^2}
=3{,}63767951714400,
}
$$

e

$$
\boxed{
\widehat\Lambda_{\rm EM}
=\sqrt{\lambda_{1,\rm EM}^{+}}
=1{,}90727017413475.
}
$$

A ambiguidade $1{,}90727$ versus $1{,}67013$ está resolvida por projeção de
simetria. Pela convenção oficial $\widehat\tau=\tau/\ell_C^2$ da Q2, a
conversão correta é

$$
\Lambda_{\rm EM}^{\rm phys}
=1{,}90727017413475\,\Lambda_C.
$$

Expressar esse resultado em GeV exige apenas a calibração metrológica de
$\Lambda_C$, parâmetro dimensional já presente na ação.

## 6. Classificação

- separação do operador e espectro: derivação condicional ao produto
  $S^3\times I$;
- números: avaliação direta;
- projeção $P_0$ e invariância do subespaço: derivação por simetria do setor;
- exclusão de $\ell\ge1$ do canal EM: classificação em torres KK distintas;
- escala dimensional: calibração ainda não fixada.
