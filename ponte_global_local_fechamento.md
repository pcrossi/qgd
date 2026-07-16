# Ponte global--local — fechamento da auditoria de existência e gap

## 1. Enunciado exato

Esta etapa pergunta se os dados já presentes na GDQ bastam para:

1. demonstrar uma sela bulk--interface global;
2. calcular o projetor físico no background obtido;
3. provar um gap uniforme;
4. promover os Lemas 1--6 de condicionais a um teorema aplicado.

O domínio cosmológico é

$$
T^4\times S^1_L\times S^3_R,
$$

enquanto o limite local oficial é

$$
\mathbb R^4\times T^4.
$$

A ação fundamental não foi modificada. A torção permanece dependente,

$$
H=d_J^c\omega.
$$

## 2. O que está demonstrado

No setor homogêneo normalizado, escrevendo

$$
x=\log L,
\qquad
y=\log R,
$$

o funcional reduzido, a menos de constantes, é

$$
W_{\rm hom}(x,y)
=4\tau e^{-2y}+x+3y.
$$

Consequentemente,

$$
\nabla W_{\rm hom}
=
\begin{pmatrix}
1\\
3-8\tau e^{-2y}
\end{pmatrix},
$$

e

$$
D^2W_{\rm hom}
=
\begin{pmatrix}
0&0\\
0&16\tau e^{-2y}
\end{pmatrix}.
$$

Logo, o produto não é uma sela com $L$ livre.

## 3. Efeito exato dos dados cosmológicos fixos

Se o raio toroidal e o raio cosmológico são dados de contorno, os vínculos
mais simples são

$$
\mathcal C_L=x-x_{\rm cos}=0,
\qquad
\mathcal C_R=y-y_{\rm cos}=0.
$$

Eles tornam as variações homogêneas admissíveis sujeitas a

$$
\delta x=\delta y=0.
$$

Como esses vínculos são lineares nessas coordenadas,

$$
D^2\mathcal C_L=D^2\mathcal C_R=0.
$$

Portanto seus multiplicadores corrigem as equações de primeira ordem, mas
não criam uma rigidez espectral adicional:

$$
D^2\!left(
W_{\rm hom}-\lambda_L\mathcal C_L-\lambda_R\mathcal C_R
\right)
=D^2W_{\rm hom}.
$$

O efeito físico desses vínculos é retirar os dois módulos globais do espaço
tangente. Eles não fornecem um termo de massa para perturbações locais.

## 4. Por que isso não demonstra a sela global

Estacionariedade no minisuperspaço homogêneo não implica
estacionariedade no espaço completo de campos. Ainda é necessário verificar

$$
D\mathcal S_{\rm GDQ}[X_*]\,\eta=0
$$

para toda perturbação admissível inhomogênea

$$
\eta=(\delta g,\delta J,\delta f)
$$

que preserve normalização, carga, fluxos de Noether e os dados cosmológicos.
O capítulo cosmológico fornece valores de raio e estimativas de densidade,
mas não fornece um funcional de vínculo local

$$
\mathcal C_{\rm cos}[g,J,f]
$$

com primeira e segunda variações definidas no espaço completo de campos.
Sem esse objeto, não há termo calculável

$$
-\lambda_{\rm cos}D^2\mathcal C_{\rm cos}
$$

na Hessiana exterior.

## 5. Consequência para o projetor físico

A fórmula abstrata permanece válida:

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

Entretanto, um projetor numérico exige avaliar $A_*=D\mathcal C(X_*)$ em um
background $X_*$ efetivamente estacionário. Como o background exterior
inhomogêneo não foi obtido, somente o projetor formal está determinado.

## 6. Consequência para o gap

O refinamento espectral já demonstrou que, sem limiar local,

$$
\Delta_R
=\frac{\sqrt3}{R}\tanh(\pi\sqrt3)
\longrightarrow0.
$$

Fixar os módulos globais remove os modos $\delta L$ e $\delta R$, mas não
altera essa conclusão para a torre física local. Um gap uniforme requer

$$
\mu_*^2>0
$$

no potencial matricial da Hessiana vinculada do background bulk--interface.
Esse coeficiente não pode ser extraído do operador de referência nem dos
valores cosmológicos isolados.

## 7. Veredito

O ciclo de auditoria termina com um resultado negativo preciso:

$$
\boxed{
\begin{gathered}
\text{os vínculos de raio fecham o minisuperspaço homogêneo,}\\
\text{mas não demonstram a sela de campos nem o gap uniforme.}
\end{gathered}
}
$$

Assim:

- a formulação variacional, o DtN, o projetor abstrato e o teste de gap estão
  fechados estruturalmente;
- a existência física da sela bulk--interface permanece aberta;
- $P^{\rm phys}$ numérico e o gap físico permanecem condicionados a essa
  sela;
- o produto homogêneo não deve ser reutilizado como substituto.

## 8. Dado mínimo ainda necessário

Há duas rotas lícitas, e apenas duas:

1. fornecer e derivar da formulação cosmológica um vínculo funcional local
   $\mathcal C_{\rm cos}[g,J,f]$, incluindo sua Hessiana;
2. resolver diretamente o sistema elíptico global warped da ação oficial,
   com o colar local terminado na interface $Y$ e compensação global de
   carga.

Uma densidade cosmológica numérica, sozinha, é condição escalar insuficiente
para reconstruir o operador exterior matricial.

## 9. Reprodutibilidade

O script `ponte_global_local_minisuperspace.py` verifica simbolicamente o
gradiente e a Hessiana acima. Sua classificação é **avaliação direta de uma
quantidade já derivada**. Ele não é simulação do background físico.
