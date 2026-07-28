---
title: "Hartman como teorema reduzido condicional"
---

# Hartman como teorema reduzido condicional

## Enunciado

No setor evanescente unidimensional reduzido:

$$
\Omega_L=[0,L],
\qquad
V_0>E,
$$

o modo estacionário é:

$$
\psi(x)=\psi_0e^{-\kappa x},
\qquad
\kappa=\frac{\sqrt{2m(V_0-E)}}{\hbar}.
$$

Portanto:

$$
\rho(x)=\rho_0e^{-2\kappa x}.
$$

Na GDQ, essa densidade é a redução Madelung do campo geométrico:

$$
\rho=e^{-(f+\bar f)/2}.
$$

O que se quer provar não é propagação superluminal. O enunciado correto é:

1. o tempo de pico/grupo pode saturar com a largura da barreira;
2. essa saturação não é velocidade de frente;
3. a GDQ reduzida fornece uma leitura causal por comprimento próprio saturado;
4. a relação $g_{xx}\propto\rho$ é condicional ao setor evanescente, não
   identidade métrica universal.

## Hipóteses da redução

A redução usa:

1. barreira estacionária;
2. modo evanescente;
3. corrente real propagante suprimida no interior;
4. transversais congeladas;
5. interface normalizada em $x=0$;
6. calibre longitudinal de medida;
7. minimização da energia geométrica do canal.

Sob essas hipóteses, a solução longitudinal admissível é:

$$
g_{xx}(x)=g_0\frac{\rho(x)}{\rho_0},
$$

logo:

$$
g_{xx}(x)=g_0e^{-2\kappa x}.
$$

Classificação:

$$
\boxed{
g_{xx}\propto\rho
\text{ é solução reduzida condicional, não novo axioma.}
}
$$

## Distância própria

A distância própria é:

$$
D_{\rm prop}(L)
=
\int_0^L\sqrt{g_{xx}(x)}\,dx.
$$

Como:

$$
\sqrt{g_{xx}(x)}
=
\sqrt{g_0}e^{-\kappa x},
$$

temos:

$$
D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}
\left(1-e^{-\kappa L}\right).
$$

No limite opaco:

$$
\lim_{L\to\infty}D_{\rm prop}(L)
=
\frac{\sqrt{g_0}}{\kappa}.
$$

Essa é a saturação geométrica de Hartman.

## Tempo próprio efetivo

$$
\tau_{\rm GDQ}(L)
=
\int_0^L\frac{ds}{v_{\rm prop}(x)}.
$$

Se, no regime estacionário, $v_{\rm prop}=v_0\le c$:

$$
\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}
\left(1-e^{-\kappa L}\right).
$$

Portanto:

$$
\lim_{L\to\infty}\tau_{\rm GDQ}(L)
=
\frac{\sqrt{g_0}}{v_0\kappa}.
$$

O tempo saturado é tempo de pico/grupo ou tempo próprio efetivo do canal. Não é
tempo de frente.

## Tempo de comparação com a literatura

A literatura de Hartman frequentemente usa o tempo de fase ou Wigner--Smith:

$$
\tau_W(E)
=
\hbar
\frac{\partial}{\partial E}
\arg T(E).
$$

Esse tempo deve ser separado do tempo de frente e do tempo próprio GDQ.

## Deformação de pacotes

Para pacote incidente:

$$
\Psi_{\rm in}(x,t)
=
\int A(E)e^{i(kx-\omega t)}\,dE,
$$

o pacote transmitido é:

$$
\Psi_T(x,t)
=
\int T(E)A(E)e^{i(kx-\omega t)}\,dE.
$$

A aproximação de tempo de grupo é legítima quando $A(E)$ é estreito e
$T(E)$ é regular na banda. Em barreiras opacas, $T(E)$ filtra o espectro e
pode remodelar o pico. Pico remodelado não é sinal superluminal.

## Frente causal

A velocidade de coordenada aparente:

$$
v_{\rm coord}(L)=\frac{L}{\tau_{\rm GDQ}(L)}
$$

pode crescer quando $L$ cresce porque $\tau_{\rm GDQ}$ satura. Mas essa razão
não é velocidade local.

A velocidade física local é:

$$
v_{\rm prop}=\frac{ds}{dt}\le c,
$$

e a frente causal obedece:

$$
v_{\rm front}\le c.
$$

Logo:

$$
\boxed{
\text{Hartman em GDQ é comprimento próprio saturado, não propagação superluminal.}
}
$$

## Alcance e pendência metrológica

Para comparar com um experimento específico é necessário declarar:

1. forma exata da barreira;
2. banda espectral do pulso;
3. definição operacional de tempo;
4. detector;
5. critério de frente;
6. contorno material.

Esses dados pertencem ao experimento. Eles não são novos axiomas da GDQ.

## Certificação Lean

O módulo
[TransportInterference.lean](../../../formal/GDQ/TransportInterference.lean)
formaliza a redução declarada nesta nota. Ele prova:

1. $0<e^{-2\kappa L}\leq1$ para $\kappa,L\geq0$;
2. a identidade exata entre a distância e seu erro exponencial;
3. $0\leq D_{\rm prop}(L)\leq\sqrt{g_0}/\kappa$;
4. a convergência de $D_{\rm prop}$ e do tempo próprio efetivo às respectivas
   assíntotas.

Lean certifica a dedução depois da hipótese
$g_{xx}=g_0e^{-2\kappa x}$. Não promove essa relação reduzida a identidade
universal da ação oficial.
