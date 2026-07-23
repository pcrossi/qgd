# Q51 — Pré-formação alfa como overlap de superfície GDQ

## 1. Problema

Gamow puro escreve:

$$
\Gamma
=
\nu P.
$$

Essa fórmula assume implicitamente que o cluster alfa já existe na superfície
do núcleo com probabilidade unitária. Em núcleos reais, isso é forte demais.

Na GDQ, o fator de pré-formação não deve ser introduzido como parâmetro
fenomenológico. Ele deve sair do overlap entre:

1. o modo coletivo de quatro nucleons ligado;
2. a cola torsional de superfície do núcleo pai;
3. o canal radial que separa núcleo filho e cluster alfa.

## 2. Forma GDQ

A taxa deve ser escrita como:

$$
\Gamma_{\rm GDQ}
=
\nu_{\rm GDQ}
S_\alpha^{\rm GDQ}
P_{\rm rad}^{\rm GDQ}.
$$

Aqui:

$$
P_{\rm rad}^{\rm GDQ}
=
\exp(-W_{\rm rad}^{\rm GDQ}),
$$

e:

$$
S_\alpha^{\rm GDQ}
=
\left|
\left\langle
\Phi_{\rm filho}\oplus\Phi_\alpha,
\Phi_{\rm pai}
\right\rangle_{\partial}^{\rm phys}
\right|^2.
$$

O produto interno correto não é o de Hilbert inserido manualmente. Ele é a
forma quadrática física induzida pela Hessiana de superfície:

$$
\langle u,v\rangle_{\partial}^{\rm phys}
=
\int_{\partial\Omega_N}
u^\dagger
\mathsf R_{\partial}^{\rm GDQ}
v\,d\Sigma.
$$

com:

$$
\mathsf R_{\partial}^{\rm GDQ}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

## 3. Diagnóstico a partir dos dados

Usando a frequência interna reduzida:

$$
\nu_{\rm int}
=
\frac{c}{2R_N}
\sqrt{\frac{2Q_\alpha}{\mu}},
$$

define-se:

$$
W_{\rm req}
=
\ln\left(
\frac{T_{1/2}^{\rm exp}\nu_{\rm int}}{\ln2}
\right).
$$

Então:

$$
\Delta W_{\rm req}
=
W_{\rm req}-W_{\rm Gamow}.
$$

Se esse resíduo for lido como pré-formação efetiva:

$$
S_{\alpha}^{\rm eff}
=
\exp(-\Delta W_{\rm req}).
$$

No dataset diagnóstico:

| Núcleo | \(\Delta W_{\rm req}\) | \(S_\alpha^{\rm eff}\) |
| --- | ---: | ---: |
| U-238 | \(-0{,}039094\) | \(1{,}039868\) |
| U-234 | \(0{,}425065\) | \(0{,}653727\) |
| U-232 | \(0{,}373825\) | \(0{,}688097\) |
| Th-232 | \(-0{,}014190\) | \(1{,}014291\) |
| Ra-226 | \(0{,}422411\) | \(0{,}655465\) |
| Po-212 | \(1{,}557848\) | \(0{,}210589\) |

## 4. Interpretação

Os valores próximos de 1 para U-238 e Th-232 indicam que, nesses casos, Gamow
com frequência interna já captura quase toda a ação.

Os valores entre \(0{,}65\) e \(0{,}69\) para U-234, U-232 e Ra-226 indicam
redução moderada de overlap.

O valor aproximadamente \(0{,}21\) para Po-212 indica forte sensibilidade à
estrutura de superfície/canal.

Valores ligeiramente maiores que 1 não devem ser lidos literalmente como
probabilidade. Eles indicam que o raio, a frequência reduzida ou os dados
diagnósticos ainda não estão na forma avaliada final.

## 5. Próxima equação a provar

O fechamento da Q51 exige substituir:

$$
S_\alpha^{\rm eff}
=
\exp(-\Delta W_{\rm req})
$$

por:

$$
S_\alpha^{\rm GDQ}
=
\left|
\left\langle
\Phi_{\rm filho}\oplus\Phi_\alpha,
\Phi_{\rm pai}
\right\rangle_{\partial}^{\rm phys}
\right|^2
$$

calculado diretamente da Hessiana de superfície.

## 6. Veredito

$$
\boxed{
\text{o resíduo da Q51 tem escala e assinatura de overlap/preformação de superfície.}
}
$$

Isso orienta o próximo cálculo: não ajustar uma barreira universal, mas
construir o projetor de cluster alfa no contorno nuclear.

