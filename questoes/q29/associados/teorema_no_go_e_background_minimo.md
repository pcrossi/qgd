# Q29 — Teorema de não transporte e background mínimo

## 1. Enunciado

Considere simultaneamente:

1. o junction equilátero $C_3$ com classe de fluxo primitiva conservada;
2. o background produto $T^5\times S^3$ com medida normalizada;
3. perfis constantes em $T^5$;
4. a interface radial $r=R(1+\varepsilon Y)$ com $Y=x_4$;
5. os geradores normalizados usados na Q29.

Então o complemento de Schur não transporta diferencialmente as rigidezes
fraca e de hipercarga:

$$
\boxed{Z_W=Z_Y.}
$$

Consequentemente,

$$
\boxed{\sin^2\theta_W=\frac38.}
$$

## 2. Prova no junction

No background $C_3$, a conservação da classe de fluxo dá

$$
\delta_rT_a=0.
$$

No ponto fechado, a derivada mista entre ângulos relativos e raios é

$$
J_{\theta r}=0.
$$

Portanto,

$$
H_{\rm eff}
=H_{\rm rel}-J_{\theta r}K_r^{-1}J_{\theta r}^{\dagger}
=H_{\rm rel}.
$$

Esse bloco estabiliza os três centros, mas não modifica normas de gauge.

## 3. Prova na interface $\ell=1$

Para cada gerador $A$ usado na representação real de $S^3\subset\mathbb R^4$,

$$
|An|^2=\frac14.
$$

Como $r$ e o elemento de área dependem somente de $Y=x_4$, todo peso da
integral é uma função $F(x_4)$. As três coordenadas transversais são
permutadas pela isotropia residual:

$$
\int_{S^3}x_1^2F(x_4)d\Omega
=\int_{S^3}x_2^2F(x_4)d\Omega
=\int_{S^3}x_3^2F(x_4)d\Omega.
$$

As derivadas $\delta_A Y$ dos quatro geradores são, a sinal irrelevante,
$x_1/2$, $x_2/2$ ou $x_3/2$. Logo suas contribuições radiais também são
iguais. Portanto,

$$
I_{W_1}=I_{W_2}=I_{W_3}=I_Y
$$

para qualquer $\varepsilon$ admissível, não apenas perturbativamente. A
pequena diferença na integração Monte Carlo anterior é ruído amostral.

## 4. Prova no fator toroidal

Para perfis constantes, a integral normalizada sobre $T^5$ é um fator comum.
Assim,

$$
\frac{Z_W}{Z_Y}=1.
$$

Combinar os três blocos preserva

$$
\frac{g'^2}{g^2}=\frac35,
\qquad
\sin^2\theta_W=\frac38.
$$

## 5. Menor extensão admissível

Para obter transporte sem inserir $2/9$, é necessário quebrar ao menos uma
hipótese do teorema. A extensão mínima que não altera a ação oficial é usar um
background global não produto, já permitido como solução métrico-dilatônica:

$$
ds^2
=e^{2A(y)}ds_{T^5}^2
+g_{ij}^{S^3}(y)dy^idy^j,
$$

com $A$ não constante e perfis espectrais distintos

$$
\Psi_W(\theta,y)\ne\Psi_Y(\theta,y).
$$

As rigidezes passam a ser

$$
K_a
=C_{\rm GDQ}
\int_{T^5\times S^3}
\mathcal U_*\,e^{3A}
|\Psi_a|^2|\xi_a|^2dV,
$$

e o bloco misto físico é

$$
J_{aA}
=\left\langle
\delta_{\Psi_a}\Phi,
\mathcal O_{\rm Hess}\delta_A(g,f)
\right\rangle_{\mathcal U_*}.
$$

O operador efetivo correto é

$$
K_{ab}^{\rm eff}
=K_{ab}-J_{aA}(H_{gf}^{-1})^{AB}J_{Bb}.
$$

## 6. Condições para um cálculo não circular

O background deve ser obtido antes da comparação fenomenológica por:

1. equações estacionárias da ação oficial para $A$, $g_{S^3}$ e $f$;
2. regularidade no antipolo;
3. condição Robin no estômato;
4. periodicidade térmica em $S^1_\beta\subset T^5$;
5. colagem global $\mathbb Z_6$ já derivada na Q28;
6. normalização $\int\mathcal U_*dV=1$.

Somente depois se resolvem os modos $\Psi_W,\Psi_Y$ e se avalia $K^{\rm eff}$.
O resultado $Z_W/Z_Y=10/21$ pode ser testado, mas não imposto como condição
de contorno, pois isso seria engenharia inversa.

## 7. Veredito

O cálculo atual fornece um teorema negativo útil:

$$
\boxed{
\text{o ansatz produto/local da Q29 não pode gerar }\frac29.
}
$$

A pendência deixou de ser uma busca indefinida: ela é a solução espectral do
background warped não produto com condições já enumeradas.
