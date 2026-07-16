# Derivação Rigorosa do Setor de Spin por Circulação

## 1. Objetivo

Construir, na geometria candidata

\[
M=\mathbb R^4\times T^4,
\]

um setor no qual:

\[
\operatorname{Hol}_\gamma=-1
\]

para uma volta de \(2\pi\) no círculo interno ativo,

\[
\operatorname{Hol}_{\gamma^2}=+1
\]

para duas voltas, e

\[
\oint_\gamma p
=h\left(n+\frac12\right).
\]

A derivação abaixo separa:

1. existência da estrutura spin;
2. escolha da estrutura spin antiperiódica;
3. ação da rotação sobre espinores;
4. espectro de circulação;
5. contribuição possível da torção de Bismut.

---

## 2. Existência da estrutura spin

Os fibrados tangentes de \(\mathbb R^4\) e \(T^4\) são triviais:

\[
T\mathbb R^4\simeq\mathbb R^4\times\mathbb R^4,
\]

\[
TT^4\simeq T^4\times\mathbb R^4.
\]

Logo,

\[
TM
\simeq
M\times\mathbb R^8.
\]

Portanto, \(M\) é paralelizável e todas as suas classes de
Stiefel–Whitney positivas se anulam. Em particular,

\[
\boxed{w_2(TM)=0.}
\]

Assim, \(M\) admite estruturas spin.

Esse resultado prova a existência, mas não seleciona uma estrutura spin
única.

---

## 3. Estruturas spin no toro

As estruturas spin de uma variedade spin formam um espaço afim sobre

\[
H^1(M,\mathbb Z_2).
\]

Como \(\mathbb R^4\) é contrátil,

\[
H^1(\mathbb R^4\times T^4,\mathbb Z_2)
\simeq H^1(T^4,\mathbb Z_2)
\simeq(\mathbb Z_2)^4.
\]

Consequentemente, existem

\[
2^4=16
\]

estruturas spin inequivalentes em \(M\), caracterizadas por

\[
\boldsymbol\varepsilon
=(\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4),
\qquad
\varepsilon_a\in\{0,1\}.
\]

Para cada ciclo fundamental \(S^1_a\subset T^4\):

- \(\varepsilon_a=0\): condição periódica;
- \(\varepsilon_a=1\): condição antiperiódica.

Escolha o primeiro círculo como direção interna ativa:

\[
\theta\equiv\theta_1,
\qquad
\theta\sim\theta+2\pi.
\]

O setor fermiônico mínimo é definido por

\[
\boxed{
\boldsymbol\varepsilon_F=(1,0,0,0).
}
\tag{1}
\]

Logo, uma seção espinorial satisfaz

\[
\boxed{
\Psi(\theta+2\pi)
=-\Psi(\theta).
}
\tag{2}
\]

A equação (2) é a origem matemática precisa da monodromia \(\pi\).

Ela é uma escolha discreta de estrutura spin, não uma consequência
automática da simples existência do toro.

---

## 4. Holonomia do círculo ativo

Seja \(\gamma\) o gerador do primeiro fator de
\(\pi_1(T^4)\):

\[
\gamma(s)
=(2\pi s,\theta_2^0,\theta_3^0,\theta_4^0),
\qquad
0\leq s\leq1.
\]

No fibrado de referenciais orientados, uma rotação por ângulo \(\alpha\)
em um plano espacial é representada por

\[
R(\alpha)\in SO(2)\subset SO(4).
\]

Seu levantamento ao grupo spin é

\[
\widetilde R(\alpha)
=\exp\left(
\frac{\alpha}{2}\,e_1e_2
\right),
\tag{3}
\]

onde os geradores de Clifford satisfazem

\[
(e_1e_2)^2=-1.
\]

Para uma volta:

\[
\widetilde R(2\pi)
=\exp(\pi e_1e_2)
=\cos\pi+e_1e_2\sin\pi
=-1.
\]

Portanto,

\[
\boxed{
\operatorname{Hol}_\gamma=-1.
}
\tag{4}
\]

Para duas voltas:

\[
\widetilde R(4\pi)
=\exp(2\pi e_1e_2)
=1,
\]

de modo que

\[
\boxed{
\operatorname{Hol}_{\gamma^2}=+1.
}
\tag{5}
\]

As equações (4) e (5) fornecem:

\[
2\pi:\Psi\mapsto-\Psi,
\]

\[
4\pi:\Psi\mapsto\Psi.
\]

Essa é a representação dupla característica de spin \(1/2\).

---

## 5. Espectro de modos antiperiódicos

Considere a direção circular de raio \(R_0\), com coordenada

\[
x=R_0\theta.
\]

Uma base de modos compatível com (2) é

\[
\Psi_n(\theta)
=u_n e^{i(n+1/2)\theta},
\qquad
n\in\mathbb Z.
\tag{6}
\]

De fato,

\[
\Psi_n(\theta+2\pi)
=e^{i2\pi(n+1/2)}
\Psi_n(\theta)
=-\Psi_n(\theta).
\]

O operador de momento na direção circular é

\[
\widehat p_\theta
=-\frac{i\hbar}{R_0}\frac{\partial}{\partial\theta}.
\]

Aplicando-o a (6):

\[
\widehat p_\theta\Psi_n
=\frac{\hbar}{R_0}
\left(n+\frac12\right)\Psi_n.
\]

Logo,

\[
\boxed{
p_{\theta,n}
=\frac{\hbar}{R_0}
\left(n+\frac12\right).
}
\tag{7}
\]

A circulação em uma volta é

\[
\oint_\gamma p\,dx
=\int_0^{2\pi}
p_{\theta,n}R_0\,d\theta.
\]

Substituindo (7):

\[
\oint_\gamma p\,dx
=
\int_0^{2\pi}
\hbar\left(n+\frac12\right)d\theta
\]

\[
=2\pi\hbar
\left(n+\frac12\right).
\]

Como

\[
h=2\pi\hbar,
\]

obtemos

\[
\boxed{
\oint_\gamma p\,dx
=h\left(n+\frac12\right).
}
\tag{8}
\]

O menor módulo ocorre para \(n=0\) ou \(n=-1\):

\[
\left|
\frac1h\oint_\gamma p\,dx
\right|
=\frac12.
\]

Assim, o valor mínimo não nulo da circulação normalizada é

\[
\boxed{s=\frac12.}
\tag{9}
\]

---

## 6. Relação com a soma de Poisson

Defina o desvio de fase:

\[
\epsilon
=\frac1\hbar\oint_\gamma p\,dx-\pi.
\]

A identidade distribucional

\[
\sum_{m\in\mathbb Z}e^{im\epsilon}
=2\pi\sum_{k\in\mathbb Z}
\delta(\epsilon-2\pi k)
\]

impõe suporte em

\[
\epsilon=2\pi k.
\]

Portanto,

\[
\frac1\hbar\oint_\gamma p\,dx
=2\pi k+\pi,
\]

ou

\[
\oint_\gamma p\,dx
=h\left(k+\frac12\right).
\]

A soma de Poisson é, assim, equivalente ao espectro antiperiódico
obtido diretamente em (6)–(8).

Ela não cria o deslocamento \(1/2\); ela converte a monodromia

\[
\operatorname{Hol}_\gamma=-1
\]

em uma condição espectral.

---

## 7. Relação com o índice de Maslov

Para um movimento semiclassicamente confinado entre dois pontos de
retorno, a condição de Einstein–Brillouin–Keller é

\[
\oint p\,dq
=2\pi\hbar
\left(
n+\frac{\mu}{4}
\right),
\]

onde \(\mu\) é o índice de Maslov.

Para dois pontos de retorno simples:

\[
\mu=2,
\]

e

\[
\oint p\,dq
=h\left(n+\frac12\right).
\]

Isso explica o mesmo deslocamento no espectro semiclassico de um sistema
confinado.

Entretanto, existem duas origens conceitualmente distintas:

- estrutura spin antiperiódica: representação dupla e rotação \(4\pi\);
- índice de Maslov: fases de cáusticas em movimento orbital.

O fato de ambas produzirem \(1/2\) não permite identificá-las sem um mapa
entre a dinâmica orbital e o fibrado spin.

---

## 8. Conexão de Bismut no fibrado spin

Se \(H\) é a torção de Bismut, a conexão induzida sobre espinores pode ser
escrita, em uma convenção usual, como

\[
\nabla_X^{B,\mathrm{spin}}
=\nabla_X^{LC,\mathrm{spin}}
+\frac18
\sum_{a,b}
H(X,e_a,e_b)\,
\gamma^a\gamma^b.
\tag{10}
\]

O transporte ao longo de \(\gamma\) é

\[
U_B(\gamma)
=\mathcal P
\exp\left[
-\oint_\gamma
\left(
\Omega^{LC}
+\frac18\iota_{\dot\gamma}H_{ab}
\gamma^a\gamma^b
\right)
\right].
\tag{11}
\]

A holonomia total contém dois fatores:

\[
\boxed{
\operatorname{Hol}^{B}_\gamma
=\varepsilon_F(\gamma)\,
\operatorname{Hol}^{B}_{\gamma,\mathrm{local}},
}
\tag{12}
\]

onde:

- \(\varepsilon_F(\gamma)=-1\) é a monodromia global da estrutura spin
  escolhida;
- \(\operatorname{Hol}^{B}_{\gamma,\mathrm{local}}\) é o transporte produzido
  pela conexão local, incluindo \(H\).

Para preservar exatamente

\[
\operatorname{Hol}^{B}_\gamma=-1,
\]

é suficiente exigir

\[
\boxed{
\operatorname{Hol}^{B}_{\gamma,\mathrm{local}}=1.
}
\tag{13}
\]

Uma condição simples que garante (13) no modelo de fundo é:

\[
\iota_{\dot\gamma}H=0
\]

ao longo do círculo ativo, juntamente com uma conexão de
Levi–Civita localmente plana nessa direção.

Mais geralmente, a torção pode ser não nula, desde que seu transporte
ordenado satisfaça:

\[
\mathcal P\exp\left[
-\frac18\oint_\gamma
H(\dot\gamma,e_a,e_b)
\gamma^a\gamma^b\,ds
\right]
=1.
\tag{14}
\]

Sem uma solução explícita para \(H\), a equação (14) deve ser imposta como
condição de compatibilidade do setor fermiônico.

---

## 9. O que foi demonstrado

Sob a escolha discreta

\[
\boldsymbol\varepsilon_F=(1,0,0,0)
\]

e a compatibilidade (13), foram demonstrados:

\[
\operatorname{Hol}_\gamma=-1,
\]

\[
\operatorname{Hol}_{\gamma^2}=+1,
\]

\[
\Psi(\theta+2\pi)=-\Psi(\theta),
\]

\[
\Psi(\theta+4\pi)=\Psi(\theta),
\]

\[
\oint_\gamma p\,dx
=h\left(n+\frac12\right),
\]

e o setor mínimo

\[
s=\frac12.
\]

Essa é uma realização matemática consistente de circulação
meio-inteira e comportamento \(4\pi\).

---

## 10. O que não foi derivado

A topologia de \(T^4\) não seleciona sozinha
\(\boldsymbol\varepsilon_F\). Existem também estruturas periódicas.

Portanto, ainda não foi demonstrado que:

- a dinâmica da GDQ seleciona exclusivamente a estrutura antiperiódica;
- o funcional de Perelman torna os outros quinze setores instáveis;
- a torção concreta do solíton satisfaz (14);
- a circulação possui exatamente o momento magnético observado;
- estados de várias partículas obedecem anticomutação;
- a estatística de Fermi–Dirac decorre da ação;
- o operador efetivo é o operador de Dirac correto.

Esses itens não invalidam a construção. Eles delimitam a diferença entre:

- **existência de um setor de spin \(1/2\)**, agora demonstrada;
- **seleção dinâmica e fenomenologia completa desse setor**, ainda aberta.

---

## 11. Axioma mínimo necessário

A nova versão da GDQ deve declarar:

> **Axioma de setor fermiônico.** A estrutura spin de
> \(M=\mathbb R^4\times T^4\) é antiperiódica ao longo do círculo interno
> ativo associado à circulação do solíton e periódica nos três ciclos
> internos restantes:
> \[
> \boldsymbol\varepsilon_F=(1,0,0,0).
> \]
> A conexão de Bismut admissível preserva essa monodromia, satisfazendo
> \(\operatorname{Hol}^{B}_{\gamma,\mathrm{local}}=1\) no ciclo fundamental.

Esse axioma substitui a inserção informal de um salto de fase \(\pi\) por
uma escolha geométrica precisa e verificável.

---

## Conclusão

A integração no toro realmente produz o valor meio-inteiro quando o
círculo ativo possui estrutura spin antiperiódica:

\[
\boxed{
\oint_\gamma p\,dx
=h\left(n+\frac12\right).
}
\]

O setor fundamental satisfaz:

\[
\boxed{s=\frac12,}
\]

\[
\boxed{2\pi\mapsto-1,}
\qquad
\boxed{4\pi\mapsto+1.}
\]

Isso estabelece uma realização matemática consistente do spin por
circulação na geometria proposta.

O resultado é uma derivação a partir da estrutura spin escolhida, não uma
seleção dinâmica dessa estrutura. O próximo problema matemático é mostrar
que a ação completa da GDQ favorece o setor
\(\boldsymbol\varepsilon_F=(1,0,0,0)\) e que a torção explícita do solíton
preserva sua holonomia.
