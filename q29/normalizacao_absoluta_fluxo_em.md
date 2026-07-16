# Q29 — Normalização absoluta pelo fluxo eletromagnético

## 1. Falha do traço bruto

Se for feita a identificação direta

$$
K_a(s)=C\operatorname{Tr}(T_a^2e^{-sL_a})
$$

com $C$ fixado em $s_0=1$, o cruzamento fornece corretamente
$\sin^2\theta_W=2/9$, mas também

$$
\alpha^{-1}_{\rm bruto}(s_*)=57{,}4076.
$$

O problema é que o traço bruto contém duas informações diferentes:

1. transporte relativo entre $W$ e $Y$;
2. redução comum da densidade de estados sob o semigrupo.

Identificar ambas com a rigidez absoluta viola a normalização da medida GDQ.

## 2. Separação correta

A medida satisfaz

$$
\int\mathcal U_s,dV=1.
$$

Além disso, depois da quebra, a direção eletromagnética pertence ao kernel:

$$
L_\gamma\Psi_\gamma=0.
$$

O fluxo de Noether eletromagnético fixa a normalização da carga:

$$
\Phi_Q=\oint_{\partial\Sigma}\star J_Q=\text{constante}.
$$

Portanto, o transporte espectral determina

$$
\frac{g'^2}{g^2}
$$

pela razão dos traços normalizados, enquanto a normalização comum é fixada por
$e(s)$ no canal protegido:

$$
g(s)=\frac{e(s)}{\sin\theta_W(s)},
\qquad
g'(s)=\frac{e(s)}{\cos\theta_W(s)}.
$$

## 3. Avaliação com a resposta de interface

Usando o candidato já derivado para a resposta eletromagnética de interface,

$$
\alpha_{\rm EM}^{-1}
=\frac{\alpha_0^{-1}}{1+\mathcal S_\partial}
=132{,}457669022,
$$

e o valor espectral $2/9$, obtemos

$$
g=0{,}653390228,
\qquad
g'=0{,}349251767,
$$

$$
m_W=80{,}403325214\ {\rm GeV},
\qquad
m_Z=91{,}168801328\ {\rm GeV}.
$$

## 4. Status lógico

O transporte angular está derivado pelo espectro. A normalização absoluta
depende da identidade de Schur eletromagnética

$$
K_{\rm EM}^{\rm eff}
=\frac{K_{\rm EM}^{(0)}}{1+\mathcal S_\partial},
$$

que ainda deve ser obtida diretamente do bloco de interface completo. Assim,
os valores acima são uma consequência condicional, não uma previsão final já
fechada.

O resultado sólido é a separação:

$$
\boxed{
\text{razão }g'/g:\text{ traço espectral};
\qquad
\text{norma }e:\text{ fluxo EM protegido.}
}
$$

A tentativa de obter $e$ no espaço cosmológico de Einstein encontrou o mesmo
teorema de anulação causal da Q38: para inserção suave e medida normalizada, a
integral fechada é zero. Ver `q29/obstrucao_normalizacao_einstein.md`.
