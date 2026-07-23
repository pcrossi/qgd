# Q51 — Protótipo matricial de \(K_\partial^{\rm phys}\)

## 1. Objetivo

O objetivo deste protótipo é validar o mecanismo matemático do projetor:

$$
P_\perp
=
P_\alpha(1-P_{\rm filho}).
$$

Ele não é previsão física. É uma matriz finita construída para mostrar que
pesos entre 0 e 1 são exatamente normas quadráticas de projeção espectral.

## 2. Base mínima

Usamos três direções:

1. \(e_0\): modo nu \(4N\);
2. \(e_1\): modo do núcleo filho;
3. \(e_2\): modo coletivo residual.

A realização mínima usa:

$$
v_\alpha
=
\sqrt p\,e_0
+\sqrt{1-p}\,e_1.
$$

Então:

$$
K_\partial^{\rm toy}
=
0\,v_\alpha v_\alpha^\top
+1\,v_\perp v_\perp^\top
+3\,e_2e_2^\top.
$$

## 3. Projetor

O projetor \(P_\alpha\) é construído pela janela espectral em torno do modo
alfa. No caso contínuo real, isso vira:

$$
P_\alpha
=
\frac1{2\pi i}
\oint_{\mathcal C_\alpha}
(z-K_\partial^{\rm phys})^{-1}\,dz.
$$

No protótipo finito, usamos a soma dos autovetores com autovalores na janela.

## 4. Resultado

A saída está em:

- `saida_prototipo_matriz_Kpartial_q51.md`.

O resultado mostra que pesos:

$$
p=0,\quad
p\simeq1,\quad
0<p<1
$$

aparecem como:

$$
\|P_\alpha e_0\|^2=p.
$$

## 5. Limitação

O protótipo usa os próprios \(p_{\rm req}\) para construir \(v_\alpha\).
Portanto, ele demonstra consistência matemática, mas não prediz os pesos.

## 6. Uso correto

O protótipo serve para confirmar que a rota:

$$
K_\partial^{\rm phys}
\to
P_\alpha
\to
P_\perp
\to
S_\alpha^{\rm GDQ}
$$

é matematicamente capaz de produzir os pesos observados sem violar
positividade.

O próximo passo físico é substituir \(K_\partial^{\rm toy}\) por blocos da
Hessiana de superfície do núcleo.
