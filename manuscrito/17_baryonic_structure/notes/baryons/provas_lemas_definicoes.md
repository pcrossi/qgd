---
title: "Provas, lemas e definições — Capítulo 17"
---

# Provas, lemas e definições — Capítulo 17

Esta nota consolida a linha correta do setor bariônico da GDQ. Ela preserva
as demonstrações e os cálculos reduzidos usados no capítulo sem importar
rotas históricas superadas.

O enunciado físico é:

$$
\text{bárion}
=
\text{sóliton trimodal colado com carga inteira e torção de superfície}.
$$

O ciclo espectral usado para extrair invariantes é

$$
\mathcal C_B\simeq T^5_{\rm trançado}\times S^3_{\rm hol}.
$$

Esse ciclo é auxiliar. O bulk local oficial continua sendo
$\mathbb R^4\times T^4$.

## 1. Volume reduzido e massa dominante

Cada câmara bariônica contribui com volume reduzido

$$
\operatorname{Vol}(\mathcal F_a)=2\pi^5.
$$

Para três estômatos,

$$
\mathcal I_B^{\rm bulk}
=
\sum_{a=1}^{3}\operatorname{Vol}(\mathcal F_a)
=
6\pi^5.
$$

Na escala eletrônica reduzida,

$$
E_0=M_ec^2,
\qquad
\frac{M_B}{M_e}=\mathcal I_B.
$$

Portanto a massa dominante do bárion é

$$
\left(\frac{M_B}{M_e}\right)_{\rm bulk}
=
6\pi^5.
$$

Numericamente,

$$
6\pi^5=1836.118108711688.
$$

Essa conclusão é condicional à seleção do background de três câmaras e à
normalização eletrônica $\mathcal I_e=1$. A soma dos volumes é exata; a seleção
dinâmica do background não é provada por essa soma.

## 2. Superfície torsional do próton

A transgressão de superfície reduzida fornece

$$
\mathcal I_p^\partial
=
\frac{3\alpha(1+2\pi^4)}{4\pi^3}.
$$

Logo,

$$
\frac{M_p}{M_e}
=
6\pi^5+\frac{3\alpha(1+2\pi^4)}{4\pi^3}.
$$

Forma equivalente:

$$
\frac{M_p}{M_e}
=
\frac{3\left[\alpha(1+2\pi^4)+8\pi^8\right]}{4\pi^3}.
$$

Com $\alpha^{-1}=137.035999177$,

$$
\frac{M_p}{M_e}
=
1836.152673188612.
$$

A comparação posterior com o valor CODATA 2022
$1836.152673426$ dá erro relativo aproximado

$$
-1.29\times10^{-10}.
$$

Os coeficientes de superfície são dados geométricos do modelo reduzido. Sua
avaliação direta na sela 8D permanece aberta.

## 3. Equilíbrio torsional do nêutron

No próton, as três tensões são coorientadas:

$$
\mathbf t_p=(1,1,1).
$$

No nêutron estacionário, o estômato invertido carrega o dobro da torção
oposta:

$$
\mathbf t_n=(1,1,-2).
$$

Essa configuração satisfaz conservação local da corrente torsional:

$$
\sum_a(\mathbf t_n)_a=1+1-2=0.
$$

Na linguagem variacional,

$$
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
$$

O invariante físico de cisalhamento é par-a-par:

$$
I_{\rm sh}^2(\mathbf t)
=
\sum_{a<b}(t_a-t_b)^2.
$$

Para o próton,

$$
I_{\rm sh}^2(\mathbf t_p)=0.
$$

Para o nêutron,

$$
I_{\rm sh}^2(\mathbf t_n)
=
(1-1)^2+(1+2)^2+(1+2)^2
=18,
$$

e portanto

$$
I_{\rm sh}(\mathbf t_n)=3\sqrt2.
$$

## 4. Projeção Fredholm--Fano e $\delta_B$

O estômato possui três canais torsionais internos. A projeção física local
ocorre no contínuo real quadridimensional. A decomposição reduzida usa o
triângulo $3$-$4$-$5$:

$$
\cos\theta_c
=
\frac{3}{\sqrt{3^2+4^2}}
=
\frac35.
$$

Como a variável fundamental é complexa, a norma elementar real--imaginária é

$$
\|1+i\|=\sqrt2.
$$

A admitância reduzida é

$$
\chi_B
=
\sqrt2\cos\theta_c
=
\frac{3\sqrt2}{5}.
$$

A fronteira do estômato é $S^3$, com

$$
\operatorname{Vol}(S^3)=2\pi^2.
$$

Logo a energia entrópica reduzida de superfície é

$$
E_\partial^{(0)}
=
\ln(2\pi^2).
$$

O excesso torsional reduzido do nêutron é

$$
\delta_B
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
=
2.530825921868.
$$

Portanto

$$
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}+\delta_B
=
1838.683499110479.
$$

A comparação posterior com o valor CODATA 2022 $1838.68366200$ dá erro relativo

$$
-8.86\times10^{-8}.
$$

Status: esta é uma derivação reduzida condicional à validade da projeção
Fredholm--Fano $3$-$4$-$5$ do setor torsional. O valor aceito não entra na
dedução; entra apenas depois, como comparação.

## 5. Carga como resíduo inteiro

A carga bariônica efetiva é obtida como resíduo de Cauchy de uma forma de
conexão no ciclo de contorno. Esquematicamente,

$$
Q
=
\frac{1}{2\pi i}
\oint_\Gamma\mathcal A.
$$

Como $\Gamma$ envolve singularidades/estômatos do fibrado, a integral pertence
à classe inteira correspondente:

$$
Q\in\mathbb Z.
$$

Essa leitura explica por que a carga total observada é inteira no contorno
global. A distribuição interna de tensões pode ser não uniforme sem mudar o
resíduo total.

## 6. Perfil torsional do nêutron

O nêutron tem carga total nula:

$$
G_E^n(0)=0.
$$

Mas a densidade interna não precisa ser nula. Use a coordenada de superfície

$$
\xi=r-r_p.
$$

A separação torsional líder é

$$
\xi_+
=
-\frac12r_p\alpha_{\rm tor}^{(2)},
\qquad
\xi_-
=
\frac12r_p\alpha_{\rm tor}^{(2)},
$$

com

$$
\alpha_{\rm tor}^{(2)}
=
2\alpha\ln(2\pi^2).
$$

O perfil variacional líder resolve a equação de calor de Perelman na camada:

$$
\left(
\partial_\tau-\partial_\xi^2
\right)H_n(\xi,\tau)=0.
$$

Com condição inicial dipolar,

$$
H_n(\xi,0)
=
|\mu_n|
\left[
\delta(\xi-\xi_+)-\delta(\xi-\xi_-)
\right],
$$

a solução é

$$
H_n(\xi,\tau_n)
=
|\mu_n|
\left[
K_{\tau_n}(\xi,\xi_+)
-K_{\tau_n}(\xi,\xi_-)
\right],
$$

onde

$$
K_\tau(\xi,\xi_0)
=
\frac1{\sqrt{4\pi\tau}}
\exp\left[-\frac{(\xi-\xi_0)^2}{4\tau}\right].
$$

A largura natural é

$$
\sqrt{2\tau_n}
=
\frac12r_p\alpha_{\rm tor}^{(2)}.
$$

O fator elétrico líder é

$$
G_E^n(q^2)
=
\int H_n(\xi,\tau_n)
j_0(q(r_p+\xi))\,d\xi.
$$

Como

$$
\int H_n\,d\xi=0,
$$

segue

$$
G_E^n(0)=0.
$$

Expansão de baixa energia:

$$
j_0(qr)=1-\frac{q^2r^2}{6}+O(q^4).
$$

Logo,

$$
-6\left.\frac{dG_E^n}{dq^2}\right|_0
=
\int H_n(\xi,\tau_n)(r_p+\xi)^2\,d\xi.
$$

No limite líder,

$$
\langle r_n^2\rangle
=
-2|\mu_n|\alpha_{\rm tor}^{(2)}r_p^2.
$$

O script `perfil_torcional_neutron.py` preserva o cálculo. A saída registra

$$
\int H_n\,d\xi\simeq -9.535541374287\times10^{-18},
$$

compatível com carga total nula no erro numérico.

## 7. Decaimento beta como quarta variação

O canal é

$$
n\to p+e^-+\bar\nu_e.
$$

O antineutrino é o modo neutro torsional:

$$
\psi_{\bar\nu}\in\ker D_{0,-3/2}^{(0)}.
$$

O endpoint

$$
Q_\beta=M_n-M_p-m_e
$$

não é energia fixa do antineutrino. O balanço correto é

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

No limite líder sem recuo:

$$
E_{\bar\nu}=\Delta M-E_e,
\qquad
m_e\le E_e\le\Delta M.
$$

A amplitude efetiva vem da quarta variação projetada da ação oficial:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}
K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+\text{permutações}.
$$

No setor não polarizado, as simetrias reduzem a amplitude a dois invariantes:

$$
\mathcal M_0=C_SS+C_TT.
$$

A média de spins fornece

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

Defina a norma contraída

$$
\mathcal J_3^2
=
2|C_S|^2+6|C_T|^2.
$$

Os coeficientes são resíduos causais:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 8. Espaço de fase e taxa total

O espaço de fase líder é

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

A forma diferencial mínima é

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2.
$$

A taxa total é

$$
\Gamma_n
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}I_\beta.
$$

O fechamento contraído histórico assume a lei reduzida de relaxamento

$$
\tau_n
=
\frac{32}{15}\alpha^{-11}
\frac{\hbar}{m_ec^2}.
$$

Equivalente em energia:

$$
\Gamma_E
=
\frac{\hbar}{\tau_n}
=
\frac{15}{32}\alpha^{11}m_ec^2.
$$

Igualando com

$$
\Gamma_E
=
\frac{\mathcal J_3^2}{2\pi^3}I_\beta,
$$

obtemos

$$
\mathcal J_3^2
=
\frac{15\pi^3}{16}
\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

Com

$$
m_e=0.51099895069\,{\rm MeV},
\qquad
\Delta M=1.29333251\,{\rm MeV},
$$

o script `validar_beta_livre_completo.py` encontra

$$
I_\beta
=
5.700456936530352\times10^{-17}\,{\rm GeV}^5,
$$

$$
\mathcal J_3^2
=
8.142351666635048\times10^{-10}\,{\rm GeV}^{-4},
$$

$$
\sqrt{\mathcal J_3^2}
=
2.853480623139931\times10^{-5}\,{\rm GeV}^{-2}.
$$

Então

$$
\Gamma_n
=
1.137140542406870\times10^{-3}\,{\rm s}^{-1},
$$

$$
\tau_n
=
879.398775004012\,{\rm s},
$$

e

$$
T_{1/2}
=
609.552781481901\,{\rm s}.
$$

Comparação posterior:

| referência | $\tau_{\rm ref}$ s | diferença s | diferença relativa |
|---|---:|---:|---:|
| PDG 2024 | 878.400000000000 | 0.998775004012 | $1.137038938994\times10^{-3}$ |

Status: avaliação fenomenológica do ansatz de taxa total. O expoente $11$ e o
fator $32/15$ não foram obtidos do determinante da Hessiana. A forma
diferencial fina, recoil, correlações angulares e separação individual de
$C_S$ e $C_T$ também continuam metrologia futura.

## 9. Rotas que não entram como fundamento positivo

Não usar como prova:

- coeficientes WKB $A_2,C_4,M_r$ sem todos os dados de colagem;
- transplante de rigidezes estáticas de outro setor como terceiro jato causal;
- palpite unitário de parâmetros que nem possui ponto de retorno;
- jatos causais separados $[z^3]F_S$ e $[z^3]F_T$ quando só a norma contraída
  é determinada;
- meia-vida absoluta obtida por ajuste de coeficientes ao alvo experimental.

Essas rotas servem como auditoria ou programa futuro, não como linha positiva
do manuscrito.

## 10. Scripts autocontidos

| Script | Papel | Classificação |
|---|---|---|
| `derivar_delta_barioes.py` | Deriva $\delta_B=\ln(2\pi^2)3\sqrt2/5$. | Derivação reduzida. |
| `derivacao_simbolica_massas_barioes.py` | Deriva $M_p/M_e$ e $M_n/M_e$. | Derivação simbólica. |
| `calcular_massas_barioes.py` | Avalia massas reduzidas. | Avaliação direta. |
| `perfil_torcional_neutron.py` | Calcula $H_n$ e $G_E^n$ líder. | Perfil variacional reduzido. |
| `validar_beta_livre_completo.py` | Calcula $I_\beta$, $\mathcal J_3$, $\tau_n$, $T_{1/2}$ e espectro. | Avaliação direta/teste de convergência/comparação. |
| `comparar_tau_neutron.py` | Compara a vida média reduzida. | Comparação fenomenológica. |

Todos escrevem saídas Markdown na pasta `scripts/`.

## 11. Status

| Bloco | Status | Limite |
|---|---|---|
| Três estômatos | Fechado estruturalmente | Background trimodal. |
| Volume $6\pi^5$ | Fechado reduzido | Razão de massa. |
| Próton | Fechado em redução de superfície | Metrologia fina exige Hessiana completa. |
| Nêutron | Fechado estruturalmente | Cisalhamento antiparalelo. |
| $\delta_B$ | Fechado condicionalmente | Depende da projeção Fredholm--Fano. |
| Perfil $H_n$ | Fechado como perfil líder | Fator de forma completo requer sonda real. |
| Beta contínuo | Fechado | Endpoint não é energia fixa. |
| Vida média | Fechada condicionalmente | Nível $10^{-3}$; diferencial futuro. |
