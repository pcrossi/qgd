# Q35 — Auditoria espectral de $\Lambda_{\rm EM}$

## 1. Enunciado

Pretende-se determinar a escala setorial

$$
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}
$$

sem identificá-la por convenção com $\Lambda_C$, com a massa do elétron ou
com a escala eletrofraca.

O domínio físico é o setor eletromagnético não quebrado obtido depois da
diagonalização generalizada $W^3$--$Y$. A entrada disponível é a Hessiana
física da ação oficial projetada no complemento de gauge.

## 2. O modo fotônico não fixa a escala

A diagonalização neutra já forneceu

$$
m_\gamma^2=0,
\qquad
v_\gamma\propto(1,1),
\qquad
Q=T_3+Y.
$$

Esse resultado identifica corretamente o gerador não quebrado. Contudo, o
autovalor zero é protegido por gauge e não define uma resolução ultravioleta:

$$
\boxed{
\Lambda_{\rm EM}\ne m_\gamma=0.
}
$$

Usar o kernel como corte destruiria precisamente a separação entre massa
física, gap interno e escala do semigrupo.

## 3. Definição espectral correta

Seja $\mathcal H_{\rm EM}^{\rm phys}$ o espaço de perturbações
eletromagnéticas após vínculos e quociente de gauge. Seja

$$
L_{\rm EM}^{(2)}
=
P_{\rm phys}\,
\operatorname{Hess}\mathcal S_{\rm GDQ}\,
P_{\rm phys}
$$

com domínio auto-adjunto $\mathcal D_{\rm EM}$ e condições de interface
derivadas da colagem. O kernel fotônico é separado por

$$
P_\gamma
=
\frac{|v_\gamma\rangle\langle v_\gamma|_K}
{\langle v_\gamma,v_\gamma\rangle_K},
\qquad
P_\perp=1-P_\gamma.
$$

A candidata espectral mínima é

$$
\lambda_{1,{\rm EM}}^+
=
\inf\operatorname{spec}
\left(
P_\perp L_{\rm EM}^{(2)}P_\perp
\big|_{\mathcal D_{\rm EM}}
\right)>0.
$$

Se o operador estiver escrito em unidades de um comprimento interno
$\ell_{\rm int}$, então

$$
\boxed{
\Lambda_{\rm EM}
=
\frac{\sqrt{\lambda_{1,{\rm EM}}^+}}{\ell_{\rm int}},
\qquad
\tau_{\rm EM}
=
\frac{\ell_{\rm int}^2}{\lambda_{1,{\rm EM}}^+}.
}
$$

Essa definição distingue:

1. o fóton sem massa, pertencente ao kernel;
2. o primeiro modo interno positivo;
3. a escala geométrica que converte o espectro adimensional;
4. as massas externas observadas.

## 4. O que existe no corpus

A matriz neutra reduzida fornece o kernel fotônico e um modo positivo,

$$
m_Z^2=0{,}0378326150
$$

na escala comum omitida. Ela não basta para calcular
$\lambda_{1,{\rm EM}}^+$ porque:

1. é uma truncagem radial do setor neutro, não o operador Hermitiano completo;
2. a Hessiana de Berger do background usado possui direção negativa;
3. o colar produto não localiza o modo fotônico;
4. o pullback métrico--dilatônico da interface global não foi derivado;
5. a escala comum foi calibrada por $W/Z$, não obtida autonomamente do setor
   eletromagnético.

Portanto, o dado atualmente ausente não é um número para inserir no solver,
mas o triplo

$$
\boxed{
\left(
L_{\rm EM}^{(2)},\,
\mathcal D_{\rm EM},\,
\ell_{\rm int}
\right)
}
$$

no background estável completo.

## 5. Auditoria da escala eletrofraca existente

O corpus contém

$$
\Lambda_0^{\rm EW}=126354{,}3162\ {\rm GeV}.
$$

Esse valor foi obtido calibrando autovalores adimensionais pelos canais
$W/Z$. Logo, a identificação

$$
\Lambda_{\rm EM}=\Lambda_0^{\rm EW}
$$

é uma hipótese de universalidade setorial, não uma derivação.

Usando $m_e$ apenas como unidade metrológica,

$$
\log_{10}\left(\frac{\Lambda_0^{\rm EW}}{m_e}\right)
=8{,}393170074.
$$

Na fórmula multiespécie já auditada, essa hipótese produz

$$
\Pi_{\rm EM}(\infty)=0{,}0675577855
$$

para os três léptons da Q39, e

$$
\Pi_{\rm EM}(\infty)=0{,}1610754352
$$

para o benchmark externo de todos os férmions carregados. Ambos satisfazem
$\Pi_{\rm EM}<1$, mas isso apenas demonstra compatibilidade com a condição
sem polo. Não demonstra
$\Lambda_{\rm EM}=\Lambda_0^{\rm EW}$.

## 6. Resultado

$$
\boxed{
\text{a escala eletrofraca existente passa no teste sem polo, mas não deriva }
\Lambda_{\rm EM}.
}
$$

O próximo cálculo legítimo é construir o operador eletromagnético completo no
background estável e calcular seu primeiro autovalor positivo depois de
remover kernel e gauge. Enquanto isso não for feito, qualquer valor numérico
de $\Lambda_{\rm EM}$ é hipótese setorial ou calibração.

## 7. Classificação

- definição de $\lambda_{1,{\rm EM}}^+$: **derivação estrutural**;
- teste de $\Lambda_0^{\rm EW}$: **teste de consistência condicional**;
- massas de quarks do benchmark: **dados externos dependentes de esquema**;
- determinação de $\Lambda_{\rm EM}$: **aberta**, por falta do operador,
  domínio e escala interna completos.
