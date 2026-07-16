# Q29 — No-go para completar a Hessiana anisotrópica sem nova rigidez

## 1. Espaço de perturbações

Seja $\mathscr H_{\rm full}$ o espaço físico de perturbações Hermitiano--
Bismut da métrica interna, depois da fixação de difeomorfismos. Ele contém o
modo homogêneo de Berger

$$
h_B
=
\delta q\,
R^2\left(2\sigma_3^2-\sigma_1^2-\sigma_2^2\right),
$$

que preserva a homogeneidade e deforma fibra e base diferencialmente.

Portanto,

$$
\operatorname{span}\{h_B\}
\subset
\mathscr H_{\rm full}.
$$

## 2. Resultado já calculado

Depois de eliminar a resposta radial, a segunda variação da ação reduzida
forneceu

$$
\boxed{
\delta^2\mathcal S[h_B,h_B]
=
H_q^{\rm eff}\|h_B\|^2,
\qquad
H_q^{\rm eff}=-2{,}67090856<0.
}
$$

Esse é um modo físico de squashing, não uma difeomorfismo pura. O vínculo de
fluxo e a condição de Noether já foram testados e não o removem.

## 3. Princípio min--max

Se $\mathbb H_{\rm full}$ é a Hessiana auto-adjunta completa, seu menor
autovalor satisfaz

$$
\lambda_{\min}(\mathbb H_{\rm full})
\leq
\frac{
\langle h_B,\mathbb H_{\rm full}h_B\rangle
}{\langle h_B,h_B\rangle}.
$$

Como o quociente de Rayleigh do modo Berger é negativo,

$$
\boxed{
\lambda_{\min}(\mathbb H_{\rm full})
\leq-2{,}67090856<0.
}
$$

Adicionar harmônicos horizontais, modos $\ell\ge1$ ou mais funções de base
num método de Galerkin não pode eliminar essa direção. Aumentar o subespaço
variacional só pode manter ou diminuir a estimativa do menor autovalor.

## 4. Consequência para a EDP completa

É possível resolver formalmente as equações estacionárias em
$(\chi,w,\bar w)$, mas o background conectado ao ramo redondo não seria um
mínimo. Sua matriz cinética eletromagnética não definiria uma resposta estável
do vácuo e não poderia ser usada para prever $\alpha$.

Logo, executar uma grande simulação angular neste ponto apenas refinaria uma
sela já demonstrada instável.

## 5. Rigidez mínima necessária

Se a interface contribuir com uma Hessiana $H_q^{\partial}$ no mesmo modo, a
condição necessária é

$$
\boxed{
H_q^{\partial}>2{,}67090856.
}
$$

No limiar,

$$
H_q^{\rm total}
=
-2{,}67090856+H_q^{\partial}>0.
$$

Essa rigidez deve ser obtida pela segunda variação do termo oficial de
contorno sob squashing de Berger. A transgressão topológica escalar já testada
é independente de $q$ e possui Hessiana nula; ela não resolve o problema.

## 6. Diferença para a quártica do modo eletrofraco

A quártica positiva anteriormente derivada estabiliza a amplitude carregada
$\beta$:

$$
a_4^{\rm total}>0.
$$

Isso não implica estabilidade do modo métrico homogêneo $q$. São direções
distintas da Hessiana:

$$
\beta
=
\text{modo torsional }\ell=1,
\qquad
q
=
\text{squashing métrico homogêneo}.
$$

Portanto, nenhum resultado anterior precisa ser descartado; apenas não se pode
usar a estabilização de $\beta$ como se estabilizasse $q$.

## 7. Próximo cálculo bem posto

Antes da EDP completa, é necessário calcular

$$
H_q^{\partial}
=
\frac{d^2}{dq^2}
\mathcal S_{\partial}^{\rm GDQ}
\bigg|_{q=q_*}
$$

para a geometria real da interface, incluindo sua segunda forma fundamental,
torção de Bismut e condição de volume/fluxo. Somente se
$H_q^{\partial}>2{,}67090856$ existe um background anisotrópico estável sobre
o qual calcular a matriz cinética completa.

## 8. Veredito

$$
\boxed{
\text{a EDP anisotrópica não deve ser usada para }\alpha
\text{ antes de estabilizar o modo Berger.}
}
$$

Esse no-go preserva todos os resultados estruturais e evita transformar uma
sela num vácuo por refinamento numérico.
