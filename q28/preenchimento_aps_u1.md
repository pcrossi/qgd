# Q28 — Preenchimento 4D e índice APS do fluxo mínimo

## 1. Geometria do preenchimento

Para o elo $S^3$, use seu preenchimento spin mínimo

$$
X_4=B^4,
\qquad
\partial B^4=S^3.
$$

Em cada esfera radial não degenerada, mantém-se a fibração de Hopf

$$
S^1\hookrightarrow S^3_r\longrightarrow S^2.
$$

Escolha uma extensão radial com $f(r)=O(r^2)$ na origem. Isso torna
$\mathcal A=f(r)A_m$ suave no ponto em que as órbitas angulares colapsam.

O fibrado de disco $D(\mathcal O(-1))$ também possui borda $S^3$, mas não é
spin; ele exigiria a fórmula completa spin$^c$, incluindo o determinante
spin$^c$. Para não omitir esse termo, ele não é usado neste protótipo mínimo.

## 2. Integral de bulk abeliana

Estenda a conexão de Hopf radialmente por

$$
\mathcal A(r)=f(r)A_m,
\qquad
f(r)=O(r^2)\text{ quando }r\to0,
\qquad
f(1)=1.
$$

Então

$$
\mathcal F
=f'\,dr\wedge A_m+f\,dA_m.
$$

Como

$$
d(\mathcal A\wedge\mathcal F)=\mathcal F\wedge\mathcal F,
$$

segue por Stokes:

$$
\int_{X_4}\mathcal F\wedge\mathcal F
=\int_{S^3}A_m\wedge dA_m
=-4\pi^2m^2
$$

na orientação adotada. A componente de grau quatro do caráter de Chern é

$$
\operatorname{ch}_2(L_m)
=\frac1{8\pi^2}\mathcal F\wedge\mathcal F.
$$

Logo,

$$
\boxed{
\int_{X_4}\operatorname{ch}_2(L_m)
=-\frac{m^2}{2}.
}
$$

O valor meio-inteiro é permitido porque $B^4$ possui borda. A parte
fracionária é cancelada pelo termo $\bar\eta$.

## 3. Índice antes de ligar a torção

Para $\beta=0$,

$$
\bar\eta(A_m)
\equiv-\frac{m^2}{2}
\pmod{\mathbb Z}.
$$

Escolhendo a extensão mínima, sem fluxo espectral adicional, os representantes
coincidem:

$$
\int_{X_4}\operatorname{ch}_2(L_m)
=\bar\eta(A_m)
=-\frac{m^2}{2}.
$$

Assim,

$$
\boxed{
\operatorname{ind}_{\rm APS}D_{m,0}^+=0.
}
$$

A conexão de Hopf isolada quantiza o fluxo, mas ainda não cria a contribuição
quiral inteira do estômato.

## 4. Fluxo espectral da torção

Ligue adiabaticamente a torção paralelizante:

$$
\beta(t)=-\frac32t,
\qquad
0\leq t\leq1.
$$

Para $m=1$, o espectro em $\beta=0$ possui, abaixo ou igual a $3/2$,

$$
\lambda=\frac12
\quad\text{com multiplicidade }1,
$$

e

$$
\lambda=\frac32
\quad\text{com multiplicidade }2.
$$

Como $\beta$ é um deslocamento escalar, o primeiro nível cruza zero em

$$
\boxed{
\beta=-\frac12
}
$$

do lado positivo para o negativo. Os dois níveis seguintes atingem zero
somente no endpoint físico

$$
\beta=-\frac32,
$$

formando

$$
h_1=2.
$$

Defina o fluxo espectral com sinal positivo para cruzamentos
negativo--para--positivo. Então, no intervalo aberto,

$$
\boxed{
\operatorname{SF}(D_{1,\beta})=-1.
}
$$

## 5. Índice final

Para a condição APS que exclui o subespaço espectral não negativo da borda,
a variação do índice é

$$
\operatorname{ind}_{\rm APS}D_{1,B}^+
-\operatorname{ind}_{\rm APS}D_{1,0}^+
=-\operatorname{SF}(D_{1,\beta}).
$$

Portanto,

$$
\boxed{
\operatorname{ind}_{\rm APS}D_{1,B}^+
=0-(-1)=1.
}
$$

Para a orientação conjugada, $m=-1$ ou $B\mapsto-B$ troca a quiralidade e o
índice assinado.

## 6. Interpretação

A unidade quiral não foi imposta por

$$
-\frac12(\eta+h)=1.
$$

Ela surgiu da composição de três dados calculados:

$$
\boxed{
\text{fluxo Hopf mínimo}
+\text{preenchimento 4D}
+\text{fluxo espectral da torção}
\Longrightarrow
\operatorname{ind}_{\rm APS}=1.
}
$$

Assim, cada estômato elementar orientado com fluxo mínimo pode fornecer uma
unidade quiral. A escolha $|m|=1$ continua vindo do setor elementar do fibrado
de Hopf sobre $S^2$, não da topologia de $B^4$. Três gerações ainda exigem
demonstrar que a geometria física possui exatamente três estômatos estáveis e
que os três operadores pertencem à mesma classe de índice.

## 7. Limites do resultado

O cálculo fecha o protótipo local $U(1)$. Ele não deriva ainda:

1. a existência de exatamente três estômatos;
2. o espectro completo $SU(3)\times SU(2)\times U(1)$;
3. as hipercargas fracionárias;
4. as normas $g_s,g,g'$;
5. a estabilidade do preenchimento sob a Hessiana completa da GDQ.

## 8. Status

$$
\boxed{
\operatorname{ind}_{\rm APS}D_{1,B}^+=1
\text{ no protótipo local orientado.}
}
$$
