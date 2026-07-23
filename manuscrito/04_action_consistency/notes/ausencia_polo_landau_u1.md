---
title: "Ausência de polo de Landau no setor U(1) efetivo"
status: "fechamento estrutural condicional"
---

# Ausência de polo de Landau no setor $U(1)$ efetivo

## Enunciado

O polo de Landau aparece quando a teoria pontual de QED é extrapolada para
energias arbitrariamente altas. Na GDQ, a pergunta correta não é qual
contratermo remove o polo, pois a teoria não usa renormalização fundamental
por contratermos. A pergunta correta é:

$$
\text{o semigrupo geométrico da Hessiana impede a extrapolação pontual que
geraria o polo?}
$$

O resultado desta nota é condicional ao setor $U(1)$ efetivo já construído
pela fase toroidal. Nesse setor, a resposta é sim: o traço de calor da
Hessiana física produz uma polarização finita e saturada para
$\tau_{\rm EM}>0$.

## Objeto fundamental

O propagador físico de resolução setorial não é um propagador pontual nu. Ele
é o operador de calor resolvido:

$$
G_\tau(L)=e^{-\tau L}L^{-1}.
$$

Aqui $L$ é o operador quadrático físico obtido da Hessiana da ação oficial
após escolha de domínio, contorno e projetor físico. Para $\tau>0$:

$$
\int d^4k\,\frac{e^{-\tau k^2}}{(k^2+m^2)^p}<\infty.
$$

Essa finitude não é uma renormalização externa. Ela vem do próprio operador
de resolução geométrica.

## Polarização abeliana

Para comparação operacional com QED, define-se a polarização transversal:

$$
\Pi_{\mu\nu}^{(\tau)}(q)
=
\left(
q_\mu q_\nu-q^2\delta_{\mu\nu}
\right)
\Pi_\tau(q^2).
$$

A transversidade é consequência da identidade de Ward geométrica demonstrada
na nota de loop toroidal:

$$
q^\mu\Pi_{\mu\nu}^{(\tau)}(q)=0.
$$

No setor $U(1)$ com uma espécie de massa $m$ e carga unitária, a função escalar
regularizada por heat-kernel é:

$$
\Pi_\tau(q_E^2)
=
\frac{2\alpha_0}{\pi}
\int_0^1
dx\,x(1-x)
\left[
E_1(\tau m^2)
-
E_1
\left(
\tau
\left[
m^2+x(1-x)q_E^2
\right]
\right)
\right].
$$

Ela satisfaz imediatamente:

$$
\Pi_\tau(0)=0.
$$

No regime $\tau q_E^2\ll1$, a diferença das exponenciais integrais recupera
o logaritmo usual:

$$
\Pi_\tau(q_E^2)
\longrightarrow
\frac{2\alpha_0}{\pi}
\int_0^1dx\,x(1-x)
\ln
\left(
1+\frac{x(1-x)q_E^2}{m^2}
\right).
$$

Para $q_E^2\gg m^2$, ainda abaixo da escala geométrica efetiva:

$$
\Pi_\tau(q_E^2)
\simeq
\frac{\alpha_0}{3\pi}
\ln\frac{q_E^2}{m^2}
+\text{constante finita}.
$$

Portanto a leitura de baixa energia reproduz o comportamento conhecido:

$$
\mathcal B_\alpha
\simeq
\frac{2}{3\pi}\alpha^2
$$

para uma espécie carregada unitária.

## Saturação ultravioleta

No ultravioleta geométrico, mantendo $\tau>0$:

$$
\lim_{q_E^2\to\infty}
E_1
\left(
\tau
\left[
m^2+x(1-x)q_E^2
\right]
\right)
=0.
$$

Como:

$$
\int_0^1x(1-x)\,dx=\frac16,
$$

segue:

$$
\Pi_\tau(\infty)
=
\frac{\alpha_0}{3\pi}E_1(\tau m^2).
$$

O acoplamento operacional é definido por resposta:

$$
\alpha_{\rm eff}(\mu)
=
\frac{\alpha_0}
{1-\Pi_\tau(\mu^2)}.
$$

Logo:

$$
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-\frac{\alpha_0}{3\pi}E_1(\tau m^2)}.
$$

O polo é evitado quando:

$$
\frac{\alpha_0}{3\pi}E_1(\tau m^2)<1.
$$

Essa é a condição matemática precisa do fechamento $U(1)$ de uma espécie.

## Múltiplas espécies

Com várias espécies carregadas, a saturação fica:

$$
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1
\left(
\frac{m_f^2}{\Lambda_{\rm EM}^2}
\right).
$$

Portanto:

$$
\alpha_{\rm eff}(\infty)
=
\frac{\alpha_0}
{1-
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1
\left(
\frac{m_f^2}{\Lambda_{\rm EM}^2}
\right)}
$$

e a condição sem polo é:

$$
\frac{\alpha_0}{3\pi}
\sum_fN_c^{(f)}Q_f^2
E_1
\left(
\frac{m_f^2}{\Lambda_{\rm EM}^2}
\right)<1.
$$

Essa expressão mostra um ponto físico importante: se uma espécie carregada
fosse exatamente sem massa no setor efetivo, $E_1(0)$ divergiria. A GDQ deve
então fornecer massa geométrica efetiva, limiar infravermelho, exclusão
topológica do zero ou tratamento térmico/cosmológico do vácuo. No setor
material usual, as espécies carregadas físicas têm limiares positivos.

## Fixação setorial de $\tau$

O parâmetro $\tau$ não é parâmetro livre de renormalização. Para cada setor
efetivo $s$:

$$
\tau_s=\Lambda_s^{-2}.
$$

No setor eletromagnético:

$$
\tau_{\rm EM}=\Lambda_{\rm EM}^{-2}.
$$

Logo:

$$
\Pi_{\rm EM}(\infty)
=
\frac{\alpha_0}{3\pi}
E_1
\left(
\frac{m^2}{\Lambda_{\rm EM}^2}
\right).
$$

O que precisa ser derivado em cada aplicação metrológica é
$\Lambda_{\rm EM}$ do operador, background e contorno. Isso não reabre a
ausência estrutural do polo; apenas determina onde a transição geométrica
ocorre em unidades físicas.

## Fechamento torsão--Reynolds

Uma rota macro--local para obter $\tau_{\rm EM}>0$ usa conservação torsional e
similaridade geométrica. Para:

$$
B=b\,\operatorname{vol}_{S^3(R)},
$$

a quantização global:

$$
\frac1{2\pi}\int_{S^3}B=n_B
$$

leva a:

$$
b=\frac{n_B}{\pi R^3},
\qquad
\frac1{12}|B|^2
=
\frac{n_B^2}{2\pi^2R^6}.
$$

No funcional radial:

$$
\mathcal W_n(R)
=
\tau
\left(
\frac6{R^2}
-
\frac{n_B^2}{2\pi^2R^6}
\right)
+3\log R,
$$

identificam-se as magnitudes:

$$
E_{\rm el}
=
\tau\frac6{R^2},
\qquad
E_{\rm tor}
=
\tau\frac{n_B^2}{2\pi^2R^6}.
$$

Define-se o número de similaridade:

$$
\operatorname{Re}_{\rm Q}
:=
\frac{E_{\rm tor}}{E_{\rm el}}
=
\frac{n_B^2}{12\pi^2R^4}.
$$

O fechamento constitutivo da ponte macro--local é:

$$
\operatorname{Re}_{\rm Q}=\alpha.
$$

Então:

$$
R^4=\frac{n_B^2}{12\pi^2\alpha},
$$

ou:

$$
R^2
=
\frac{|n_B|}{\sqrt{12}\,\pi\sqrt\alpha}.
$$

A condição estacionária radial é:

$$
x^3-4\tau x^2+\frac{\tau n_B^2}{\pi^2}=0,
\qquad
x=R^2.
$$

Assim:

$$
\tau_{\rm EM}^{\rm dimless}
=
\frac{x^3}
{4x^2-n_B^2/\pi^2},
\qquad
x=\frac{|n_B|}{\sqrt{12}\,\pi\sqrt\alpha}.
$$

A solução é positiva para:

$$
\alpha<\frac13.
$$

A resolução relativa é:

$$
\widehat\Lambda_{\rm EM}
=
\left(
\tau_{\rm EM}^{\rm dimless}
\right)^{-1/2}.
$$

Para $\alpha_{\rm IR}=1/137$ e $n_B=1$:

$$
R=1{,}0370743523,
\qquad
\tau_{\rm EM}^{\rm dimless}=0{,}2749005225,
\qquad
\widehat\Lambda_{\rm EM}=1{,}9072701741.
$$

O valor experimental efetivo $\alpha^{-1}\simeq128$ em escalas eletrofracas
é tratado como benchmark de running externo, não como entrada fundamental
desse fechamento.

## No-go do colar cilíndrico local

O colar local infinito não pode sozinho fixar uma escala eletromagnética
positiva. Para o canal radial Neumann no intervalo de comprimento $L$:

$$
\lambda_0=0,
\qquad
\lambda_1=\frac{\pi^2}{L^2}.
$$

Quando $L\to\infty$:

$$
\lambda_1\to0.
$$

Logo a escala eletromagnética não vem de um colar cilíndrico local infinito.
Ela depende da colagem global, do comprimento efetivo ou da resolução
setorial herdada pelo background.

## Status

O resultado fechado é:

$$
\boxed{
\text{o polo de Landau não é singularidade fundamental da GDQ no setor }U(1)
\text{ efetivo}
}
$$

porque a polarização espectral satura para $\tau_{\rm EM}>0$.

Permanecem como refinamentos:

1. calcular $\Lambda_{\rm EM}$ em unidades físicas a partir da colagem global;
2. auditar a igualdade constitutiva $\operatorname{Re}_{\rm Q}=\alpha$ como
   princípio oficial da ponte macro--local;
3. estender o cálculo para setores não abelianos com a Hessiana completa de
   Bismut;
4. inserir backgrounds materiais reais para comparação metrológica.

