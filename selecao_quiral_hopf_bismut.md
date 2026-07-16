# Seleção do triplet quiral de Hopf pela estrutura complexa

## 1. Pergunta

Qual dos dois tripletos de formas harmônicas de \(T^4\), auto-dual ou
anti-auto-dual, representa o setor axial de Hopf que acopla ao aparelho?

## 2. Resposta curta

Para a orientação complexa padrão de \(\mathbb C^2\), o triplet hipercähler
associado ao mapa de Hopf é auto-dual:

\[
\boxed{\chi=+.}
\]

Essa seleção é geométrica, não experimental. Se a orientação complexa for
invertida ou a estrutura for conjugada, os papéis de \(+\) e \(-\) são
trocados.

Portanto, a afirmação física correta é:

\[
\boxed{
\text{a estrutura complexa e a orientação selecionam o triplet;}
\quad
\text{o campo do aparelho seleciona uma direção dentro dele.}
}
\]

---

## 3. Estrutura complexa na fatia normal

A fatia normal do estômato foi identificada na Q42 como

\[
\mathbb C^2\simeq\mathbb R^4.
\]

Escreva

\[
z_1=x^1+ix^2,
\qquad
z_2=x^3+ix^4.
\]

Escolha o coframe ortonormal

\[
e^1=dx^1,\quad e^2=dx^2,
\quad e^3=dx^3,\quad e^4=dx^4
\]

e a orientação complexa

\[
\boxed{
e^1\wedge e^2\wedge e^3\wedge e^4>0.
}

A forma Hermitiana fundamental é

\[
\boxed{
\Omega_1=e^1\wedge e^2+e^3\wedge e^4.
}
\]

Com essa orientação:

\[
*\Omega_1=\Omega_1.
\]

---

## 4. Triplet hipercähler

A estrutura quaterniônica de \(\mathbb R^4\) fornece três 2-formas:

\[
\boxed{
\begin{aligned}
\Omega_1&=e^1\wedge e^2+e^3\wedge e^4,\\
\Omega_2&=e^1\wedge e^3-e^2\wedge e^4,\\
\Omega_3&=e^1\wedge e^4+e^2\wedge e^3.
\end{aligned}
}
\]

Elas satisfazem:

\[
\boxed{*\Omega_i=+\Omega_i.}
\]

Após normalização:

\[
\Sigma_i^+=\frac{\Omega_i}{\sqrt2}.
\]

Esse é exatamente o triplet auto-dual construído na matriz de Gram de
\(T^4\).

---

## 5. Relação com o mapa de Hopf

Para \(u=(z_1,z_2)^T\in S^3\subset\mathbb C^2\), o mapa de Hopf é

\[
\boxed{
n_i(u)=u^\dagger\sigma_i u,
\qquad
\boldsymbol n\in S^2.
}
\]

Em coordenadas reais:

\[
n_1=2(x^1x^3+x^2x^4),
\]

\[
n_2=2(x^1x^4-x^2x^3),
\]

\[
n_3=(x^1)^2+(x^2)^2-(x^3)^2-(x^4)^2,
\]

na esfera unitária, salvo a convenção de sinal para \(\sigma_2\).

O grupo \(SU(2)\) que atua em \(u\) rotaciona simultaneamente o vetor
\(n_i\) e o triplet \(\Omega_i\). Assim, o mapa equivarante entre o módulo de
Hopf e o setor de 2-formas é

\[
\boxed{
\Omega_{\rm Hopf}(u)
=n^i(u)\Sigma_i^+.
}
\]

Essa construção identifica o \(SU(2)\) de Hopf com o fator auto-dual da
decomposição

\[
\operatorname{Spin}(4)
=SU(2)_+\times SU(2)_-.
\]

---

## 6. Papel da conexão de Bismut

Numa variedade Hermitiana, a conexão de Bismut preserva:

\[
\nabla^Bg=0,
\qquad
\nabla^BJ=0.
\]

Sua torção é, na convenção escolhida,

\[
H=d^c\Omega
\]

ou a expressão com sinal oposto, dependendo da definição de \(d^c\).

Como \(\nabla^B\) preserva \(J\), uma deformação contínua que não inverte a
orientação complexa permanece no mesmo fator quiral. A torção pode misturar
componentes dentro do triplet e alterar suas normas, mas não troca
automaticamente \(SU(2)_+\) por \(SU(2)_-\).

Portanto, na orientação complexa padrão:

\[
\boxed{
\omega_{\rm SG}(P)
=n^i(P)\Sigma_i^+.
}

---

## 7. O que significa inverter a orientação

Sob

\[
e^1\wedge e^2\wedge e^3\wedge e^4
\longmapsto
-e^1\wedge e^2\wedge e^3\wedge e^4,
\]

o operador de Hodge troca seus autoespaços:

\[
\mathcal H^2_+\leftrightarrow\mathcal H^2_-.
\]

Do mesmo modo, conjugação da estrutura complexa pode trocar a identificação
do fator de \(\operatorname{Spin}(4)\).

Esse processo não corresponde a spin para cima versus spin para baixo. Os
dois resultados de Stern--Gerlach são:

\[
\boldsymbol n=+\boldsymbol n_A,
\qquad
\boldsymbol n=-\boldsymbol n_A
\]

dentro do mesmo triplet quiral.

A troca \(+\leftrightarrow-\) dos tripletos corresponde a mudança de
orientação/quiralidade geométrica mais profunda, possivelmente relacionada a
setor conjugado ou antipartícula, e deve ser estudada separadamente.

---

## 8. Acoplamento selecionado

O canal torsional do aparelho fica

\[
\delta\mathcal A
=y(x,t)n^i(P)\Sigma_i^+.
\]

O campo clássico produz um vetor de sobreposição \(j_i\). O acoplamento é

\[
S_{\rm int}^{\rm red}
=g_0Xn^ij_i.
\]

Definindo

\[
\boldsymbol n_A
=\frac{\boldsymbol j}{|\boldsymbol j|},
\qquad
g_X=g_0|\boldsymbol j|,
\]

recupera-se

\[
\boxed{
S_{\rm int}^{\rm red}
=g_XX\boldsymbol n(P)\cdot\boldsymbol n_A.
}

O aparelho escolhe \(\boldsymbol n_A\); a estrutura complexa já escolheu o
espaço tridimensional em que esse vetor vive.

---

## 9. Status lógico da seleção

### Demonstrado

1. a orientação complexa padrão torna o triplet hipercähler auto-dual;
2. o mapa de Hopf transforma no mesmo \(SU(2)_+\);
3. a conexão de Bismut preserva \(g\) e \(J\);
4. o eixo do aparelho é uma direção dentro do triplet, não sua origem.

### Condicional

1. a identificação \(\chi=+\) depende da orientação complexa oficial;
2. convenções opostas de Hodge podem chamar o mesmo setor de \(-\);
3. é preciso verificar que a colagem global do estômato preserva essa
   orientação;
4. backgrounds não diagonais podem misturar a base, embora não devam trocar a
   classe quiral sem degenerescência ou inversão de orientação.

### Ainda aberto

1. relação precisa com partículas e antipartículas;
2. ação de paridade e conjugação de carga na colagem completa;
3. seleção dinâmica caso existam domínios de orientação oposta.

## 10. Próximo passo

Com a quiralidade fixada, o próximo cálculo é a sobreposição

\[
j_i
=\langle\Sigma_i^+,J_{\rm app}\rangle
\]

entre o campo clássico levantado ao bulk e o perfil torsional do estômato.
Essa integral deve produzir \(g_X\) e conectar a taxa informacional do detector
ao campo de Stern--Gerlach.

Essa sobreposição foi estruturada em `sobreposicao_campo_hopf_gx.md`. O mapa
equivariante é único a menos da escala de soldagem \(\ell_B\), e o acoplamento
ao ponteiro é \(g_X=\mu_{\rm GDQ}|\partial_X\boldsymbol B_{\rm eff}|\), com
\(\mu_{\rm GDQ}=(q\ell_B/c)I_H\).

## 11. Veredito

\[
\boxed{
\text{a orientação complexa padrão seleciona o triplet auto-dual de Hopf;}
\quad
\text{o campo do aparelho seleciona apenas uma direção nesse triplet.}
}
\]
