# Q51 — No-go para proxy simples de camada

## 1. Pergunta

Após formular \(P_\perp\), testamos se o peso de projeção poderia ser
aproximado apenas pela distância do núcleo filho a números mágicos.

Define-se:

$$
D_{\rm shell}
=
d_Z^2+d_N^2.
$$

## 2. Resultado

A saída está em:

- `saida_teste_shell_proxy_q51.md`.

Resumo:

| Núcleo | \(D_{\rm shell}\) | \(p_{\rm req}\) |
| --- | ---: | ---: |
| U-238 | \(388\) | \(0{,}000000\) |
| U-234 | \(260\) | \(0{,}938269\) |
| U-232 | \(208\) | \(0{,}630933\) |
| Th-232 | \(232\) | \(0{,}000000\) |
| Ra-226 | \(116\) | \(0{,}812735\) |
| Po-212 | \(0\) | \(0{,}507847\) |

Nenhuma função escalar simples de \(D_{\rm shell}\) resolve o padrão.

## 3. Interpretação

O fato de U-238 e Th-232 terem \(p_{\rm req}=0\) mesmo longe de camada fechada
mostra que a simples distância a números mágicos é insuficiente.

O fato de Po-212 ter filha duplamente mágica \(^{208}{\rm Pb}\) e mesmo assim
\(p_{\rm req}\approx0{,}51\) mostra que a camada fechada não atua como bloqueio
escalar absoluto.

Logo, \(P_\perp\) depende do espectro real e dos overlaps no produto de
superfície, não apenas de contagem de nucleons.

## 4. Veredito

$$
\boxed{
\text{não fechar Q51 com proxy de números mágicos.}
}
$$

O projetor deve ser calculado por Riesz a partir de \(K_\partial^{\rm phys}\).

