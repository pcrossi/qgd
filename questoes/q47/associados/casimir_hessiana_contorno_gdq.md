# Casimir como resposta de contorno da Hessiana GDQ

## 1. Domínio ideal

Considere duas placas planas ideais, paralelas, infinitas, separadas por:

$$
a>0.
$$

O domínio interno é:

$$
\Omega_a
=
\mathbb R^2_{\parallel}\times[0,a].
$$

No setor eletromagnético efetivo, a Hessiana física projetada reduz, no
limite plano e sem torção ativa de material, ao operador transversal de ondas:

$$
K_{\rm EM}^{\rm eff}
\sim
-\partial_t^2
+c^2(-\Delta_{\parallel}-\partial_z^2).
$$

Essa é uma redução efetiva da Hessiana GDQ, não substituição da ação oficial.

## 2. Condições de contorno ideais

Para placas condutoras ideais, os modos físicos satisfazem condições
equivalentes a condutor perfeito. Na redução escalar por polarização, isso
aparece como Dirichlet/Neumann combinados.

O espectro longitudinal ideal é:

$$
k_z=\frac{n\pi}{a},
\qquad
n=1,2,3,\ldots
$$

e:

$$
\omega_{n,\boldsymbol k_\parallel}
=
c\sqrt{k_\parallel^2+\left(\frac{n\pi}{a}\right)^2}.
$$

## 3. Energia renormalizada por diferença

A energia formal por área é:

$$
\frac{E(a)}{A}
=
\frac{\hbar}{2}
\sum_n
\int\frac{d^2k_\parallel}{(2\pi)^2}
\omega_{n,\boldsymbol k_\parallel}.
$$

Esta soma isolada diverge. O observável físico é a diferença entre a energia
com placas separadas por $a$ e a energia de referência sem confinamento, mais
os contratermos geométricos locais de área/superfície que não dependem de $a$
na força ideal.

Na linguagem GDQ, o regulador é auxiliar para calcular a parte universal:

$$
\frac{E_\epsilon(a)}{A}
=
\frac{\hbar}{2}
\sum_n
\int\frac{d^2k_\parallel}{(2\pi)^2}
\omega_{n,\boldsymbol k_\parallel}
e^{-\epsilon\omega_{n,\boldsymbol k_\parallel}}.
$$

Depois subtrai-se a energia livre correspondente. O limite finito universal é:

$$
\frac{\Delta E(a)}{A}
=
-\frac{\pi^2\hbar c}{720a^3}.
$$

## 4. Pressão

A pressão é:

$$
P(a)
=
-\frac{\partial}{\partial a}
\left(
\frac{\Delta E(a)}{A}
\right).
$$

Logo:

$$
P(a)
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

O sinal negativo indica atração.

## 5. O que é GDQ nesse cálculo?

O número universal acima coincide com a soma padrão de modos porque, no limite
de placas ideais, a Hessiana física reduz ao operador de ondas transversais
convencional.

A contribuição GDQ não é trocar esse resultado por outro. Ela é:

1. identificar a soma de modos como determinante da Hessiana física projetada;
2. interpretar a força como diferença de impedância/pressão geométrica entre
   interior e exterior;
3. tratar as placas como contornos/aparelhos clássicos que alteram o domínio
   da Hessiana;
4. exigir que materiais reais entrem por operadores de interface, não por
   condições ideais impostas sem controle.

## 6. DtN/Schur para placas reais

Para placas reais, a condição de contorno ideal deve ser substituída por uma
impedância:

$$
\mathsf R_{\rm plate}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

Então o determinante físico tem a forma esquemática:

$$
\Delta E
=
\frac{\hbar}{2}
\operatorname{Tr}_{\rm phys}
\log K_{\rm cav}(\mathsf R_1,\mathsf R_2)
-\Delta E_{\rm ref}.
$$

Temperatura entra por compactificação euclidiana do tempo físico ou soma de
Matsubara:

$$
\omega_m=\frac{2\pi m k_BT}{\hbar}.
$$

Materiais entram por resposta dielétrica/condutiva efetiva, isto é, pela
própria $\mathsf R_{\rm plate}(\omega,k_\parallel,T)$.

## 7. Regulador físico ou auxiliar?

Há duas camadas:

1. o regulador matemático usado para extrair a parte universal ideal é
   auxiliar;
2. a GDQ possui corte/rigidez física no UV, mas o coeficiente universal
   $-\pi^2\hbar c/(240a^4)$ não depende dos detalhes desse corte quando
   $a$ é muito maior que a escala microscópica.

Portanto, no problema ideal, o regulador deve desaparecer da resposta final.
Em materiais reais, o corte físico e a resposta de material aparecem em
$\mathsf R_{\rm plate}$ e deixam de ser universais.

