# Questão 56 — Energia escura

## 1. Enunciado

A questão pergunta se a GDQ consegue explicar a densidade de energia escura,
respondendo obrigatoriamente:

1. por que a densidade do próton define a densidade UV;
2. por que a diluição é linear;
3. por que há 28 modos multiplicativos;
4. por que a projeção é \(\alpha^2\);
5. se a equação de estado é \(w=-1\);
6. como perturbações cosmológicas evoluem.

Arquivos legados usados como fonte:

- `pt-br/22 - Densidade de Energia do Vácuo.md`;
- `pt-br/32 - Fenomenologia Astrofísica e Cosmológica da GDQ.md`;
- `pt-br/Apêndice 2 - Auditoria e Validação Numérica do Setor Cosmológico e Gravitacional.md`.

## 2. Veredito

$$
\boxed{
\text{Q56 fechada estruturalmente e condicionalmente ao contorno cosmológico global.}
}
$$

O mecanismo é coerente dentro da GDQ:

$$
\rho_{\Lambda}^{\rm GDQ}
=
\alpha^2\,N_{\rm Cartan}\,\rho_{\rm UV}\,
\frac{r_p}{R_H}\,\frac{1}{c^2}.
$$

Mas a predição metrológica absoluta usa dados de fronteira do universo
observável, principalmente \(R_H=c/H_0\). Isso não é falha: em cosmologia o
raio/horizonte do universo observado é condição de contorno do problema, não
algo que uma teoria local possa deduzir sem especificar a solução global.

## 3. Cadeia dedutiva mínima

No setor cosmológico de Einstein, a GDQ usa a cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\text{sela cosmológica global}
\to
\text{tensão UV bariônica}
\to
\text{diluição global--local}
\to
\text{projeção gravitacional real}
\to
\rho_\Lambda .
$$

O espaço relevante aqui é o cosmológico/espectral, não simplesmente o bulk
local plano. Portanto os resultados dependem da ponte global--local já
registrada como teorema condicional.

## 4. Por que a densidade do próton define a densidade UV?

Na GDQ, o próton é o sóliton bariônico estável mínimo com três estômatos. Ele
é a primeira configuração material estacionária capaz de armazenar densidade
de energia de forma estável sem colapso singular.

Assim, a densidade UV física do vácuo não é a soma plana de modos de ponto zero
da TQC. Ela é a densidade máxima de tensão que o meio geométrico suporta antes
de reorganizar-se como matéria bariônica estável:

$$
\rho_{\rm UV}
=
\frac{M_p c^2}{V_p},
\qquad
V_p=\frac{4\pi}{3}r_p^3.
$$

Com o raio protonico vigente do projeto,

$$
r_p=0{,}840778765450\,{\rm fm},
$$

essa escala é:

$$
\rho_{\rm UV}
\simeq
6{,}04\times10^{34}\,{\rm J/m^3}.
$$

Status: redução física GDQ. A escolha do raio protonico é herdada da Q30/Q40.

## 5. Por que a diluição é linear?

A diluição linear vem da medida ponderada de Perelman no colar global. O ponto
central é que a densidade efetiva não se propaga como uma densidade volumétrica
plana \(1/R^3\). Ela é transportada como tensão radial/holográfica filtrada
pelo dilatão:

$$
f(r)\sim \ln\left(\frac{r}{r_p}\right),
\qquad
e^{-f(r)}
=
\frac{r_p}{r}.
$$

Ao integrar no volume radial:

$$
\int_{r_p}^{R_H} e^{-f(r)}r^2\,dr
=
\int_{r_p}^{R_H}\frac{r_p}{r}r^2\,dr
=
\frac{r_p}{2}\left(R_H^2-r_p^2\right).
$$

Dividindo pelo volume cosmológico \(R_H^3\), no limite \(R_H\gg r_p\):

$$
\rho_{\rm diluida}
\propto
\frac{r_p R_H^2}{R_H^3}
=
\frac{r_p}{R_H}.
$$

Portanto a lei linear não é uma escolha dimensional solta; ela nasce do perfil
logarítmico da medida/dilatão no transporte global.

Status: derivação estrutural condicionada ao perfil assintótico
\(f(r)\sim\ln(r/r_p)\) no colar cosmológico.

## 6. Por que há 28 modos multiplicativos?

O fator 28 é a contagem dos canais antissimétricos de torção/cisalhamento no
espaço real efetivo de dimensão 8:

$$
N_{\rm Cartan}
=
\dim\Lambda^2(\mathbb R^8)
=
\binom{8}{2}
=
\frac{8\cdot7}{2}
=
28.
$$

Fisicamente, esses são os canais independentes pelos quais a tensão
antis-simétrica de Cartan--Bismut pode distribuir a resposta elástica do vácuo
no espaço de fase geométrico.

Status: contagem geométrica exata. O uso multiplicativo cosmológico assume
equipartição/isotropia do background global.

## 7. Por que a projeção é \(\alpha^2\)?

A densidade \(\rho_{\rm eff}\) ainda pertence ao setor geométrico complexo
completo. A gravidade macroscópica mede apenas a projeção real efetiva do canal
que acopla ao tensor métrico observável.

Pela Q37, a constante \(\alpha\) é a normalização geométrica do canal
eletromagnético primitivo herdado do ensemble de Einstein. Um acoplamento
gravitacional de densidade é quadrático na amplitude projetada do canal real;
logo:

$$
\rho_{\rm grav}
=
\alpha^2\rho_{\rm eff}.
$$

Isso não significa importar QED como fundamento. Significa usar a
normalização GDQ do canal \(U(1)_Q\), já transportada pela ponte global--local,
para projetar a tensão complexa no observável real.

Status: condicional à Q37 e à ponte global--local.

## 8. Equação de estado

Na sela homogênea e estacionária, a contribuição de energia escura tem tensor
efetivo:

$$
T_{\mu\nu}^{(\Lambda)}
=
-\rho_\Lambda c^2\,g_{\mu\nu}.
$$

Comparando com o fluido perfeito:

$$
T_{\mu\nu}
=
(\rho c^2+p)u_\mu u_\nu+p g_{\mu\nu},
$$

obtém-se:

$$
p_\Lambda=-\rho_\Lambda c^2,
\qquad
w=\frac{p_\Lambda}{\rho_\Lambda c^2}=-1.
$$

A equação de continuidade FLRW confirma:

$$
\dot\rho_\Lambda+3H(1+w)\rho_\Lambda=0.
$$

Se \(w=-1\), então:

$$
\dot\rho_\Lambda=0.
$$

Portanto a resposta da Q56 é:

$$
\boxed{
w=-1
\text{ no background estacionário homogêneo.}
}
$$

Correções \(w\neq -1\) só aparecem se forem incluídos modos elásticos
dinâmicos, anisotropias, dissipação ou variação lenta do contorno cosmológico.

## 9. Perturbações cosmológicas

No limite exatamente \(\Lambda\), a energia escura não possui perturbação
propagante própria:

$$
\delta\rho_\Lambda=0,
\qquad
\delta p_\Lambda=-c^2\delta\rho_\Lambda=0.
$$

Na GDQ, entretanto, a energia escura é uma tensão elástica de background. As
perturbações admissíveis não são “partículas de energia escura”; são modos da
Hessiana física em torno da sela cosmológica:

$$
\left[
\partial_t^2
+3H\partial_t
+c_s^2\frac{k^2}{a^2}
+m_{\rm gap}^2
\right]\delta\Phi_k
=
J_k^{\rm matter}.
$$

Se a Hessiana cosmológica possui gap positivo,

$$
m_{\rm gap}^2>0,
$$

então os modos livres decaem ou ficam suprimidos em grandes escalas. A matéria
bariônica pode gerar resposta elástica pequena via fonte \(J_k^{\rm matter}\),
mas essa resposta não equivale a um fluido frio que aglomera como matéria
escura.

Status: fechado estruturalmente. A evolução quantitativa exige resolver a
Hessiana cosmológica no background global específico.

## 10. Avaliação numérica

O script auditável está em:

- `questoes/q56/associados/calcular_rho_lambda_q56.py`

Ele avalia:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2\,
28\,
\frac{M_pc^2}{(4\pi/3)r_p^3}
\frac{r_p}{R_H}
\frac1{c^2}.
$$

Com \(H_0=67{,}4\,{\rm km/s/Mpc}\), \(R_H=c/H_0\),
\(\Omega_\Lambda=0{,}6847\) e o raio protonico vigente, o cálculo retorna:

$$
\rho_\Lambda^{\rm GDQ}
\simeq
6{,}14\times10^{-27}\,{\rm kg/m^3}.
$$

Comparado com a densidade inferida do mesmo par \((H_0,\Omega_\Lambda)\):

$$
\rho_\Lambda^{\rm obs}
\simeq
5{,}84\times10^{-27}\,{\rm kg/m^3},
$$

o erro relativo é aproximadamente:

$$
\frac{\rho_\Lambda^{\rm GDQ}-\rho_\Lambda^{\rm obs}}
{\rho_\Lambda^{\rm obs}}
\simeq
5{,}0\%.
$$

Essa diferença não deve ser escondida: ela mede a sensibilidade do resultado ao
contorno cosmológico e à escolha operacional do raio/projeção. Usando os
valores legados de \(R_H\), \(R_{\max}\) e \(r_p\), o próprio manuscrito antigo
obtinha erro menor. A formulação correta deve declarar que o número final é
condicionado ao conjunto cosmológico usado.

## 11. Respostas diretas às seis perguntas

1. A densidade do próton define a densidade UV porque o próton é o sóliton
   bariônico estável mínimo e fixa a tensão máxima materializada do vácuo.
2. A diluição é linear porque o dilatão assintótico \(f\sim\ln(r/r_p)\) dá
   peso \(e^{-f}=r_p/r\), e a integração radial dividida pelo volume deixa
   \(r_p/R_H\).
3. Há 28 modos porque a torção/cisalhamento antissimétrico em 8 dimensões tem
   \(\binom82=28\) componentes independentes.
4. A projeção é \(\alpha^2\) porque o observável gravitacional real é quadrático
   na amplitude do canal \(U(1)_Q\) normalizado pela Q37.
5. A equação de estado é \(w=-1\) na sela homogênea estacionária.
6. Perturbações evoluem como modos da Hessiana cosmológica; com gap positivo,
   são suprimidas/decadentes, com resposta forçada pequena à matéria.

## 12. Limitações que permanecem

As limitações abaixo não reabrem a estrutura da Q56, mas impedem chamar a
estimativa de predição metrológica absoluta:

1. \(R_H\) é dado de contorno cosmológico.
2. A equipartição dos 28 modos requer background global isotrópico.
3. A projeção \(\alpha^2\) depende da Q37 e da ponte global--local.
4. A evolução perturbativa quantitativa exige a Hessiana cosmológica completa.
5. A comparação experimental depende da escolha de \(H_0\) e
   \(\Omega_\Lambda\).

## 13. Status final

$$
\boxed{
\text{Q56 fechada estruturalmente; metrologia fina condicionada ao contorno cosmológico.}
}
$$

## 14. Onde estamos

A Q56 não está sendo fechada como simulação cosmológica completa. Ela está
sendo fechada como resposta estrutural ao problema da escala da energia escura.

O resultado obtido é:

$$
\rho_\Lambda^{\rm GDQ}
=
\alpha^2
N_{\rm Cartan}
\rho_{\rm UV}^{p}
\frac{r_p}{R_H}
\frac1{c^2},
\qquad
N_{\rm Cartan}=28.
$$

Essa expressão responde por que a escala observada é pequena sem recorrer à
soma plana de energias de ponto zero:

1. a escala UV física é a tensão do sóliton protonico estável;
2. o transporte global--local dilui essa tensão linearmente por \(r_p/R_H\);
3. a torção/cisalhamento 8D fornece 28 canais independentes;
4. a gravidade real observa a projeção quadrática \(\alpha^2\);
5. a sela homogênea estacionária tem \(w=-1\);
6. perturbações são modos da Hessiana cosmológica, não partículas livres de
   energia escura.

Portanto, a GDQ fornece uma cadeia explicativa para a escala de
\(\rho_\Lambda\). Isso é mais forte do que inserir uma constante cosmológica
livre, mas ainda é mais fraco do que um ajuste cosmológico completo contra CMB,
BAO, supernovas e crescimento de estrutura.

## 15. O que não está sendo reivindicado

Para evitar confusão:

1. não foi calculado todo o histórico cosmológico do universo;
2. não foi executado ajuste de CMB/BAO/SNe;
3. não foi derivado \(H_0\) do nada;
4. não foi provada numericamente a Hessiana cosmológica completa;
5. não foi usado o erro de poucos por cento como prova final.

O ponto correto é: dado o contorno cosmológico macroscópico, a GDQ produz a
escala correta da energia escura por uma cadeia geométrica curta e auditável.

## 16. Plano de extensão

O programa natural de extensão é:

### 16.1 Fixar o contorno cosmológico GDQ

Comparar três escolhas de fronteira:

1. horizonte de Hubble:

   $$
   R_H=\frac{c}{H_0};
   $$

2. horizonte de partículas \(R_{\rm part}\);
3. horizonte de de Sitter:

   $$
   R_{\rm dS}=\sqrt{\frac{3}{\Lambda}}.
   $$

O objetivo é decidir qual desses raios é o contorno variacional correto da ação
GDQ no setor de energia escura.

### 16.2 Derivar o perfil global \(f(r)\)

Elevar a hipótese assintótica:

$$
f(r)\sim\ln\left(\frac{r}{r_p}\right)
$$

a uma solução de sela do setor cosmológico da ação oficial, com condições de
bordo em \(r_p\) e no horizonte cosmológico.

### 16.3 Auditar a equipartição dos 28 modos

Provar quando:

$$
\rho_{\rm eff}
=
28\,\rho_{\rm canal}
$$

é válido. Em background isotrópico, isso é natural; em background anisotrópico,
o fator deve ser substituído por um traço espectral:

$$
28
\longrightarrow
\operatorname{Tr}_{\Lambda^2(\mathbb R^8)} P_{\rm cos}.
$$

### 16.4 Derivar a projeção \(\alpha^2\) como corolário explícito

Escrever a ponte:

$$
\text{Q37}
\to
\alpha_{\rm Einstein}
\to
\alpha_{\rm lab}
\to
\rho_{\rm grav}=\alpha^2\rho_{\rm eff}
$$

sem deixar a projeção apenas como referência cruzada.

### 16.5 Construir a Hessiana cosmológica

Montar:

$$
K_{\rm cos}^{\rm phys}
=
P^{\rm phys}
\operatorname{Hess}_{\Phi_{\rm cos}}
\mathcal S_{\rm GDQ}
P^{\rm phys}.
$$

Com isso, obter:

1. gap cosmológico \(m_{\rm gap}^2\);
2. velocidade efetiva \(c_s^2\);
3. resposta a fontes bariônicas \(J_k^{\rm matter}\);
4. evolução linear de perturbações.

### 16.6 Comparação observacional posterior

Depois da Hessiana:

1. calcular \(H(z)\);
2. calcular distância luminosidade \(D_L(z)\);
3. comparar com supernovas;
4. calcular escala BAO;
5. calcular crescimento \(f\sigma_8\);
6. estudar assinatura em CMB apenas como etapa final.

## 17. Fechamento operacional

Com este documento, a Q56 fica encerrada no nível apropriado:

$$
\boxed{
\text{resposta estrutural completa às perguntas obrigatórias}
}
$$

e a continuação passa a ser:

$$
\boxed{
\text{programa cosmológico metrológico da GDQ.}
}
$$
