---
title: "Decaimento beta e quarta variação"
---

# Decaimento beta e quarta variação

O decaimento beta é tratado como transição entre backgrounds:

$$
n\to p+e^-+\bar\nu_e.
$$

O antineutrino é modo neutro torsional:

$$
\psi_{\bar\nu}
\in
\ker D_{0,-3/2}^{(0)}.
$$

## 1. Enunciado físico

O erro a evitar é tratar:

$$
Q_\beta
=
M_n-M_p-m_e
$$

como energia fixa do antineutrino. O balanço correto é:

$$
M_nc^2-M_pc^2
=
E_e+E_{\bar\nu}+E_{\rm recoil}.
$$

No limite líder em que o recuo do próton é desprezado:

$$
E_{\bar\nu}
=
\Delta M-E_e,
\qquad
m_e\le E_e\le\Delta M.
$$

Assim, a GDQ deve reproduzir um espectro contínuo de elétrons, não uma linha
monoenergética.

## 2. Origem variacional da amplitude

A amplitude efetiva é:

$$
\mathcal V_{\rm eff}^{(4)}
=
\mathcal S_{\rm GDQ}^{(4)}
-
\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}
\mathcal S_{\rm GDQ}^{(3)}
+
\text{permutações}.
$$

Aqui:

- $\mathcal S_{\rm GDQ}^{(4)}$ é a quarta variação física da ação oficial no
  background bariônico;
- $\mathcal S_{\rm GDQ}^{(3)}K_\perp^{-1}\mathcal S_{\rm GDQ}^{(3)}$ é a
  eliminação dos modos transversais não observados por complemento de Schur;
- $K_\perp$ é a Hessiana física nos modos ortogonais à subvariedade de
  matching;
- as permutações impõem a simetrização compatível com as orientações
  torsionais dos canais.

Logo, a GDQ não adiciona um vértice fundamental de Fermi. O vértice efetivo é
o resíduo local da quarta variação projetada na cirurgia torsional.

## 3. Redução por simetrias

Homogeneidade temporal, conservação de energia, conservação de carga,
conservação de fluxo torsional e isotropia residual restringem o setor não
polarizado a dois invariantes:

$$
\mathcal M_0
=
C_SS+C_TT.
$$

No setor não polarizado:

$$
\frac12\sum_{\rm spins}|\mathcal M_0|^2
=
2|C_S|^2+6|C_T|^2.
$$

Definimos:

$$
\mathcal J_3^2
:=
2|C_S|^2+6|C_T|^2.
$$

Essa é a norma contraída que entra na taxa total. Ela não determina sozinha
as correlações angulares, pois estas dependem da razão e fase relativas entre
$C_S$ e $C_T$.

Os coeficientes reduzidos são resíduos causais:

$$
C_A
=
\frac{\hbar}{\Lambda_C^2}
\frac{2\pi i}{(4\pi)^4}
[z^3]F_A,
\qquad
A\in\{S,T\}.
$$

## 4. Espaço de fase contínuo

O espaço de fase líder é:

$$
I_\beta
=
\int_{m_e}^{\Delta M}
p_eE_e(\Delta M-E_e)^2\,dE_e,
\qquad
p_e=\sqrt{E_e^2-m_e^2}.
$$

A forma diferencial mínima é:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2.
$$

Se efeitos de superfície e recoil forem incluídos, a forma correta é:

$$
\frac{d\Gamma}{dE_e}
=
\frac{\mathcal J_3^2}{2\pi^3\hbar}
p_eE_e(\Delta M-E_e)^2
\mathcal C_{\rm geom}(E_e),
$$

com:

$$
\mathcal C_{\rm geom}
=
1+\delta_{\rm surf}
+\delta_{\rm recoil}
+\delta_{\rm rad}
+\delta_{\rm tors}
+\cdots .
$$

Esses termos são respostas geométricas de canal carregado, superfície,
recuo e torção. Eles não alteram a ação oficial.

## 5. Status

O bloco beta está fechado para:

1. correção do endpoint;
2. canais GDQ $p$, $e^-$ e $\bar\nu_e$;
3. amplitude efetiva reduzida;
4. espectro contínuo mínimo;
5. taxa total.

Permanece condicional para:

1. separação individual de $C_S$ e $C_T$;
2. correlações angulares;
3. recoil e forma diferencial metrológica;
4. respostas de superfície de ordem superior.

Verificação autocontida:
[[../../scripts/saida_validar_beta_livre_completo|Saída — validação beta livre GDQ]].
