# Derivação da sela torsional conformal da ação oficial

## 1. Enunciado e status

O objetivo é verificar se a ação oficial da GDQ seleciona uma configuração
com torção não nula dentro da família já construída:

$$
g(a)=e^{2ax^0}\delta,
\qquad
\omega(a)=e^{2ax^0}\omega_0,
\qquad
H(a)=d_J^c\omega(a).
$$

O cálculo abaixo é uma variação restrita e exata nessa família. Ele não
substitui a futura variação simultânea de todos os componentes de
$(g,J,H,f)$.

## 2. Domínio, contorno e normalização

As hipóteses são:

1. folha euclidiana positiva;
2. bulk local $\mathbb R^4\times T^4$;
3. Haar de $T^4$ normalizada a um;
4. largura gaussiana $\tau>0$;
5. parâmetro real positivo do contorno $z_\tau>0$;
6. razão de escala

$$
q=\frac{z_\tau}{\tau}>0;
$$

7. vínculo probabilístico

$$
\int_{\mathbb R^4\times T^4}\mathcal U\,dV_g=1.
$$

O potencial e a densidade são:

$$
\operatorname{Re}f
=
\frac{|x|^2}{4\tau}+f_0,
\qquad
\rho
=
\exp\left(-\frac{|x|^2}{4\tau}-f_0\right).
$$

A medida oficial é:

$$
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^4}.
$$

Como:

$$
\sqrt{\det g}=e^{8ax^0},
$$

$f_0$ não pode ser mantido fixo durante a variação em $a$. Ele deve preservar
o vínculo de normalização.

## 3. Momentos gaussianos

Para $c\in\mathbb R$, defina:

$$
I_c(a)
=
\int_{\mathbb R^4}
\exp\left(
-\frac{|x|^2}{4\tau}+cax^0
\right)d^4x.
$$

Completando o quadrado em $x^0$:

$$
-\frac{(x^0)^2}{4\tau}+cax^0
=
-\frac{(x^0-2c a\tau)^2}{4\tau}
+c^2a^2\tau.
$$

Portanto:

$$
I_c(a)
=(4\pi\tau)^2e^{c^2a^2\tau}.
$$

Na gaussiana inclinada, cada coordenada possui variância $2\tau$ e somente
$x^0$ possui média $2ca\tau$. Logo:

$$
\left\langle |x|^2\right\rangle_c
=
8\tau+4c^2a^2\tau^2.
$$

Consequentemente:

$$
\left\langle
\frac{|x|^2}{4\tau^2}
\right\rangle_c
=
\frac2\tau+c^2a^2,
$$

e:

$$
\left\langle
\frac{|x|^2}{4\tau}
\right\rangle_c
=
2+c^2a^2\tau.
$$

## 4. Vínculo de normalização

Defina:

$$
u=\tau a^2.
$$

O vínculo usa $c=8$:

$$
1
=
\frac{e^{-f_0}}{(4\pi z_\tau)^4}
(4\pi\tau)^2e^{64u}.
$$

Assim:

$$
f_0(a)
=
f_{\rm base}+64u,
$$

onde:

$$
f_{\rm base}
=
\ln\left(
\frac{(4\pi\tau)^2}{(4\pi z_\tau)^4}
\right).
$$

Uma medida de Haar do toro com volume $V_T$ apenas acrescentaria
$\ln V_T$ a $f_{\rm base}$ e não alteraria a equação de sela.

## 5. Inserção dos invariantes torsionais

Os módulos Lean anteriores provaram:

$$
\mathcal R^B
=
-60a^2e^{-2ax^0},
$$

$$
|\nabla f|_g^2
=
e^{-2ax^0}\frac{|x|^2}{4\tau^2},
$$

$$
\sqrt{\det g}
=
e^{8ax^0}.
$$

O setor $\mathcal R^B+|\nabla f|^2$ usa, portanto, o momento $c=6$. Depois de
dividir pelo vínculo normalizado, ele fornece:

$$
q e^{-28u}(2-24u).
$$

O setor $\operatorname{Re}f-4$ usa o momento $c=8$ e fornece:

$$
f_{\rm base}-2+128u.
$$

Salvo o prefator positivo $\hbar/\Lambda_C^2$, independente de $a$, a ação
oficial reduzida é:

$$
\boxed{
\mathcal A_{\rm red}(u)
=
q e^{-28u}(2-24u)
+f_{\rm base}-2+128u.
}
$$

Nenhum termo fundamental $|H|^2$ foi acrescentado.

## 6. Equação de sela

A derivada exata é:

$$
\frac{d\mathcal A_{\rm red}}{du}
=
q e^{-28u}(672u-80)+128.
$$

Como $u=\tau a^2$, temos:

$$
\frac{d\mathcal A_{\rm red}}{da}
=
2\tau a
\left[
q e^{-28u}(672u-80)+128
\right].
$$

O ramo $a=0$ é sempre estacionário. Um ramo torsional não nulo satisfaz:

$$
\boxed{
q e^{-28u_*}(672u_*-80)+128=0.
}
$$

Nos extremos:

$$
\left.\frac{d\mathcal A_{\rm red}}{du}\right|_{u=0}
=
128-80q,
$$

e:

$$
\left.
\frac{d\mathcal A_{\rm red}}{du}
\right|_{u=5/42}
=
128.
$$

Logo:

$$
\boxed{
q>\frac85
\quad\Longrightarrow\quad
\exists!\,
u_*\in\left(0,\frac5{42}\right)
}
$$

que resolve a equação de sela. A unicidade segue de:

$$
\frac{d^2\mathcal A_{\rm red}}{du^2}
=
q e^{-28u}(2912-18816u)>0
$$

em todo o intervalo $0<u<5/42$.

## 7. Forma analítica da raiz

Usando a função de Lambert $W$, a raiz é:

$$
\boxed{
u_*(q)
=
\frac1{28}
\left[
\frac{10}{3}
-
W_0\left(
\frac{16}{3q}e^{10/3}
\right)
\right],
\qquad
q>\frac85.
}
$$

As duas orientações torsionais são:

$$
\boxed{
a_*
=
\pm\sqrt{\frac{u_*(q)}{\tau}}.
}
$$

Como $u_*>0$, segue $a_*\ne0$ e a componente já formalizada:

$$
H_{451}=2a_*e^{2a_*x^0}
$$

é não nula.

## 8. Estabilidade na direção conformal

Na raiz não nula:

$$
\left.
\frac{d^2\mathcal A_{\rm red}}{da^2}
\right|_{a_*}
=
4\tau u_*
q e^{-28u_*}
(2912-18816u_*)
>0.
$$

Portanto, os dois ramos $\pm a_*$ são mínimos estritos na direção reduzida
$a$. Para $q>8/5$, o ramo $a=0$ possui rigidez negativa nessa direção. O
limiar:

$$
q_c=\frac85
$$

é uma bifurcação torsional exata.

## 9. Exemplo de controle, não calibração

Para $q=2$:

$$
u_*
\simeq
0.00609305738684,
$$

e:

$$
a_*\sqrt{\tau}
\simeq
\pm0.0780580385793.
$$

O valor $q=2$ é apenas um exemplo de verificação. Ele não é usado como
constante universal nem foi escolhido por comparação experimental.

## 10. Status científico

O resultado demonstra:

1. existência de uma sela torsional não nula da ação oficial na família
   conformal normalizada;
2. condição física explícita sobre o contorno, $q>8/5$;
3. duas orientações $\pm a_*$;
4. estabilidade estrita na direção conformal $a$.

O que ainda não foi demonstrado:

1. estabilidade contra todas as flutuações métricas, dilatônicas e
   torsionais não homogêneas;
2. remoção completa dos modos de gauge;
3. gap da Hessiana física acoplada;
4. completude e colagem global do atlas.

Assim, o objeto obtido é um **background torsional de sela derivada,
condicional ao setor reduzido e ao contorno $q>8/5$**. Ele ainda não deve ser
promovido a sóliton material 8D completamente estável.
