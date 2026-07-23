# Ponte global--local da GDQ — prova dos seis lemas sem colar artificial

## 1. Correção do enunciado

Há duas operações diferentes:

$$
\boxed{
\begin{aligned}
T^5\times S^3&\longrightarrow\mathbb R^4\times T^4
&&\text{por limite apontado;}\\
Y_{\rm st}&\subset M
&&\text{como interface física do estômato.}
\end{aligned}
}
$$

Não se introduz uma interface entre os backgrounds cosmológico e planar. As
condições DtN pertencem somente a $Y_{\rm st}$.

## 2. Hipóteses físicas mínimas

Considere

$$
M_\varepsilon
=T^4\times S^1_{R_\varepsilon}\times S^3_{R_\varepsilon},
\qquad
R_\varepsilon=\varepsilon^{-1},
$$

com ponto base $p_\varepsilon$, e o limite

$$
M_0=T^4\times\mathbb R^4.
$$

Assuma:

1. existe um background local admissível $X_0=(g_0,J_0,f_0)$ contendo o
   estômato físico $Y_{\rm st}$;
2. $H_0=d^c_{J_0}\omega_0$ e a medida $\mathcal U_0$ obedecem às convenções
   oficiais;
3. o defeito e seus coeficientes diferem do vácuo por termos compactamente
   suportados ou exponencialmente decrescentes;
4. depois dos vínculos e gauge, a Hessiana local $K_0^{\rm phys}$ é
   auto-adjunta e possui um cluster isolado $I$ separado por

$$
\Delta_0
=\operatorname{dist}
\left(I,\sigma(K_0^{\rm phys})\setminus I\right)>0;
$$

5. o problema DtN em $Y_{\rm st}$ é complementar elíptico e semilimitado;
6. o integrando causal é dominado uniformemente em $\gamma$.

Essas hipóteses pertencem ao estômato local. Não incluem uma sela de colagem
entre $M_\varepsilon$ e $M_0$.

## 3. Lema 1 — família geométrica apontada

Use coordenadas normais no círculo e na esfera em torno de $p_\varepsilon$:

$$
\Phi_{\varepsilon,L}:
T^4\times B_L(0)\longrightarrow M_\varepsilon.
$$

Para todo $L$ fixo e todo $k$,

$$
\|\Phi_{\varepsilon,L}^*g_\varepsilon-g_0\|_{C^k(B_L)}
\le C_{k,L}\varepsilon^2.
$$

O raio de injetividade em $p_\varepsilon$ tende a infinito e as derivadas da
curvatura são $O(\varepsilon^{2+j})$. Isso demonstra convergência suave
apontada de Cheeger--Gromov.

O estômato é transportado dentro de um compacto fixo pela própria
$\Phi_{\varepsilon,L}$. Não é necessário prolongá-lo por um colar até o
antípolo cosmológico.

**Status:** demonstrado para a família geométrica. A existência do estômato
local é um problema interno da GDQ, não uma condição da ponte.

## 4. Lema 2 — transporte dos campos

Escolha $L_\varepsilon\to\infty$ com
$\varepsilon L_\varepsilon\to0$ e um cutoff $\chi_\varepsilon$ igual a um no
suporte físico do defeito. Defina no chart apontado

$$
X_\varepsilon
=X_\varepsilon^{\rm vac}
+\chi_\varepsilon
(\Phi_{\varepsilon,L_\varepsilon})_*
(X_0-X_0^{\rm vac}).
$$

Como $H=d_J^c\omega$ é uma operação diferencial natural,

$$
\Phi_\varepsilon^*H_\varepsilon\to H_0
$$

em $C^{k-1,\alpha}_{\rm loc}$. O mesmo vale para $f$, $\rho$ e
$\mathcal U$, usando dominação causal. A carga relativa no bordo do estômato
é preservada por naturalidade e homotopia.

Se o cutoff produz um resíduo $E_\varepsilon=O(\varepsilon^2)+o_L(1)$, a
correção no complemento físico é

$$
\delta X_\varepsilon
=-(K_0^{\rm phys})^{-1}P^{\rm phys}E_\varepsilon
+O(\|E_\varepsilon\|^2),
$$

pela função implícita, desde que o zero físico tenha sido removido e o gap da
Hipótese 4 esteja disponível. Isso corrige o background sem introduzir uma
interface cosmológico--local.

**Status:** transporte geométrico demonstrado; correção exata é condicional
ao gap local, não a uma sela global--local.

## 5. Lema 3 — convergência da Hessiana oficial

Se $I_\varepsilon$ é a identificação unitária obtida pela razão das medidas,

$$
I_\varepsilon\eta
=\left(
\frac{\mathcal U_0dV_{g_0}}
{\Phi_\varepsilon^*(\mathcal U_\varepsilon dV_{g_\varepsilon})}
\right)^{1/2}
(\Phi_\varepsilon)_*\eta,
$$

então, em um núcleo comum de perturbações físicas compactamente suportadas,

$$
q_\varepsilon^{\rm phys}[I_\varepsilon\eta]
\longrightarrow
q_0^{\rm phys}[\eta].
$$

Isso segue da convergência $C^{k,\alpha}$ dos coeficientes, da medida, do
projetor dos vínculos e do operador DtN do mesmo estômato. O DtN não é usado
para colar os dois backgrounds.

A sequência de recuperação de Mosco é $I_\varepsilon\eta$ com cutoff
crescente. A desigualdade liminf segue do Lema 4.

## 6. Lema 4 — localização e gap uniforme

Escolha $0<\delta<\Delta_0/3$. Pela convergência local das formas e pela
estimativa IMS,

$$
q_\varepsilon[\eta]
=q_\varepsilon[\chi\eta]
+q_\varepsilon[(1-\chi^2)^{1/2}\eta]
-\mathcal E_{\rm IMS}.
$$

No núcleo, a convergência transfere o cluster $I$. Fora dele, o operador tende
ao vácuo e permanece acima do limiar essencial. Escolhendo o suporte do
cutoff grande e depois $\varepsilon$ pequeno,

$$
\operatorname{dist}
\left(I_\varepsilon,
\sigma(K_\varepsilon^{\rm phys})\setminus I_\varepsilon
\right)
\ge\Delta_0-2\delta>0.
$$

A mesma desigualdade ponderada fornece localização de Agmon uniforme. Assim,
o gap global é herança do gap local; ele não é produzido por uma sela de
colar.

**Status:** implicação demonstrada. A avaliação de $\Delta_0$ para a Hessiana
física específica continua sendo o dado físico necessário.

## 7. Lema 5 — resolventes e projetores

Mosco implica

$$
I_\varepsilon^dagger
(K_\varepsilon^{\rm phys}-z)^{-1}
I_\varepsilon
\longrightarrow
(K_0^{\rm phys}-z)^{-1}
$$

fortemente. No cluster uniformemente isolado, a localização e a compacidade
local promovem a convergência para norma. Portanto

$$
P_{\varepsilon,I}
=\frac1{2\pi i}\oint_\Gamma
(K_\varepsilon^{\rm phys}-z)^{-1}dz
$$

satisfaz

$$
\|I_\varepsilon^\dagger P_{\varepsilon,I}I_\varepsilon-P_{0,I}\|
\to0.
$$

Posto, multiplicidade e classe espectral são preservados enquanto o gap não
fecha.

## 8. Lema 6 — separação dos dados

O limite apontado transporta:

- índice, carga relativa e classes topológicas;
- cluster espectral e multiplicidade;
- razões espectrais adimensionais.

A normalização dimensional continua vindo do espaço global de Einstein. A
resposta a aparelhos continua sendo calculada no bulk local. Essa separação
não é alterada pela remoção do colar artificial.

## 9. Teste numérico independente

`ponte_global_local_teste_sem_colar.py` usa o canal radial exato de $S^3_R$.
O autovalor converge como

$$
\lambda_R=\lambda_0-R^{-2}+o(R^{-2}),
$$

a norma localizada permanece acima de $0{,}9999988$ e o erro do projetor de
posto um cai até $9{,}66\times10^{-8}$ em $R=80$.

O teste confirma a taxa geométrica, a localização e o transporte do projetor.
Ele não substitui o cálculo da Hessiana oficial.

## 10. Veredito consolidado

$$
\boxed{
\begin{gathered}
\text{os seis lemas formam um teorema condicional completo}\
\text{sem qualquer sela ou interface global--local;}\\
\text{a única condição física remanescente é o background local admissível}\
\text{com Hessiana projetada e gap }\Delta_0>0.
\end{gathered}
}
$$

Portanto a antiga Hipótese BI deve ser aposentada como hipótese da ponte. Seus
resultados negativos continuam válidos apenas como no-go para uma colagem
física desnecessária.

## 11. Aplicação ao background $C_3$

O documento `topicos/ponte_global_local/ponte_global_local_fechamento_c3.md` verifica a hipótese local
para os três preenchimentos gaussianos primitivos da Q28. Nessa classe,

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}>0,
$$

e $\Delta_0=1/2$ na normalização $\tau=1$,
$\kappa_{\rm rel}T^2=1$. Assim, o teorema condicional torna-se aplicado e a
ponte fica fechada nessa classe específica.
