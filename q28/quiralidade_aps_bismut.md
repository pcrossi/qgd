# Q28 — Bloco 5 — Quiralidade, torção de Bismut e termo APS

## 1. Objetivo

Este bloco trata duas pendências da Q28:

1. como a GDQ seleciona \(SU(2)_L\), e não \(SU(2)_R\);
2. como os estômatos/bordas entram no índice por uma condição APS.

A meta é formular a projeção quiral:

\[
P_L=\frac12(1-\Gamma_{\rm GDQ})
\]

e o termo de borda:

\[
\eta_{\partial}.
\]

---

## 2. Operador de Dirac--Bismut com borda

No domínio interno regularizado \(\mathcal I^\circ\), removem-se pequenos tubos
ao redor dos estômatos. Assim:

\[
\partial\mathcal I^\circ
=
\bigsqcup_a \partial_a.
\]

O operador é:

\[
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+
\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iA_\mu
\right).
\]

Perto da borda, ele se decompõe como:

\[
\boxed{
\slashed D_{B,A}
=
\gamma^n
\left(
\partial_n
+
\mathcal D_{\partial,B,A}
+
\mathcal K
\right),
}
\]

onde:

1. \(n\) é a direção normal à borda;
2. \(\mathcal D_{\partial,B,A}\) é o operador tangencial de borda;
3. \(\mathcal K\) contém curvatura média, torção normal e termos de conexão.

---

## 3. Condição APS

A condição de Atiyah--Patodi--Singer remove modos de borda que propagariam com
orientação errada.

Se:

\[
\mathcal D_{\partial,B,A}\varphi_k=\lambda_k\varphi_k,
\]

a condição APS escolhe:

\[
\boxed{
P_{\ge0}\psi|_{\partial\mathcal I^\circ}=0
}
\]

ou a convenção equivalente, dependendo da orientação.

O índice fica:

\[
\boxed{
\operatorname{Ind}(\slashed D_{B,A}^{+})
=
\int_{\mathcal I^\circ}
\widehat A(T\mathcal I)
\operatorname{ch}(E_{\rm int})
-
\frac12
\left(
\eta_{\partial}(0)+h_{\partial}
\right).
}
\]

Aqui:

\[
\eta_{\partial}(s)
=
\sum_{\lambda_k\ne0}
\operatorname{sign}(\lambda_k)|\lambda_k|^{-s},
\]

e:

\[
h_{\partial}=\dim\ker\mathcal D_{\partial,B,A}.
\]

---

## 4. Papel físico da condição APS na GDQ

Na GDQ, a borda do estômato não é uma parede artificial; ela representa a
remoção regularizada de uma garganta/topologia singular.

A condição APS implementa:

\[
\boxed{
\text{somente modos compatíveis com a orientação causal e a holonomia do estômato são físicos.}
}
\]

Isso é a tradução matemática da seleção por:

1. causalidade de Sudarshan;
2. monodromia fermiônica;
3. circulação de spin;
4. estabilidade de Perelman.

---

## 5. Operador quiral efetivo

Definimos:

\[
\boxed{
\Gamma_{\rm GDQ}
=
i\gamma^0\gamma^1\gamma^2\gamma^3
\mathcal C_B,
}
\]

onde \(\mathcal C_B\) é a correção de orientação induzida pela torção de Bismut
e pela cola. No limite sem torção:

\[
\mathcal C_B\to0,
\qquad
\Gamma_{\rm GDQ}\to\gamma^5.
\]

O projetor é:

\[
\boxed{
P_L=\frac12(1-\Gamma_{\rm GDQ}),
\qquad
P_R=\frac12(1+\Gamma_{\rm GDQ}).
}
\]

A condição física é:

\[
\boxed{
SU(2)\text{ atua apenas em }P_LE_{\rm int}.
}
\]

Logo:

\[
SU(2)\to SU(2)_L.
\]

---

## 6. Seleção de mão esquerda

A torção de Bismut define uma 3-forma orientada:

\[
B\in\Omega^3(\mathcal I).
\]

Sua contração com a orientação spinorial define um sinal de helicidade
geométrica:

\[
\sigma_B(\psi)
=
\operatorname{sign}
\langle\psi,
B_{\mu\nu\lambda}\gamma^{\mu\nu\lambda}
\psi\rangle.
\]

A estabilidade causal exige:

\[
\sigma_B(\psi)=-1
\]

para os dubletos que fecham o circuito causal de Sudarshan. Assim:

\[
\boxed{
\psi\in P_LE_{\rm int}.
}
\]

Os modos de helicidade oposta:

\[
\psi\in P_RE_{\rm int}
\]

não carregam o \(SU(2)_L\); aparecem como singletos direitos conjugados.

---

## 7. Interpretação da assimetria fraca

O resultado não é:

\[
SU(2)_R\text{ foi destruído arbitrariamente.}
\]

O resultado é:

\[
\boxed{
SU(2)_R
\text{ não atua como calibre dinâmico estável no setor causal/APS selecionado.}
}
\]

Assim, o setor efetivo visível é:

\[
\boxed{
SU(2)_L.
}
\]

Essa é a forma GDQ da quiralidade fraca.

---

## 8. Contribuição de borda e três gerações

Cada estômato contribui para a assimetria espectral de borda:

\[
\eta_a.
\]

Para três classes estáveis:

\[
\eta_{\partial}
=
\sum_{a=1}^{3}\eta_a.
\]

A condição de fechamento geracional é:

\[
\boxed{
-\frac12(\eta_{\partial}+h_{\partial})
=
3
\quad
\text{no setor geracional líquido}
}
\]

ou, de forma equivalente, a soma bulk + borda produz:

\[
\boxed{
\operatorname{rank}_{\rm gen}
\operatorname{Ind}(\slashed D_{B,A}^{+})
=3.
}
\]

Isso conecta:

\[
\text{estômatos}
\quad\Longleftrightarrow\quad
\text{borda APS}
\quad\Longleftrightarrow\quad
\text{três gerações estáveis}.
\]

---

## 9. Compatibilidade com anomalias

Uma anomalia seria uma falha da medida quântica sob transformação de gauge:

\[
\delta_\alpha \log Z\ne0.
\]

No índice APS, a variação de borda cancela a variação de bulk quando o espectro
é globalmente consistente:

\[
\boxed{
\delta_\alpha
\left(
\int_{\mathcal I^\circ}
\widehat A\,\operatorname{ch}(E)
-
\frac12\eta_{\partial}
\right)
=0.
}
\]

Isso é a versão geométrica do cancelamento de anomalias.

---

## 10. O que este bloco fecha

Este bloco fornece:

1. o operador tangencial de borda;
2. a condição APS;
3. a forma do termo \(\eta_{\partial}\);
4. a projeção quiral \(P_L\);
5. a seleção de \(SU(2)_L\);
6. a interpretação dos três estômatos como contribuição de borda para três
   gerações.

---

## 11. O que ainda falta

Ainda falta avaliar explicitamente:

1. o espectro de \(\mathcal D_{\partial,B,A}\);
2. \(\eta_{\partial}(0)\);
3. \(h_{\partial}\);
4. a forma exata de \(\mathcal C_B\);
5. a prova de que somente \(P_LE_{\rm int}\) possui \(SU(2)\) dinâmico estável.

Status:

\[
\boxed{
\text{quiralidade e APS estruturados; falta avaliação espectral da borda.}
}
