# Núcleo crítico do par mesônico pela torção dupla

## 1. Correção da coordenada de nucleação

O ansatz anterior escreveu

$$
V(a)=V_0+\nu a^2+O(a^4),
$$

o que produz uma contribuição torsional quadrática negativa. Essa afirmação é
correta somente se $a$ for uma coordenada coletiva cuja variação de volume
comece em $a^2$. Ela não pode ser transferida automaticamente para o raio
físico $r$ de uma nova garganta.

Para uma garganta tridimensional com elo $S^3$, a lei geométrica natural é

$$
\boxed{
V(r)=V_0+\nu_3r^3+O(r^4),
\qquad \nu_3>0.
}
$$

Consequentemente, a torção favorece a abertura no primeiro termo cúbico, não
necessariamente na Hessiana radial em $r=0$.

## 2. Custo das duas calotas redondas

Use como benchmark local duas meias esferas redondas de dimensão quatro e
raio $r$. Para cada calota,

$$
R_{S^4}=\frac{12}{r^2},
$$

$$
\operatorname{Vol}\left(\frac12S^4_r\right)
=\frac{4\pi^2}{3}r^4.
$$

Logo,

$$
\int_{\frac12S^4_r}R\,dV
=16\pi^2r^2.
$$

As duas calotas fornecem

$$
\boxed{
\int_{\text{duas calotas}}R\,dV
=32\pi^2r^2.
}
$$

Defina o peso causal local da parcela de curvatura da ação oficial por

$$
\mathfrak w_\gamma
:=\operatorname{Re}
\int_\gamma
\frac{\hbar}{\Lambda_C^2}
\mathcal U_0(\tau)\,d\tau.
$$

O fator $\tau$ que multiplica $R$ na ação cancela o $1/\tau$ da medida
externa. Se $\mathcal U$ puder ser congelada no valor local $\mathcal U_0$ ao
nível quadrático, o custo das calotas é

$$
\boxed{
A_{\text{cap}}r^2
=32\pi^2\mathfrak w_\gamma r^2.
}
$$

Esse é um cálculo direto no ansatz redondo; não é ainda o mínimo entre todas
as geometrias de calota.

## 3. Custo do colar curto

Para um colar produto $S^3_r\times[0,L]$ com $L=\ell r$,

$$
R_{S^3_r\times I}=\frac6{r^2},
$$

$$
\operatorname{Vol}(S^3_r\times[0,\ell r])
=2\pi^2\ell r^4.
$$

Portanto,

$$
\int_{S^3_r\times[0,\ell r]}R\,dV
=12\pi^2\ell r^2.
$$

No benchmark redondo,

$$
\boxed{
A_2
=\pi^2(32+12\ell)\mathfrak w_\gamma
+A_{f,\Psi}^{(2)},
}
$$

onde $A_{f,\Psi}^{(2)}$ reúne qualquer custo quadrático adicional de $f$, da
transgressão e do matching. Para um contorno físico coercivo espera-se
$\mathfrak w_\gamma>0$, mas esse sinal deve vir da especificação de $\gamma$.

## 4. Ganho produzido pela torção dupla

A torção preferencial do estômato contrário é

$$
Q_{\text{pref}}=2\tau.
$$

Assim,

$$
E_T(r)
=\frac{\kappa_T(2\tau)^2}{2V(r)}
=\frac{2\kappa_T\tau^2}{V(r)}.
$$

Com $V(r)=V_0+\nu_3r^3+O(r^4)$,

$$
E_T(r)-E_T(0)
=-\frac{2\kappa_T\tau^2\nu_3}{V_0^2}r^3
+O(r^4).
$$

Defina

$$
\boxed{
B_3:=\frac{2\kappa_T\tau^2\nu_3}{V_0^2}>0.
}
$$

O fator dois do estômato contrário aparece ao quadrado na energia e fornece o
fator quatro em $Q_{\text{pref}}^2=(2\tau)^2$.

## 5. Potencial reduzido do núcleo

Até quarta ordem, o potencial radial possui a forma

$$
\boxed{
\Delta\mathcal A(r)
=A_2r^2-B_3r^3+C_4r^4+o(r^4),
\qquad r\geq0.
}
$$

Aqui:

1. $A_2>0$ é o custo das duas calotas e do colar;
2. $B_3>0$ é o ganho causado pela redistribuição da torção dupla;
3. $C_4>0$ representa a estabilização ultravioleta, o matching de $f$ e os
   termos superiores da geometria.

Como

$$
\Delta\mathcal A''(0)=2A_2>0,
$$

o estado sem par é localmente estável no raio físico. A criação ocorre por um
núcleo crítico finito.

## 6. Existência do núcleo crítico

Os pontos estacionários não nulos satisfazem

$$
2A_2-3B_3r+4C_4r^2=0.
$$

Eles existem se

$$
\boxed{
9B_3^2\geq32A_2C_4.
}
$$

Os dois raios são

$$
r_\pm
=\frac{3B_3\pm\sqrt{9B_3^2-32A_2C_4}}{8C_4}.
$$

O menor, $r_-$, é a barreira/núcleo crítico; o maior, $r_+$, é o ramo
bimodal estabilizado quando sua ação for inferior à origem.

## 7. Condição para o ramo bimodal ser energeticamente preferido

O polinômio pode ser escrito como

$$
\Delta\mathcal A(r)
=r^2(A_2-B_3r+C_4r^2).
$$

Existe $r>0$ com $\Delta\mathcal A(r)<0$ se, e somente se,

$$
\boxed{
B_3^2>4A_2C_4.
}
$$

No limiar degenerado,

$$
B_3^2=4A_2C_4,
$$

e o novo mínimo toca a energia do nêutron em

$$
r_*=\frac{B_3}{2C_4}.
$$

Substituindo a torção dupla, a condição é

$$
\boxed{
\left(
\frac{2\kappa_T\tau^2\nu_3}{V_0^2}
\right)^2
>4A_2C_4.
}
$$

Essa é a desigualdade quantitativa que expressa “a torção preferencial cria o
par” no ansatz radial físico.

## 8. Interpretação dinâmica

Mesmo quando $B_3^2>4A_2C_4$, a origem continua separada do ramo bimodal por
uma barreira em $r_-$. Portanto, há duas possibilidades:

1. o contorno causal fornece uma sela de túnel atravessando $r_-$;
2. uma flutuação/dinâmica coletiva leva o sistema além do raio crítico.

Para o decaimento espontâneo do nêutron livre, a primeira opção é a rota
natural. A taxa exige avaliar a ação da sela completa, não apenas a altura do
polinômio truncado.

## 9. Relação com o resultado quadrático anterior

O resultado

$$
\lambda_T
=-\frac{4\kappa_T\tau^2\nu}{V_0^2}
$$

permanece correto para uma coordenada coletiva $a$ definida por
$\Delta V=\nu a^2$. Ele não é uma Hessiana universal em relação ao raio
geométrico. Para $\Delta V\sim r^3$, a contribuição torsional inicia na ordem
cúbica.

Logo, o enunciado conservador vigente é:

$$
\boxed{
\text{a torção dupla favorece o par e pode criar um núcleo crítico finito;}
}
$$

$$
\boxed{
\text{ela não prova, sozinha, instabilidade infinitesimal em }r=0.
}
$$

## 10. Parâmetros que ainda precisam ser derivados

Para decidir a desigualdade sem ajuste, calcular da ação oficial:

$$
\mathfrak w_\gamma,
\qquad
\ell,
\qquad
A_{f,\Psi}^{(2)},
\qquad
\nu_3,
\qquad
C_4.
$$

O alvo experimental da vida média não pode participar da determinação desses
coeficientes.

## 11. Classificação

- integral de curvatura das calotas e do colar redondos: avaliação analítica
  direta do ansatz;
- termo torsional cúbico: derivação exata sob fluxo fixo e
  $V(r)=V_0+\nu_3r^3+O(r^4)$;
- potencial $A_2r^2-B_3r^3+C_4r^4$: redução efetiva local;
- critérios $9B_3^2\geq32A_2C_4$ e $B_3^2>4A_2C_4$: identidades algébricas;
- valores de $A_2,B_3,C_4$: ainda condicionais aos backgrounds e ao contorno;
- nucleação e taxa: abertas até a solução causal da sela.
