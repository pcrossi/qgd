# Derivação reduzida do efeito Hartman na GDQ

## 1. Domínio do problema

O efeito Hartman é analisado no setor efetivo unidimensional:

$$
\Omega_L=[0,L]\subset\mathbb R_x
$$

com barreira retangular:

$$
V(x)=V_0>E,
\qquad
0<x<L.
$$

No interior da barreira, o modo estacionário é evanescente:

$$
\psi(x)=\psi_0 e^{-\kappa x},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Assim:

$$
\rho(x)=|\psi(x)|^2=\rho_0 e^{-2\kappa x}.
$$

Na GDQ, esta expressão não é ontologia fundamental de função de onda. Ela é a
redução Madelung do campo geométrico:

$$
\rho=e^{-(f+\bar f)/2}.
$$

## 2. O que se pretende provar

A Q45 não precisa provar que uma partícula atravessa uma barreira com
velocidade superluminal. O objetivo correto é provar que:

1. o tempo de pico/grupo pode saturar com $L$;
2. essa saturação não é velocidade de frente;
3. a geometria efetiva da GDQ fornece uma leitura causal do fenômeno;
4. a relação $g_{xx}\propto\rho$ é uma solução reduzida sob hipóteses
   explícitas, não uma identidade métrica universal.

## 3. Relação métrica reduzida

No setor evanescente estacionário, a fase transportadora fica suprimida dentro
da barreira. O campo relevante é a parte real de $f$, equivalente à densidade
hidrodinâmica.

Assume-se:

1. transversais congeladas;
2. ausência de corrente real propagante dentro da barreira;
3. contorno assintótico normalizado em $x=0$;
4. calibre longitudinal no qual a densidade geométrica define o elemento de
   linha efetivo do canal evanescente.

Nessas hipóteses, a solução longitudinal admissível é:

$$
g_{xx}(x)=g_{xx}(0)\frac{\rho(x)}{\rho_0}.
$$

Como:

$$
\rho(x)=\rho_0e^{-2\kappa x},
$$

segue:

$$
g_{xx}(x)=g_0e^{-2\kappa x}.
$$

Portanto:

$$
ds=\sqrt{g_{xx}}\,dx=\sqrt{g_0}e^{-\kappa x}dx.
$$

## 4. Essa relação resulta da ação oficial?

Sim, mas apenas como teorema reduzido e condicional.

A ação oficial permanece:

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

A relação $g_{xx}\propto\rho$ não é obtida variando uma ação auxiliar
Einstein--Hilbert, nem deve ser promovida a lei universal.

Ela resulta da ação oficial depois de impor:

1. redução unidimensional;
2. congelamento dos modos transversais;
3. setor evanescente estacionário;
4. calibre de medida longitudinal;
5. normalização na interface;
6. condição de minimização da energia geométrica do canal sem corrente
   transportadora.

Em termos operacionais:

$$
\delta\mathcal S_{\rm GDQ}=0
\quad
\text{no setor reduzido}
\quad
\Longrightarrow
\quad
g_{xx}=g_0\rho/\rho_0.
$$

O resultado é, portanto:

$$
\boxed{
g_{xx}\propto\rho
\text{ é uma solução reduzida do canal evanescente, não um axioma novo.}
}
$$

## 5. Distância própria saturada

A distância própria dentro da barreira é:

$$
D_{\rm prop}(L)
=\int_0^L\sqrt{g_{xx}(x)}\,dx.
$$

Substituindo a solução reduzida:

$$
D_{\rm prop}(L)
=\sqrt{g_0}\int_0^L e^{-\kappa x}\,dx.
$$

Logo:

$$
D_{\rm prop}(L)
=\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

No limite opaco:

$$
\lim_{L\to\infty}D_{\rm prop}(L)
=\frac{\sqrt{g_0}}{\kappa}.
$$

Esta é a versão geométrica da saturação de Hartman.

## 6. Tempo usado

Existem várias noções de tempo de tunelamento. A Q45 usa duas, separadas:

1. tempo de grupo ou Wigner--Smith, usado para comparar com a literatura:

$$
\tau_{\rm W}(E)
=\hbar\frac{\partial}{\partial E}\arg T(E);
$$

2. tempo próprio efetivo GDQ do canal evanescente:

$$
\tau_{\rm GDQ}(L)
=\int_0^L\frac{ds}{v_{\rm prop}(x)}.
$$

Se a velocidade física local no canal reduzido é limitada por:

$$
v_{\rm prop}\le c,
$$

e, no regime estacionário, é tomada como constante efetiva $v_0$, então:

$$
\tau_{\rm GDQ}(L)
=\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Assim:

$$
\lim_{L\to\infty}\tau_{\rm GDQ}(L)
=\frac{\sqrt{g_0}}{v_0\kappa}.
$$

O tempo GDQ acima é tempo de trânsito próprio reduzido. Ele explica
geometricamente a saturação. A comparação metrológica com experimentos deve
especificar se o observável é atraso de fase, tempo de permanência, tempo de
Larmor, tempo de Büttiker--Landauer ou tempo de chegada.

## 7. Deformação de pulsos

Para um pacote incidente:

$$
\Psi_{\rm in}(x,t)
=\int A(E)e^{i(kx-\omega t)}\,dE,
$$

o pacote transmitido é:

$$
\Psi_{\rm T}(x,t)
=\int T(E)A(E)e^{i(kx-\omega t)}\,dE.
$$

A aproximação de tempo de grupo é válida quando:

1. $A(E)$ é estreito;
2. $T(E)$ não distorce fortemente a banda;
3. não há zeros ou singularidades próximos à faixa observada;
4. o pico transmitido ainda representa o mesmo ramo analítico do pacote.

Em barreiras opacas, $T(E)$ atua como filtro espectral. Portanto, picos podem
ser avançados por reshaping. Isso não mede velocidade de sinal.

Na GDQ, essa deformação é tratada pela mesma separação:

$$
\text{pico/centroide}
\ne
\text{frente causal}.
$$

O pico segue a resposta espectral do canal. A frente segue o domínio causal da
equação efetiva reconstruída.

## 8. Velocidade de frente

A frente de um sinal é a primeira descontinuidade ou primeiro suporte novo
causalmente gerado por uma perturbação. Ela não é o máximo do pacote
transmitido.

Na GDQ, a velocidade de frente permanece causal porque a reconstrução física
impõe cones locais:

$$
v_{\rm front}\le c.
$$

A contração de distância própria não altera essa afirmação. Ela apenas diz que
o comprimento físico efetivo do canal evanescente é:

$$
D_{\rm prop}(L)
\le
\frac{\sqrt{g_0}}{\kappa}.
$$

Logo, a razão de coordenada:

$$
\frac{L}{\tau_{\rm GDQ}(L)}
$$

pode crescer sem limite quando $L\to\infty$, mas essa razão não é velocidade
local nem velocidade de frente.

## 9. Resultado consolidado

No setor declarado:

$$
\rho(x)=\rho_0e^{-2\kappa x},
\qquad
g_{xx}(x)=g_0e^{-2\kappa x}.
$$

Então:

$$
D_{\rm prop}(L)
=\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right),
$$

e:

$$
\tau_{\rm GDQ}(L)
=\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Portanto:

$$
\boxed{
\text{o efeito Hartman é saturação geométrica de comprimento próprio,
não propagação superluminal.}
}
$$

## 10. Limitação

A Q45 fica fechada estruturalmente, não metrologicamente. Para comparar com um
experimento específico é necessário declarar:

1. forma exata da barreira;
2. banda espectral do pulso;
3. definição operacional de tempo;
4. detector;
5. critério de frente;
6. contornos materiais.

Esses dados pertencem ao experimento. Não são novos axiomas da GDQ.
Foram registrados em `ideias/possibilidades.md` como refinamento futuro, sem
reabrir o fechamento estrutural da Q45.
