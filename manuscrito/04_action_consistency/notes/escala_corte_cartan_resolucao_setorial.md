---
title: "Escala de Cartan, resolução de fluxo e escalas setoriais"
---

# Escala de Cartan, resolução de fluxo e escalas setoriais

Esta nota fixa uma ambiguidade importante: a palavra “corte” não deve nomear
um único número usado em todos os contextos. Na GDQ aparecem três objetos
diferentes:

$$
\Lambda_C,
\qquad
\widehat\Lambda_\tau,
\qquad
m_i.
$$

Eles não têm a mesma função.

## 1. A escala que aparece na ação

Na ação oficial, $\Lambda_C$ aparece no prefator:

$$
\frac{\hbar}{\Lambda_C^2}.
$$

Na convenção adotada no manuscrito, as coordenadas já foram normalizadas por
um comprimento de Cartan $\ell_C$. Por isso, $\Lambda_C$ é o número de corte
adimensional associado a essa normalização:

$$
\Lambda_C
=
\ell_C k_C.
$$

No ponto de referência de Cartan:

$$
\Lambda_C=1.
$$

A escala física correspondente não deve ser escrita com o mesmo símbolo. Ela é:

$$
k_C=\ell_C^{-1},
\qquad
E_C=\hbar c\,k_C
=
\frac{\hbar c}{\ell_C}.
$$

Assim:

$$
\left[
\frac{\hbar}{\Lambda_C^2}
\right]
=
[\hbar],
$$

porque $\Lambda_C$ é adimensional dentro da ação normalizada.

## 2. A escala do kernel de calor

O amortecimento perturbativo declarado no Capítulo 4 vem do semigrupo de calor
da Hessiana normalizada:

$$
K_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}.
$$

No limite plano:

$$
L_{\rm GDQ}^{(2)}
\to
p_E^2+m^2.
$$

Logo o setor cinético produz:

$$
e^{-\tau p_E^2}.
$$

Se escrevemos esse fator na forma usual:

$$
e^{-p_E^2/\widehat\Lambda_\tau^2},
$$

então:

$$
\widehat\Lambda_\tau
=
\tau^{-1/2}.
$$

$\widehat\Lambda_\tau$ é uma escala de resolução da seção de fluxo. Ela não é
uma nova constante fundamental, não é massa de partícula e não substitui
$\Lambda_C$ no prefator da ação.

## 3. Massas não são cortes universais

Para um setor físico $i$, a Hessiana reduzida define um operador:

$$
L_i^{(2)}\psi_{i,n}
=
\lambda_{i,n}\psi_{i,n}.
$$

No regime plano com massa efetiva:

$$
\lambda_{i,p}
\simeq
p_E^2+m_i^2.
$$

Então:

$$
e^{-\tau\lambda_{i,p}}
=
e^{-\tau p_E^2}
e^{-\tau m_i^2}.
$$

A massa $m_i$ desloca o espectro do setor. Ela não redefine o princípio
universal de resolução:

$$
\widehat\Lambda_\tau=\tau^{-1/2}.
$$

Portanto, a identificação

$$
\Lambda_i=m_i
$$

não é uma definição válida de corte ultravioleta universal.

## 4. Por que $m_e$ não pode ser corte universal

Se alguém escrevesse:

$$
\Lambda_{\rm UV}=m_e c^2
\simeq
0{,}511\,{\rm MeV},
$$

então um modo externo com energia de escala $E$ sofreria, em uma leitura
ingênua de corte duro gaussiano, o fator:

$$
\exp
\left[
-
\left(
\frac{E}{m_ec^2}
\right)^2
\right].
$$

Para qualquer processo em escala de GeV ou TeV, esse fator é praticamente
zero. Isso contradiria a existência de física de altas energias já descrita
por teorias efetivas operacionais.

Logo:

$$
m_ec^2
$$

pode ser escala inercial/Compton do setor eletrônico, mas não corte
ultravioleta universal da GDQ.

## 5. Por que $1\,{\rm GeV}$ também não pode ser parede universal

Uma escala da ordem de $1\,{\rm GeV}$ é natural em setores hadrônicos,
solitônicos ou de confinamento. Mas, se usada como parede universal:

$$
\exp
\left[
-
\left(
\frac{E}{1\,{\rm GeV}}
\right)^2
\right],
$$

ela também suprimiria indevidamente processos eletrofracos e de colisores com
$E\gg1\,{\rm GeV}$.

Portanto, $1\,{\rm GeV}$ só pode entrar como escala setorial, por exemplo
associada ao espectro de um operador hadrônico:

$$
L_{\rm had}^{(2)}.
$$

## 6. Classificação final

O vocabulário correto é:

| Símbolo | Papel | Status |
|---|---|---|
| $\Lambda_C$ | número de corte adimensional da ação normalizada | dado estrutural da escrita oficial |
| $\ell_C$ | comprimento físico de Cartan | escala física a ser calibrada ou derivada conforme o setor |
| $k_C=\ell_C^{-1}$ | número de onda físico | restauração dimensional |
| $E_C=\hbar c/\ell_C$ | energia física de Cartan | restauração dimensional |
| $\widehat\Lambda_\tau=\tau^{-1/2}$ | resolução espectral da seção de fluxo | derivada do kernel de calor |
| $m_i$ | massa/autovalor de uma excitação | dado espectral do setor físico |
| $\Lambda_{\rm setor}$ | escala efetiva de um setor | deve vir do espectro de $L_i^{(2)}$ |

Conclusão:

$$
\boxed{
\Lambda_C
\neq
\widehat\Lambda_\tau
\neq
m_i.
}
$$

