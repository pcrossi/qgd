# Q35 — Fechamento por conservação torsional e número de Reynolds geométrico

## 1. Enunciado

Pretende-se ligar a resolução local do heat kernel à estrutura global sem
exigir que um infinitésimo da fibra determine sozinho uma escala absoluta.

As hipóteses são:

1. conservação local da torção, $dB=0$;
2. quantização global do fluxo, $(2\pi)^{-1}\int_{S^3}B=n_B$;
3. equilíbrio radial da ação torsional reduzida;
4. definição constitutiva de $\alpha$ como razão de similaridade entre a
   deformação torsional e a rigidez elástica de curvatura;
5. calibração metrológica separada para converter a escala adimensional em
   unidades físicas.

## 2. Conservação e quantização

Para

$$
B=b\,\operatorname{vol}_{S^3(R)},
$$

a quantização fornece

$$
b=\frac{n_B}{\pi R^3},
\qquad
\frac1{12}|B|^2
=
\frac{n_B^2}{2\pi^2R^6}.
$$

A conservação local impede que o coeficiente de fluxo varie livremente no
colar. A densidade muda apenas pela geometria.

## 3. As duas energias do número de similaridade

No funcional radial já consolidado,

$$
\mathcal W_n(R)
=
\tau
\left(
\frac6{R^2}
-\frac{n_B^2}{2\pi^2R^6}
\right)
+3\log R,
$$

identificam-se as magnitudes

$$
E_{\rm el}
=
\tau\frac6{R^2},
\qquad
E_{\rm tor}
=
\tau\frac{n_B^2}{2\pi^2R^6}.
$$

A definição precisa do Reynolds geométrico é

$$
\boxed{
\operatorname{Re}_{\rm Q}
:=
\frac{E_{\rm tor}}{E_{\rm el}}
=
\frac{n_B^2}{12\pi^2R^4}.
}
$$

O postulado constitutivo que traduz o significado físico de estrutura fina é

$$
\boxed{
\operatorname{Re}_{\rm Q}=\alpha.
}
$$

Essa igualdade é mais forte que uma analogia verbal. Ela deve ser tratada
como definição constitutiva da ponte macro--local e auditada contra a ação.

## 4. Raio fixado por $\alpha$

Da igualdade anterior,

$$
R^4=\frac{n_B^2}{12\pi^2\alpha},
$$

portanto

$$
\boxed{
R^2
=
\frac{|n_B|}{\sqrt{12}\,\pi\sqrt\alpha}.
}
$$

Assim, $\alpha$ liga a carga torsional global quantizada à resposta elástica
local e remove a liberdade adimensional do raio.

## 5. Resolução do fluxo

A condição estacionária já derivada é

$$
x^3-4\tau x^2+\frac{\tau n_B^2}{\pi^2}=0,
\qquad
x=R^2.
$$

Logo,

$$
\boxed{
\tau_{\rm EM}^{\rm dimless}
=
\frac{x^3}
{4x^2-n_B^2/\pi^2},
\qquad
x=\frac{|n_B|}{\sqrt{12}\,\pi\sqrt\alpha}.
}
$$

Existe solução positiva quando

$$
\boxed{\alpha<\frac13.}
$$

A escala de resolução relativa fica

$$
\boxed{
\widehat\Lambda_{\rm EM}
=
\left(\tau_{\rm EM}^{\rm dimless}\right)^{-1/2}.
}
$$

## 6. Ponte macro--local

A cadeia resultante é

$$
\boxed{
\begin{aligned}
dB=0
&\longrightarrow \text{fluxo local conservado},\\
n_B\in\mathbb Z
&\longrightarrow \text{carga global},\\
\operatorname{Re}_{\rm Q}=\alpha
&\longrightarrow \text{razão macro--local},\\
\delta_R\mathcal W_n=0
&\longrightarrow \tau_{\rm EM}^{\rm dimless}>0.
\end{aligned}
}
$$

Em unidades físicas, a convenção oficial da Q2 identifica a unidade da
resolução como o comprimento de Cartan

$$
\ell_C=\frac{\hbar c}{\Lambda_C},
\qquad
\widehat\tau=\frac{\tau}{\ell_C^2}.
$$

Portanto,

$$
\tau_{\rm EM}^{\rm phys}
=
\ell_C^2\tau_{\rm EM}^{\rm dimless},
$$

e

$$
\boxed{
\Lambda_{\rm EM}^{\rm phys}
=
\widehat\Lambda_{\rm EM}\Lambda_C.
}
$$

A calibração de $\Lambda_C$ não altera a razão geométrica; apenas expressa em
unidades físicas o parâmetro dimensional já presente na ação.

## 7. Relação com o colar espectral

No colar compacto, o cálculo independente forneceu

$$
\Lambda_{\rm EM}^{\rm colar}=\frac{\pi}{L}.
$$

Compatibilidade com a resolução de fluxo exige

$$
\boxed{
\frac{L}{\ell_C}
=
\pi\sqrt{\tau_{\rm EM}^{\rm dimless}}.
}
$$

Essa equação não é uma derivação local de $L$: é a condição de colagem que
transporta o número de similaridade para o domínio global.

## 8. Avaliação de baixa energia e benchmark do LHC

Para o valor correto de baixa energia

$$
\alpha_{\rm IR}=\frac1{137},
\qquad
n_B=1,
$$

obtém-se

$$
R=1{,}0370743523,
\qquad
\tau_{\rm EM}^{\rm dimless}=0{,}2749005225,
$$

$$
\widehat\Lambda_{\rm EM}=1{,}9072701741.
$$

O valor

$$
\alpha_{\rm LHC}^{\rm efetivo}\simeq\frac1{128}
$$

é preservado separadamente como benchmark experimental de alta energia. Ele
pertence ao running efetivo entre o regime infravermelho e o LHC e não deve
ser usado como valor fundamental na condição constitutiva de baixa energia.

## 9. Status

O fechamento é:

$$
\boxed{
\text{Q35 fechada estruturalmente por }
dB=0,\ n_B\in\mathbb Z,\ \operatorname{Re}_{\rm Q}=\alpha
\text{ e equilíbrio radial.}
}
$$

Permanece posterior:

1. derivar ou elevar explicitamente
   $\operatorname{Re}_{\rm Q}=\alpha$ a princípio constitutivo oficial;
2. fixar a calibração metrológica;
3. calcular a colagem global e verificar
   $L/\ell_C=\pi\sqrt{\tau_{\rm EM}^{\rm dimless}}$;
4. auditar separadamente o valor físico de $\alpha$.

Esses itens refinam a realização e a metrologia, mas não reabrem o mecanismo
de ausência do polo: $\tau_{\rm EM}>0$ e a saturação do heat kernel já foram
demonstradas.
