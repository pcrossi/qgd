# Operador ressonante da cirurgia do nêutron

## 1. Operador coletivo

A ação radial reduzida é

$$
\mathcal A_{\rm red}[r]
=\int ds\left[
\frac{M_r}{2}\dot r^2+U(r)
\right],
$$

com

$$
U(r)=A_2r^2-B_3r^3+C_4r^4.
$$

Para massa coletiva constante e medida coletiva $w(r)dr$, o operador
auto-adjunto antes da continuação de saída é

$$
\boxed{
K_r
=-\frac{\hbar^2}{2w(r)}
\frac{d}{dr}\left[
\frac{w(r)}{M_r}\frac{d}{dr}
\right]+U(r).
}
$$

O ansatz unidimensional canônico usa $w(r)=1$. Uma escolha como $w=r^3$
seria a medida de uma coordenada radial espacial em quatro dimensões, mas não
segue automaticamente para uma coordenada coletiva; por isso não é adotada
silenciosamente.

## 2. Domínio causal

O raio satisfaz $r\geq0$. A origem possui condição regular/refletora

$$
\psi'(0)=0,
$$

e o lado exterior usa condição puramente de saída

$$
\psi(r)\sim e^{+ik r},
\qquad r\to\infty,
$$

na folha causal selecionada por $\gamma$. O problema não é auto-adjunto após
essa continuação e seus polos são

$$
E_{\rm res}=E_0-\frac{i\hbar\Gamma_n}{2}.
$$

Logo,

$$
\boxed{
\Gamma_n=-\frac{2}{\hbar}\operatorname{Im}E_{\rm res},
\qquad
\tau_n=\Gamma_n^{-1}.
}
$$

## 3. Escala adimensional

Defina

$$
r=\frac{A_2}{B_3}x,
\qquad
E_*=\frac{A_2^3}{B_3^2},
$$

e

$$
\lambda=\frac{A_2C_4}{B_3^2},
\qquad
\eta=\frac{\hbar^2B_3^4}{2M_rA_2^5}.
$$

Então

$$
\boxed{
\frac{K_r}{E_*}
=-\eta\frac{d^2}{dx^2}
+x^2-x^3+\lambda x^4
}
$$

para $w=1$. Toda a ressonância radial depende apenas de $(\lambda,\eta)$;
a escala dimensional final é $E_*/\hbar$.

O ramo com região de ação inferior existe quando

$$
\lambda<\frac14.
$$

## 4. Bounce

O primeiro ponto de retorno de energia reduzida zero é

$$
r_t
=\frac{B_3-\sqrt{B_3^2-4A_2C_4}}{2C_4}.
$$

A ação de ida e volta é

$$
\boxed{
S_B
=2\sqrt{2M_r}
\int_0^{r_t}
r\sqrt{A_2-B_3r+C_4r^2}\,dr.
}
$$

A frequência harmônica na origem é

$$
\omega_0=\sqrt{\frac{2A_2}{M_r}}.
$$

No nível WKB líder, omitindo o determinante de flutuações,

$$
\boxed{
\Gamma_n^{\rm WKB}
\simeq\frac{\omega_0}{2\pi}
e^{-S_B/\hbar}.
}
$$

Essa fórmula é uma aproximação controlável somente quando $S_B/\hbar\gg1$.
O prefator exato requer o determinante da Hessiana em torno do bounce e os
dois canais de Bismut normalizados.

## 5. Inclusão dos modos transversais

O operador radial completo contém a autoenergia de Schur

$$
\boxed{
K_{\rm res}(E)
=K_r-J_{r\perp}
(K_\perp-E-i0_\gamma)^{-1}
J_{\perp r}.
}
$$

O sinal $i0_\gamma$ é determinado pela folha de saída. A parte imaginária da
resolvente produz a largura. Esse é o mesmo $K_\perp^{-1}$ que apareceu na
quarta variação projetada.

## 6. Dados necessários para um número físico

São necessários:

$$
A_2,
\quad B_3,
\quad C_4,
\quad M_r,
\quad J_{r\perp},
\quad K_\perp.
$$

Os quatro primeiros definem a taxa radial WKB. Os dois últimos dão o prefator
e a decomposição nos canais eletrônico e neutro. Atualmente $B_3$ possui
fórmula torsional, mas $A_2,C_4,M_r$ ainda contêm os momentos causais e o
matching.

## 7. Resultado

O operador, o domínio, a continuação causal, a escala adimensional e a taxa
WKB estão construídos. Não existe valor numérico único porque o corpus não
fornece os coeficientes dimensionais do operador. Escolher números naturais
para eles seria um benchmark sintético, não uma solução da ação oficial.

## 8. Reprodutibilidade

O cálculo da ação de bounce e da taxa está em
`neutron/calcular_taxa_wkb_cirurgia.py`.
