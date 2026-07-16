# Ponte global--local — redução do exterior cosmológico warped

## 1. Domínio

O exterior cosmológico é tratado como uma variedade de cohomogeneidade um
ao longo do ciclo $S^1$, com órbitas

$$
T^4\times S^3.
$$

Esse problema é distinto do colar normal local de Berger. A coordenada $s$
parametriza o arco cosmológico entre a interface do estômato e a região
compensadora global.

## 2. Ansatz métrico

Use

$$
g_+
=N(s)^2ds^2
+A(s)^2g_{T^4}
+c(s)^2g_{S^3},
$$

onde $g_{T^4}$ é plano e $g_{S^3}$ tem raio unitário e escalar $6$.
Introduza a derivada própria

$$
\dot X=N^{-1}X'.
$$

As variáveis logarítmicas são

$$
x=\log A,
\qquad
y=\log c.
$$

## 3. Estrutura Hermitiana

Num coframe ortonormal, tome

$$
e^{1,\ldots,4}=A\,dx^{1,\ldots,4},
\qquad
e^5=Nds,
$$

$$
e^{6,7,8}=c\,\sigma_{1,2,3}.
$$

A forma fundamental é

$$
\omega
=e^{12}+e^{34}+e^{58}+e^{67}.
$$

Ela pareia o ciclo $S^1$ com a fibra de Hopf e preserva a estrutura usada no
Lema 1.

## 4. Torção de Bismut dependente

Calculando $d\omega$ e aplicando $d_J^c$, obtém-se, até o sinal global de
orientação,

$$
\boxed{
H
=-2\dot x\,e^8\wedge(e^{12}+e^{34})
+2\left(\dot y-e^{-y}\right)e^{678}.
}
$$

No limite homogêneo,

$$
\dot x=\dot y=0,
$$

resta a torção paralelizante de $S^3$. No limite cônico local
$c(s)=s$, o segundo termo se anula.

Na convenção tensorial do projeto,

$$
\boxed{
|H|^2
=48\dot x^2
+24\left(\dot y-e^{-y}\right)^2.
}
$$

Nenhuma amplitude de torção foi introduzida independentemente.

## 5. Curvatura de Levi--Civita

Para o produto duplamente warped,

$$
\boxed{
\begin{aligned}
R_{\rm LC}
=\;&6e^{-2y}
-8(\ddot x+\dot x^2)
-6(\ddot y+\dot y^2)\\
&-12\dot x^2
-6\dot y^2
-24\dot x\dot y.
\end{aligned}
}
$$

Equivalentemente,

$$
R_{\rm LC}
=6e^{-2y}
-8\ddot x-6\ddot y
-20\dot x^2-12\dot y^2-24\dot x\dot y.
$$

## 6. Medida

Escreva

$$
f=u+iv.
$$

O fator radial da medida oficial é

$$
\mathscr V
=A^4c^3e^{-u}
=e^{4x+3y-u}.
$$

O volume constante de $T^4\times S^3$ e o fator
$(4\pi z_\tau)^{-4}$ são mantidos no prefator global.

## 7. Ação reduzida antes da integração por partes

Numa fatia de $\tau$,

$$
I_+^{(2)}
=\int ds\,N\mathscr V
\left\{
\tau\left[
R_{\rm LC}
-\frac1{12}|H|^2
+\dot u^2+\dot v^2
\right]
+u-4
\right\}.
$$

Essa expressão ainda contém $\ddot x$ e $\ddot y$.

## 8. Forma de primeira ordem

Depois da integração por partes variacionalmente completa, mantendo o
concomitante de bordo em $\boldsymbol\Theta_{\rm GDQ}$, resulta

$$
\boxed{
I_+^{(1)}
=\int ds\,N\mathscr V
\left\{
\tau\mathcal K_+
+u-4
\right\},
}
$$

com

$$
\boxed{
\begin{aligned}
\mathcal K_+
=\;&8\dot x^2
+4\dot y^2
+24\dot x\dot y
-8\dot u\dot x
-6\dot u\dot y\\
&+\dot u^2+\dot v^2
+4e^{-y}\dot y
+4e^{-2y}.
\end{aligned}
}
$$

O termo $4e^{-y}\dot y$ não deve ser descartado isoladamente: a medida
$\mathscr V$ depende de $(x,y,u)$.

## 9. Testes internos

### 9.1 Background homogêneo

Para derivadas nulas,

$$
\mathcal R_{\rm GDQ}
=4e^{-2y}
=\frac4{c^2},
$$

reproduzindo o resultado homogêneo já auditado.

### 9.2 Torção plana

No limite local cônico, com $c=s$ e torção toroidal nula,

$$
\dot y=e^{-y},
$$

e o componente $e^{678}$ de $H$ desaparece.

### 9.3 Ausência de campo independente

Todos os termos de $H$ são funções de $(A,c,N)$ e de suas primeiras
derivadas. Portanto a redução respeita a convenção oficial.

## 10. Momentos cosmológicos

Definindo primeiro o momento em relação à derivada própria,

$$
P_X=\frac{\partial(N\mathscr V\tau\mathcal K_+)}{\partial\dot X},
$$

obtêm-se

$$
\boxed{
P_x
=N\tau\mathscr V
\left(16\dot x+24\dot y-8\dot u\right),
}
$$

$$
\boxed{
P_y
=N\tau\mathscr V
\left(8\dot y+24\dot x-6\dot u+4e^{-y}\right),
}
$$

$$
\boxed{
P_u
=N\tau\mathscr V
\left(2\dot u-8\dot x-6\dot y\right),
}
$$

$$
\boxed{
P_v
=2N\tau\mathscr V\dot v.
}
$$

Na parametrização com derivadas próprias, o momento canônico em relação a
$X'$ é obtido dividindo essas expressões por $N$.

Para evitar ambiguidade, a colagem usa os momentos canônicos

$$
p_X:=\frac{P_X}{N}.
$$

## 11. Colagem

Na interface $Y$, os momentos acima devem satisfazer

$$
P_A^++P_A^-=0
$$

com orientação exterior consistente, depois da projeção sobre o espaço de
traços permitido pelos vínculos. Essa igualdade fornece a condição Robin sem
coeficientes escolhidos pelo alvo.

## 12. Sistema a resolver

O background exterior é definido por:

1. Euler--Lagrange de $(x,y,u,v)$;
2. restrição do lapse $N$;
3. normalização de $\mathcal U$;
4. vínculos $\mathcal C_L$, $\mathcal C_R$ e $\mathcal C_E$;
5. carga e fluxos de Noether;
6. colagem dos momentos em $Y$;
7. compensação global no arco oposto.

## 13. Status e limite de validade

$$
\boxed{
\text{ansatz exterior, }H,\ R_{\rm LC},\ I_+^{(1)}
\text{ e momentos canônicos derivados no subsector isotrópico.}
}
$$

Este ansatz impõe $a=c$ no $S^3$. Ele é útil como teste de consistência, mas
não pode ser usado na colagem física completa porque eliminaria o modo Berger.
A extensão correta está em `ponte_global_local_exterior_berger.md`.
