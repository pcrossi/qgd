# Q29 — Problema de Sturm--Liouville eletrofraco bem normalizado

## 1. Funcional quadrático

Depois da projeção sobre um canal interno $a$, escreva a parte radial da
Hessiana oficial como

$$
S_a^{(2)}
=\frac12\int_\epsilon^\pi
\left[p(\chi)|\Psi_a'|^2+q_a(\chi)|\Psi_a|^2\right]d\chi
+\frac12\Psi_a(\epsilon)^\dagger
\mathsf M_{\partial,a}\Psi_a(\epsilon).
$$

No ansatz warped da Q29, a rigidez líder possui a forma

$$
p(\chi)
=\frac{C_{\rm GDQ}}{R^2}
e^{-F(\chi)+3A(\chi)}\sin^2\chi,
$$

salvo o fator toroidal comum já absorvido em $C_{\rm GDQ}$. O peso espectral é

$$
w(\chi)=C_{\rm GDQ}e^{-F+3A}\sin^2\chi.
$$

## 2. Equação e condições de contorno

A variação fornece

$$
-\frac{d}{d\chi}\left(p\Psi_a'\right)
+q_a\Psi_a
=\lambda_a w\Psi_a.
$$

No antipolo regular,

$$
\Psi_a'(\pi)=0.
$$

No estômato, considerando a orientação do normal exterior do intervalo,

$$
\boxed{
p(\epsilon)\Psi_a'(\epsilon)
=\mathsf M_{\partial,a}\Psi_a(\epsilon).
}
$$

Portanto, o operador Robin propriamente dito é

$$
\boxed{
\mathsf R_a
=p(\epsilon)^{-1}\mathsf M_{\partial,a}.
}
$$

## 3. Matriz de interface

O pullback de Hopf já calculado dá

$$
\mathsf M_\partial
=\kappa_\partial\mathsf B(g,g'),
\qquad
\kappa_\partial=Z_\beta\beta_*^2=v^2.
$$

Assim,

$$
\mathsf M_{\partial,\gamma}=0,
$$

$$
\mathsf M_{\partial,W}=\frac{g^2v^2}{4},
$$

$$
\mathsf M_{\partial,Z}=\frac{(g^2+g'^2)v^2}{4}.
$$

Esses são coeficientes de massa quadráticos da ação efetiva. Eles só se tornam
parâmetros Robin após a divisão por $p(\epsilon)$.

## 4. Parâmetro adimensional que o solver necessita

Em coordenada $\chi$, defina

$$
\eta_a
=\frac{\mathsf M_{\partial,a}}{p(\epsilon)}.
$$

Usando $\kappa_\partial/C_{\rm GDQ}$,

$$
\eta_a
=R^2e^{F(\epsilon)-3A(\epsilon)}
\frac{\kappa_\partial}{C_{\rm GDQ}}
\frac{b_a(g,g')}{\sin^2\epsilon},
$$

onde

$$
b_\gamma=0,
\qquad
b_W=\frac{g^2}{4},
\qquad
b_Z=\frac{g^2+g'^2}{4}.
$$

## 5. Dado ainda necessário

O cálculo anterior determinou

$$
\frac{\kappa_\partial}{C_{\rm GDQ}}
=3{,}9495054\times10^{-5}.
$$

Contudo, $\eta_a$ também depende do valor normalizado
$F(\epsilon)-3A(\epsilon)$. A solução líder calculou $A'$, mas a constante de
$A$ e o valor de $F$ dependem da normalização global, do volume de $T^5$ e da
condição de bordo dilatônica. Sem esses dados, atribuir um número a $\eta_a$
seria escolher implicitamente a normalização do bulk.

## 6. Critério para executar o solver físico

O solver fica completamente determinado quando forem fornecidos pela mesma
solução estacionária:

1. $A(\chi)$ com sua constante fixada;
2. $F(\chi)$;
3. $q_a(\chi)$, obtido da Hessiana métrico-dilatônica;
4. $p(\epsilon)$;
5. as condições Robin acima.

Antes disso, é possível apenas fazer uma varredura em $\eta_a$. Tal varredura
é análise de sensibilidade, não previsão da GDQ e não pode ser usada para
selecionar $10/21$.
