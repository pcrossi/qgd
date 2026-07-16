# Ponte global--local — Porta A: contorno causal e fatorização energética

## 1. Enunciado auditado

O objetivo desta auditoria é decidir se o vínculo energético pode ser escrito
como

$$
\mathcal C_E
=K_\gamma(\alpha)
\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1,
$$

ou se a dependência causal deve permanecer dentro da integral oficial,

$$
\mathcal C_E
=\frac{\hbar}{\Lambda_C^2\beta_EE_H}
\operatorname{Phys}\!\int_\gamma
\mathscr E(z_\tau)\frac{dz_\tau}{z_\tau}-1,
$$

onde

$$
\mathscr E(z_\tau)
:=
\frac{p_0^{\rm red}(z_\tau)e^{-x_0(z_\tau)}}{Z_0(z_\tau)}.
$$

Não se usa o valor observado de $G$, a raiz desejada do solver ou qualquer
normalização escolhida pelo alvo.

## 2. Dados canônicos encontrados

### 2.1 Variável causal

A definição vigente é

$$
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
$$

Logo, $\tau$ e $t$ não são identificados. O contorno satisfaz

$$
\gamma\subset\mathbb C_{z_\tau}.
$$

Fontes: `questão_4.md:134-164` e `questão_6.md:185-257`.

### 2.2 Prescrição causal atualmente declarada

O documento canônico associa $\gamma$ à combinação simétrica

$$
G_{\rm sym}
=\frac12(G_{\rm ret}+G_{\rm adv}).
$$

Também estabelece que integrais de termos exatos se anulam quando o
integrando é monovalorado e regular, o contorno não cruza cortes e as
singularidades internas estão controladas.

Fonte: `questão_4.md:168-206`.

Tomada isoladamente, essa formulação não explicitava:

1. uma parametrização orientada de $\gamma$;
2. se $\gamma$ é fechado, aberto ou uma thimble relativa no setor energético;
3. o mapa preciso entre o símbolo $d\tau/\tau$ da ação e
   $dz_\tau/z_\tau$ no plano causal;
4. a reconstrução hermitiana em termos dos contornos conjugados;
5. a normalização da extração de Laurent.

O item 5 e a forma correta do item 4 foram posteriormente explicitados pelo
projetor físico normalizado da Q29, descrito na próxima subseção. Ainda assim,
a parametrização de uma família causal não estacionária e sua eventual
deformação em thimbles não estão fixadas por esse projetor abstrato.

### 2.3 Projetor físico normalizado e realidade

O documento canônico mais recente explicita o mapa físico que já estava
implícito na extração de Laurent das Q4 e Q9. Para

$$
w_\gamma
=\frac1{2\pi i}\oint_\gamma\frac{dz}{z}\neq0,
$$

define-se

$$
\boxed{
\mathfrak P_\gamma[F]
:=\frac1{2\pi i w_\gamma}
\oint_\gamma F(z)\frac{dz}{z}.
}
$$

Para winding unitário, $\mathfrak P_\gamma[F]=F_0$. Em particular,

$$
\boxed{\mathfrak P_\gamma[1]=1.}
$$

O fator normalizador não é inserido na ação oficial. Ele pertence ao mapa de
reconstrução física que extrai o mesmo coeficiente $E_0$ já usado nas equações
locais. A compatibilidade variacional segue da linearidade:

$$
\delta\mathfrak P_\gamma[\mathscr L]
=\mathfrak P_\gamma[\delta\mathscr L].
$$

Fonte principal: `q29/projetor_causal_cauchy_normalizado.md:18-114`.
Compatibilidade anterior: `questão_4.md:389-426` e
`questão_9.md:810-843`.

Quando a condição hermitiana precisa ser exibida, usa-se o par de contornos
conjugados

$$
\mathcal S_{\rm phys}^{\mathbb R}
=\frac12\left(
\mathfrak P_{\gamma_+}[\mathscr L]
+\overline{\mathfrak P_{\gamma_-}[\mathscr L]}
\right),
$$

e não $\operatorname{Re}\oint$ sem normalização. Fonte:
`q29/projetor_causal_cauchy_normalizado.md:71-100`.

### 2.4 Normalização da medida

Para uma inserção suave, a medida normalizada deve ser tratada como kernel
completo. O fator $(4\pi z)^{-4}$ isolado não pode ser contado como polo,
pois sua integração contra o gaussiano e a normalização de massa produzem uma
expansão regular.

Fontes: `q38/criterio_residuo_contorno_gdq.md:57-62` e
`q38/derivacao_causal_residuo_q38.md:81-108`.

## 3. Critério exato de fatorização

A fatorização escalar existe somente se houver uma decomposição demonstrada

$$
\mathscr E(z)=E_{\rm rad}\,k_\gamma(z),
$$

na qual $E_{\rm rad}$ seja independente de $z$ em todo o contorno e
$k_\gamma$ seja conhecido antes da solução radial. Nesse caso,

$$
K_\gamma
=\mathfrak P_\gamma[k_\gamma].
$$

Os fatores dimensionais $\hbar/(\Lambda_C^2\beta_EE_H)$ permanecem fora do
projetor causal e não devem ser confundidos com $K_\gamma$.

Essa condição não foi demonstrada. Na construção vigente,

$$
p_0^{\rm red}=p_0^{\rm red}(z),
\qquad
x_0=x_0(z),
\qquad
Z_0=Z_0(z),
$$

porque todos são avaliados no background que depende do parâmetro de fluxo.
A normalização folha a folha não remove essa dependência relativa.

Portanto, em geral,

$$
\boxed{
\mathfrak P_\gamma[\mathscr E]
\neq
\mathfrak P_\gamma[1]\,\mathscr E(z_*)
}
$$

e a integral deve permanecer não fatorada.

## 4. Setor estacionário

Se o background é estacionário ao longo da classe causal e

$$
\mathscr E(z)=E_{\rm rad},
$$

então, pela linearidade do projetor normalizado,

$$
\mathfrak P_\gamma[\mathscr E]
=E_{\rm rad}\mathfrak P_\gamma[1]
=E_{\rm rad}.
$$

Consequentemente,

$$
\boxed{K_\gamma=1}
$$

para a **parcela causal**. Isso não determina o valor de $E_{\rm rad}$ nem os
fatores dimensionais da redução.

Não há contradição com o teorema de anulação da Q38. Lá foi estudada a
1-forma $F_R(z)dz$ do coeficiente de curvatura, enquanto o projetor físico
atua sobre $F(z)dz/z$ e extrai $F_0$. São objetos de contorno diferentes.

## 5. Auditoria da sela térmica

A Q38 contém o primeiro winding relativo

$$
I_1(\tau)\propto
\tau^{-4}\exp\left(-\frac{\beta_E^2}{4\tau}\right),
$$

cujo ponto estacionário como **função $I_1$** é

$$
\tau_*^{(I)}=\frac{\beta_E^2}{16}.
$$

Fonte: `questão_38_final.md:134-157`.

Esse resultado não localiza automaticamente a integral energética oficial.
Ao incluir a medida $d\tau/\tau$, o peso escalar correspondente passa a ser

$$
\tau^{-5}\exp\left(-\frac{\beta_E^2}{4\tau}\right),
$$

e seu ponto estacionário real é

$$
\boxed{
\tau_*^{(I\,d\tau/\tau)}
=\frac{\beta_E^2}{20}.
}
$$

Mais geralmente, se a resposta radial introduzir uma potência ou fase, a
sela muda novamente. Além disso, a segunda derivada de $\log I_1$ no ponto
$\beta_E^2/16$ é

$$
\left.\frac{d^2}{d\tau^2}\log I_1\right|_{\tau_*}
=-\frac4{\tau_*^2}<0,
$$

isto é, um máximo no eixo real positivo. Seu uso numa integral complexa exige
uma thimble de descida, orientação, fase e prefator gaussiano. Esses dados não
foram derivados para $\gamma$.

Portanto a sela térmica da Q38 é uma aproximação controlada do setor de
winding relativo, mas não fornece atualmente $K_\gamma$ para a energia.

## 6. Forma correta vigente da Porta A

No setor estacionário, o vínculo reduz-se legitimamente a

$$
\boxed{
\mathcal C_E
=\frac{\hbar}{\Lambda_C^2\beta_EE_H}
\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1,
}
$$

pois $K_\gamma=\mathfrak P_\gamma[1]=1$.

Para uma família causal não estacionária, a forma correta é

$$
\boxed{
\mathcal C_E
=\frac{\hbar}{\Lambda_C^2\beta_EE_H}
\mathfrak P_\gamma\!\left[
\frac{p_0^{\rm red}(z)e^{-x_0(z)}}{Z_0(z)}
\right]-1.
}
$$

Nesse segundo caso, o projetor deve atuar no integrando completo e não pode
ser substituído por um escalar independente. A aplicação exige especificar:

1. os ramos retardado e avançado;
2. orientação e classe homológica de $\gamma$;
3. contorno fechado ou ciclo relativo;
4. operação de realidade;
5. tratamento de cortes e polos;
6. eventual deformação para thimbles.

## 7. Veredito

$$
\boxed{
\text{$K_\gamma=1$ no setor estacionário; fora dele, não há fatorização.}
}
$$

Mais precisamente:

- no setor estacionário, $K_\gamma=1$ é consequência do projetor de Cauchy
  normalizado e não um ajuste;
- esse resultado não altera a ação oficial;
- numa família $X(z)$ não estacionária, a fatorização é inválida e
  $\mathfrak P_\gamma$ deve agir sobre a resposta completa;
- a sela $\beta_E^2/16$ não pode ser transplantada para a integral oficial
  sem incluir $d\tau/\tau$, a resposta radial e a geometria do contorno;
- a Porta A está fechada para o ansatz estacionário, mas permanece aberta se
  o fechamento exigir uma família causal genuinamente não estacionária.

O solver estacionário pode, portanto, usar $K_\gamma=1$. Se ele falhar de
forma convergente, essa falha não autoriza variar $K_\gamma$; deve-se testar a
necessidade de uma família $X(z)$ e então aplicar o projetor ao integrando
completo.
