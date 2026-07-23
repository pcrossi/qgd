# Q37 — fórmula legada como média no universo de Einstein

## 1. Escopo

A fórmula legada

$$
\alpha_E
=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}
$$

não coincide com a rigidez DtN local redonda. Ela pode, contudo, receber uma
interpretação matemática coerente como **média cosmológica de Einstein**.

Essa interpretação não altera a ação oficial e não afirma que cada ponto do
bulk local tenha esse acoplamento. Ela define o número global herdado pela
carta laboratorial depois do transporte já demonstrado em Q37.

## 2. Domínio global e câmara fundamental

Considere o domínio cosmológico auxiliar

$$
K_E=T^5\times S^3
$$

com a medida estacionária de Einstein--Bismut

$$
d\mu_E=\mathcal U_E\,dV_E,
\qquad
\int_{K_E}d\mu_E=1.
$$

Escolha os cinco ângulos não orientados na câmara
$[0,\pi]^5$. Seu volume angular é

$$
\operatorname{Vol}_{\rm ang}(T^5_+)=\pi^5.
$$

As permutações assinadas pares formam

$$
W(D_5)\simeq(\mathbb Z_2)^4\rtimes S_5,
\qquad
|W(D_5)|=1920.
$$

Se o ensemble cosmológico soma igualmente as câmaras relacionadas por essa
simetria, o peso de uma câmara fundamental é

$$
\mathcal V_{\rm chamber}
=\frac{\pi^5}{|W(D_5)|}
=\frac{\pi^5}{1920}.
$$

Aqui $W(D_5)$ não é chamado de holonomia. Ele organiza a média discreta das
orientações globais do toro de Einstein.

## 3. Por que surge a raiz quarta

O laboratório observa quatro direções físicas. Seja
$\mathsf C_E$ o tensor positivo de complacência obtido pela média global da
Hessiana nas quatro direções transportadas. O escalar isotrópico associado a
esse tensor não é seu volume, mas sua média geométrica:

$$
C_E
=\left(\det\mathsf C_E\right)^{1/4}.
$$

No setor isotrópico, a média de Einstein distribui o peso da câmara igualmente
entre os quatro autovalores. Assim,

$$
\det\mathsf C_E=\mathcal V_{\rm chamber}
$$

e

$$
\boxed{
C_E
=\left(\frac{\pi^5}{1920}\right)^{1/4}.
}
$$

A raiz quarta deixa, portanto, de ser uma correção dimensional arbitrária:
ela é a média geométrica dos quatro autovalores físicos. Essa conclusão é
condicional à isotropia estatística da medida de Einstein e à identificação
do determinante da complacência com o peso da câmara fundamental.

## 4. Projetor isotrópico local

Para comparar a complacência global com a circulação elétrica observada,
projeta-se a resposta sobre os dois planos complexos da seção física. Defina
o projetor médio

$$
\mathcal P_{\rm iso}
=\frac{1}{\pi^4}
\left(\frac32\right)^2
\frac12
=\frac{9}{8\pi^4}.
$$

Os fatores têm papéis separados:

1. $\pi^{-4}$ normaliza a câmara angular dos quatro eixos físicos;
2. $(3/2)^2$ é o fator de conversão entre resposta longitudinal e resposta
   tangencial em cada um dos dois planos complexos isotrópicos;
3. $1/2$ evita contar duas vezes as orientações conjugadas da circulação.

Nesta leitura, $\mathcal P_{\rm iso}$ não é uma nova constante fundamental.
Ele é a definição do mapa de média entre o tensor cosmológico e o canal
elétrico escalar. Para elevá-lo a teorema da ação oficial, ainda seria preciso
calcular esse projetor diretamente pela contração da Hessiana global. Em
particular, a razão $3/2$ não deve ser apresentada isoladamente como lei
universal de todo background Hermitiano.

## 5. Fórmula média

A constante cosmológica média é então

$$
\boxed{
\alpha_E^{\rm mean}
=\mathcal P_{\rm iso}C_E
=\frac{9}{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}.
}
$$

Numericamente,

$$
\alpha_E^{\rm mean}
=0{,}007297348\ldots,
\qquad
(\alpha_E^{\rm mean})^{-1}
=137{,}036082448\ldots.
$$

O teorema de transporte do canal fotônico permite herdar essa média no
laboratório, se ela for a normalização global correta:

$$
\alpha_{\rm lab}=\alpha_E^{\rm mean}.
$$

## 6. Relação com o resultado DtN local

Não há contradição lógica entre

$$
(\alpha_E^{\rm mean})^{-1}=137{,}036082448\ldots
$$

e a aproximação local redonda

$$
(\alpha_{\rm DtN}^{\rm red})^{-1}=137{,}604601779\ldots.
$$

O primeiro número é uma média global sobre câmaras e orientações do universo
de Einstein. O segundo é a resposta de uma única interface redonda antes da
média cosmológica completa. O erro seria identificar os dois operadores.

A conexão entre eles deve ser escrita como uma média de operadores,

$$
\mathsf C_E
=\int_{K_E/W(D_5)}
\mathsf T_y^*\,
\mathsf C_{\rm DtN}(y)\,
\mathsf T_y,d\mu_E(y),
$$

onde $\mathsf T_y$ transporta cada resposta local para uma seção comum. Em
geral,

$$
\left(\det\langle\mathsf C_{\rm DtN}\rangle_E\right)^{1/4}
\ne
\langle K_{\partial}^{\rm red}\rangle_E.
$$

Assim, o valor global não precisa ser obtido corrigindo escalarmente uma única
4-bola.

## 7. Estatuto científico

A fórmula legada passa a ter o seguinte estatuto:

$$
\boxed{
\text{fórmula exata de uma prescrição geométrica de média cosmológica,}
}
$$

mas ainda

$$
\boxed{
\text{teorema condicional da GDQ, não avaliação direta concluída da Hessiana.}
}
$$

Para convertê-la em previsão derivada, faltam somente duas identidades:

1. provar que o ensemble físico usa a câmara de $W(D_5)$ com pesos uniformes;
2. obter $\mathcal P_{\rm iso}=9/(8\pi^4)$ pela contração da Hessiana global,
   em vez de adotá-lo como prescrição de projeção.

Essa classificação preserva simultaneamente o sentido geométrico forte da
fórmula, sua precisão fenomenológica e a distinção entre interpretação e
derivação.

## 8. Lema de uniformidade do ensemble

Seja $\Phi_a=(g_a,J_a,H_a,f_a,\mathcal U_a)$ o background associado à câmara
$\mathcal C_a$. A ação de $\gamma\in W(D_5)$ é definida por pullback:

$$
\Phi_{\gamma a}=\gamma^*\Phi_a,
\qquad
\mathcal C_{\gamma a}=\gamma\mathcal C_a.
$$

Não se exige que uma câmara axialmente selecionada seja fixa por todo o grupo.
Exige-se que o ensemble contenha sua órbita completa. Como a ação oficial é
covariante por pullback e o contorno cosmológico é transportado junto,

$$
\mathcal S_{\rm GDQ}[\Phi_{\gamma a}]
=\mathcal S_{\rm GDQ}[\Phi_a].
$$

Para as simetrias contínuas conectadas à identidade, a identidade de Noether
fornece

$$
dJ_\xi=0,
$$

logo os fluxos que rotulam a órbita não mudam durante a evolução. A parte
discreta não produz nova corrente de Noether; ela preserva diretamente a rede
de fluxos:

$$
Q\longmapsto M_\gamma Q,
\qquad
M_\gamma^TG_EM_\gamma=G_E.
$$

Assim, a ação euclidiana on shell e a energia livre são constantes na órbita:

$$
F_{\gamma a}=F_a.
$$

Se a ação de $W(D_5)$ nas câmaras é transitiva, a função de partição é

$$
Z_E(\beta_E)
=\sum_{a=1}^{1920}e^{-\beta_EF_a}
=1920e^{-\beta_EF_0}.
$$

Portanto

$$
\boxed{
p_a
=\frac{e^{-\beta_EF_a}}{Z_E}
=\frac1{1920}.
}
$$

A temperatura cancela porque a degenerescência é exata. Ela só modifica os
pesos se o background ou o contorno quebrarem $W(D_5)$.

### 8.1 Forma equivalente no quociente

Se as câmaras são descrições equivalentes, e não setores físicos distintos,
a mesma conclusão é obtida sem soma térmica. Para qualquer observável
invariante $\mathcal O$,

$$
\int_{T^5}\mathcal O\,d\mu_E
=\sum_{\gamma\in W(D_5)}
\int_{\gamma\mathcal C}\mathcal O\,d\mu_E
=1920
\int_{\mathcal C}\mathcal O\,d\mu_E.
$$

Logo

$$
\boxed{
\int_{\mathcal C}\mathcal O\,d\mu_E
=\frac1{1920}
\int_{T^5}\mathcal O\,d\mu_E.
}
$$

O fator uniforme está, portanto, demonstrado sob três hipóteses explícitas:

1. covariância da ação e do contorno sob o pullback;
2. inclusão da órbita completa no ensemble;
3. transitividade da ação nas 1920 câmaras.

Essas hipóteses são precisamente a formulação matemática da isotropia global
do universo de Einstein. Com elas, a primeira das duas identidades pendentes
da seção 7 fica fechada. O projetor é tratado na seção seguinte e, no loop
final registrado em `fechamento_alpha_hessiana_loop.md`, foi reinterpretado
como contração da Hessiana média/corrente simplética no setor axial coerente.

## 9. Contração isotrópica do projetor

Na seção física real de dimensão quatro, um vetor unitário $n\in S^3$ com
medida de Haar normalizada satisfaz

$$
\langle n_i n_j n_k n_l\rangle
=\frac{
\delta_{ij}\delta_{kl}
+\delta_{ik}\delta_{jl}
+\delta_{il}\delta_{jk}
}{4(4+2)}.
$$

Para qualquer eixo unitário $u$,

$$
\left\langle(n\cdot u)^4\right\rangle
=\frac{3}{4\cdot6}
=\frac18.
$$

Esse é o coeficiente da projeção do tensor isotrópico de quarta ordem que
contrai a resposta quadrática sobre um canal axial. No elo $S^3$, a forma de
Cartan--Schouten possui três direções
ortonormais. Para o autovetor Hopf axial coerente, as três amplitudes são
somadas antes da norma:

$$
\operatorname{tr}_{S^3}\mathsf H_Q=3H_Q,
\qquad
\left|\operatorname{tr}_{S^3}\mathsf H_Q\right|^2=9|H_Q|^2.
$$

Portanto a contração tensorial é

$$
\mathcal P_{\rm tensor}
=3^2\left\langle(n\cdot u)^4\right\rangle
=\frac98.
$$

A câmara angular das quatro direções físicas tem volume $\pi^4$. Depois da
normalização,

$$
\boxed{
\mathcal P_{\rm iso}
=\frac{\mathcal P_{\rm tensor}}{\pi^4}
=\frac9{8\pi^4}.
}
$$

Nenhum valor de $\alpha$ foi usado. A derivação depende da medida isotrópica
de Haar, das três direções Cartan--Schouten e da coerência do autovetor axial.
Se as componentes fossem incoerentes, as normas seriam somadas e o fator $9$
seria substituído por $3$. No ansatz Hopf coerente vigente, a condição é
satisfeita por construção.

## 10. Fechamento da fórmula média

Com o lema de uniformidade e a contração isotrópica,

$$
\boxed{
\alpha_E^{\rm mean}
=\frac9{8\pi^4}
\left(\frac{\pi^5}{1920}\right)^{1/4}.
}
$$

A fórmula está **fechada condicionalmente** para o ensemble isotrópico de
Einstein e o autovetor Hopf axial coerente. Ela continua sendo uma média
global, não a rigidez de uma única interface redonda.
