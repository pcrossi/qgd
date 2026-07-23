---
title: "Provas, lemas e definições — Capítulo 6"
---

# Provas, lemas e definições — Capítulo 6

Esta nota registra a linha matemática limpa da ponte global--local. Ela deve
ser lida como complemento técnico do Capítulo 6: o corpo do capítulo explica a
construção; esta nota conserva as hipóteses, os operadores, as provas e os
testes reduzidos em forma autocontida.

O objetivo não é identificar o Universo de Einstein com o laboratório. O
objetivo é provar que certos setores localizados podem ser transportados entre
o espaço cosmológico/espectral e o bulk local oficial sem perder métrica,
medida, Hessiana física, gap e projetores espectrais.

## Dados e convenções

O espaço local oficial da GDQ é

$$
M_0=\mathbb R^4\times T^4.
$$

O espaço cosmológico/espectral usado nesta ponte é uma família apontada

$$
M_R=T^4\times S^1_R\times S^3_R,
\qquad R\to\infty.
$$

Aqui $R$ é raio geométrico. Equivalentemente pode-se escrever
$R=\varepsilon^{-1}$ e tomar $\varepsilon\to0^+$.

Os campos transportados são

$$
X=(g,J,H,f,\mathcal U),
\qquad
H=d_J^c\omega_g,
\qquad
\rho=e^{-(f+\bar f)/2},
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

Nenhum passo altera a ação oficial. Fontes, vínculos e termos de interface
entram apenas como dados de problema variacional ou como restrições físicas
sobre o background.

## Lema 1 — Limite apontado

**Enunciado.** Em uma vizinhança de raio próprio fixo ao redor de um ponto
base, a família $T^4\times S^1_R\times S^3_R$ converge suavemente para
$T^4\times\mathbb R^4$ quando $R\to\infty$.

**Prova.** No fator $S^1_R$, a coordenada de arco já torna a métrica localmente
plana:

$$
ds^2_{S^1_R}=du^2.
$$

No fator $S^3_R$, use coordenadas normais geodésicas no ponto base. A expansão
local da métrica é

$$
g_{ij}^{(R)}(x)
=\delta_{ij}
-\frac13R_{ikjl}^{(R)}(0)x^kx^l
+O(|x|^3/R^3).
$$

Como a curvatura seccional da esfera de raio $R$ é $R^{-2}$,

$$
R_{ikjl}^{(R)}=O(R^{-2}).
$$

Logo, em qualquer bola fixa $|x|\le L$,

$$
\left\|g^{(R)}-\delta\right\|_{C^k(B_L)}
=O(R^{-2})
$$

para todo $k$ finito, após escolher cartas normais compatíveis. O fator
$T^4$ é preservado. Portanto

$$
T^4\times S^1_R\times S^3_R
\xrightarrow[R\to\infty]{\rm apontado}
T^4\times\mathbb R^4.
$$

O teste numérico reduzido
`scripts/verificar_limite_apontado_torus_esfera.py` calcula o erro angular
local em $S^3_R$ e confirma a escala $O(R^{-2})$:

| $R$ | erro máximo | $E_RR^2$ |
|---:|---:|---:|
| 5 | $1.326242503606\times10^{-2}$ | $0.33156063$ |
| 100 | $3.333288889207\times10^{-5}$ | $0.33332889$ |
| 200 | $8.333305555719\times10^{-6}$ | $0.33333222$ |

Esse teste é uma verificação de consistência geométrica, não uma prova
numérica independente do lema.

## Lema 2 — Transporte de campos e medida

**Enunciado.** Se os campos $g_R,J_R,H_R,f_R$ convergem em cartas apontadas e
as densidades ponderadas são dominadas por uma função integrável comum, então
os espaços ponderados e os funcionais locais convergem após o transporte
unitário correto da medida.

**Prova.** Seja $\Phi_R:U_0\to U_R$ a carta de identificação apontada. O
transporte ingênuo de funções não preserva norma quando a medida muda. A
medida física é

$$
d\mu_R=\mathcal U_R\,dV_{g_R}.
$$

Defina o jacobiano relativo $J_R$ por

$$
\Phi_R^*d\mu_R=J_R\,d\mu_0.
$$

O transporte unitário entre espaços ponderados é

$$
(I_R\psi)(\Phi_R(x))=J_R(x)^{-1/2}\psi(x).
$$

Então

$$
\int_{U_R}|I_R\psi|^2\,d\mu_R
=\int_{U_0}|\psi|^2\,d\mu_0.
$$

Como $g_R,J_R,H_R,f_R$ convergem em $C^k_{\rm loc}$ e $\mathcal U_RdV_{g_R}$
é dominada, o teorema da convergência dominada fornece a convergência dos
termos integrais da ação e das formas quadráticas locais.

O script `scripts/verificar_transporte_medida_ponderada.py` verifica o ponto
crítico: sem o jacobiano, a norma escala artificialmente; com o jacobiano, a
norma fica igual a $1$ para escalas $a=0.5,1,2,4$.

## Lema 3 — Hessiana física e convergência de formas

**Enunciado.** Sob convergência local dos campos, dos vínculos e dos
projetores físicos, as formas quadráticas da Hessiana física convergem no
sentido de Mosco no núcleo comum de perturbações localizadas.

**Construção.** Reúna os campos relevantes em $X=(g,J,f)$, com $H=d_J^c\omega_g$.
Os vínculos físicos são agrupados em

$$
\mathcal C(X)=0.
$$

Eles incluem normalização da medida, carga, fluxo de interface e cargas de
Noether mantidas fixas. O funcional aumentado é

$$
\mathscr L(X,\lambda)
=S_{\rm phys}(X)-\langle\lambda,\mathcal C(X)\rangle.
$$

O background admissível satisfaz

$$
D_X\mathscr L(X_*,\lambda_*)=0,
\qquad
\mathcal C(X_*)=0.
$$

Se $C_*=D\mathcal C(X_*)$ lineariza os vínculos e $R_*$ gera as redundâncias
de gauge, o espaço físico é obtido impondo

$$
C_*\eta=0,
\qquad
R_*^\dagger\mathbb G_*\eta=0.
$$

Defina

$$
A_*=
\begin{pmatrix}
C_*\\
R_*^\dagger\mathbb G_*
\end{pmatrix}.
$$

O projetor conjunto é

$$
P^{\rm phys}
=I-\mathbb G_*^{-1}A_*^\dagger
\left(A_*\mathbb G_*^{-1}A_*^\dagger\right)^+A_*.
$$

A Hessiana vinculada é

$$
\mathbb H_*
=D_X^2\mathscr L(X_*,\lambda_*)
=D^2S_{\rm phys}(X_*)
-\sum_a\lambda_*^aD^2\mathcal C_a(X_*).
$$

O operador físico é

$$
K_*^{\rm phys}
=P^{{\rm phys}\dagger}\mathbb H_*P^{\rm phys}.
$$

Quando há uma interface $Y$, a eliminação do exterior ou dos modos
complementares é feita por complemento de Schur:

$$
K_Q^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

Esse inverso só é lícito depois de remover zeros de simetria e provar gap no
setor complementar.

**Prova.** Nas cartas apontadas e nos transportes unitários $I_R$, considere
as formas físicas

$$
q_R^{\rm phys}[\eta]
=\langle \eta,K_R^{\rm phys}\eta\rangle_R.
$$

No núcleo comum de perturbações compactamente suportadas, os coeficientes dos
operadores, as medidas, os vínculos e os projetores convergem. Portanto

$$
q_R^{\rm phys}[I_R\eta]\to q_0^{\rm phys}[\eta].
$$

A semicontinuidade inferior global é fornecida pelo controle exterior e pelo
gap do Lema 4. Com a aproximação densa por funções localizadas e a estimativa
liminf, obtém-se convergência de Mosco.

## Lema 4 — Localização e gap uniforme

**Enunciado.** Se o operador físico local possui um cluster isolado abaixo do
limiar exterior e se as formas convergem localmente, então o cluster
correspondente da família apontada permanece uniformemente isolado e seus
modos são localizados.

**Prova.** Seja $I$ um intervalo contendo o cluster local. Defina

$$
\Delta_0
=\operatorname{dist}
\left(
I,\sigma(K_0^{\rm phys})\setminus I
\right)>0.
$$

Escolha $0<\delta<\Delta_0/3$. Uma partição IMS com cutoff $\chi$ separa
núcleo e exterior:

$$
q_R[\eta]
=q_R[\chi\eta]
+q_R[\sqrt{1-\chi^2}\eta]
-\mathcal E_{\rm IMS}[\eta].
$$

O erro depende de $|d\chi|^2$ e pode ser tornado menor que $\delta$ escolhendo
a transição do cutoff larga o suficiente. No núcleo, a convergência local das
formas dá erro menor que $\delta$ para $R$ grande. No exterior, o limiar do
vácuo impede que modos abaixo do cluster escapem. Logo

$$
\operatorname{dist}
\left(
I_R,\sigma(K_R^{\rm phys})\setminus I_R
\right)
\ge\Delta_0-2\delta>0.
$$

Para localização, use um peso de Agmon $e^{ar}$, com $a$ menor que o valor
permitido pelo gap. A identidade ponderada fornece

$$
\int e^{2ar}
\left(
|\nabla\eta_R|^2+|\eta_R|^2
\right)d\mu_R
\le C.
$$

Assim a norma não se espalha pelo volume crescente.

O script `scripts/verificar_gap_localizacao_toy.py` ilustra a distinção entre
gap físico e gap artificial de compactificação. No modelo reduzido, aumentando
o domínio de $L=4$ até $L=18$, o autovalor ligado permanece
$-6.6361862202$ e o gap estabiliza em $3.7425977750$, enquanto a massa fora de
$|x|>2$ permanece da ordem de $10^{-3}$.

## Lema 5 — Resolventes e projetores de Riesz

**Enunciado.** Com convergência de Mosco e gap uniforme, os resolventes
convergem fora do espectro e os projetores de Riesz dos clusters isolados
convergem.

**Prova.** Pela teoria de formas fechadas, convergência de Mosco implica
convergência forte dos resolventes:

$$
(K_R^{\rm phys}+1)^{-1}\to(K_0^{\rm phys}+1)^{-1}.
$$

Se $\Gamma$ é uma curva fechada no plano complexo envolvendo apenas o cluster
isolado, o projetor espectral é

$$
P_{R,I}
=\frac{1}{2\pi i}\int_\Gamma
(z-K_R^{\rm phys})^{-1}\,dz.
$$

O gap uniforme impede que o espectro cruze $\Gamma$. Portanto os projetores
convergem. Em clusters finitos localizados, a convergência é forte e preserva
multiplicidade.

O script `scripts/verificar_resolvente_riesz_toy.py` verifica a forma finita
desse argumento: quando $\varepsilon$ cai de $0.2$ para $0.01$, o erro do
projetor cai de $6.722577\times10^{-2}$ para
$3.278796\times10^{-3}$.

## Lema 6 — Separação entre herança topológica e normalização contínua

**Enunciado.** A ponte transporta setores localizados, multiplicidades,
classes topológicas e clusters espectrais isolados. Ela não determina
automaticamente normalizações contínuas, constantes metrológicas nem respostas
de aparelhos.

**Prova.** Os Lemas 1--5 controlam limites locais, formas quadráticas e
subespaços espectrais. Esses objetos são estáveis sob convergência apontada e
gap. Porém uma normalização contínua depende de integrais globais de fluxo,
impedâncias de contorno e acoplamentos de fonte, por exemplo

$$
Z^{-1}\sim\int |\xi|^2\,d\mu,
\qquad
\mathsf R=K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

Essas expressões podem mudar se o canal for massless, se houver fuga para o
bulk, se a fronteira física mudar ou se o aparelho alterar o DtN. Portanto a
ponte não autoriza deduzir $\alpha$, $G$, massas, momentos ou respostas de
detector apenas por transporte topológico. Cada normalização exige cálculo
próprio.

## Relógio causal e redução de Madelung

O parâmetro de fluxo $\tau$ não é o tempo físico $t$. A compatibilidade entre
a forma logarítmica do fluxo e o relógio macroscópico é expressa por

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)=\kappa\,dt.
$$

Isso equivale a exigir que a dilatação relativa

$$
F(t)=\frac{\tau_\gamma(t)}{\tau_0}
$$

seja homomorfismo entre translações temporais e dilatações positivas:

$$
F(t_1+t_2)=F(t_1)F(t_2).
$$

Sob continuidade ou monotonia física, a equação funcional de Cauchy dá

$$
F(t)=e^{\kappa t},
\qquad
\tau_\gamma(t)=\tau_0e^{\kappa t}.
$$

O script `scripts/verificar_homomorfismo_relogio.py` verifica essa identidade
para $\tau_0=2.0$ e $\kappa=0.37$, com defeitos numéricos da ordem de
$10^{-16}$.

A igualdade canônica de Madelung

$$
\Pi_{S_R}=\rho
$$

não é identidade universal off-shell da ação oficial. Ela é a resposta
hidrodinâmica no setor reduzido em que:

1. o relógio causal fixa $\kappa$ constante no laboratório;
2. a normalização probabilística seleciona $N_\rho=1$;
3. a carga de fase seleciona $Q_S=1$;
4. modos rápidos de amplitude e shift foram amortecidos pelo aparelho;
5. o sistema relaxou para o mínimo de Routh;
6. a desigualdade de Cauchy--Schwarz é saturada.

No mínimo,

$$
\left(
\int_\Sigma\frac{\Pi_{S_R}^2}{\rho}\,d\Sigma
\right)
\left(
\int_\Sigma\rho\,d\Sigma
\right)
\ge
\left(
\int_\Sigma\Pi_{S_R}\,d\Sigma
\right)^2.
$$

Com $Q_S=N_\rho=1$, a igualdade exige $\Pi_{S_R}=\rho$. Fisicamente, isso
significa que a mecânica quântica projetiva aparece como a hidrodinâmica
observável do setor termalizado e medido da GDQ, não como substituição da
ação fundamental.

## Setor aplicado $C_3$

No background estacionário reduzido com três centros, equilíbrio local de
torção e simetria cíclica $C_3$, o modo comum é removido por Noether e os dois
modos relativos ficam no setor físico. O menor autovalor físico tem a forma

$$
\Delta_0
=\min\left\{
\frac32\kappa_{\rm rel}T^2,
\frac1{2\tau}
\right\}.
$$

Na normalização primitiva do setor,

$$
\Delta_0=\frac12.
$$

Esse resultado fecha a ponte como teorema aplicado para esse background:
o cluster trimodal é localizado, possui gap e tem projetor transportável pelo
limite apontado. Ele não prova que todos os backgrounds da GDQ possuem três
centros, nem calcula por si só massas ou normalizações contínuas.

## Rotas excluídas do manuscrito positivo

As seguintes rotas foram úteis historicamente, mas não entram como fundamento
do manuscrito:

- colares artificiais ajustados para produzir uma sela;
- shooting antipodal sem cadeia variacional completa;
- cancelamento por ruído escalar sem fonte derivada da ação;
- modo Beltrami homogêneo quando o acoplamento de interface fica nulo;
- solver sem background de sela admissível;
- normalização de constantes por alvo experimental;
- identificação direta entre $T^5\times S^3$ e $\mathbb R^4\times T^4$ sem
  limite apontado, transporte de medida e projetores.

Esses itens podem permanecer em registros de auditoria, mas não devem ser
usados como provas no texto principal.

## Resumo de status

| Item | Status | Observação |
|---|---|---|
| Limite apontado | Demonstrado | Erro local $O(R^{-2})$. |
| Transporte de medida | Demonstrado sob regularidade/dominação | Exige jacobiano unitário. |
| Hessiana física | Condicional | Exige background admissível, vínculos e projetor. |
| Mosco/resolvente/Riesz | Condicional | Exige gap e domínio controlado. |
| Setor $C_3$ | Fechado como teorema aplicado | Gap primitivo $\Delta_0=1/2$. |
| Normalizações contínuas | Separadas | Devem ser calculadas em cada setor físico. |

