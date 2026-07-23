# Questão 47 — Efeito Casimir

## 1. Enunciado

A questão pergunta:

1. se o resultado vem da GDQ ou da soma padrão de modos;
2. qual é a contribuição geométrica nova;
3. como materiais, temperatura e geometria real são tratados;
4. se o regulador é físico ou auxiliar.

O capítulo legado associado é:

- `pt-br/39 - O Efeito Casimir e a Pressao de Vacuo.md`.

Adendo técnico:

- `questoes/q47/associados/casimir_hessiana_contorno_gdq.md`.

## 2. Status curto

$$
\boxed{
\text{Q47 fechada estruturalmente no limite de placas ideais.}
}
$$

O que está fechado:

1. recuperação da pressão de Casimir ideal;
2. classificação da soma de modos como determinante da Hessiana efetiva
   projetada;
3. interpretação GDQ como diferença de impedância/pressão geométrica de
   contorno;
4. separação entre regulador auxiliar e corte físico microscópico;
5. encaminhamento de material, temperatura e geometria real para cálculo de
   interface.

O que fica em `ideias/possibilidades.md`:

1. placas reais;
2. resposta dielétrica/condutiva;
3. temperatura finita;
4. rugosidade;
5. geometria finita;
6. comparação metrológica.

## 3. O resultado vem da GDQ ou da soma padrão de modos?

No limite ideal, o valor numérico vem da mesma estrutura espectral que a soma
padrão de modos. A diferença é a classificação.

Na GDQ, os modos não são postulados como flutuações livres fundamentais. Eles
são automodos do operador físico obtido pela cadeia:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
\text{domínio com placas}
\to
\operatorname{Tr}_{\rm phys}\log K_{\rm phys}.
$$

No fundo plano, no setor eletromagnético efetivo, a Hessiana reduzida tem o
mesmo espectro transversal usado no cálculo padrão:

$$
\omega_{n,\boldsymbol k_\parallel}
=
c\sqrt{k_\parallel^2+\left(\frac{n\pi}{a}\right)^2}.
$$

Logo, a energia universal por área é:

$$
\frac{\Delta E(a)}{A}
=
-\frac{\pi^2\hbar c}{720a^3}.
$$

E a pressão é:

$$
P(a)
=
-\frac{\partial}{\partial a}
\left(
\frac{\Delta E(a)}{A}
\right)
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

Portanto:

$$
\boxed{
\text{o número ideal é recuperado; a GDQ fornece a origem geométrica do operador e do contorno.}
}
$$

## 4. Qual é a contribuição geométrica nova?

A contribuição nova não é mudar a constante universal do limite ideal. A
contribuição GDQ é interpretar a força como resposta de contorno da geometria.

As placas alteram o domínio da Hessiana física. Isso muda a densidade
espectral entre interior e exterior:

$$
\Delta\rho_{\rm spec}
=
\rho_{\rm int}-\rho_{\rm ext}.
$$

Essa diferença produz uma tensão:

$$
P
=
-\partial_a
\left(
\frac{\hbar}{2}
\operatorname{Tr}_{\rm phys}\log K_{\rm cav}
-\frac{\hbar}{2}
\operatorname{Tr}_{\rm phys}\log K_{\rm ref}
\right).
$$

Fisicamente, isso é diferença de impedância/pressão geométrica do vácuo
entre a região confinada e a região externa.

## 5. Materiais, temperatura e geometria real

Materiais reais não devem ser escondidos em “condições de contorno ideais”.
Na GDQ, eles entram como fonte/contorno clássico do aparelho:

$$
J_{\rm plate}^{\rm clássico}
\to
\delta\Phi_{\rm plate}
\to
K_{\rm phys}
\to
\mathsf R_{\rm plate}.
$$

A impedância efetiva é:

$$
\mathsf R_{\rm plate}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY}.
$$

Com duas placas:

$$
K_{\rm cav}
=
K_{\rm cav}(\mathsf R_1,\mathsf R_2,a).
$$

Temperatura finita entra pela compactificação euclidiana do tempo físico ou
pela soma de Matsubara:

$$
\omega_m
=
\frac{2\pi m k_BT}{\hbar}.
$$

Geometria real entra no domínio e no operador de bordo:

$$
\Omega_a
\to
\Omega_{\rm real},
\qquad
\mathsf R_{\rm plate}
\to
\mathsf R_{\rm real}(\omega,k_\parallel,T,\text{material}).
$$

Esses itens são metrológicos. Eles foram registrados em
`ideias/possibilidades.md`.

## 6. O regulador é físico ou auxiliar?

No cálculo ideal, o regulador é auxiliar.

Pode-se usar:

$$
e^{-\epsilon\omega}
$$

ou zeta/heat-kernel para separar a parte dependente de $a$ dos termos locais
de referência. O resultado universal deve ser independente do regulador:

$$
P(a)
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

Na GDQ existe uma escala física de rigidez/corte microscópico, mas ela não
deve ser usada para escolher a constante ideal. Para $a$ muito maior que a
escala microscópica, o termo universal é insensível ao corte.

Em materiais reais, a física microscópica reaparece na impedância da placa:

$$
\mathsf R_{\rm plate}(\omega,k_\parallel,T).
$$

Portanto:

$$
\boxed{
\text{regulador ideal: auxiliar; corte/rigidez GDQ: físico, mas só afeta correções não universais.}
}
$$

## 7. Respostas diretas às perguntas obrigatórias

1. O resultado ideal coincide com a soma padrão de modos, mas na GDQ essa soma
   é lida como determinante da Hessiana física projetada em domínio com
   contorno.
2. A contribuição geométrica nova é a interpretação por impedância/pressão de
   contorno e o protocolo para derivar placas reais por DtN/Schur.
3. Materiais, temperatura e geometria real entram por $\mathsf R_{\rm plate}$,
   Matsubara/tempo térmico e domínio real. São aplicações metrológicas.
4. O regulador do cálculo ideal é auxiliar; o corte físico da GDQ só entra nas
   correções não universais ou materiais.

## 8. Veredito

$$
\boxed{
\text{Q47 fechada estruturalmente.}
}
$$

No limite de placas ideais, a GDQ recupera:

$$
P(a)
=
-\frac{\pi^2\hbar c}{240a^4}.
$$

O fechamento é estrutural porque identifica o operador, o domínio ideal, o
papel do contorno e a interpretação geométrica. A comparação com materiais
reais fica como refinamento futuro, não como lacuna da resposta ideal.
