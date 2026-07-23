# Questão 54 — Como a relatividade geral emerge?

## Status

$$
\boxed{
\text{fechada estruturalmente e condicionalmente}
}
$$

A Questão 54 está fechada quanto à forma macroscópica da Relatividade Geral:
a equação métrica ponderada da ação oficial da GDQ reduz-se, sob média
torsional macroscópica e fechamento hidrodinâmico, à equação de Einstein com
constante cosmológica.

Ela permanece condicional quanto à metrologia completa: o valor absoluto de
$G$, o valor de $\Lambda$ e eventuais correções pós-newtonianas torsionais
dependem do background global, dos contornos e dos resíduos de torção. Isso
não reabre a emergência estrutural de Einstein; apenas separa forma local de
normalização global.

## 1. Enunciado

A pergunta exige responder cinco pontos:

1. qual limite da ação produz Einstein--Hilbert;
2. como $G$ aparece;
3. qual tensor energia--momento acopla à métrica;
4. se a equivalência fraca e forte é preservada;
5. quais correções pós-newtonianas são previstas.

## 2. Dados e hipóteses usadas

Partimos apenas da ação oficial da GDQ,

$$
\mathcal{S}_{\mathrm{GDQ}} = \int_{\gamma}
\left[ \int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
$$

As convenções preservadas são

$$
\rho=e^{-(f+\bar f)/2},
\qquad
S_R=\frac{\hbar}{2i}(f-\bar f),
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
$$

O limite considerado é:

1. projeção física macroscópica para quatro dimensões;
2. background admissível estacionário;
3. média de torção em corpos ou regiões não polarizadas;
4. fechamento hidrodinâmico da tensão contida em $f$, $\rho$, $S_R$ e na
   resposta métrica;
5. normalização newtoniana no campo fraco.

## 3. Da ação oficial à equação métrica ponderada

A variação da ação oficial em relação à métrica produz a equação métrica
ponderada. Na notação consolidada do Capítulo 7:

$$
\begin{aligned}
0={}&\tau\mathcal U
\left(R_{\mu\nu}+P_{\mu\nu}^{(f)}\right)
\\
&+\tau\left(
g_{\mu\nu}\Delta\mathcal U
-\nabla_\mu\nabla_\nu\mathcal U
\right)
\\
&-\frac12\mathcal U
\left(\mathcal L_0-\lambda\right)g_{\mu\nu}.
\end{aligned}
$$

Essa equação é o ponto de partida correto. Ela não é a equação de Einstein
postulada: é a equação métrica da GDQ com peso $\mathcal U$ e campo complexo
$f$.

Na carta real escrevemos

$$
f=f_R+i\theta,
\qquad
\theta=\frac{S_R}{\hbar},
\qquad
\rho=e^{-f_R}.
$$

Logo,

$$
f_R=-\ln\rho.
$$

A identidade exata da densidade é

$$
\nabla_\mu\nabla_\nu f_R
=
\nabla_\mu f_R\nabla_\nu f_R
-\frac1\rho\nabla_\mu\nabla_\nu\rho.
$$

Como $\mathcal U\propto e^{-f_R}$ na seção considerada,

$$
\frac{\nabla_\mu\nabla_\nu\mathcal U}{\mathcal U}
=
-\nabla_\mu\nabla_\nu f_R
+\nabla_\mu f_R\nabla_\nu f_R.
$$

Os termos quadráticos em $\nabla f_R$ cancelam entre a tensão de $f$ e a
variação do peso. Dividindo por $\tau\mathcal U$, obtém-se a forma reduzida:

$$
R_{\mu\nu}
+\nabla_\mu\nabla_\nu f_R
+\nabla_\mu\theta\nabla_\nu\theta
+\Xi g_{\mu\nu}
=0,
$$

com

$$
\Xi
=
-\Delta f_R
+|\nabla f_R|^2
-\frac{\mathcal L_0-\lambda}{2\tau}.
$$

Esse é o elo matemático essencial: a curvatura macroscópica aparece
diretamente da equação métrica da GDQ, e os termos restantes são tensões de
densidade, fase, pressão efetiva e traço.

## 4. Média torsional e conexão de Levi--Civita

A conexão de Bismut pode ser escrita como

$$
\Gamma^{B\,a}{}_{bc}
=
\Gamma^{LC\,a}{}_{bc}
+\frac12H^a{}_{bc}.
$$

Para uma região macroscópica não polarizada, assume-se a média

$$
\langle H^a{}_{bc}\rangle_L\to0.
$$

Então

$$
\Gamma^B\to\Gamma^{LC}.
$$

Portanto, no setor médio macroscópico, a geometria efetiva é descrita pela
conexão sem torção. Isso explica por que a Relatividade Geral aparece como
limite clássico mesmo que a GDQ tenha torção constitutiva em escala
microscópica.

Se a média torsional não se anula — objeto polarizado, rotação, defeito,
interface ou meio anisotrópico — a GDQ prevê correções fora da RG pura.

## 5. Tensor energia--momento que acopla à métrica

O tensor energia--momento não é inserido como fonte externa fundamental. Ele
é definido variacionalmente como a tensão macroscópica conservada gerada pelos
campos da GDQ:

$$
T_{\mu\nu}^{\rm GDQ}
=
\left\langle
T_{\mu\nu}^{(\theta)}
+T_{\mu\nu}^{(\rho)}
+T_{\mu\nu}^{(H)}
+T_{\mu\nu}^{\rm bordo}
\right\rangle_L.
$$

Em palavras:

- $T_{\mu\nu}^{(\theta)}$ vem da fase/circulação $S_R$;
- $T_{\mu\nu}^{(\rho)}$ vem dos gradientes de densidade e pressão efetiva;
- $T_{\mu\nu}^{(H)}$ vem da torção de Bismut/Cartan;
- $T_{\mu\nu}^{\rm bordo}$ vem de contornos físicos e aparelhos quando
  presentes.

No regime hidrodinâmico, essa média assume a forma constitutiva usual de um
fluido efetivo,

$$
T_{\mu\nu}
=
\left(\epsilon+p\right)
\frac{u_\mu u_\nu}{c^2}
+p\,g_{\mu\nu}
+\Pi_{\mu\nu}^{\rm tor}
+\Pi_{\mu\nu}^{\rm visc}.
$$

Na RG pura macroscópica, os termos residuais anisotrópicos são desprezados:

$$
\Pi_{\mu\nu}^{\rm tor}\to0,
\qquad
\Pi_{\mu\nu}^{\rm visc}\to0.
$$

## 6. Redução trace-reversed e forma de Einstein

Depois do fechamento hidrodinâmico, a equação métrica reduzida toma a forma
trace-reversed:

$$
R_{\mu\nu}
=
\kappa_G
\left(
T_{\mu\nu}
-\frac12g_{\mu\nu}T
\right)
+\Lambda g_{\mu\nu}.
$$

Contraindo em quatro dimensões:

$$
R=-\kappa_GT+4\Lambda.
$$

Substituindo de volta:

$$
\boxed{
R_{\mu\nu}
-\frac12g_{\mu\nu}R
+\Lambda g_{\mu\nu}
=
\kappa_GT_{\mu\nu}.
}
$$

Essa é a equação de Einstein como correspondência macroscópica da GDQ.

## 7. Qual limite da ação produz Einstein--Hilbert?

O funcional Einstein--Hilbert não substitui a ação oficial. Ele aparece como
ação efetiva macroscópica depois que os graus internos, torsionais e de
densidade são projetados:

$$
S_{\rm eff}^{\rm grav}[h]
=
C_R
\int_{\Sigma_4}
\left(
R[h]-2\Lambda
\right)
\sqrt{-h}\,d^4x
+S_{\rm eff}^{\rm mat}[h,\Psi_{\rm eff}]
+\cdots.
$$

A variação desse funcional efetivo em relação a $h^{\mu\nu}$ gera a mesma
equação trace-reversed obtida diretamente da equação métrica ponderada.
Assim:

$$
\boxed{
\text{Einstein--Hilbert é a ação efetiva do setor métrico macroscópico,
não a ação fundamental da GDQ.}
}
$$

O coeficiente é

$$
C_R=\frac{c^4}{16\pi G}.
$$

Na linguagem da Q38, formalmente:

$$
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)}.
$$

Logo,

$$
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
$$

## 8. Como $G$ aparece?

Há dois níveis distintos.

### 8.1 Normalização local: o fator $8\pi$

No campo fraco:

$$
g_{00}
\simeq
-\left(1+\frac{2\Phi}{c^2}\right).
$$

Então,

$$
G_{00}
\simeq
\frac{2}{c^2}\nabla^2\Phi.
$$

Para matéria não relativística:

$$
T_{00}\simeq\rho_m c^2.
$$

A componente $00$ fornece

$$
\frac{2}{c^2}\nabla^2\Phi
=
\kappa_G\rho_m c^2.
$$

Logo,

$$
\nabla^2\Phi
=
\frac{\kappa_Gc^4}{2}\rho_m.
$$

Comparando com Poisson,

$$
\nabla^2\Phi
=
4\pi G\rho_m,
$$

temos

$$
\boxed{
\kappa_G=\frac{8\pi G}{c^4}.
}
$$

Esse cálculo fixa a normalização geométrica da forma de Einstein.

### 8.2 Valor absoluto de $G$

O valor absoluto de $G$ não é determinado por um infinitésimo local do bulk.
Ele pertence à normalização global do background cosmológico e ao problema de
contorno da Q38.

No estado vigente:

$$
\Pi_G
=
\frac{G M_p^2}{\hbar c}
$$

é o grupo adimensional correto. A Q38 registra que $G$ é um resultado
condicionado ao espaço cosmológico de Einstein e à colagem global. Portanto:

$$
\boxed{
\text{o limite local fixa a forma e o fator }8\pi;
\quad
\text{o background global fixa o valor de }G.
}
$$

## 9. Equivalência fraca e forte

### 9.1 Equivalência fraca

A equivalência fraca é preservada no setor macroscópico porque todos os corpos
de teste não polarizados seguem a mesma métrica efetiva média.

A condição suficiente é

$$
\langle H^a{}_{bc}\rangle_L=0,
\qquad
\langle \Pi_{\mu\nu}^{\rm tor}\rangle_L=0.
$$

Então a equação de movimento reduz-se à geodésica de Levi--Civita:

$$
u^\nu\nabla_\nu^{LC}u^\mu=0.
$$

Assim, a aceleração não depende da composição interna do corpo.

### 9.2 Equivalência forte

A equivalência forte é preservada apenas no mesmo limite torsional médio e
universal. Em regiões com torção residual, spin polarizado, interfaces,
meios anisotrópicos ou backgrounds cosmológicos não homogêneos, a GDQ admite
correções controladas por:

$$
\delta\Gamma^\mu{}_{\nu\rho}
=
\frac12H^\mu{}_{\nu\rho},
$$

e por tensões anisotrópicas:

$$
\Pi_{\mu\nu}^{\rm tor}\neq0.
$$

Portanto a resposta correta é:

$$
\boxed{
\text{WEP preservado no regime médio não polarizado;
SEP preservado condicionalmente; correções torsionais são possíveis fora
desse setor.}
}
$$

## 10. Correções pós-newtonianas previstas

No setor torsionalmente médio, a GDQ reproduz os coeficientes PPN líderes da
RG:

$$
\gamma_{\rm PPN}=1,
\qquad
\beta_{\rm PPN}=1.
$$

As correções aparecem quando algum dos seguintes termos não se anula:

1. torção residual macroscópica;
2. gradientes não homogêneos do dilatão $f_R$;
3. pressão interna ou viscosidade geométrica;
4. termos de borda/aparelho;
5. background cosmológico de Einstein não localmente desprezível.

Esquematicamente:

$$
\gamma_{\rm PPN}
=
1+\delta\gamma_H+\delta\gamma_f+\delta\gamma_{\partial},
$$

$$
\beta_{\rm PPN}
=
1+\delta\beta_H+\delta\beta_f+\delta\beta_{\partial}.
$$

No limite solar usual, a previsão estrutural é:

$$
|\delta\gamma|,\ |\delta\beta|
\ll1,
$$

porque a média torsional e os gradientes internos são suprimidos em corpos
macroscópicos não polarizados.

Os coeficientes numéricos finos ainda não foram derivados de uma Hessiana
global completa para o Sistema Solar. Essa é uma extensão metrológica, não uma
lacuna da recuperação estrutural de Einstein.

## 11. Respostas diretas às cinco perguntas

| Pergunta | Resposta GDQ | Status |
|---|---|---|
| Qual limite da ação produz Einstein--Hilbert? | O limite macroscópico torsionalmente médio da equação métrica ponderada; EH é ação efetiva equivalente. | Fechado estruturalmente |
| Como $G$ aparece? | Localmente por $\kappa_G=8\pi G/c^4$ via Poisson; numericamente pelo background global Q38. | Condicional ao contorno global |
| Qual tensor energia--momento acopla? | A tensão variacional média de fase, densidade, torção e bordos da GDQ. | Fechado estruturalmente |
| WEP/SEP são preservados? | WEP sim no setor não polarizado; SEP sim condicionalmente no setor torsional médio. | Fechado condicionalmente |
| Quais correções PPN? | $\gamma=\beta=1$ no limite médio; correções de torção, dilatão, viscosidade e borda. | Forma fechada; coeficientes finos futuros |

## 12. Conclusão

A Relatividade Geral emerge na GDQ como teoria efetiva macroscópica do setor
métrico estacionário. A equação de Einstein não é colocada por fora: ela é a
forma trace-reversed da equação métrica ponderada depois de média torsional e
fechamento hidrodinâmico.

O que a Q54 fecha é a correspondência estrutural:

$$
\mathcal S_{\rm GDQ}
\to
\text{equação métrica ponderada}
\to
\text{média torsional}
\to
T_{\mu\nu}^{\rm GDQ}
\to
G_{\mu\nu}+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}.
$$

O que permanece setorial é a metrologia de $G$, $\Lambda$ e dos resíduos
PPN, que depende do problema global de contorno já organizado na Q38.

## 13. Registro de fechamento e refinamentos

Registro final:

$$
\boxed{
\text{Q54 fechada estruturalmente e condicionalmente.}
}
$$

A questão não fica aberta por não recalcular o valor absoluto de $G$ dentro do
limite local. Isso já foi separado na Q38: $G$ é normalização global de
contorno/background, enquanto a Q54 pergunta como a Relatividade Geral emerge
como teoria macroscópica.

O fechamento cobre:

1. a redução da equação métrica ponderada da GDQ para a forma trace-reversed;
2. a forma de Einstein com constante cosmológica;
3. a identificação de $T_{\mu\nu}$ como tensão variacional média dos campos
   GDQ;
4. a normalização local $\kappa_G=8\pi G/c^4$ pelo limite de Poisson;
5. a preservação do princípio de equivalência fraco no setor macroscópico
   não polarizado;
6. a recuperação PPN líder $\gamma=\beta=1$ no mesmo setor.

Refinamentos que não reabrem a Q54:

1. calcular coeficientes PPN finos para o Sistema Solar a partir da Hessiana
   física do background gravitacional real;
2. avaliar resíduos torsionais em corpos rotantes, polarizados ou com
   estrutura interna anisotrópica;
3. conectar quantitativamente $\Lambda$ ao background cosmológico consolidado;
4. testar variações experimentais de $G$ como resposta de contorno/aparelho,
   sem redefinir o valor global de $G$;
5. construir simulações de campo fraco com torção residual para comparar com
   precessão, lenteamento e atraso Shapiro.
