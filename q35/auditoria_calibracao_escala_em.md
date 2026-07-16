# Q35 — Auditoria da calibração da escala eletromagnética

## 1. Enunciado

Determinar se a razão geométrica

$$
\widehat\Lambda_{\rm EM}=1{,}90727017413475
$$

pode ser convertida numa energia física usando diretamente a calibração pelo
elétron da Q36.

## 2. Regra metrológica correta

A Q36 fornece, para um operador espectral e um estado de referência do mesmo
setor,

$$
E_n=E_0\varepsilon_n,
\qquad
E_0=\frac{M_ec^2}{\varepsilon_e}.
$$

Logo, a escala eletromagnética seria

$$
\boxed{
\Lambda_{\rm EM}^{\rm phys}
=M_ec^2\frac{\widehat\Lambda_{\rm EM}}{\varepsilon_e^{(\rm EM)}}.
}
$$

Não é permitido definir $\varepsilon_e^{(\rm EM)}=1$ sem demonstrar que o
elétron é o estado de referência normalizado do mesmo operador que produziu
$\widehat\Lambda_{\rm EM}$.

## 3. Diagnóstico da tentativa direta

Tomar $\ell_{\rm met}=\hbar/(M_ec)$ equivale a impor
$\varepsilon_e^{(\rm EM)}=1$. Isso produziria

$$
\Lambda_{\rm EM}^{\rm phys}=0{,}9746130563\ {\rm MeV}.
$$

Esse número é apenas a consequência da normalização imposta. Não é uma
previsão da GDQ e não deve ser interpretado como corte UV eletromagnético
universal.

## 4. Resultado que independe da calibração

A Q35 demonstrou, em variáveis adimensionais,

$$
\tau_{\rm EM}^{\rm dimless}=0{,}274900522513626>0
$$

e a saturação do determinante geométrico. Portanto, a ausência estrutural do
polo não depende de converter $\widehat\Lambda_{\rm EM}$ em MeV ou GeV.

A calibração é necessária somente para localizar a energia física da
transição entre a aproximação pontual e o regime geométrico.

## 5. Unidade oficial da resolução

A Q2 já define a variável adimensional do fluxo por

$$
\widehat\tau=\frac{\tau}{\ell_C^2},
\qquad
\ell_C=\frac{\hbar c}{\Lambda_C}.
$$

Logo, a quantidade denominada $\tau_{\rm EM}^{\rm dimless}$ na Q35 é
precisamente $\widehat\tau_{\rm EM}$ quando a mesma convenção oficial é
mantida. Portanto,

$$
\tau_{\rm EM}^{\rm phys}
=\ell_C^2\widehat\tau_{\rm EM}
$$

e


$$
\boxed{
\Lambda_{\rm EM}^{\rm phys}
=\frac{1}{\ell_C\sqrt{\widehat\tau_{\rm EM}}}
=\widehat\Lambda_{\rm EM}\,\Lambda_C
}
$$

em unidades naturais; com unidades explícitas, $\Lambda_C$ é a energia
$\hbar c/\ell_C$.

Isso não impõe $\Lambda_{\rm EM}=\Lambda_C$: a razão prevista é

$$
\boxed{
\frac{\Lambda_{\rm EM}}{\Lambda_C}
=1{,}90727017413475.
}
$$

A escala de Cartan é parâmetro dimensional da ação oficial. Seu valor em GeV
é uma calibração metrológica da teoria, não algo que possa ser produzido por
uma razão adimensional.

## 6. Veredito

$$
\boxed{
\text{Q35 está calibrada em unidades de Cartan:
}\Lambda_{\rm EM}=1{,}90727017413475\,\Lambda_C.
}
$$

O espectro global fixou, no subespaço invariante de $S^3$ da Q35,

$$
\lambda_{1,\rm EM}^{+}=3{,}63767951714400,
\qquad
\widehat\Lambda_{\rm EM}=1{,}90727017413475.
$$

Ver `q35/espectro_global_em_s3_colar.md`. Para escrever o resultado em GeV,
resta apenas declarar o valor metrológico de $\Lambda_C$ usado pela ação.
Isso não é uma pendência específica da Q35 e não exige $1/128$.

O valor $1/128$ não é necessário e não participa desta auditoria.
