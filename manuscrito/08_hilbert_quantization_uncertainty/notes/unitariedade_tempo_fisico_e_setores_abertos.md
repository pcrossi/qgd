---
title: "Unitariedade em tempo físico e setores abertos"
---

# Unitariedade em tempo físico e setores abertos

Esta nota separa quatro objetos distintos:

1. o fluxo geométrico em $\tau$;
2. o semigrupo euclidiano usado na reconstrução;
3. a evolução unitária no tempo físico $t$;
4. a evolução dissipativa aparente de um setor projetado ou aberto.

O ponto central é: a GDQ pode ter fluxo geométrico dissipativo em $\tau$ sem
perder unitariedade física em $t$, desde que o setor reconstruído possua
Hamiltoniano autoadjunto no espaço de Hilbert físico.

## 1. Dado estrutural

O espaço físico reconstruído é

$$
\mathcal H_{\rm phys}
=
\overline{
\mathcal D_+/
(\mathcal N+\mathcal G)
}.
$$

Aqui $\mathcal D_+$ é o domínio de funcionais de suporte euclidiano positivo,
$\mathcal N$ é o subespaço de norma nula pela reflexão positiva e
$\mathcal G$ representa redundâncias geométricas removidas por quociente.

As translações euclidianas positivas induzem um semigrupo

$$
T_E(a+b)=T_E(a)T_E(b),
\qquad
a,b\ge0.
$$

Quando o setor satisfaz as hipóteses de reconstrução, esse semigrupo é positivo
e contrativo:

$$
\|T_E(a)\|\le1.
$$

Então existe um operador autoadjunto positivo $H$ tal que

$$
T_E(a)=e^{-aH/\hbar},
\qquad
H=H^\dagger,
\qquad
H\ge0.
$$

Esse $H$ é o gerador físico reconstruído. Ele não é o gerador do fluxo
geométrico bruto em $\tau$.

## 2. Prova por Stone

Se $H$ é autoadjunto em um domínio denso $D(H)\subset\mathcal H_{\rm phys}$, o
teorema de Stone fornece o grupo unitário fortemente contínuo

$$
U(t)=e^{-itH/\hbar}.
$$

Pelo cálculo funcional espectral,

$$
U(t)^\dagger
=
e^{+itH/\hbar}.
$$

Logo

$$
U(t)^\dagger U(t)
=
e^{+itH/\hbar}e^{-itH/\hbar}
=I.
$$

Portanto, para quaisquer $\Psi,\Phi\in\mathcal H_{\rm phys}$,

$$
\langle U(t)\Psi,U(t)\Phi\rangle
=
\langle\Psi,\Phi\rangle.
$$

Em particular,

$$
\|U(t)\Psi\|^2=\|\Psi\|^2.
$$

## 3. Prova diferencial

No domínio comum em que a equação de Schrödinger reconstruída faz sentido,

$$
i\hbar\frac{d\Psi}{dt}=H\Psi,
\qquad
i\hbar\frac{d\Phi}{dt}=H\Phi.
$$

Então

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle
=
\left\langle\frac{d\Psi}{dt},\Phi\right\rangle
+
\left\langle\Psi,\frac{d\Phi}{dt}\right\rangle.
$$

Substituindo as equações de movimento,

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle
=
\frac{i}{\hbar}\langle H\Psi,\Phi\rangle
-
\frac{i}{\hbar}\langle\Psi,H\Phi\rangle.
$$

Como $H=H^\dagger$,

$$
\langle H\Psi,\Phi\rangle
=
\langle\Psi,H\Phi\rangle.
$$

Assim,

$$
\frac{d}{dt}\langle\Psi,\Phi\rangle=0.
$$

Tomando $\Phi=\Psi$,

$$
\frac{d}{dt}\|\Psi(t)\|^2=0.
$$

## 4. Contração euclidiana não é perda de probabilidade

O semigrupo euclidiano é

$$
T_E(a)=e^{-aH/\hbar},
\qquad
a\ge0.
$$

Se $H\ge0$, suas componentes espectrais são amortecidas por
$e^{-aE/\hbar}$. Isso é contração em parâmetro euclidiano, não evolução física
em tempo real.

A evolução física reconstruída é

$$
U(t)=e^{-itH/\hbar}.
$$

As componentes espectrais recebem fases $e^{-itE/\hbar}$, de módulo unitário.
Logo:

$$
\boxed{
\text{contração em }a\text{ ou em }\tau
\neq
\text{perda de probabilidade em }t.
}
$$

Na linguagem da GDQ, $\tau$ organiza fluxo, escala, regularização e seleção de
setores. O tempo físico $t$ organiza a evolução observável depois da
reconstrução operacional.

## 5. Estados instáveis e projeções

Um estado instável não exige abandonar a unitariedade fundamental. Ele indica
que o observador escolheu um setor parcial.

Decomponha o Hilbert total fechado como

$$
\mathcal H_{\rm total}
=
\mathcal H_P\oplus\mathcal H_Q.
$$

O setor $P$ é o canal monitorado; $Q$ é o restante do campo, ambiente, contínuo
ou canais não registrados. Se

$$
H_{\rm total}=H_{\rm total}^\dagger,
$$

então

$$
U_{\rm total}(t)
=
e^{-itH_{\rm total}/\hbar}
$$

é unitário.

Porém, ao eliminar $Q$, o setor $P$ pode adquirir um gerador efetivo não
autoadjunto:

$$
H_{\rm eff}
=
H_{PP}
\Delta H
-
\frac{i}{2}\Gamma,
\qquad
\Gamma\ge0.
$$

Assim, a norma projetada pode decair:

$$
\|P\Psi(t)\|^2<\|P\Psi(0)\|^2.
$$

Fisicamente, a probabilidade não desapareceu. Ela saiu do canal $P$ e foi para
$Q$.

## 6. Teoria aberta como redução efetiva

Se o aparelho ou ambiente não é acompanhado explicitamente, o estado reduzido é

$$
\rho_P(t)
=
\operatorname{Tr}_Q\rho_{\rm total}(t).
$$

A evolução total continua sendo

$$
\rho_{\rm total}(t)
=
U_{\rm total}(t)\rho_{\rm total}(0)U_{\rm total}(t)^\dagger.
$$

Sob aproximações Markovianas, a evolução reduzida pode ser escrita como

$$
\frac{d\rho_P}{dt}
=
-
\frac{i}{\hbar}[H_P,\rho_P]
+
\sum_\alpha
\left(
L_\alpha\rho_P L_\alpha^\dagger
-
\frac12
\{L_\alpha^\dagger L_\alpha,\rho_P\}
\right).
$$

Esta equação é uma linguagem efetiva de subsistema. Ela não altera a ação
oficial da GDQ. A ação oficial descreve o sistema geométrico fechado; a equação
aberta aparece quando parte dos graus de liberdade é integrada ou ignorada.

## 7. Status lógico

O resultado é um teorema condicional:

$$
\boxed{
H=H^\dagger
\quad\Longrightarrow\quad
U(t)=e^{-itH/\hbar}
\text{ preserva o produto interno físico.}
}
$$

A parte não condicional é a álgebra da prova. A parte condicional é a
verificação, setor por setor, de que a reconstrução fornece $H$ autoadjunto e
domínio físico adequado.

