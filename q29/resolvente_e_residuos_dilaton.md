# Q29 — Resolvente dilatônico e resíduos do estômato

## 1. Correção da rota logarítmica

Uma expansão

$$
F_Q(z)=F_0+C\log(z-z_*)+\cdots
$$

possui monodromia, mas não um resíduo meromorfo de $F_Q(z)dz$. De fato,

$$
\oint_{|z-z_*|=r}\log(z-z_*)dz
\propto r
$$

e tende a zero quando $r\to0$. Logo, a covariância calculada anteriormente é
o coeficiente da resposta logarítmica, não diretamente um resíduo de Cauchy.

## 2. Objeto causal correto

Considere a transformada resolvente da equação linearizada:

$$
\widehat c(z)
=(z-L_f)^{-1}J_{\rm stoma}.
$$

Projetando sobre a inserção eletromagnética,

$$
\widehat F_Q(z)
=\langle\Phi_Q,(z-L_f)^{-1}J_{\rm stoma}\rangle_\mu.
$$

Para uma base ortonormal $L_f\psi_n=\lambda_n\psi_n$,

$$
\boxed{
\widehat F_Q(z)
=\sum_n
\frac{
\langle\Phi_Q,\psi_n\rangle_\mu
\langle\psi_n,J_{\rm stoma}\rangle
}{z-\lambda_n}.
}
$$

Assim, os resíduos são genuínos:

$$
\boxed{
\operatorname{Res}_{z=\lambda_n}\widehat F_Q
=\langle\Phi_Q,\psi_n\rangle
\langle\psi_n,J_{\rm stoma}\rangle.
}
$$

## 3. Modo zero

A fonte compensada

$$
J_{\rm stoma}=\delta_\epsilon-\mu
$$

é ortogonal ao modo constante. Portanto,

$$
\operatorname{Res}_{z=0}\widehat F_Q=0.
$$

Isso preserva a normalização total e evita reintroduzir o polo espúrio
$(4\pi z)^{-n}$.

## 4. Polos físicos

Os modos não homogêneos possuem overlaps não nulos e geram polos simples nos
autovalores positivos. O solver calcula diretamente $\lambda_n$ e cada
resíduo. A susceptibilidade estática anterior é recuperada por

$$
\langle\Phi_Q,L_f^{-1}J\rangle
=\sum_{n>0}
\frac{\operatorname{Res}_{\lambda_n}\widehat F_Q}{\lambda_n}.
$$

Portanto, a resposta localizada pode ser reinterpretada sem alterar nenhum
resultado anterior: ela é a soma dos polos físicos do resolvente.

### 4.1 Resultado numérico

Para a malha de $5000$ pontos e os primeiros $120$ modos, obtém-se

$$
\lambda_0=0,
\qquad
\langle\psi_0,J_{\rm stoma}\rangle
=-1{,}95\times10^{-12},
$$

confirmando numericamente a ausência do polo constante. Os primeiros polos
positivos e resíduos são

| $n$ | $\lambda_n$ | $\operatorname{Res}_n$ |
|---:|---:|---:|
| 1 | $1{,}7768490824$ | $-26{,}0446338196$ |
| 2 | $3{,}1779908389$ | $-4{,}2799259926$ |
| 3 | $4{,}7687097838$ | $-2{,}5525611228$ |
| 4 | $6{,}8576447442$ | $-1{,}7167791932$ |
| 5 | $9{,}4724664746$ | $-1{,}2302738052$ |

A soma truncada fornece

$$
\sum_{n=1}^{120}\frac{\operatorname{Res}_n}{\lambda_n}
=-17{,}1215332872.
$$

O cálculo direto da equação de Poisson localizada havia fornecido

$$
\operatorname{Cov}_\mu(\Phi_Q,c)
=-17{,}1214968064.
$$

A diferença relativa é aproximadamente

$$
2{,}13\times10^{-6},
$$

e decorre do truncamento modal. Assim, a decomposição em resíduos reproduz a
resposta estática independente.

### 4.2 Convergência

| pontos | modos | $\sum \operatorname{Res}_n/\lambda_n$ |
|---:|---:|---:|
| 2500 | 80 | $-17{,}1216460635$ |
| 5000 | 120 | $-17{,}1215332872$ |
| 5000 | 160 | $-17{,}1215409560$ |
| 8000 | 160 | $-17{,}1215107798$ |

Os autovalores e resíduos baixos permanecem estáveis com o refinamento. A
soma total dos resíduos sem o denominador não é o observável estático e
converge mais lentamente para uma fonte delta localizada; ela não deve ser
usada como normalização física.

## 5. Monodromia

A monodromia não precisa criar artificialmente um polo. Ela seleciona o
contorno causal e quais autovalores/resíduos são envolvidos. A amplitude da
fonte continua devendo vir da classe de circulação, mas agora multiplica
resíduos espectrais bem definidos.

## 6. Próximo passo

É necessário identificar, pela prescrição causal de Sudarshan, qual conjunto
de polos $\lambda_n$ está dentro de $\gamma$ e qual combinação avançada--
retardada contribui para a parte real. Somente então se calcula $K_Q$.

O cálculo presente prova três fatos, sem pós-ajuste:

1. a localização no estômato excita modos físicos não homogêneos;
2. a normalização remove exatamente o modo constante, mas não cancela a
   resposta espectral;
3. a resposta de Poisson é recuperada pela soma dos resíduos do resolvente.

Ele ainda não fixa a amplitude topológica da fonte nem a prescrição causal do
contorno. Portanto, não constitui sozinho uma derivação numérica de $\alpha$.

## 7. Auditoria da proposta de `zz1.md`

### 7.1 O que a topologia realmente fixa

No elo tridimensional do estômato, a normalização natural não é um primeiro
número de Chern integrado diretamente em $S^3$, pois

$$
H^2(S^3)=0.
$$

O invariante apropriado é o winding de uma aplicação $S^3\to G$, a classe de
Hopf, ou o fluxo de uma $3$-forma de torção:

$$
k
=
\frac{1}{\mathcal N_G}
\int_{S^3}H_B
\in\mathbb Z.
$$

Para o defeito elementar, $k=1$. Isso justifica precisamente a condição de
fluxo unitário usada no cálculo,

$$
p(\epsilon)c'(\epsilon)=-1,
$$

salvo orientação. Logo, a amplitude topológica adimensional da fonte já foi
fixada no solver. O número $-17{,}1215$ é a resposta do background GDQ a uma
unidade topológica; não foi obtido ajustando a carga elétrica.

Essa quantização ainda não fornece automaticamente o coeficiente dimensional
que converte o fluxo torsional em rigidez eletromagnética. Essa conversão deve
ser obtida pelo pullback da ação oficial e pela normalização do modo de Hopf.

### 7.2 O que a causalidade realmente seleciona

Uma prescrição retardada não escolhe arbitrariamente apenas o primeiro modo.
Para uma evolução de segunda ordem, a continuação causal tem a forma

$$
G_R(\omega)
=
\sum_{n>0}
\frac{|\psi_n\rangle\langle\psi_n|}
{(\omega+i0)^2-\lambda_n},
$$

e contém todos os modos permitidos pela fonte e pelo observável. Para uma
evolução térmica ou de fluxo de primeira ordem, analogamente,

$$
G_R(\zeta)
=
\sum_{n>0}
\frac{|\psi_n\rangle\langle\psi_n|}
{\zeta+\lambda_n-i0}.
$$

O sinal de $i0$ escolhe retardado ou avançado, mas não apaga os polos
superiores. Apenas uma lei adicional de projeção, simetria ou limite
assintótico poderia isolar o modo fundamental. Escolher esse modo porque ele
produz um número desejado seria circular.

No limite estático, a prescrição causal retorna

$$
\widehat F_Q(0)
=
-\sum_{n>0}\frac{\operatorname{Res}_n}{\lambda_n},
$$

até a convenção de sinal do operador. Portanto, a resposta estática completa
continua sendo a soma já verificada contra a solução de Poisson.

### 7.3 Consequência

`zz1.md` identifica corretamente os dois ingredientes físicos — fluxo
quantizado e causalidade —, mas eles não constituem duas liberdades numéricas:

1. o fluxo elementar $k=1$ já normaliza a fonte;
2. a causalidade fixa o lado analítico do resolvente, não um subconjunto
   escolhido de seus polos;
3. o elo ainda faltante é o mapa variacional entre a unidade de
   winding/torção e o coeficiente do termo $|F_Q|^2$ na ação reduzida.

Parecia que o cálculo decisivo restante seria o elemento misto da Hessiana oficial

$$
\mathcal J_{BQ}
=
\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta B\,\delta F_Q}
\bigg|_*,
$$

junto com a rigidez dilatônica $\mathcal K_f$. Eliminando a resposta
dilatônica, o coeficiente eletromagnético físico deve ser

$$
K_Q^{\rm eff}
=
K_Q^{(0)}
-
\mathcal J_{Qf}\mathcal K_f^{-1}\mathcal J_{fQ}.
$$

A soma de resíduos agora calculada avalia explicitamente a parte
$\mathcal K_f^{-1}$ desse complemento de Schur. Falta derivar os dois vértices
mistos $\mathcal J_{Qf}$ da ação oficial; isso é mais preciso do que procurar
um polo especial por inspeção.

O cálculo direto posterior mostrou, contudo, que

$$
\mathcal J_{Qf}=0
$$

em $F_Q=0$: a covariância é o vértice cúbico $fF_Q^2$. Portanto, eliminar uma
resposta induzida por $F_Q$ corrige apenas $F_Q^4$. O termo cinético somente é
vestido se o fluxo topológico gerar previamente um background dilatônico não
trivial. Ver `q29/hessiana_mista_dilatao_hopf.md`.
