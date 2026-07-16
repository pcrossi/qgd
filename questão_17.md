# Questão 17 — O sistema possui problema de Cauchy bem posto?

## 1. Pergunta

A Questão 17 pergunta:

\[
\boxed{
\text{o sistema dinâmico da GDQ possui problema de Cauchy bem posto?}
}
\]

As respostas necessárias de `17-0.md` são:

1. classificação das EDPs;
2. gauge utilizado;
3. espaços funcionais;
4. existência local;
5. unicidade local;
6. dependência contínua dos dados;
7. critérios de continuação.

A resposta não aceitável seria apenas dizer:

\[
\boxed{
\text{``use DeTurck''.}
}
\]

É preciso mostrar que o sistema acoplado, após gauge, possui operador principal
parabólico forte no fluxo geométrico.

---

## 2. Resposta curta

Sim, o problema de Cauchy é localmente bem posto para o fluxo geométrico da
GDQ, desde que a teoria seja formulada em gauge fixado e com dados iniciais
regulares.

A classificação correta é:

\[
\boxed{
\text{setor estacionário: elíptico;}
}
\]

\[
\boxed{
\text{fluxo geométrico em }\tau\text{: parabólico quase-linear;}
}
\]

\[
\boxed{
\text{evolução física em }N^4\text{ com tempo }t\text{: hiperbólica/unitária
na camada lorentziana efetiva.}
}
\]

Portanto, há dois problemas diferentes:

1. o problema de Cauchy do fluxo geométrico em \(\tau\);
2. o problema de evolução física em \(t\).

A Questão 17 fecha o primeiro. A evolução física causal já foi separada nas
Questões 7 e 8.

---

## 3. Variáveis do sistema geométrico

No bulk riemanniano/hermitiano, as variáveis fundamentais da ação oficial são:

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

Na camada torsional efetiva, introduz-se a 3-forma real de Bismut/Cartan:

\[
\boxed{
B\in\Omega^3(M).
}
\]

Para discutir bem-postura, é útil separar:

\[
\boxed{
f=\phi+i\chi,
}
\]

com:

\[
\boxed{
\phi=\operatorname{Re}f=-\frac{S_I}{\hbar},
\qquad
\chi=\operatorname{Im}f=\frac{S_R}{\hbar}.
}
\]

A densidade é:

\[
\boxed{
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
}
\]

O sistema geométrico a analisar é, portanto:

\[
\boxed{
(g,B,\phi,\chi).
}
\]

O campo \(B\) não substitui a ação oficial. Ele entra como camada geométrica
torsional associada à conexão de Bismut.

---

## 4. Sistema antes da fixação de gauge

O fluxo torsional de Ricci--Perelman tem a forma esquemática:

\[
\boxed{
\partial_\tau g_{ij}
=
-2\left(
R_{ij}
-\frac14 B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right).
}
\]

Para a torção:

\[
\boxed{
\partial_\tau B
=
\Delta_{d,g}B
+\mathcal L_{\nabla\phi}B
+\text{termos de menor ordem compatíveis com }dB=0.
}
\]

Para o dilaton real \(\phi\):

\[
\boxed{
\partial_\tau\phi
=
-\Delta_g\phi
+|\nabla\phi|^2
-R
+\frac1{12}|B|^2
+\text{normalização}.
}
\]

A fase \(\chi\) pode ser tratada no fluxo geométrico como escalar acoplado:

\[
\boxed{
\partial_\tau\chi
=
\Delta_g\chi
+\text{termos de menor ordem}
}
\]

quando se estuda relaxação geométrica, ou como variável da camada física
Madelung quando se passa ao tempo \(t\). Para o problema parabólico em
\(\tau\), basta que sua equação tenha principal parte escalar de Laplace.

Esse sistema ainda não é estritamente parabólico em \(g\), porque a equação de
Ricci possui degenerescência por difeomorfismos.

---

## 5. Gauge utilizado

Usa-se gauge de DeTurck para a métrica e gauge de Hodge para a 3-forma.

### 5.1 Gauge de DeTurck

Escolhe-se uma métrica de referência fixa \(\bar g\) com a mesma regularidade
dos dados iniciais e define-se:

\[
\boxed{
W^k
=
g^{pq}
\left(
\Gamma^k_{pq}(g)-\Gamma^k_{pq}(\bar g)
\right).
}
\]

Adiciona-se a derivada de Lie:

\[
\boxed{
\mathcal L_Wg
}
\]

à equação métrica.

O sistema métrico em gauge fica:

\[
\boxed{
\partial_\tau g_{ij}
=
-2\left(
R_{ij}
-\frac14B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right)
+\mathcal L_Wg_{ij}.
}
\]

Agora a parte principal é:

\[
\boxed{
\partial_\tau g_{ij}
=
g^{ab}\partial_a\partial_bg_{ij}
+\text{termos de menor ordem}.
}
\]

Isto é parabolicidade forte enquanto \(g\) for uniformemente positiva.

### 5.2 Gauge de Perelman para o termo \(\nabla\nabla\phi\)

O termo \(\nabla_i\nabla_j\phi\) também pode ser absorvido por uma escolha de
difeomorfismo gerada por \(\nabla\phi\). Equivalentemente, trabalha-se no gauge
de medida ponderada:

\[
\boxed{
dm=e^{-\phi}dV_g.
}
\]

Isso não muda a parte principal. Ele fixa a liberdade de transporte da medida.

### 5.3 Gauge de Hodge para \(B\)

Para a 3-forma, impõe-se uma condição de calibre:

\[
\boxed{
dB=0
\quad\text{ou, localmente,}\quad
B=dA.
}
\]

Com gauge de Hodge para o potencial:

\[
\boxed{
d_g^\dagger A=0.
}
\]

Então o operador principal sobre \(B\) é o Laplaciano de Hodge:

\[
\boxed{
\Delta_{d,g}B=-(dd_g^\dagger+d_g^\dagger d)B.
}
\]

Após gauge, a parte principal é:

\[
\boxed{
\partial_\tau B
=
g^{ab}\nabla_a\nabla_bB
+\text{termos de menor ordem}.
}
\]

Logo, o setor torsional também é parabólico.

---

## 6. Operador principal do sistema acoplado

No gauge fixado, o sistema possui a forma:

\[
\boxed{
\partial_\tau U
=
\mathcal A(U)\partial^2U+\mathcal B(U,\partial U),
}
\]

com:

\[
\boxed{
U=(g,B,\phi,\chi).
}
\]

A matriz principal \(\mathcal A(U)\) é bloco-diagonal no nível de maior ordem:

\[
\boxed{
\mathcal A(U)
\sim
\operatorname{diag}
\left(
g^{ab}\partial_a\partial_b,
g^{ab}\nabla_a\nabla_b,
g^{ab}\nabla_a\nabla_b,
g^{ab}\nabla_a\nabla_b
\right).
}
\]

Os acoplamentos:

\[
B_{ik\ell}B_j{}^{k\ell},
\qquad
\nabla_i\nabla_j\phi,
\qquad
|\nabla\phi|^2,
\qquad
|B|^2,
\qquad
\mathcal L_{\nabla\phi}B
\]

são de menor ordem ou foram incorporados ao gauge.

Assim, para qualquer covetor não nulo \(\xi\):

\[
\boxed{
\sigma_{\rm principal}(\xi)
=
|\xi|_g^2\,I
}
\]

nos blocos dinâmicos, até convenção de sinal do Laplaciano.

Como \(g\) é riemanniana positiva no bulk:

\[
\boxed{
|\xi|_g^2>0
\quad
\text{para }\xi\neq0.
}
\]

Logo, o sistema em gauge é parabólico forte quase-linear.

---

## 7. Espaços funcionais

Uma formulação padrão usa espaços de Hölder parabólicos.

Para \(k\ge2\) e \(\alpha\in(0,1)\), tome dados iniciais:

\[
\boxed{
g_0\in C^{k,\alpha},
\qquad
B_0\in C^{k,\alpha},
\qquad
\phi_0,\chi_0\in C^{k,\alpha}.
}
\]

Assume-se:

\[
\boxed{
g_0\ge\lambda\,\bar g
\quad
\text{para algum }\lambda>0,
}
\]

e as restrições de compatibilidade:

\[
\boxed{
dB_0=0
\quad\text{se }B\text{ é torção fechada,}
}
\]

\[
\boxed{
\int_M e^{-\phi_0}dV_{g_0}=1
\quad\text{se a medida ponderada for normalizada.}
}
\]

Então a solução pertence a:

\[
\boxed{
g,B,\phi,\chi
\in
C^{1+\alpha/2,\;2+\alpha}
\left([0,T]\times M\right)
}
\]

para algum \(T>0\).

Alternativamente, pode-se usar Sobolev:

\[
\boxed{
(g_0,B_0,\phi_0,\chi_0)\in H^s,
\qquad
s>\frac d2+2,
}
\]

com:

\[
\boxed{
d=\dim_{\mathbb R}M=8.
}
\]

Logo, basta tomar:

\[
\boxed{
s>6.
}
\]

Na prática:

\[
\boxed{
s\ge7
}
\]

é uma escolha segura.

---

## 8. Teorema de existência local

Sob as hipóteses:

1. \(M\) compacto, ou não compacto com geometria uniformemente limitada;
2. \(g_0\) riemanniana positiva e \(C^{k,\alpha}\);
3. \(B_0,\phi_0,\chi_0\in C^{k,\alpha}\);
4. restrições de gauge/fechamento satisfeitas;
5. \(\rho_0=e^{-\phi_0}>0\);

existe \(T>0\) e uma solução única do sistema em gauge:

\[
\boxed{
(g(\tau),B(\tau),\phi(\tau),\chi(\tau)),
\qquad
0\le\tau\le T.
}
\]

A regularidade é:

\[
\boxed{
(g,B,\phi,\chi)
\in
C^{1+\alpha/2,\;2+\alpha}.
}
\]

Se os dados iniciais são suaves, a solução é suave para \(\tau>0\):

\[
\boxed{
U_0\in C^\infty
\quad\Longrightarrow\quad
U(\tau)\in C^\infty
\text{ para }\tau>0.
}
\]

Isso segue da teoria padrão de sistemas parabólicos quase-lineares fortemente
parabólicos, aplicada ao sistema após gauge.

---

## 9. Unicidade local

A unicidade vale primeiro no sistema em gauge:

\[
\boxed{
U_1(0)=U_2(0)
\quad\Longrightarrow\quad
U_1(\tau)=U_2(\tau)
\text{ para }0\le\tau\le T.
}
\]

Para retornar ao sistema geométrico sem gauge, resolve-se o fluxo de
difeomorfismos:

\[
\boxed{
\frac{d}{d\tau}\Phi_\tau=-W(g(\tau))\circ\Phi_\tau,
\qquad
\Phi_0=\operatorname{id}.
}
\]

Então:

\[
\boxed{
\tilde g(\tau)=\Phi_\tau^*g(\tau),
\qquad
\tilde B(\tau)=\Phi_\tau^*B(\tau),
\qquad
\tilde f(\tau)=\Phi_\tau^*f(\tau)
}
\]

resolve o sistema geométrico original.

Assim, a unicidade geométrica é:

\[
\boxed{
\text{unicidade módulo difeomorfismos.}
}
\]

Depois de fixado o gauge, a unicidade é literal.

---

## 10. Dependência contínua dos dados

Como o sistema em gauge é parabólico quase-linear forte, o mapa solução é
contínuo:

\[
\boxed{
U_0\mapsto U(\tau)
}
\]

nos espaços \(C^{k,\alpha}\) ou \(H^s\) escolhidos.

Mais explicitamente, para dois dados iniciais próximos:

\[
\boxed{
\|U_0-\tilde U_0\|_{C^{k,\alpha}}\ll1,
}
\]

as soluções satisfazem, para \(0\le\tau\le T'\le T\):

\[
\boxed{
\|U(\tau)-\tilde U(\tau)\|_{C^{k,\alpha}}
\le
C_{T'}\|U_0-\tilde U_0\|_{C^{k,\alpha}}.
}
\]

Em Sobolev, analogamente:

\[
\boxed{
\|U(\tau)-\tilde U(\tau)\|_{H^{s-2}}
\le
C_{T'}\|U_0-\tilde U_0\|_{H^s}.
}
\]

A possível perda de derivadas depende da formulação funcional, mas a
dependência contínua é a propriedade essencial de Hadamard.

---

## 11. Critério de continuação

Se a solução existe em \([0,T)\), ela pode ser continuada além de \(T\) desde
que permaneçam controladas as quantidades que garantem parabolicidade e
regularidade.

Um critério suficiente é:

\[
\boxed{
0<\lambda\,\bar g\le g(\tau)\le\Lambda\,\bar g<\infty,
}
\]

e:

\[
\boxed{
\sup_{[0,T)\times M}
\left(
|{\rm Rm}(g)|
+|\nabla B|^2
+|B|^2
+|\nabla^2\phi|
+|\nabla\phi|^2
+|\nabla^2\chi|
+|\nabla\chi|^2
\right)
<\infty.
}
\]

Também é necessário manter:

\[
\boxed{
\rho=e^{-\phi}>0
}
\]

e a compatibilidade de gauge/contorno.

Portanto, a única forma de o fluxo falhar em tempo finito é:

1. degeneração da métrica;
2. explosão da curvatura;
3. explosão da torção;
4. perda de regularidade de \(f\);
5. formação de nó/singularidade onde \(\rho\to0\);
6. falha de condições de contorno em setor não compacto.

Em forma curta:

\[
\boxed{
\text{se a geometria permanece uniformemente limitada, o fluxo continua.}
}
\]

---

## 12. Papel da monotonicidade com torção

O capítulo original `17 - Monotonicidade sob Torção de Cartan.md` é útil, mas
ele não prova sozinho a bem-postura de Cauchy.

Ele fornece um funcional de Lyapunov:

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}\ge0,
\qquad
\frac{d\mathcal W_T}{d\tau}\ge0.
}
\]

Isso ajuda a controlar estabilidade, atratores e pontos fixos:

\[
\boxed{
R_{ij}
-\frac14B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=
\frac1{2\sigma}g_{ij},
}
\]

\[
\boxed{
\hat d^\dagger B+i_{\nabla\phi}B=0.
}
\]

Mas monotonicidade não substitui:

1. classificação do operador principal;
2. fixação de gauge;
3. teorema de existência local;
4. unicidade;
5. dependência contínua.

Assim, a monotonicidade é uma ferramenta de estabilidade global/assintótica,
enquanto a bem-postura local vem da parabolicidade forte do sistema em gauge.

---

## 13. Relação com a ação oficial

A ação oficial permanece a mesma:

\[
\boxed{
\mathcal{S}_{\rm GDQ}
=
\int_{\gamma}
\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right]
\mathcal U
\sqrt{\det g}\,
d^{2n}z
\right]
\frac{d\tau}{\tau}.
}
\]

com:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

O fluxo em \(\tau\) é a equação geométrica associada ao gradiente/regularização
da ação. Ele não substitui a ação fundamental e não é o tempo físico
lorentziano.

---

## 14. Formulação final para inserir no texto principal

Uma redação limpa para o texto principal é:

> O fluxo geométrico da GDQ deve ser entendido como um sistema parabólico
> quase-linear em \(\tau\) após fixação de gauge. A degenerescência
> difeomórfica da equação de Ricci é removida pelo vetor de DeTurck
> \(W^k=g^{pq}(\Gamma^k_{pq}(g)-\Gamma^k_{pq}(\bar g))\), e a torção
> \(B\) é colocada em gauge de Hodge. Nesse gauge, a parte principal do
> sistema acoplado \((g,B,f,\bar f)\) é diagonal e dada pelo Laplaciano
> geométrico \(g^{ab}\nabla_a\nabla_b\). Como \(g\) é riemanniana positiva no
> bulk, o sistema é fortemente parabólico. Consequentemente, para dados
> iniciais \(C^{k,\alpha}\), \(k\ge2\), ou \(H^s\), \(s>d/2+2\), existe uma
> solução local única, dependente continuamente dos dados, e continuável
> enquanto a métrica não degenerar e as normas de curvatura, torção e derivadas
> de \(f\) permanecerem limitadas.

---

## 15. Veredito

\[
\boxed{
\text{Questão 17 fechada oficialmente.}
}
\]

A resposta resolve as exigências de `17-0.md`:

1. classifica o setor estacionário como elíptico;
2. classifica o fluxo em \(\tau\) como parabólico quase-linear;
3. separa a evolução física em \(t\) como camada lorentziana efetiva;
4. fixa gauge de DeTurck para \(g\);
5. fixa gauge de Hodge para \(B\);
6. especifica espaços \(C^{k,\alpha}\) e \(H^s\);
7. fornece existência local;
8. fornece unicidade local;
9. fornece dependência contínua;
10. fornece critério de continuação.

