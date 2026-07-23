# Background global: produto livre ou geometria cosmológica vinculada

## 1. Questão

O DtN exterior precisa ser avaliado num background que seja estacionário no
espaço admissível. Considere a geometria homogênea

$$
T^4\times S^1_L\times S^3_R
$$

com $f=u$ constante e normalização

$$
\int\mathcal U,dV=1.
$$

## 2. Escalar geométrico

Na convenção

$$
d\sigma_i=2\epsilon_{ijk}\sigma_j\wedge\sigma_k,
$$

tem-se

$$
R_{\rm LC}=\frac6{R^2}.
$$

A torção homogênea satisfaz

$$
H=\frac2R e^{678},
$$

e, na convenção tensorial,

$$
|H|^2=\frac{24}{R^2}.
$$

Logo,

$$
\boxed{
\mathcal R_{\rm GDQ}
=R_{\rm LC}-\frac1{12}|H|^2
=\frac4{R^2}.
}
$$

## 3. Normalização da medida

Como

$$
\operatorname{Vol}(M)=C\,L R^3,
$$

a normalização fixa

$$
u
=\log(CLR^3)-4\log(4\pi z_\tau).
$$

O integrando on shell homogêneo, omitindo constantes, é

$$
W_{\rm hom}(L,R)
=\frac{4\tau}{R^2}+\log L+3\log R+C_0-4.
$$

Portanto,

$$
\boxed{
\frac{\partial W_{\rm hom}}{\partial\log L}=1.
}
$$

## 4. Consequência

Se $L$ for um módulo variado livremente, o produto homogêneo não é ponto
crítico da ação normalizada. Isso é a obstrução do fator toroidal plano.

Esse resultado não se aplica se $L$ e $R$ são dados cosmológicos de contorno
e, portanto, não pertencem ao espaço de variações. Nesse caso há duas
formulações lícitas:

1. restringir as variações a
   $\delta L=\delta R=0$;
2. introduzir multiplicadores dos vínculos cosmológicos
   $L=L_{\rm cos}$ e $R=R_{\rm cos}$.

Os multiplicadores representam tensão/energia externa do problema
cosmológico; não alteram a ação fundamental.

## 5. Hessiana vinculada

Se os dados cosmológicos são escritos como vínculos $\mathcal C_{\rm cos}$,
a Hessiana exterior correta é

$$
K_+^{\rm phys}
=P^{{\rm phys}\dagger}
\left[
D^2\mathcal S_{\rm GDQ}
-\lambda_{\rm cos}^aD^2\mathcal C_{{\rm cos},a}
\right]
P^{\rm phys}.
$$

Usar apenas $D^2\mathcal S_{m GDQ}$ enquanto se mantém artificialmente o
produto fixo seria inconsistente.

## 6. O que isso decide

- Produto com módulos livres: excluído como sela.
- Produto com raios cosmológicos prescritos: admissível como problema
  vinculado, desde que os multiplicadores sejam calculados.
- Background warped dinâmico: continua sendo a rota sem congelamento dos
  módulos.

Assim, há duas rotas finais honestas para calcular $\mu_*$:

1. fornecer os vínculos cosmológicos e avaliar a Hessiana vinculada;
2. resolver o background warped completo.

As conservações já determinam a forma dos vínculos, mas não fornecem os
valores de $L_{\rm cos}$, $R_{\rm cos}$ e da energia cosmológica, que são dados
de contorno do problema.

