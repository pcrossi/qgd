# Questão 6 — O que é \(\tau\)?

## 1. Pergunta

A Questão 6 pergunta:

\[
\boxed{
\text{o que é }\tau?
}
\]

A inconsistência original era que \(\tau\) aparecia como:

1. tempo de fluxo;
2. variável com dimensão de área;
3. tempo difusivo;
4. logaritmo adimensional de escala;
5. coordenada imaginária associada ao tempo físico \(t\).

A resolução exige uma definição fundamental e mapas dimensionais para os usos
secundários.

---

## 2. Definição fundamental

A definição final é:

\[
\boxed{
\tau\in\mathbb R_+
\text{ é o parâmetro real de fluxo geométrico/difusivo da GDQ.}
}
\]

Sua dimensão física é:

\[
\boxed{
[\tau]=L^2.
}
\]

Portanto, \(\tau\) não é fundamentalmente o tempo físico cronológico e não é
fundamentalmente o logaritmo adimensional da escala de renormalização.

Seu papel primário é parametrizar o fluxo de Perelman, o kernel de calor e a
resolução geométrica da teoria.

---

## 3. Origem difusiva

No fluxo de calor geométrico, a equação modelo tem a forma:

\[
\partial_\tau u=\Delta u-Ru.
\]

Como:

\[
[\Delta]=L^{-2},
\]

a consistência dimensional exige:

\[
[\partial_\tau]=L^{-2},
\qquad
[\tau]=L^2.
\]

No espaço real de dimensão \(d\), o kernel de calor escala como:

\[
K(\tau)\sim(4\pi\tau)^{-d/2}.
\]

Na GDQ:

\[
d=2n,
\qquad
n=4,
\qquad
d=8.
\]

Logo:

\[
\boxed{
K(\tau)\sim(4\pi\tau)^{-4}.
}
\]

Equivalentemente:

\[
(4\pi\tau)^{-d/2}
=(4\pi\tau)^{-n}
\quad
\text{quando }d=2n.
\]

Assim, a forma antiga \(\tau^{-2}\) só é admissível em setor real 4D reduzido
ou em rascunho antigo. Ela não é o kernel fundamental do bulk \(8D\).

---

## 4. Relação com a ação oficial

A ação oficial contém:

\[
\int_\gamma(\cdots)\frac{d\tau}{\tau}.
\]

O fator:

\[
\frac{d\tau}{\tau}
\]

é adimensional, pois \(\tau\) tem dimensão \(L^2\). Ele implementa uma medida
logarítmica de escala no contorno, sem transformar \(\tau\) em variável
adimensional.

A medida funcional correta é:

\[
\boxed{
\mathcal U[f,\bar f,z_\tau]
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

Com:

\[
n=4.
\]

No eixo real difusivo:

\[
z_\tau\to\tau,
\]

e:

\[
\mathcal U
\sim
\frac{e^{-(f+\bar f)/2}}{(4\pi\tau)^4}.
\]

---

## 5. Relação com o tempo físico \(t\)

O tempo físico cronológico tem dimensão:

\[
[t]=T.
\]

Como:

\[
[\tau]=L^2,
\]

a expressão:

\[
\tau+it
\]

é dimensionalmente incorreta.

A variável causal complexa correta é:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

com:

\[
\boxed{
\nu_0=\frac{\hbar}{2m_0}.
}
\]

Como:

\[
[\nu_0]=\frac{L^2}{T},
\]

temos:

\[
[\nu_0t]=L^2,
\qquad
[z_\tau]=L^2.
\]

Portanto:

\[
\boxed{
\tau\neq t.
}
\]

A relação correta é:

\[
\boxed{
t
\mapsto
i\nu_0t
\text{ como parte imaginária de }z_\tau.
}
\]

---

## 6. Relação com a causalidade de Sudarshan

O contorno causal \(\gamma\) deve ser entendido como contorno no plano de
\(z_\tau\), não como uma identificação direta entre \(t\) e \(\tau\).

\[
\boxed{
\gamma\subset\mathbb C_{z_\tau}.
}
\]

A prescrição causal de Sudarshan atua sobre:

\[
z_\tau=\tau+i\nu_0t.
\]

Assim:

1. \(\tau\) fornece o eixo difusivo/reológico;
2. \(i\nu_0t\) fornece o eixo causal/cronológico;
3. \(\gamma\) seleciona os polos, resíduos e setores físicos.

Logo, a identificação:

\[
t=-i\tau
\]

deve ser descartada como definição fundamental.

A forma correta é:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

---

## 7. Relação com renormalização

\(\tau\) não é diretamente o logaritmo da escala de renormalização.

Como \(\tau\) tem dimensão \(L^2\), primeiro deve-se formar uma variável
adimensional. Usando a escala de Cartan \(\ell_C\):

\[
\boxed{
\widehat\tau=\frac{\tau}{\ell_C^2}.
}
\]

Então:

\[
\boxed{
s=\log\widehat\tau
=
\log\left(\frac{\tau}{\ell_C^2}\right).
}
\]

Essa é a variável logarítmica correta de escala geométrica.

Consequentemente:

\[
\boxed{
\frac{\partial}{\partial s}
=
\tau\frac{\partial}{\partial\tau}.
}
\]

Se \(\mu\) for uma escala de energia/momento, o mapa dimensional admissível é:

\[
\boxed{
\widehat\tau
\sim
\frac{1}{\mu^2\ell_C^2}.
}
\]

Logo:

\[
\boxed{
s
\sim
-2\log(\mu\ell_C).
}
\]

Portanto, a escrita antiga:

\[
\ln\mu\to\tau
\]

deve ser substituída por:

\[
\boxed{
\ln\mu
\leftrightarrow
-\frac12s
\quad
\text{com}
\quad
s=\log\left(\frac{\tau}{\ell_C^2}\right).
}
\]

De forma curta:

\[
\boxed{
\tau\neq\log\mu.
}
\]

---

## 8. Relação com \(\epsilon\)

Na redução efetiva, define-se:

\[
\boxed{
\widehat\tau=\frac{\tau}{\ell_C^2}.
}
\]

O parâmetro de complacência/escala \(\epsilon\) é:

\[
\boxed{
\epsilon^2=2\widehat\tau
=
\frac{2\tau}{\ell_C^2}.
}
\]

Ou:

\[
\boxed{
\epsilon=\sqrt{\frac{2\tau}{\ell_C^2}}.
}
\]

Essa relação é uma convenção de redução numa janela efetiva. Ela não transforma
\(\tau\) em campo local.

Dentro de uma janela física local:

\[
\boxed{
\tau
\text{ e }
\epsilon
\text{ são tratados como parâmetros fixos.}
}
\]

Entre janelas:

\[
\boxed{
\tau
\text{ pode variar como parâmetro de escala geométrica.}
}
\]

---

## 9. A evolução em \(\tau\) é física ou auxiliar?

A resposta precisa é:

\[
\boxed{
\text{a evolução em }\tau\text{ é física como fluxo geométrico/de escala,
mas não é evolução cronológica local.}
}
\]

Ela é física porque altera:

1. a resolução geométrica;
2. o fluxo de Perelman;
3. a escala efetiva;
4. o kernel difusivo;
5. a janela de regularização geométrica.

Mas ela é auxiliar em relação à dinâmica local em \(N^4\), onde o tempo físico
é:

\[
\boxed{
t.
}
\]

Portanto:

\[
\boxed{
\partial_\tau
\text{ é derivada de fluxo/escala;}
\qquad
\partial_t
\text{ é derivada temporal física local.}
}
\]

---

## 10. Mapa final dos usos de \(\tau\)

| Uso no texto | Status final | Forma correta |
|---|---|---|
| tempo de fluxo | correto com ressalva | fluxo geométrico, não tempo cronológico |
| variável de área | correto | \([\tau]=L^2\) |
| tempo difusivo | correto | parâmetro do kernel de calor |
| logaritmo de escala | incorreto diretamente | \(s=\log(\tau/\ell_C^2)\) |
| variável adimensional | incorreto diretamente | \(\widehat\tau=\tau/\ell_C^2\) |
| coordenada imaginária associada a \(t\) | correto só com fator dimensional | \(z_\tau=\tau+i\nu_0t\) |
| \(\tau+it\) | incorreto | \(z_\tau=\tau+i\nu_0t\) |
| \(t=-i\tau\) | incorreto como identidade | usar contorno em \(z_\tau\) |
| \(\tau^{-2}\) no bulk | incorreto para \(n=4\) complexo | \((4\pi\tau)^{-4}\) |
| \(d\tau/\tau\) | correto | medida logarítmica adimensional |

---

## 11. Correções oficiais aos trechos antigos

### 11.1 Onde o texto diz \(\tau+it\)

Substituir por:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

### 11.2 Onde o texto diz \(t=-i\tau\)

Substituir por:

\[
\boxed{
\text{continuação causal no plano }z_\tau,
\text{ sem identificação direta entre }t\text{ e }\tau.
}
\]

### 11.3 Onde o texto diz \(\tau\) adimensional

Substituir por:

\[
\boxed{
\widehat\tau=\frac{\tau}{\ell_C^2}.
}
\]

### 11.4 Onde o texto diz \(\ln\mu\to\tau\)

Substituir por:

\[
\boxed{
s=\log\left(\frac{\tau}{\ell_C^2}\right),
\qquad
s\sim-2\log(\mu\ell_C).
}
\]

### 11.5 Onde o texto usa \((4\pi\tau)^{-n/2}\)

Corrigir conforme a convenção dimensional:

Se \(d\) é dimensão real:

\[
\boxed{
(4\pi\tau)^{-d/2}.
}
\]

Se \(n\) é dimensão complexa e \(d=2n\):

\[
\boxed{
(4\pi\tau)^{-n}.
}
\]

Na GDQ final:

\[
\boxed{
n=4,
\qquad
(4\pi\tau)^{-4}.
}
\]

---

## 12. Fórmula final de referência

A forma final para a Questão 6 é:

\[
\boxed{
\tau\in\mathbb R_+,
\qquad
[\tau]=L^2.
}
\]

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

\[
\boxed{
\widehat\tau=\frac{\tau}{\ell_C^2},
\qquad
s=\log\widehat\tau.
}
\]

\[
\boxed{
\frac{\partial}{\partial s}
=
\tau\frac{\partial}{\partial\tau}.
}
\]

\[
\boxed{
K(\tau)\sim(4\pi\tau)^{-4}
\quad
\text{no bulk }M=\mathbb R^4\times T^4.
}
\]

---

## 13. Status da Questão 6

\[
\boxed{
\text{Questão 6 fechada oficialmente.}
}
\]

A teoria passa a usar uma única ontologia:

\[
\boxed{
\tau
\text{ é fluxo geométrico/difusivo com dimensão }L^2;
}
\]

\[
\boxed{
t
\text{ é tempo físico cronológico;}
}
\]

\[
\boxed{
z_\tau
\text{ é a variável causal complexa;}
}
\]

\[
\boxed{
s
\text{ é a variável logarítmica de escala/RG.}
}
\]

