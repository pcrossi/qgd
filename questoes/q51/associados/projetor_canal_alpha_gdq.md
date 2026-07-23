# Q51 — Projetor físico do canal alfa

## 1. Problema

A aproximação espectral média:

$$
E_\partial^{\rm spec}
=
\frac4{\alpha}\mathcal I_\Sigma(\chi_{\rm curv})
$$

fica na escala correta, mas não seleciona o canal físico. Ela aplica a
impedância de superfície média a todo modo \(4N\), sem distinguir:

1. modos de gauge;
2. translações;
3. deformações coletivas do núcleo filho;
4. componentes que não formam cluster alfa;
5. componentes de camada fechada ou quase fechada.

Logo, falta o projetor:

$$
P_\perp.
$$

## 2. Definição variacional correta

Seja \(K_{\partial}^{\rm phys}\) a Hessiana física de superfície do background
nuclear, já com vínculos e gauge removidos.

O subespaço alfa é selecionado por uma janela espectral \(\mathcal C_\alpha\)
no espectro de \(K_{\partial}^{\rm phys}\). O projetor de Riesz é:

$$
P_\alpha
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_{\partial}^{\rm phys})^{-1}\,dz.
$$

O projetor físico de canal deve remover os modos que não participam da emissão:

$$
P_\perp
=
P_\alpha
\left(
1-P_{\rm gauge}
-P_{\rm trans}
-P_{\rm filho}
\right),
$$

entendido como composição ortogonal no produto de superfície físico.

Mais explicitamente, no subespaço já reduzido:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

## 3. Energia de superfície final

Com esse projetor:

$$
E_\partial^{\rm GDQ}
=
\langle
P_\perp\Phi_{4N},
\mathsf R_\partial^{\rm GDQ}
P_\perp\Phi_{4N}
\rangle_\partial.
$$

E:

$$
S_\alpha^{\rm GDQ}
=
\exp(-E_\partial^{\rm GDQ}).
$$

## 4. Diagnóstico do peso de projeção

Da aproximação espectral média temos \(E_\partial^{\rm spec}\). Do diagnóstico
experimental temos \(E_\partial^{\rm req}\). Define-se:

$$
p_{\rm req}
=
\frac{E_\partial^{\rm req}}{E_\partial^{\rm spec}}.
$$

Esse número não é usado como ajuste. Ele mede qual fração da impedância média
o projetor real precisa preservar.

No dataset diagnóstico:

| Núcleo | \(p_{\rm req}\) | \(\sqrt{p_{\rm req}}\) |
| --- | ---: | ---: |
| U-238 | \(0{,}000000\) | \(0{,}000000\) |
| U-234 | \(0{,}938269\) | \(0{,}968643\) |
| U-232 | \(0{,}630934\) | \(0{,}794313\) |
| Th-232 | \(0{,}000000\) | \(0{,}000000\) |
| Ra-226 | \(0{,}812735\) | \(0{,}901518\) |
| Po-212 | \(0{,}507847\) | \(0{,}712634\) |

## 5. Interpretação

O fato importante é:

$$
0\le p_{\rm req}\le1
$$

para todos os casos do teste.

Isso é compatível com a interpretação de \(p_{\rm req}\) como norma quadrática
de projeção:

$$
p_{\rm req}
\sim
\frac{
\|P_\perp\Phi_{4N}\|_{\mathsf R}^2
}{
\|\Phi_{4N}\|_{\mathsf R}^2
}.
$$

Portanto, a impedância média não precisa mudar de sinal nem ser recalibrada.
Ela precisa ser filtrada pelo projetor espectral correto.

## 6. O que falta calcular diretamente

Para transformar isso em previsão:

1. construir \(K_{\partial}^{\rm phys}\) para o núcleo pai;
2. identificar a janela espectral \(\mathcal C_\alpha\);
3. calcular \(P_\alpha\) por integral de Riesz;
4. remover o subespaço do núcleo filho;
5. avaliar \(E_\partial^{\rm GDQ}\).

## 7. Veredito

$$
\boxed{
\text{o próximo elo da Q51 é matematicamente bem definido: calcular }P_\perp.
}
$$

A boa notícia é que os pesos requeridos estão no intervalo de um projetor
ortogonal. Isso torna a rota coerente.

