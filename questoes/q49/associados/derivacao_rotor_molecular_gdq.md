# Derivação reduzida do rotor molecular na GDQ

## 1. Escopo

Este adendo organiza a parte matematicamente aproveitável do capítulo legado
`pt-br/41 - O Rotor Rigido Molecular.md` sem transformar a GDQ em mecânica
quântica ordinária.

A cadeia usada é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_{\rm mol,*}
\to
\operatorname{Hess}\mathcal S_{\rm GDQ}
\to
K_{\rm ang}\oplus K_r
\to
\text{domínio angular e radial}
\to
E_J.
$$

Aqui \(\Phi_{\rm mol,*}\) é o background estacionário de uma molécula diatômica
como dois nós geométricos ligados por uma ponte de fluxo.

## 2. Coordenadas coletivas

No regime de baixa energia, se os modos internos rápidos possuem gap, a
Hessiana física pode ser projetada nas coordenadas coletivas:

$$
R(t)\in \mathbb R_+,
\qquad
\Omega(t)\in S^2.
$$

O raio \(R\) mede a distância efetiva entre os dois centros, enquanto
\(\Omega\) mede a orientação da ligação no laboratório.

O funcional efetivo quadrático toma a forma:

$$
L_{\rm eff}
=
\frac{\mu_{\rm GDQ}}{2}\dot R^2
+
\frac{\mu_{\rm GDQ}R^2}{2}|\dot\Omega|^2
-
V_{\rm GDQ}(R)
+
\cdots .
$$

A massa reduzida \(\mu_{\rm GDQ}\), o raio de equilíbrio \(R_0\) e a rigidez
radial

$$
k_{\rm GDQ}
=
\left.
\frac{d^2V_{\rm GDQ}}{dR^2}
\right|_{R_0}
$$

devem ser derivados da Hessiana da ponte molecular para uma previsão absoluta.
Quando são tomados de dados espectroscópicos, o cálculo é comparação
fenomenológica, não previsão cega.

## 3. Origem de \(J(J+1)\)

O setor angular é o Laplace--Beltrami sobre a esfera de orientações:

$$
K_{\rm ang}
=
-
\frac{\hbar^2}{2I_0}\Delta_{S^2},
\qquad
I_0=\mu_{\rm GDQ}R_0^2.
$$

Como:

$$
-
\Delta_{S^2}Y_{Jm}
=
J(J+1)Y_{Jm},
\qquad
J=0,1,2,\ldots,
\qquad
m=-J,\ldots,J,
$$

segue:

$$
E_J^{(0)}
=
B_{\rm GDQ}J(J+1),
\qquad
B_{\rm GDQ}
=
\frac{\hbar^2}{2I_0}.
$$

Classificação:

$$
\boxed{
\text{o fator }J(J+1)\text{ é derivado do domínio angular }S^2
\text{ e da Hessiana reduzida.}
}
$$

Na linguagem do capítulo legado, a circulação/holonomia fixa a consistência
topológica dos estados fechados; a forma \(J(J+1)\) vem do operador angular
autoadjunto no domínio \(S^2\).

## 4. Distorção centrífuga

Perto do equilíbrio:

$$
V_{\rm GDQ}(R)
=
V_0+\frac{1}{2}k_{\rm GDQ}(R-R_0)^2+\cdots ,
$$

com frequência vibracional:

$$
\omega_e^2
=
\frac{k_{\rm GDQ}}{\mu_{\rm GDQ}}.
$$

Para momento angular fixo \(L^2=\hbar^2J(J+1)\), a energia radial efetiva é:

$$
E(R;J)
=
\frac{\hbar^2J(J+1)}{2\mu_{\rm GDQ}R^2}
+
\frac{1}{2}\mu_{\rm GDQ}\omega_e^2(R-R_0)^2.
$$

Escrevendo \(R=R_0+x\) e expandindo em \(x/R_0\):

$$
\frac{1}{R^2}
=
\frac{1}{R_0^2}
\left(
1-\frac{2x}{R_0}+\frac{3x^2}{R_0^2}+\cdots
\right).
$$

O mínimo em primeira ordem satisfaz:

$$
\mu_{\rm GDQ}\omega_e^2x
-
\frac{\hbar^2J(J+1)}{\mu_{\rm GDQ}R_0^3}
=0,
$$

logo:

$$
x_*(J)
=
\frac{\hbar^2J(J+1)}
{\mu_{\rm GDQ}^2\omega_e^2R_0^3}.
$$

Substituindo \(x_*(J)\) na energia e mantendo termos até ordem
\([J(J+1)]^2\), obtém-se:

$$
E_J
=
B_{\rm GDQ}J(J+1)
-
D_{\rm GDQ}[J(J+1)]^2
+
\cdots ,
$$

com:

$$
D_{\rm GDQ}
=
\frac{\hbar^4}
{2\mu_{\rm GDQ}^3\omega_e^2R_0^6}
=
\frac{4B_{\rm GDQ}^3}{\hbar^2\omega_e^2}.
$$

Em unidades espectroscópicas de número de onda, se \(B\) e \(\omega_e\) forem
ambos expressos em \({\rm cm}^{-1}\), a forma usual é:

$$
D_{\rm GDQ}
\simeq
\frac{4B_{\rm GDQ}^3}{\omega_e^2}.
$$

## 5. Reclassificação do parâmetro elástico legado

O capítulo legado escreveu:

$$
D
=
\gamma_{\rm elastic}
\frac{\hbar^4}{4I_0^3\omega_e^2}.
$$

Como \(I_0=\mu R_0^2\), a derivação reduzida acima dá:

$$
\frac{\hbar^4}{2\mu^3R_0^6\omega_e^2}
=
\frac{\hbar^4}{2I_0^3\omega_e^2}.
$$

Portanto, o símbolo \(\gamma_{\rm elastic}\) do texto legado não deve ser
tratado como novo parâmetro fundamental. Ele representa a diferença entre:

1. o modelo radial harmônico mínimo;
2. a Hessiana física completa da ponte molecular, incluindo anisotropia,
   torção, anharmonicidade e resposta de contorno.

No setor harmônico reduzido:

$$
\gamma_{\rm elastic}^{\rm red}=2
$$

na normalização usada pelo capítulo legado. Uma reescrita mais limpa é remover
\(\gamma_{\rm elastic}\) da fórmula fundamental e escrever diretamente
\(D_{\rm GDQ}\) pela rigidez radial \(k_{\rm GDQ}\).

## 6. O que fica provado

Fica provado no setor reduzido:

1. \(J(J+1)\) vem do operador angular em \(S^2\);
2. \(B_{\rm GDQ}=\hbar^2/(2\mu_{\rm GDQ}R_0^2)\);
3. a distorção centrífuga líder é negativa na energia e tem forma
   \(-D[J(J+1)]^2\);
4. \(D_{\rm GDQ}=4B_{\rm GDQ}^3/(\hbar^2\omega_e^2)\) em energia, ou
   \(D_{\rm GDQ}\simeq4B_{\rm GDQ}^3/\omega_e^2\) em \({\rm cm}^{-1}\);
5. não há necessidade de inserir um parâmetro elástico universal novo no rotor
   ideal.

## 7. O que permanece condicional

A previsão absoluta para várias moléculas exige calcular, para cada background
molecular GDQ:

$$
\Phi_{\rm mol,*}
\mapsto
\mu_{\rm GDQ},
\quad
R_0,
\quad
k_{\rm GDQ},
\quad
\omega_e.
$$

Sem isso, usar \(R_0\), \(B\) ou \(\omega_e\) experimentais transforma o
resultado em comparação fenomenológica. Essa limitação não reabre o espectro
do rotor ideal; ela apenas define a etapa metrológica molecular futura.
