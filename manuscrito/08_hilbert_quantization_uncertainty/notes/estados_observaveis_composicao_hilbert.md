---
title: "Estados, observáveis e composição no Hilbert reconstruído"
---

# Estados, observáveis e composição no Hilbert reconstruído

Esta nota completa a construção operacional do espaço de Hilbert físico. Ela
não introduz o Hilbert como ontologia primária. Ela mostra como a camada
geométrica da GDQ passa a falar a linguagem operacional de estados,
observáveis, evolução e sistemas compostos quando o setor admite reflexão
positiva, quociente por nulos e remoção de redundâncias.

## 1. Espaço físico

O ponto de partida é o espaço reconstruído:

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

Aqui $\mathcal D_+$ é o domínio de funcionais de suporte temporal positivo,
$\mathcal N$ é o subespaço de norma nula e $\mathcal G$ reúne redundâncias
geométricas, como difeomorfismos, escolhas de seção, modos longitudinais e
modos de bordo exatos.

O produto interno físico é:

$$
\langle [F],[G]\rangle_{\mathcal H}
=
\langle \Theta F\,G\rangle_E.
$$

No setor regular de uma partícula, a mesma estrutura reduz para:

$$
\mathcal H_1
=
L^2(N,E,d\Sigma_h),
$$

com:

$$
\Psi
=
\sqrt{\rho}\,e^{iS_R/\hbar},
\qquad
\rho=e^{-(f+\bar f)/2}.
$$

## 2. Estados físicos

Um estado puro é um vetor normalizado:

$$
|\Psi\rangle\in\mathcal H_{\rm phys},
\qquad
\|\Psi\|=1.
$$

Como a fase global não muda nenhum observável, o estado físico puro é o raio:

$$
|\Psi\rangle
\sim
e^{i\alpha}|\Psi\rangle.
$$

Em setores abertos, subsistemas, coarse graining ou interação com aparelho, a
descrição correta é uma matriz densidade:

$$
\varrho\ge0,
\qquad
\operatorname{Tr}\varrho=1.
$$

Essa matriz densidade não substitui a geometria. Ela é a descrição operacional
do setor reconstruído após ignorar graus de liberdade não monitorados ou após
condicionar o sistema ao aparelho.

## 3. Observáveis

Um observável físico é um operador autoadjunto densamente definido:

$$
A:D(A)\subset\mathcal H_{\rm phys}\to\mathcal H_{\rm phys},
\qquad
A=A^\dagger.
$$

Em forma mais geral, pode ser tratado como elemento autoadjunto de uma álgebra
local:

$$
A\in\mathcal A(O),
\qquad
A=A^\dagger.
$$

O domínio é parte da definição. Uma expressão formal que não possui domínio
denso, fechamento autoadjunto e condições de contorno compatíveis ainda não é
um observável físico fechado.

Pelo teorema espectral, se $E_A(\Delta)$ é o projetor espectral associado ao
intervalo $\Delta\subset\mathbb R$, então:

$$
\mathbb P_A(\Delta)
=
\langle\Psi,E_A(\Delta)\Psi\rangle
$$

para estado puro, e:

$$
\mathbb P_A(\Delta)
=
\operatorname{Tr}(\varrho E_A(\Delta))
$$

para estado misto.

No setor de posição:

$$
\mathbb P(x\in R)
=
\int_R |\Psi(x)|^2\,d\Sigma_h
=
\int_R \rho(x)\,d\Sigma_h.
$$

Assim, a densidade geométrica positiva $\rho$ torna-se a densidade de Born
somente depois da reconstrução operacional do setor regular.

## 4. Evolução

O parâmetro $\tau$ é parâmetro de fluxo geométrico. Ele não é, sozinho, o grupo
unitário de tempo físico.

Quando a reconstrução em tempo físico fornece um Hamiltoniano autoadjunto:

$$
H=H^\dagger,
$$

a evolução é:

$$
U(t)=e^{-itH/\hbar}.
$$

Pelo teorema espectral:

$$
U(t)^\dagger U(t)=I.
$$

Portanto:

$$
\|U(t)\Psi\|=\|\Psi\|.
$$

Esse é um teorema condicional do setor reconstruído: exige domínio,
autoadjunticidade e positividade física.

## 5. Sistemas compostos

Para dois sistemas distinguíveis e aproximadamente desacoplados, a composição
operacional é:

$$
\mathcal H_{AB}
=
\mathcal H_A\otimes\mathcal H_B.
$$

O produto interno fatoriza:

$$
\langle
\psi_A\otimes\psi_B,
\phi_A\otimes\phi_B
\rangle_{AB}
=
\langle\psi_A,\phi_A\rangle_A
\langle\psi_B,\phi_B\rangle_B.
$$

Um estado emaranhado é um vetor de $\mathcal H_A\otimes\mathcal H_B$ que não
admite fatoração simples:

$$
\Psi_{AB}\ne\psi_A\otimes\psi_B.
$$

Na linguagem GDQ, isso significa que a configuração geométrica total não se
separa em duas geometrias independentes. Há correlação global de fase,
holonomia, contorno ou medida.

Para observáveis:

$$
A
\mapsto
A\otimes I_B,
\qquad
B
\mapsto
I_A\otimes B.
$$

Em estados produto:

$$
\langle A\otimes B\rangle_{\psi_A\otimes\psi_B}
=
\langle A\rangle_{\psi_A}
\langle B\rangle_{\psi_B}.
$$

## 6. Sistemas idênticos

Para $N$ sistemas idênticos, primeiro forma-se $\mathcal H^{\otimes N}$.
Depois projeta-se no setor estatístico adequado.

Para bósons:

$$
\mathcal H_N^{(+)}
=
\operatorname{Sym}^N\mathcal H.
$$

Para férmions:

$$
\mathcal H_N^{(-)}
=
\wedge^N\mathcal H.
$$

Na GDQ, essa regra operacional deve ser compatível com a holonomia, a estrutura
spin e a topologia do setor. Ela não é tomada como substituto da explicação
geométrica de spin-estatística; é a forma Hilbertiana após a reconstrução.

## 7. Status

O resultado é fechado estruturalmente:

$$
\text{GDQ geométrica}
\to
\text{medida e positividade setorial}
\to
\mathcal H_{\rm phys}
\to
\text{estados, observáveis, evolução e composição}.
$$

O fechamento completo de cada setor ainda exige verificar existência da medida,
reflexão positiva, cluster, autoadjunticidade essencial, domínio comum denso,
remoção consistente de redundâncias e fatorização tensorial para sistemas
assintoticamente separados.

