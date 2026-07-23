# Questão 26 — Como surge spin \(1/2\)?

## 1. Pergunta

A Questão 26 pergunta:

\[
\boxed{
\text{como a GDQ obtém spin }1/2\text{ sem reduzi-lo a uma circulação escalar
inteira?}
}
\]

`26-0.md` exige:

1. fibrado spin;
2. álgebra de Clifford;
3. representação de \(\mathrm{Spin}(3,1)\);
4. operador de Dirac;
5. transformação sob \(2\pi\) e \(4\pi\);
6. graus de liberdade físicos.

A resposta não aceitável é:

\[
\boxed{
\text{usar apenas circulação inteira ou definir }\kappa=\pm1.
}
\]

---

## 2. Resposta curta

Spin \(1/2\) surge quando o setor físico da GDQ é definido sobre uma variedade
lorentziana spin \((N,h)\), com fibrado principal:

\[
\boxed{
P_{\mathrm{Spin}}(N)\to N
}
\]

que levanta o fibrado ortonormal:

\[
\boxed{
P_{\mathrm{Spin}}(N)
\longrightarrow
P_{\mathrm{SO}}(N).
}
\]

O campo fermiônico é uma seção do fibrado espinorial:

\[
\boxed{
\psi\in\Gamma(S\otimes E),
}
\]

onde:

- \(S=P_{\mathrm{Spin}}(N)\times_{\rho_D}\mathbb C^4\) é o fibrado de
  espinores de Dirac;
- \(E\) é o fibrado interno de carga/gauge;
- \(\rho_D\) é a representação espinorial de \(\mathrm{Spin}(3,1)\).

A álgebra de Clifford satisfaz:

\[
\boxed{
\{\gamma^a,\gamma^b\}=2\eta^{ab}.
}
\]

Os geradores de Lorentz na representação espinorial são:

\[
\boxed{
\Sigma^{ab}=\frac14[\gamma^a,\gamma^b].
}
\]

Uma rotação espacial de ângulo \(\theta\) atua como:

\[
\boxed{
U(\theta)=\exp\!\left(-\frac{i\theta}{\hbar}\,\mathbf n\cdot\mathbf S\right),
\qquad
\mathbf S=\frac{\hbar}{2}\boldsymbol\sigma
}
\]

no subespaço de spin. Portanto:

\[
\boxed{
U(2\pi)=-I,
\qquad
U(4\pi)=I.
}
\]

Esse é o conteúdo matemático de spin \(1/2\).

Na GDQ, a vorticidade/torsão de Cartan pode dar a interpretação geométrica do
spin, mas não substitui a estrutura spinorial.

---

## 3. Existência de estrutura spin

Pela Questão 2, a variedade fundamental oficial é:

\[
\boxed{
M=\mathbb R^4\times T^4.
}
\]

Como os fibrados tangentes de \(\mathbb R^4\) e \(T^4\) são triviais:

\[
\boxed{
TM\simeq M\times\mathbb R^8.
}
\]

Logo:

\[
\boxed{
w_2(TM)=0.
}
\]

Portanto, \(M\) admite estrutura spin.

As estruturas spin são classificadas por:

\[
\boxed{
H^1(M,\mathbb Z_2)
\simeq
H^1(T^4,\mathbb Z_2)
\simeq
(\mathbb Z_2)^4.
}
\]

Assim existem:

\[
\boxed{
2^4=16
}
\]

estruturas spin inequivalentes no setor interno.

No espaço-tempo físico efetivo \((N,h)\), a formulação fermiônica exige:

\[
\boxed{
w_2(TN)=0.
}
\]

ou, equivalentemente, a existência de um fibrado principal
\(\mathrm{Spin}(3,1)\):

\[
\boxed{
P_{\mathrm{Spin}}(N)\to N.
}
\]

Se \(N\) for a folha física herdada da estrutura trivial de \(M\), essa
condição é natural. Em backgrounds mais gerais, ela precisa ser imposta ou
verificada.

---

## 4. Fibrado spin e levantamento duplo

O grupo de Lorentz próprio ortócrono é:

\[
\boxed{
SO^+(3,1).
}
\]

Seu recobrimento duplo é:

\[
\boxed{
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C).
}
\]

Existe um homomorfismo:

\[
\boxed{
\pi:\mathrm{Spin}^+(3,1)\to SO^+(3,1)
}
\]

com núcleo:

\[
\boxed{
\ker\pi=\{\pm1\}.
}
\]

Isso é o ponto essencial.

Uma rotação de \(2\pi\) é a identidade em \(SO(3)\), mas corresponde a
\(-1\) em \(\mathrm{Spin}(3)\simeq SU(2)\):

\[
\boxed{
R(2\pi)=I\in SO(3),
\qquad
\widetilde R(2\pi)=-I\in SU(2).
}
\]

Após \(4\pi\):

\[
\boxed{
\widetilde R(4\pi)=I.
}
\]

Portanto:

\[
\boxed{
\text{spin }1/2\text{ é representação do recobrimento duplo, não rotação
vetorial ordinária.}
}
\]

---

## 5. Álgebra de Clifford

No espaço tangente lorentziano com métrica \(\eta=\mathrm{diag}(-,+,+,+)\), a
álgebra de Clifford é gerada por \(\gamma^a\) satisfazendo:

\[
\boxed{
\gamma^a\gamma^b+\gamma^b\gamma^a=2\eta^{ab}I.
}
\]

Em coordenadas curvas:

\[
\boxed{
\gamma^\mu=e^\mu_a\gamma^a,
}
\]

e:

\[
\boxed{
\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}I.
}
\]

Os geradores espinoriais são:

\[
\boxed{
\Sigma^{ab}
=
\frac14[\gamma^a,\gamma^b].
}
\]

Para uma transformação de Lorentz infinitesimal:

\[
\boxed{
\Lambda=\exp(\omega_{ab}J^{ab}),
}
\]

a ação no espinor é:

\[
\boxed{
\psi\mapsto
\exp\!\left(\frac12\omega_{ab}\Sigma^{ab}\right)\psi.
}
\]

Essa representação é a origem algébrica dos graus de liberdade de spin.

---

## 6. Representação de \(\mathrm{Spin}(3,1)\)

Como:

\[
\boxed{
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C),
}
\]

as representações fundamentais são:

\[
\boxed{
\left(\frac12,0\right)
\quad\text{e}\quad
\left(0,\frac12\right).
}
\]

Um espinor de Dirac é:

\[
\boxed{
\psi_D
\in
\left(\frac12,0\right)\oplus\left(0,\frac12\right).
}
\]

Ou seja:

\[
\boxed{
S_D=S_L\oplus S_R.
}
\]

Cada componente de Weyl tem duas componentes complexas. O espinor de Dirac
tem quatro componentes complexas antes de impor equações de movimento,
realidade, energia positiva ou restrições físicas.

---

## 7. Operador de Dirac com torção e gauge

Na GDQ, o setor espinorial efetivo usa o operador:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA^a_\mu
\right).
}
\]

Aqui:

- \(\nabla^{\rm LC}\) é a conexão de Levi--Civita spinorial;
- \(B_{\mu\nu\lambda}\) é a 3-forma torsional/Bismut/Cartan efetiva;
- \(A^a_\mu\) são conexões de gauge efetivas;
- \(q_a\) são as cargas no setor \(E\);
- \(\gamma^{\nu\lambda}=\frac12[\gamma^\nu,\gamma^\lambda]\).

A ação efetiva é:

\[
\boxed{
S_{\rm spin}
=
\int_N
\bar\psi
\left(
i\hbar\slashed D_{B,A}
-mc
\right)
\psi
\sqrt{-h}\,d^4x.
}
\]

O símbolo principal satisfaz:

\[
\boxed{
(\gamma^\mu k_\mu)^2
=
h^{\mu\nu}k_\mu k_\nu.
}
\]

Assim, os espinores compartilham o cone causal da métrica física \(h\).

---

## 8. Transformação sob \(2\pi\) e \(4\pi\)

Restrinja a um subgrupo espacial:

\[
\boxed{
\mathrm{Spin}(3)\simeq SU(2)
\longrightarrow
SO(3).
}
\]

Uma rotação por ângulo \(\theta\) em torno de \(\mathbf n\) atua no spinor de
duas componentes como:

\[
\boxed{
U(\theta)
=
\exp\left(
-i\frac{\theta}{2}\mathbf n\cdot\boldsymbol\sigma
\right).
}
\]

Para \(\theta=2\pi\):

\[
\boxed{
U(2\pi)
=
\exp(-i\pi\,\mathbf n\cdot\boldsymbol\sigma)
=
-I.
}
\]

Para \(\theta=4\pi\):

\[
\boxed{
U(4\pi)=I.
}
\]

Logo:

\[
\boxed{
\psi\mapsto-\psi\text{ sob }2\pi,
\qquad
\psi\mapsto\psi\text{ sob }4\pi.
}
\]

Esse é o comportamento característico de spin \(1/2\).

---

## 9. Relação com circulação e holonomia

A circulação trabalhada nas Questões 2 e 23 permanece útil, mas deve ser lida
corretamente.

Para uma fase escalar:

\[
\boxed{
\oint dS_R=Nh.
}
\]

Para setor spinorial antiperiódico:

\[
\boxed{
\psi(\theta+2\pi)=-\psi(\theta).
}
\]

Os modos permitidos são:

\[
\boxed{
\psi_n(\theta)\propto e^{i(n+1/2)\theta}.
}
\]

Logo:

\[
\boxed{
\oint p_\theta\,d\theta
=
h\left(n+\frac12\right).
}
\]

Esse resultado vem da estrutura spin, não de uma circulação escalar arbitrária.

Portanto:

\[
\boxed{
\text{circulação/holonomia é a manifestação geométrica; estrutura spin é a
causa matemática.}
}
\]

---

## 10. Papel da torção/vorticidade de Cartan

O capítulo 9 interpreta spin como vorticidade hidrodinâmica acoplada à torção
de Cartan.

Essa intuição é aproveitável:

\[
\boxed{
\text{spin físico pode aparecer como densidade de vorticidade/torção de um
solíton.}
}
\]

Em linguagem geométrica, uma densidade de spin pode acoplar-se à torção:

\[
\boxed{
B_{\mu\nu\lambda}
\sim
\kappa\,S_{\mu\nu\lambda}.
}
\]

Mas isso não substitui:

1. fibrado spin;
2. álgebra de Clifford;
3. representação de \(\mathrm{Spin}(3,1)\);
4. operador de Dirac.

A formulação correta é:

\[
\boxed{
\text{a estrutura spinorial fornece o quantum }1/2;
\text{ a torção/vorticidade fornece a interpretação geométrica e o acoplamento.}
}
\]

---

## 11. Graus de liberdade físicos

Um espinor de Dirac em \(3+1\) dimensões tem:

\[
\boxed{
4\text{ componentes complexas}
}
\]

off-shell.

Sob a equação de Dirac, os modos físicos de uma partícula massiva possuem:

\[
\boxed{
2\text{ polarizações de spin}
}
\]

para a partícula, e:

\[
\boxed{
2\text{ polarizações}
}
\]

para a antipartícula.

No setor quiral sem massa:

\[
\boxed{
\left(\frac12,0\right)
\quad\text{ou}\quad
\left(0,\frac12\right)
}
\]

há uma helicidade física por partícula, dependendo das condições de realidade,
carga e representação.

Em linguagem operacional:

\[
\boxed{
s_z=\pm\frac{\hbar}{2}
}
\]

são os dois resultados possíveis de um experimento tipo Stern--Gerlach para
uma partícula spin \(1/2\) não relativística.

---

## 12. Relação com Stern--Gerlach

O Stern--Gerlach não deve ser usado como definição de spin \(1/2\). Ele é uma
medição operacional da representação já existente.

No limite não relativístico, o acoplamento efetivo é:

\[
\boxed{
H_{\rm int}
=
-\boldsymbol\mu\cdot\mathbf B,
\qquad
\boldsymbol\mu
=
g\frac{q}{2m}\mathbf S.
}
\]

Com:

\[
\boxed{
\mathbf S=\frac{\hbar}{2}\boldsymbol\sigma.
}
\]

Então:

\[
\boxed{
S_z=\pm\frac{\hbar}{2}.
}
\]

A GDQ pode interpretar a força como resposta mecânico-geométrica do solíton ao
campo externo, mas os dois autovalores vêm da representação spinorial.

---

## 13. O que ainda não está demonstrado dinamicamente

A Questão 26 pode ser fechada estruturalmente. Porém, ainda não está
demonstrado dinamicamente:

1. por que uma das 16 estruturas spin de \(T^4\) é selecionada;
2. por que um solíton específico realiza exatamente o setor de Dirac do
   elétron;
3. como derivar massas e cargas simultaneamente;
4. como estabilizar todos os modos espinoriais;
5. como obter o espectro completo de partículas a partir do operador
   \(\slashed D_{B,A}\).

Essas são questões setoriais posteriores.

---

## 14. Resposta final da Questão 26

Spin \(1/2\) surge porque o setor fermiônico da GDQ é formulado em um fibrado
spinorial:

\[
\boxed{
\psi\in\Gamma(S\otimes E),
\qquad
S=P_{\mathrm{Spin}}(N)\times_{\rho_D}\mathbb C^4.
}
\]

A álgebra de Clifford é:

\[
\boxed{
\{\gamma^\mu,\gamma^\nu\}=2h^{\mu\nu}.
}
\]

A representação relevante é:

\[
\boxed{
\left(\frac12,0\right)\oplus\left(0,\frac12\right)
}
\]

de:

\[
\boxed{
\mathrm{Spin}^+(3,1)\simeq SL(2,\mathbb C).
}
\]

Sob rotações espaciais:

\[
\boxed{
U(2\pi)=-I,
\qquad
U(4\pi)=I.
}
\]

Logo:

\[
\boxed{
s_z=\pm\frac{\hbar}{2}.
}
\]

A torção/vorticidade de Cartan fornece a interpretação geométrica do spin no
solíton, mas o quantum \(1/2\) vem da estrutura spinorial e da representação de
\(\mathrm{Spin}(3,1)\).

Portanto:

\[
\boxed{
\text{Questão 26 fechada estruturalmente.}
}
\]

---

## 15. Complemento: formulação Hopf--Cauchy por resíduos

A formulação por circulação/Hopf foi consolidada no adendo
[spin_hopf_residuo_cauchy.md](associados/spin_hopf_residuo_cauchy.md).

O ponto central é que a circulação não deve ser lida como circulação escalar
inteira ordinária. No contorno normal do estômato, o setor spinorial corresponde
a uma meia-monodromia. Em uma carta complexa transversal \(z\), uma seção local
spinorial tem comportamento:

\[
s(z)=z^{1/2}s_0(z),
\]

com \(s_0\) holomorfa e não nula. A conexão logarítmica é:

\[
\Omega_S=d\log s
=
\frac12\frac{dz}{z}+d\log s_0.
\]

Como \(d\log s_0\) não contribui ao resíduo:

\[
\operatorname{Res}_{z=0}\Omega_S=\frac12.
\]

Pelo teorema dos resíduos de Cauchy:

\[
\frac{1}{2\pi i}\oint_\gamma\Omega_S
=
\frac12.
\]

Convertendo para a fase física:

\[
\oint_\gamma dS_R
=
\frac{h}{2}
=
\pi\hbar,
\]

e:

\[
\exp\left(
\frac{i}{\hbar}\oint_\gamma dS_R
\right)
=
-1.
\]

Após duas voltas:

\[
(-1)^2=1.
\]

Portanto, a rota por resíduos reproduz:

\[
2\pi\mapsto-1,
\qquad
4\pi\mapsto+1.
\]

Na linguagem de Hopf, isso é a mesma afirmação de que:

\[
S^3\simeq SU(2)\to SO(3)
\]

é um recobrimento duplo e que \(u\) e \(-u\) determinam o mesmo projetor físico:

\[
P=uu^\dagger.
\]

Assim:

\[
\boxed{
\text{Cauchy prova a rigidez topológica da meia-circulação quando o contorno
do estômato realiza a classe Hopf/spinorial simples.}
}
\]

Esse complemento fecha a falta Hopf/resíduos da Q26 sem alterar a prova
spinorial principal. A seleção dinâmica de uma das estruturas spin de \(T^4\)
permanece como problema espectral posterior e não reabre o fechamento
estrutural de spin \(1/2\).
