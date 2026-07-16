# Questão 13 — Por que \(\mathcal U=\rho\)?

## 1. Pergunta

A Questão 13 pergunta:

\[
\boxed{
\text{por que a medida }\mathcal U\text{ é igual à densidade }\rho?
}
\]

O problema apontado em `13-0.md` é correto:

\[
\boxed{
\text{duas funções satisfazerem a mesma equação de transporte não implica que
sejam iguais.}
}
\]

Para provar igualdade por evolução, seria necessário fornecer:

1. mesmas condições iniciais;
2. mesmas condições de contorno;
3. espaço funcional;
4. teorema de unicidade aplicável.

Mas, na formulação já consolidada da GDQ, a resposta mais forte é outra:

\[
\boxed{
\mathcal U\text{ não é uma segunda função independente que precisa ser
identificada dinamicamente com }\rho.
}
\]

Ela é definida constitucionalmente a partir do mesmo campo fundamental
\(f,\bar f\).

---

## 2. Correção da pergunta

A igualdade literal:

\[
\mathcal U=\rho
\]

não é a forma final correta da ação oficial.

A forma correta, já fixada nas Questões 4, 5 e 9, é:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

Como:

\[
\boxed{
\rho
=
e^{-(f+\bar f)/2},
}
\]

segue:

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

Portanto a igualdade exata é:

\[
\boxed{
(4\pi z_\tau)^n\mathcal U=\rho.
}
\]

Ou, definindo a medida sem o fator de kernel:

\[
\boxed{
\widetilde{\mathcal U}
:=
(4\pi z_\tau)^n\mathcal U,
}
\]

temos:

\[
\boxed{
\widetilde{\mathcal U}=\rho.
}
\]

Essa é a forma que deve substituir qualquer frase ambígua do tipo
\(\mathcal U=\rho\).

---

## 3. Definição de \(\rho\)

O campo fundamental complexo da GDQ é:

\[
\boxed{
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
}
\]

Seu conjugado é:

\[
\boxed{
\bar f
=
-\frac{S_I}{\hbar}
-i\frac{S_R}{\hbar}.
}
\]

Somando:

\[
\boxed{
f+\bar f
=
-\frac{2S_I}{\hbar}.
}
\]

Logo:

\[
\boxed{
e^{-(f+\bar f)/2}
=
e^{S_I/\hbar}.
}
\]

Define-se a densidade hidrodinâmica de Madelung--Perelman como:

\[
\boxed{
\rho
:=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
}
\]

Assim:

\[
\boxed{
\rho\text{ não é campo novo independente;}
\quad
\rho\text{ é projeção real positiva de }f.
}
\]

---

## 4. Definição de \(\mathcal U\)

A medida que entra na ação oficial é:

\[
\boxed{
\mathcal U[f,\bar f,z_\tau]
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

Com:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

Portanto:

\[
\boxed{
\mathcal U[f,\bar f,z_\tau]
=
\frac{\rho[f,\bar f]}{(4\pi z_\tau)^n}.
}
\]

Isso mostra que \(\mathcal U\) tem duas partes:

1. uma parte material/probabilística:

\[
\rho=e^{-(f+\bar f)/2};
\]

2. uma parte de kernel geométrico/difusivo:

\[
(4\pi z_\tau)^{-n}.
\]

Logo:

\[
\boxed{
\mathcal U\text{ é a densidade de Perelman--Madelung ponderada pelo kernel de
calor causal.}
}
\]

---

## 5. Por que não é preciso teorema de unicidade

Se \(\mathcal U\) e \(\rho\) fossem campos independentes, o argumento:

\[
\partial_\tau\mathcal U+\nabla\cdot(\mathcal Uv)=0
\]

e:

\[
\partial_\tau\rho+\nabla\cdot(\rho v)=0
\]

não bastaria para concluir:

\[
\mathcal U=\rho.
\]

De fato, a diferença:

\[
w:=\mathcal U-\rho
\]

satisfaria:

\[
\partial_\tau w+\nabla\cdot(wv)=0.
\]

Mas isso só implica \(w=0\) se:

\[
w|_{\tau=\tau_0}=0
\]

e se houver unicidade no espaço funcional escolhido.

Na GDQ final, essa rota não é necessária, porque:

\[
\boxed{
\rho
=
e^{-(f+\bar f)/2}
}
\]

e:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
}
\]

são definições derivadas do mesmo campo fundamental \(f\).

Portanto:

\[
\boxed{
\mathcal U\text{ e }\rho\text{ não são duas soluções independentes de uma
mesma PDE.}
}
\]

São a mesma densidade geométrica escrita com ou sem o fator de kernel.

---

## 6. Se alguém exigir a prova por unicidade

Apesar de a resposta constitucional ser suficiente, é possível registrar a
rota alternativa por unicidade.

Defina:

\[
\widetilde{\mathcal U}
:=
(4\pi z_\tau)^n\mathcal U.
\]

A pergunta correta passa a ser:

\[
\boxed{
\widetilde{\mathcal U}=\rho?
}
\]

Suponha que \(\widetilde{\mathcal U}\) e \(\rho\) satisfaçam a mesma equação de
transporte:

\[
\boxed{
\partial_\tau u+\nabla_A(u v^A)=0
}
\]

no domínio:

\[
\boxed{
M=\mathbb R^4\times T^4.
}
\]

Assuma:

1. \(v\in L^1([0,T];W^{1,\infty}_{\rm loc}(M))\);
2. \(u\in L^\infty([0,T];L^1(M))\);
3. \(u\ge0\);
4. \(u\) possui decaimento suficiente no setor \(\mathbb R^4\);
5. \(u\) é periódico no setor \(T^4\);
6. as condições de bordo em \(\gamma\) anulam termos exatos;
7. a condição inicial é a mesma:

\[
\boxed{
\widetilde{\mathcal U}(\tau_0,x)=\rho(\tau_0,x).
}
\]

Então:

\[
w:=\widetilde{\mathcal U}-\rho
\]

satisfaz:

\[
\partial_\tau w+\nabla_A(wv^A)=0,
\qquad
w(\tau_0)=0.
\]

Pelo teorema de unicidade para a equação linear de transporte com campo de
velocidades Lipschitz em espaço, segue:

\[
\boxed{
w(\tau,x)=0
\quad
\forall \tau\in[0,T].
}
\]

Logo:

\[
\boxed{
\widetilde{\mathcal U}=\rho.
}
\]

E portanto:

\[
\boxed{
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

Essa rota é aceitável, mas é secundária. A formulação final da GDQ não depende
dela, porque a igualdade já é uma definição estrutural.

---

## 7. Espaço funcional mínimo

Para a rota por unicidade, um espaço funcional suficiente é:

\[
\boxed{
\rho,\widetilde{\mathcal U}
\in
C^1([0,T]\times M)
\cap
L^1(M)
}
\]

com:

\[
\boxed{
v\in C^1([0,T]\times M).
}
\]

Essa hipótese é forte, mas simples.

Uma versão mais fraca e mais moderna usa soluções renormalizadas de
DiPerna--Lions, exigindo regularidade Sobolev para \(v\). Porém a GDQ não
precisa dessa sofisticação para fechar a questão conceitual, porque a igualdade
principal não vem da PDE.

---

## 8. Condições iniciais e de contorno

Na interpretação por unicidade, as condições iniciais são:

\[
\boxed{
\widetilde{\mathcal U}(\tau_0,x)
=
\rho(\tau_0,x)
=
e^{-(f(\tau_0,x)+\bar f(\tau_0,x))/2}.
}
\]

As condições de contorno são:

1. periodicidade em \(T^4\):

\[
u(x+\ell_a)=u(x);
\]

2. decaimento em \(\mathbb R^4\):

\[
u(x)v(x)\to0
\quad
\text{no infinito};
\]

3. ou suporte compacto para variações;
4. fechamento de termos exatos pelo contorno \(\gamma\):

\[
\boxed{
\oint_\gamma dF=0.
}
\]

Com isso, a integração por partes não gera fluxo de bordo não contabilizado.

---

## 9. Relação com a regra de Born

A função de onda efetiva é:

\[
\boxed{
\Psi
=
\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Como:

\[
\rho=e^{S_I/\hbar},
\]

temos:

\[
\sqrt\rho
=
e^{S_I/(2\hbar)}.
}
\]

Logo:

\[
\boxed{
|\Psi|^2
=
\rho.
}
\]

Portanto a regra de Born, na camada efetiva, é:

\[
\boxed{
P(\Omega)
=
\int_\Omega |\Psi|^2\,d\mu
=
\int_\Omega \rho\,d\mu.
}
\]

Na medida da ação:

\[
\boxed{
\mathcal U\,d^{2n}z
=
\frac{\rho}{(4\pi z_\tau)^n}d^{2n}z.
}
\]

O fator \((4\pi z_\tau)^{-n}\) pertence ao kernel geométrico/difusivo, não muda
o fato de que a densidade probabilística local é:

\[
\boxed{
\rho=|\Psi|^2.
}
\]

---

## 10. O que deve ser corrigido no texto original

Sempre que o texto disser:

\[
\mathcal U=\rho,
\]

deve-se substituir por uma das formas:

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}
}
\]

ou:

\[
\boxed{
(4\pi z_\tau)^n\mathcal U=\rho.
}
\]

Se o texto estiver trabalhando com a medida sem kernel, pode declarar:

\[
\boxed{
\widetilde{\mathcal U}=\rho.
}
\]

Mas deve definir:

\[
\boxed{
\widetilde{\mathcal U}:=(4\pi z_\tau)^n\mathcal U.
}
\]

Assim a notação fica consistente com a ação oficial.

---

## 11. Status da Questão 13

\[
\boxed{
\text{Questão 13 fechada oficialmente.}
}
\]

A resposta final é:

\[
\boxed{
\rho
=
e^{-(f+\bar f)/2}.
}
\]

E:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

Portanto:

\[
\boxed{
(4\pi z_\tau)^n\mathcal U=\rho.
}
\]

A igualdade não depende de duas soluções independentes satisfazerem a mesma
equação de transporte. Ela decorre da definição constitucional de
\(\mathcal U\) e da definição hidrodinâmica de \(\rho\) a partir do mesmo campo
fundamental \(f\).

Se alguém insistir na rota dinâmica, a igualdade exige mesmas condições
iniciais, mesmas condições de contorno, espaço funcional adequado e unicidade
da equação de transporte.

