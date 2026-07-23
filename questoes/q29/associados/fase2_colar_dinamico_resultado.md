# Q29 — Fase 2 do colar dinâmico: background, estabilidade e fóton

## 1. Objetivo

Esta fase usa a redução radial derivada em
`fase1_colar_dinamico_reducao_radial.md` para responder três perguntas:

1. os dados de interface já derivados selecionam um background não-produto?
2. esse background remove o modo Berger negativo?
3. o modo eletromagnético possui norma radial finita?

Nenhum coeficiente é calibrado por $\alpha$.

## 2. Auditoria da interface disponível

A interface de Hopf já derivada fornece, no setor de calibre,

$$
\mathsf B
=\frac14
\begin{pmatrix}
1&0&0&0\\
0&1&0&0\\
0&0&1&-1\\
0&0&-1&1
\end{pmatrix}.
$$

Ela determina o canal eletromagnético nulo e os canais massivos, mas não é a
Hessiana da interface no setor métrico--dilatônico $(a,c,f)$. Portanto, não é
lícito reutilizar seus autovalores como coeficientes Robin de $a,c,f$.

O único termo métrico de bordo atualmente derivado é a completação ponderada
por curvatura extrínseca. Depois de combinada com o bulk, ela cancela as
derivadas normais da curvatura e deixa, para uma extremidade livre sem outra
ação de interface,

$$
\Pi_a=\Pi_c=\Pi_f=0.
$$

## 3. Consequência das condições naturais

Na gauge $N=1$,

$$
\Pi_a=4\tau e^{-f}(ca'+ac'-acf'),
$$

$$
\Pi_c=2\tau e^{-f}a(2a'-af'),
$$

$$
\Pi_f=2\tau e^{-f}a(acf'-ac'-2ca').
$$

Para $a,c>0$, o sistema $\Pi_A=0$ implica sucessivamente

$$
f'=2\frac{a'}a,
$$

$$
\frac{c'}c=\frac{a'}a,
$$

e

$$
a'=0.
$$

Logo,

$$
\boxed{a'=c'=f'=0}
$$

na extremidade natural. Se as mesmas condições forem usadas para fechar todo
o colar sem uma fonte métrico--dilatônica adicional, o ramo estacionário
selecionado é o cilindro homogêneo, não um colar dinâmico localizado.

## 4. Ramo cilíndrico isotrópico

Considere

$$
a=c=R,
\qquad f=f_0,
\qquad h=\text{constante}.
$$

As equações radiais e a restrição reduzem a

$$
\boxed{h^2=4R^4}
$$

e

$$
\boxed{f_0-n-\lambda=-\frac{4\tau}{R^2}.}
$$

Assim, a torção pode sustentar o raio homogêneo, mas os dados disponíveis não
geram uma transição radial de squashing.

## 5. Estabilidade

O ramo encontrado coincide com a classe cilíndrica já auditada. Nela, a
Hessiana de interface métrica é

$$
H_q^{\partial}=0,
$$

enquanto o modo homogêneo de Berger possui

$$
H_q^{\mathrm{bulk,eff}}=-2{,}67090856.
$$

Portanto,

$$
\boxed{H_q^{\mathrm{total}}=-2{,}67090856<0.}
$$

A projeção pela restrição radial não remove esse modo: ele é precisamente uma
variação anisotrópica física a volume/fluxo vinculados já testada no setor
Berger. Logo, o background disponível não é um mínimo físico adequado para
predizer a normalização absoluta.

## 6. Localização eletromagnética

No canal do fóton, a matriz de interface possui autovalor zero. No cilindro
homogêneo, o modo radial fundamental é constante. Sua norma contém

$$
\|\Psi_\gamma\|^2
\propto
\int_{r_c}^{r_\infty}
e^{-f_0}R^3\|\xi_Q\|^2\,dr.
$$

O integrando é constante e positivo. Em um colar não compacto,

$$
\boxed{\|\Psi_\gamma\|^2=\infty.}
$$

Consequentemente,

$$
e^2\longrightarrow0
$$

na interpretação de redução dimensional: o modo não está localizado. Em um
colar compacto de comprimento $L$, a norma é finita mas proporcional a $L$;
então $\alpha$ depende do tamanho global e do coeficiente dimensional $Z_C$,
que não foram determinados por esta solução local.

## 7. Comparação com o antigo background warped

O solver anterior em $(A,F)$ sobre $[\epsilon,\pi]$ é um problema cosmológico
compacto distinto e fornece um background warped regularizado. Ele permanece
válido dentro de seu ansatz, mas não resolve a nova Hessiana anisotrópica
$(a,c,f)$ e não pode ser usado como prova de estabilização Berger. Misturar os
dois problemas esconderia justamente a condição de colagem que está ausente.

## 8. Veredito da Fase 2

Com todos os termos atualmente derivados da ação oficial:

$$
\boxed{
\begin{array}{l}
\text{background não-produto selecionado: não;}\\
\text{estabilidade Berger: não;}\\
\text{fóton localizado no colar infinito: não;}\\
\text{previsão absoluta de }\alpha\text{: não.}
\end{array}}
$$

Este é um fechamento negativo, não uma interrupção do cálculo. A Fase 2
identificou exatamente o elemento matemático ausente:

$$
\boxed{
I_{\mathrm{int}}^{(a,c,f)}
\quad\text{ou, equivalentemente, uma colagem global que determine}
\quad
\frac{\partial I_{\mathrm{int}}}{\partial(a,c,f)}.
}
$$

Sem esse pullback, não existe condição Robin métrica capaz de selecionar um
colar não-produto. Introduzi-la por escolha numérica seria acrescentar uma
nova hipótese constitutiva.

## 9. Status científico da Q29 após as duas fases

Permanecem estabelecidos o modo eletrofraco, a quebra quadrática, a estrutura
de massa e o canal eletromagnético nulo. Permanecem abertos:

1. a estabilidade anisotrópica do background completo;
2. a localização espectral do fóton;
3. a normalização dimensional global;
4. a previsão absoluta de $\alpha$.

O próximo avanço não é outro ajuste numérico. É derivar a ação de colagem
métrico--dilatônica do estômato a partir da solução global da GDQ.
