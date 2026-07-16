# Q28 — Pullback da Hessiana oficial ao kernel geracional

## 1. Hessiana oficial relevante

Escreva as flutuações da ação oficial como

$$
\Phi=(s,h),
$$

onde $s$ é a flutuação real de $(f+\bar f)/2$ e $h$ é a flutuação métrica
Hermitiana. A segunda variação já derivada possui a forma

$$
\mathcal S_{\rm GDQ}^{(2)}
=\frac12\langle\Phi,\mathcal O_{\rm Hess}^{(2)}\Phi\rangle,
$$

com

$$
\mathcal O_{\rm Hess}^{(2)}
=
\begin{pmatrix}
\mathcal O_{ss}&\mathcal O_{sg}\\
\mathcal O_{gs}&\mathcal O_{gg}
\end{pmatrix}.
$$

Após a fixação de gauge, seu símbolo principal é formado pelo Laplaciano com
drift no setor escalar e pelo operador de Lichnerowicz com drift no setor
métrico. O operador normalizado é

$$
L_{\rm GDQ}^{(2)}
=\tau^{-1}\mathcal O_{\rm Hess}^{(2)}.
$$

## 2. Projetor espectral

Se $P(\boldsymbol\theta)$ é o projetor ortogonal no subespaço dos modos zero
selecionados, a conexão e a curvatura de Berry podem ser escritas sem escolha
de base como

$$
\nabla^{\rm B}=P\,d,
$$

$$
\boxed{
\mathcal F^{\rm B}=P\,dP\wedge dP\,P.
}
$$

Portanto, uma classe de Chern não nula exige

$$
\partial_{\theta_i}P\ne0
$$

em pelo menos duas direções independentes.

## 3. Avaliação no background produto estacionário

Considere o background atualmente especificado,

$$
K=T^5\times S^3,
$$

com métrica produto, coeficientes independentes dos ângulos do toro e
dilatão estacionário translacionalmente invariável. Então

$$
[L_{\rm GDQ}^{(2)},T_i]=0,
$$

onde $T_i$ gera translações em $\theta_i$. Equivalentemente,

$$
[L_{\rm GDQ}^{(2)},-i\partial_{\theta_i}]=0.
$$

As autofunções se separam em modos de Fourier:

$$
\Phi_{\boldsymbol k,A}(\boldsymbol\theta,y)
=e^{i\boldsymbol k\cdot\boldsymbol\theta}\phi_A(y).
$$

O setor de menor energia usado no kernel geracional possui

$$
\boldsymbol k=0.
$$

Logo, seu projetor é constante no toro:

$$
P(\boldsymbol\theta)=P_0,
\qquad
d_{T^5}P=0.
$$

Inserindo isso na fórmula universal de Berry,

$$
\boxed{
\mathcal F_T^{\rm B}=0.
}
$$

Consequentemente,

$$
M_{12}=0,
\qquad
M_{34}=0,
$$

e

$$
\boxed{
A=\operatorname{tr}(M_{12}M_{34})=0.
}
$$

Com a colagem mínima $\nu(g)=1$,

$$
\boxed{
N_{ab}=A\nu(g)=0.
}
$$

## 4. Efeito da holonomia plana

Substituir os momentos por

$$
k_i\longmapsto k_i+Q_i
$$

através de holonomias constantes pode deslocar autovalores e selecionar
setores, mas não torna o projetor localmente dependente de
$\boldsymbol\theta$. Assim,

$$
dP=0
$$

permanece verdadeiro e nenhuma classe $a_4$ é produzida.

O mesmo vale para um cociclo projetivo tratado apenas como dado discreto de
transição: ele restringe a colagem, mas uma curvatura integral precisa ser
fornecida por uma conexão não plana compatível.

## 5. Condição necessária para $A\ne0$

O background precisa quebrar a separação produto no próprio operador
quadrático. Uma forma geral mínima seria

$$
L(\boldsymbol\theta,y)
=L_0(y)
+\sum_iV_i(\boldsymbol\theta,y),
$$

com

$$
\partial_{\theta_i}P\ne0.
$$

Para um autovalor isolado, a derivada do projetor é determinada pela resposta
espectral

$$
\partial_iP
=-R_\perp(\partial_iL)P
-P(\partial_iL)R_\perp,
$$

onde

$$
R_\perp=(1-P)(L-\lambda)^{-1}(1-P).
$$

Assim, a curvatura não deve ser postulada. Ela é calculável quando forem
fornecidos os termos mistos

$$
\partial_iL
$$

do background estacionário global.

## 6. Veredito

No background produto atualmente definido pela Q28, a avaliação direta da
Hessiana dá

$$
\boxed{
M_{12}=M_{34}=A=N_{ab}=0.
}
$$

Portanto, esse background não deriva três gerações. Para prosseguir sem
ajuste, é necessário obter da equação estacionária da ação oficial um
background global não produto — com warp, torção ou dilatão misto — e então
repetir o cálculo do projetor espectral.
