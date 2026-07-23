# Questão 10 — A ação produz a equação de continuidade?

## 1. Pergunta

A Questão 10 pergunta:

\[
\boxed{
\text{a ação produz a equação de continuidade?}
}
\]

O problema apontado em `10-0.md` é que a ação oficial do capítulo 4 não
exibe, de forma transparente, um termo temporal capaz de produzir:

\[
\partial_\tau\rho.
\]

A resposta necessária é demonstrar:

\[
\boxed{
\frac{\delta I}{\delta S_R}=0
\Longrightarrow
\partial_\tau\rho+\nabla_\mu(\rho v^\mu)=0.
}
\]

com integração por partes e condições de bordo.

---

## 2. Resposta curta

Sim, a ação produz a continuidade, mas não por uma variação ingênua do
integrando geométrico estático isolado.

A continuidade aparece na redução Madelung/canônica da ação GDQ, quando se
decompõe:

\[
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar},
\]

e:

\[
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
\]

O campo \(S_R\) é a fase. A ação é invariante sob deslocamento global:

\[
\boxed{
S_R\mapsto S_R+\hbar\alpha.
}
\]

Pelo teorema de Noether, essa simetria gera a conservação da corrente de
Madelung.

Na forma canônica local, o setor relevante da ação é:

\[
\boxed{
I_{\rm Mad}[\rho,S_R]
=
\int d\lambda
\int_{\Sigma_\lambda}
\rho
\left[
\partial_\lambda S_R
+\frac12
G^{AB}
\partial_A S_R
\partial_B S_R
+V_{\rm eff}[\rho,g]
\right]
d\mu_g.
}
\]

Aqui:

- \(\lambda\) é o parâmetro de evolução da redução; no setor de fluxo pode ser
  \(\tau\), e no setor físico pode ser \(t\);
- \(G^{AB}\) é a métrica inversa efetiva no setor considerado;
- \(d\mu_g=\sqrt g\,d^dx\);
- \(V_{\rm eff}\) contém termos que dependem de \(\rho,g\), mas não de
  \(S_R\) sem derivadas.

Variando \(S_R\), obtém-se:

\[
\boxed{
\partial_\lambda\rho+\nabla_A(\rho v^A)=0.
}
\]

Com:

\[
\boxed{
v^A=G^{AB}\partial_BS_R.
}
\]

Se \(\lambda=\tau\), esta é exatamente:

\[
\boxed{
\partial_\tau\rho+\nabla_A(\rho v^A)=0.
}
\]

---

## 3. Por que o termo \(\rho\,\partial_\tau S_R\) é necessário

Uma ação puramente do tipo:

\[
\int
\rho
G^{AB}
\partial_A S_R
\partial_BS_R
dV
\]

produz apenas uma equação elíptica estacionária:

\[
\nabla_A(\rho v^A)=0.
\]

Ela não produz:

\[
\partial_\tau\rho.
\]

Para obter continuidade dinâmica é necessário o termo simplético/canônico:

\[
\boxed{
\rho\,\partial_\tau S_R.
}
\]

Esse termo é o análogo hidrodinâmico do termo canônico:

\[
p\,\dot q.
\]

Na GDQ, ele é permitido porque:

1. \(S_R\) é a fase de \(f\);
2. \(\rho\) é o peso de medida derivado de \(f+\bar f\);
3. a ação tem uma direção de fluxo/contorno \(z_\tau\);
4. a redução local da ação de contorno produz uma estrutura canônica entre
   densidade e fase.

Assim:

\[
\boxed{
(\rho,S_R)
\text{ formam o par canônico da representação Madelung.}
}
\]

---

## 4. Ação reduzida no parâmetro de fluxo

Para responder diretamente ao `10-0.md`, tome:

\[
\lambda=\tau.
\]

O setor de fase da ação reduzida é:

\[
\boxed{
I_\tau[\rho,S_R]
=
\int_{\tau_1}^{\tau_2}
d\tau
\int_{\Sigma_\tau}
\rho
\left[
\partial_\tau S_R
+\frac12
G^{AB}
\partial_A S_R
\partial_B S_R
+V_{\rm eff}[\rho,g]
\right]
d\mu_g.
}
\]

Defina:

\[
\boxed{
v^A
=
G^{AB}\partial_BS_R.
}
\]

Então:

\[
\frac12
G^{AB}
\partial_A S_R
\partial_BS_R
\]

é o termo cinético de corrente.

O potencial efetivo:

\[
V_{\rm eff}[\rho,g]
\]

inclui curvatura, potencial de Bohm, termos barotrópicos e termos geométricos,
mas não altera a variação em \(S_R\) se não depender de \(S_R\) sem derivadas.

---

## 5. Variação em relação a \(S_R\)

Faça:

\[
S_R\mapsto S_R+\varepsilon\eta.
\]

Então:

\[
\delta S_R=\eta,
\qquad
\delta(\partial_\tau S_R)=\partial_\tau\eta,
\qquad
\delta(\partial_A S_R)=\partial_A\eta.
\]

A variação do setor relevante é:

\[
\delta I_\tau
=
\int d\tau
\int_{\Sigma_\tau}
\rho
\left[
\partial_\tau\eta
+G^{AB}\partial_BS_R\,\partial_A\eta
\right]
d\mu_g.
\]

Usando:

\[
v^A=G^{AB}\partial_BS_R,
\]

temos:

\[
\boxed{
\delta I_\tau
=
\int d\tau
\int_{\Sigma_\tau}
\rho
\left[
\partial_\tau\eta
+v^A\partial_A\eta
\right]
d\mu_g.
}
\]

---

## 6. Integração por partes no tempo de fluxo

O primeiro termo é:

\[
\int_{\tau_1}^{\tau_2}d\tau
\int_{\Sigma_\tau}
\rho\,\partial_\tau\eta\,d\mu_g.
\]

Integrando por partes:

\[
\int d\tau
\int
\rho\,\partial_\tau\eta\,d\mu_g
=
\left[
\int_{\Sigma_\tau}
\rho\eta\,d\mu_g
\right]_{\tau_1}^{\tau_2}
-
\int d\tau
\int
\eta\,\partial_\tau(\rho\,d\mu_g).
\]

Se a medida \(d\mu_g\) for fixa na janela:

\[
\partial_\tau(\rho\,d\mu_g)
=
(\partial_\tau\rho)d\mu_g.
\]

Se \(g\) evolui com \(\tau\), a forma correta é:

\[
\boxed{
\partial_\tau(\rho\,d\mu_g)
=
\partial_\tau(\rho\sqrt g)\,d^dx.
}
\]

Ou seja, a continuidade fundamental no bulk com medida variável é:

\[
\boxed{
\partial_\tau(\rho\sqrt g)
+\partial_A(\rho v^A\sqrt g)
=0.
}
\]

Na notação covariante relativa à medida:

\[
\boxed{
\partial_\tau\rho+\nabla_A(\rho v^A)=0
}
\]

quando \(\nabla_A\) é entendido como divergência compatível com \(d\mu_g\) e a
variação de medida é absorvida pela medida conjugada de Perelman.

---

## 7. Integração por partes espacial

O segundo termo é:

\[
\int d\tau
\int_{\Sigma_\tau}
\rho v^A\partial_A\eta\,d\mu_g.
\]

Usando a divergência covariante:

\[
\int_{\Sigma}
\rho v^A\partial_A\eta\,d\mu_g
=
\int_{\partial\Sigma}
\eta\,\rho v^A n_A\,d\Sigma
-
\int_{\Sigma}
\eta\,\nabla_A(\rho v^A)\,d\mu_g.
\]

Logo:

\[
\boxed{
\delta I_\tau
=
B_{\tau}
+B_{\partial\Sigma}
-
\int d\tau
\int_{\Sigma_\tau}
\eta
\left[
\partial_\tau\rho
+\nabla_A(\rho v^A)
\right]
d\mu_g.
}
\]

No caso com medida variável:

\[
\boxed{
\delta I_\tau
=
B_{\tau}
+B_{\partial\Sigma}
-
\int d\tau
\int d^dx\,
\eta
\left[
\partial_\tau(\rho\sqrt g)
+\partial_A(\rho v^A\sqrt g)
\right].
}
\]

---

## 8. Condições de bordo

Os termos de bordo são:

\[
B_\tau
=
\left[
\int_{\Sigma_\tau}
\rho\eta\,d\mu_g
\right]_{\tau_1}^{\tau_2},
\]

e:

\[
B_{\partial\Sigma}
=
\int d\tau
\int_{\partial\Sigma_\tau}
\eta\,\rho v^A n_A\,d\Sigma.
\]

Eles desaparecem se:

1. \(\eta=0\) nos extremos \(\tau_1,\tau_2\);
2. ou o contorno \(\gamma\) é fechado e cancela termos exatos;
3. ou os campos são periódicos no ciclo de \(\gamma\);
4. ou \(\eta\) tem suporte compacto;
5. e, espacialmente, \(\eta=0\) em \(\partial\Sigma\);
6. ou não há bordo físico;
7. ou há condição de não fluxo:

\[
\boxed{
\rho v^A n_A=0
\quad
\text{em}
\quad
\partial\Sigma.
}
\]

Essas são as condições de bordo necessárias.

---

## 9. Equação de Euler--Lagrange para \(S_R\)

Como \(\eta\) é arbitrário no interior, a estacionariedade:

\[
\delta I_\tau=0
\]

implica:

\[
\boxed{
\partial_\tau\rho
+\nabla_A(\rho v^A)
=0.
}
\]

Ou, com medida variável:

\[
\boxed{
\partial_\tau(\rho\sqrt g)
+\partial_A(\rho v^A\sqrt g)
=0.
}
\]

Esta é a equação de continuidade.

Portanto:

\[
\boxed{
\frac{\delta I_\tau}{\delta S_R}=0
\Longrightarrow
\partial_\tau\rho+\nabla_A(\rho v^A)=0.
}
\]

---

## 10. Relação com a ação oficial

A ação oficial é:

\[
\mathcal S_{\rm GDQ}
=
\int_\gamma
\int_M
\frac{\hbar}{\Lambda_C^2}
\mathcal U
\mathcal L_0
\sqrt{\det g}
d^{2n}z
\frac{d\tau}{\tau}.
\]

Ela permanece intocada.

A continuidade não é adicionada externamente. Ela aparece quando:

1. decompomos \(f\) em \(S_I,S_R\);
2. identificamos \(\rho=e^{S_I/\hbar}\);
3. passamos para a representação Madelung;
4. extraímos o setor canônico da ação de contorno;
5. variamos a fase \(S_R\).

Em forma curta:

\[
\boxed{
\mathcal S_{\rm GDQ}
\longrightarrow
I_{\rm Mad}[\rho,S_R]
\quad
\Longrightarrow
\quad
\frac{\delta I_{\rm Mad}}{\delta S_R}=0
\quad
\Longrightarrow
\quad
\partial_\tau\rho+\nabla_A(\rho v^A)=0.
}
\]

---

## 11. Relação com Noether

A mesma equação pode ser lida como corrente de Noether da simetria:

\[
\boxed{
S_R\mapsto S_R+\hbar\alpha.
}
\]

Como a ação depende de \(S_R\) apenas por derivadas, há uma corrente:

\[
\boxed{
J^\tau=\rho,
\qquad
J^A=\rho v^A.
}
\]

A conservação:

\[
\partial_\tau J^\tau+\nabla_AJ^A=0
\]

é:

\[
\boxed{
\partial_\tau\rho+\nabla_A(\rho v^A)=0.
}
\]

Portanto:

\[
\boxed{
\text{continuidade = Noether da fase }S_R.
}
\]

---

## 12. Versão física em tempo lorentziano

Na camada física reconstruída, o parâmetro de evolução é \(t\), não \(\tau\).

Então a forma correspondente é:

\[
\boxed{
\partial_t\rho+\nabla_i(\rho v^i)=0.
}
\]

Essa equação é a continuidade física em \(N^4\).

A versão em \(\tau\) é a continuidade de fluxo/escala da representação
Madelung--Perelman.

As duas não devem ser confundidas:

\[
\boxed{
\tau=\text{fluxo geométrico;}
\qquad
t=\text{tempo físico.}
}
\]

A compatibilidade entre elas é organizada por:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

---

## 13. Resposta direta ao problema do `10-0.md`

O problema dizia:

\[
\text{“a ação do capítulo 4 não apresenta claramente um termo temporal capaz
de produzir }\partial_\tau\rho.”}
\]

A resposta é:

\[
\boxed{
\text{o termo temporal aparece na redução canônica Madelung da ação de
contorno: }\rho\,\partial_\tau S_R.
}
\]

Com ele:

\[
\frac{\delta I}{\delta S_R}=0
\]

gera:

\[
\boxed{
\partial_\tau\rho+\nabla_\mu(\rho v^\mu)=0.
}
\]

Sem esse termo, só se obtém a equação estacionária:

\[
\nabla_\mu(\rho v^\mu)=0.
\]

Portanto, o termo canônico é essencial.

---

## 14. Status vigente da Questão 10

\[
\boxed{
\text{Questão 10 fechada estruturalmente e condicionalmente no setor
Madelung.}
}
\]

A ação oficial produz diretamente a conservação da corrente de fase:

\[
\boxed{
\nabla_\mu\widehat J_S^\mu=0.
}
\]

Essa parte é uma consequência variacional/Noether da simetria global de
deslocamento de \(S_R\).

A forma temporal de Madelung,

\[
\boxed{
\partial_\tau\rho+\nabla_\mu(\rho v^\mu)=0.
}
\]

ou, com medida variável,

\[
\boxed{
\partial_\tau(\rho\sqrt g)
+\partial_\mu(\rho v^\mu\sqrt g)
=0.
}
\]

é obtida quando a redução física seleciona a polarização canônica em que o
momento da fase coincide com a densidade transportada:

\[
\boxed{
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}.
}
\]

Essa identificação não é uma identidade off-shell universal da ação oficial.
Ela é uma condição/redução física do setor de Madelung, tratada na ponte
global--local e na auditoria do termo canônico.

Portanto, a resposta precisa é:

\[
\boxed{
\text{sim para a corrente conservada de fase;}
\qquad
\text{sim para a continuidade de Madelung no setor canônico polarizado;}
\qquad
\text{não como identidade universal de toda solução GDQ.}
}
\]
