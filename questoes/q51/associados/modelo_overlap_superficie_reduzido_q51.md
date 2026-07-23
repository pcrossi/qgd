# Q51 — Modelo reduzido de overlap de superfície

## 1. Motivação

O benchmark mostrou que a troca:

$$
\nu_0\to\nu_{\rm int}
$$

melhora pouco a comparação com meias-vidas alfa, enquanto a métrica
exponencial legada:

$$
g_{rr}^{\rm leg}
=
\exp(-\alpha^2V_C/Q_\alpha)
$$

não melhora a série.

Isso indica que o termo ausente não é uma correção universal simples da
barreira. O termo ausente tem escala de overlap/preformação do cluster alfa na
superfície nuclear.

## 2. Taxa correta

A forma reduzida deve ser:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
S_\alpha^{\rm GDQ}
\exp(-W_{\rm rad}^{\rm GDQ}).
$$

Aqui:

1. \(\nu_{\rm GDQ}\) é a frequência normal interna;
2. \(W_{\rm rad}^{\rm GDQ}\) é a ação radial efetiva;
3. \(S_\alpha^{\rm GDQ}\) é o overlap de superfície.

## 3. Overlap como forma quadrática de superfície

O cluster alfa é um modo coletivo de quatro nucleons no contorno do núcleo.
Se \(\Phi_{4N}\) denota esse modo e \(P_\perp\) remove componentes de gauge,
translação e modos já pertencentes ao núcleo filho, então:

$$
E_{\partial}^{\rm GDQ}[\alpha]
=
\langle
P_\perp\Phi_{4N},
\mathsf R_{\partial}^{\rm GDQ}
P_\perp\Phi_{4N}
\rangle_{\partial}.
$$

A impedância de superfície é:

$$
\mathsf R_{\partial}^{\rm GDQ}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

Logo:

$$
S_\alpha^{\rm GDQ}
=
\exp(-E_{\partial}^{\rm GDQ}[\alpha]).
$$

## 4. Diagnóstico inverso

Enquanto \(E_{\partial}^{\rm GDQ}\) não for calculado diretamente, podemos
dimensionar o que ele precisa produzir.

Define-se:

$$
W_{\rm req}
=
\ln\left(
\frac{T_{1/2}^{\rm exp}\nu_{\rm int}}{\ln2}
\right),
$$

e:

$$
\Delta W_{\rm req}
=
W_{\rm req}-W_{\rm Gamow}.
$$

Então:

$$
S_\alpha^{\rm eff}
=
\exp(-\Delta W_{\rm req}).
$$

Para evitar interpretar valores maiores que 1 como probabilidade, define-se
a energia positiva requerida:

$$
E_{\partial}^{\rm req}
=
\max(\Delta W_{\rm req},0).
$$

## 5. Resultado diagnóstico

A saída numérica está em:

- `saida_diagnostico_overlap_superficie_q51.md`.

O resultado mostra duas classes:

1. U-238 e Th-232: o canal radial com \(\nu_{\rm int}\) já é suficientemente
   próximo, e o resíduo negativo aponta para refinamento de raio/frequência ou
   dataset;
2. U-234, U-232, Ra-226 e Po-212: há energia positiva de superfície a ser
   prevista por \(E_{\partial}^{\rm GDQ}\).

## 6. Veredito

$$
\boxed{
\text{a próxima peça da Q51 é }S_\alpha^{\rm GDQ}
\text{ como overlap de superfície.}
}
$$

Isso preserva a GDQ como GDQ: não se introduz fator espectroscópico manual;
calcula-se a impedância de superfície do background nuclear.

