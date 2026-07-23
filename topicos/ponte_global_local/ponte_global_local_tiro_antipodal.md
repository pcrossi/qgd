# Tiro antipodal — primeiro diagnóstico

> **Veredito posterior:** o tiro direto até o antipolo não é uma formulação
> global válida. O colar de Berger é uma carta local em torno de $Y_0$ e não
> fornece coordenada radial global no produto
> $T^4\times S^1\times S^3$. As condições de equador abaixo foram úteis como
> diagnóstico, mas não podem substituir o DtN do exterior multidimensional.

## 1. Objetivo

Após a carga fixar $c_0$, a garganta geral possui três dados a determinar pela
colagem:

$$
a_0,
\qquad
p_{a,0},
\qquad
\tau.
$$

Para comprimento antipodal $L$ dado, a simetria no equador exige

$$
\dot a(L/2)=0,
\qquad
\dot c(L/2)=0,
\qquad
\dot u(L/2)=0.
$$

Portanto, o resíduo correto é tridimensional:

$$
\mathfrak R(a_0,p_{a,0},\tau)
=\bigl(\dot a,\dot c,\dot u\bigr)_{L/2}.
$$

## 2. Correção da hipótese de garganta redonda

A carga e a minimalidade dão

$$
h_0=-2c_0^2,
$$

mas não dão

$$
a_0=c_0.
$$

Essa igualdade era um ansatz redondo. O tiro uniparamétrico em $p_{a,0}$
consegue, em geral, anular apenas uma das três condições de simetria. Logo,
$a_0/c_0$ deve permanecer variável até a colagem.

Na garganta geral, a restrição do lapse fornece

$$
u_0
=4-\frac{8\tau}{a_0^2}
+\frac{4\tau c_0^2}{a_0^4}
+\frac{p_v^2e^{2u_0}}{4\tau a_0^4c_0^2}.
$$

Essa equação substitui a fórmula especializada da garganta redonda.

## 3. Controle numérico no setor sem harmônico angular

Foi realizado um teste exploratório adimensional com

$$
c_0=1,
\qquad
p_v=0,
\qquad
L/2=0.5.
$$

Uma busca limitada em $(a_0,p_{a,0},\tau)$ não encontrou zero interno. A
melhor solução atingiu a fronteira superior imposta a $\tau$ e manteve
resíduo não nulo. Esse resultado é classificado como **diagnóstico numérico
negativo do setor de teste**, não como teorema de inexistência.

Esse teste não representa o estômato físico completo, mas a razão não é
$p_v=0$. O momento $p_v$ mede o fluxo **radial** da fase. Num background
estacionário sem vazamento de probabilidade, espera-se justamente

$$
p_v=0.
$$

A circulação do defeito é angular. Como

$$
S_R=\hbar v,
$$

a condição

$$
\oint dS_R=2\pi\hbar m
$$

exige

$$
v(r,\Omega)=v_0(r)+m\psi,
\qquad m\in\mathbb Z,
$$

onde $\psi$ é a coordenada da fibra de Hopf. Na métrica de Berger,

$$
|dv|^2=(\dot v_0)^2+\kappa_\psi\frac{m^2}{c^2}.
$$

$\kappa_\psi$ é fixado pela periodicidade de $\psi$ e pela normalização das
formas de Maurer--Cartan; não é coeficiente fenomenológico.

## 4. Dados necessários para o tiro físico

O problema físico requer:

1. $c_0$ obtido da carga relativa e da normalização de
   $\mathcal V_\sigma$;
2. inteiro de circulação $m$ e normalização geométrica $\kappa_\psi$;
3. $L=\pi R_{\rm cos}$ como condição cosmológica de contorno;
4. orientação do par $(q,-q)$.

Esses dados devem ser inseridos antes da busca. Variar $p_v$ ou $L$ para
forçar o fechamento converteria o cálculo em ajuste e não será feito.

## 5. Resultado metodológico

O mapa de tiro correto foi determinado e possui o mesmo número de equações e
incógnitas. O teste também mostrou que:

1. a garganta redonda não pode ser imposta antes da solução;
2. o setor $m=0$ não deve ser confundido com o defeito circulante;
3. a escala cosmológica entra como dado de contorno, não como constante
   produzida pela variação local.

O controle anterior deve ser lido como teste do setor $m=0$, não do setor
elementar $m=1$.

## 6. Auditoria do tiro com $m=1$

Foi implementada uma busca em

$$
(a_0,p_{a,0},\tau)
$$

com o termo de Hopf $m=1$. As buscas multissemente não produziram uma raiz
interior robusta; soluções aproximadas empurraram $p_{a,0}$ ou $\tau$ às
fronteiras impostas.

Esse comportamento não será interpretado como inexistência da sela. A
condição usada exigia que o mesmo colar local alcançasse um equador antipodal
com

$$
(\dot a,\dot c,\dot u)=0.
$$

Mas $S^1\times S^3$ não é globalmente foliado pelas órbitas $S^3$ do ansatz
normal $\mathbb C^2$. Logo, a condição sobre-estende a carta local.

O resultado correto do teste é

$$
\boxed{
\text{o tiro antipodal direto pelo colar foi excluído como rota global.}
}
$$

A colagem legítima deve parar numa interface $Y$ dentro da validade do colar
e usar o DtN da Hessiana no exterior global completo.
