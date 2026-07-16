# Questão 19 — Monotonicidade implica estabilidade?

## 1. Pergunta

A Questão 19 pergunta:

\[
\boxed{
\text{a monotonicidade dos funcionais geométricos implica estabilidade das
partículas/solítons?}
}
\]

As perguntas obrigatórias de `19-0.md` são:

1. qual funcional é monotônico?
2. sob quais hipóteses?
3. a monotonicidade é crescente ou decrescente?
4. qual é a relação com energia física?
5. o extremo é mínimo, máximo ou sela?
6. qual é o espectro da segunda variação?

O critério de resolução é:

\[
\boxed{
\text{calcular a Hessiana ou operador de Jacobi e demonstrar estabilidade.}
}
\]

---

## 2. Resposta curta

Monotonicidade não implica estabilidade automaticamente.

Ela fornece um funcional de Lyapunov para o fluxo geométrico. Para concluir
estabilidade de um solíton, é preciso mostrar que o ponto crítico é um extremo
estável no setor físico, isto é, que a Hessiana/operador de Jacobi não possui
autovalores negativos após remover modos de gauge e simetrias.

A forma correta é:

\[
\boxed{
\text{monotonicidade}
+
\text{ponto crítico}
+
\text{Hessiana positiva módulo modos zero}
\Longrightarrow
\text{estabilidade orbital/local.}
}
\]

Sem a Hessiana:

\[
\boxed{
\text{monotonicidade sozinha não fecha estabilidade de partícula.}
}
\]

---

## 3. Qual funcional é monotônico?

No setor torsional/Bismut, o funcional de energia fixada é:

\[
\boxed{
\mathcal F_T(g,B,\phi)
=
\int_M
\left(
R
-\frac1{12}|B|^2
+|\nabla\phi|^2
\right)
e^{-\phi}\,dV_g.
}
\]

Aqui:

\[
\boxed{
\phi=\operatorname{Re}f,
\qquad
\rho=e^{-\phi}=e^{-(f+\bar f)/2}.
}
\]

O funcional de escala variável é:

\[
\boxed{
\mathcal W_T(g,B,\phi,\sigma)
=
\int_M
\left[
\sigma
\left(
R
-\frac1{12}|B|^2
+|\nabla\phi|^2
\right)
+\phi-d
\right]
(4\pi\sigma)^{-d/2}e^{-\phi}\,dV_g.
}
\]

No bulk da GDQ:

\[
\boxed{
d=2n=8.
}
\]

Esses funcionais são auxiliares de estabilidade geométrica. Eles não
substituem a ação oficial:

\[
\boxed{
\mathcal S_{\rm GDQ}
\text{ permanece a ação fundamental.}
}
\]

---

## 4. Sob quais hipóteses?

A monotonicidade vale sob hipóteses geométricas precisas.

Assume-se:

1. \(M\) compacto sem bordo, ou não compacto com decaimento suficiente;
2. \(g\) riemanniana/hermitiana positiva no bulk;
3. \(B\) é 3-forma real antissimétrica;
4. \(dB=0\) ou a condição de Bianchi torsional correspondente;
5. \(e^{-\phi}dV_g\) é normalizável;
6. os termos de bordo desaparecem;
7. o fluxo é escrito em gauge adequado;
8. as soluções são regulares no intervalo considerado.

A normalização de medida é:

\[
\boxed{
\int_M e^{-\phi}\,dV_g=1
}
\]

ou, na versão com kernel:

\[
\boxed{
\int_M(4\pi\sigma)^{-d/2}e^{-\phi}\,dV_g=1.
}
\]

No caso da GDQ complexa:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}
}
\]

é a parte real positiva da medida. A fase \(\operatorname{Im}f\) entra na
camada Madelung/topológica, mas não destrói a positividade da medida.

---

## 5. A monotonicidade é crescente ou decrescente?

Com a convenção usada no capítulo 17, os funcionais crescem ao longo de
\(\tau\):

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}\ge0,
\qquad
\frac{d\mathcal W_T}{d\tau}\ge0.
}
\]

Explicitamente:

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}
=
2\int_M
\left|
R_{ij}
-\frac14B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
\right|^2
e^{-\phi}\,dV_g
+
\frac16
\int_M
\left|
d_\phi^\dagger B
\right|^2
e^{-\phi}\,dV_g
\ge0.
}
\]

Para \(\mathcal W_T\):

\[
\boxed{
\frac{d\mathcal W_T}{d\tau}
=
2\sigma\int_M
\left|
R_{ij}
-\frac14B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
-\frac1{2\sigma}g_{ij}
\right|^2
d\mu
+
\frac{\sigma}{6}
\int_M
\left|
d_\phi^\dagger B
\right|^2
d\mu
\ge0.
}
\]

com:

\[
\boxed{
d\mu=(4\pi\sigma)^{-d/2}e^{-\phi}dV_g.
}
\]

Se outra convenção de sinal para o fluxo for usada, o mesmo conteúdo pode
aparecer como funcional decrescente. O essencial é:

\[
\boxed{
\text{o funcional é monotônico e sua derivada é soma de quadrados.}
}
\]

---

## 6. Pontos críticos

A igualdade:

\[
\boxed{
\frac{d\mathcal F_T}{d\tau}=0
}
\]

ocorre se:

\[
\boxed{
R_{ij}
-\frac14B_{ik\ell}B_j{}^{k\ell}
+\nabla_i\nabla_j\phi
=0,
}
\]

e:

\[
\boxed{
d_\phi^\dagger B=0.
}
\]

Para \(\mathcal W_T\), o ponto crítico satisfaz:

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
d_\phi^\dagger B=0.
}
\]

Essas são as equações de solíton Ricci--Bismut/Perelman.

---

## 7. Relação com energia física

\(\mathcal F_T\) e \(\mathcal W_T\) não são automaticamente a energia física
medida em MeV ou GeV.

Eles são funcionais geométricos de Lyapunov. A energia física do solíton deve
ser obtida pela ação oficial ou por Hamiltoniano efetivo da redução física:

\[
\boxed{
E[\mathfrak S]
=
H_{\rm eff}[\mathfrak S]
}
\]

e:

\[
\boxed{
m[\mathfrak S]
=
\frac{E[\mathfrak S]-E_{\rm vac}}{c^2}.
}
\]

A relação correta é:

\[
\boxed{
\mathcal F_T,\mathcal W_T
\text{ controlam estabilidade geométrica;}
\qquad
E
\text{ mede energia física.}
}
\]

Em um setor estacionário normalizado, pode-se usar o funcional geométrico para
definir a parte elástica/entrópica da energia efetiva:

\[
\boxed{
E_{\rm geom}
\propto
\frac{\hbar}{\Lambda_C^2}\mathcal I_T,
\qquad
\mathcal I_T=\mathcal F_T
\text{ ou }
\mathcal W_T,
}
\]

mas a proporcionalidade e a subtração do vácuo precisam ser especificadas no
setor físico.

---

## 8. O extremo é mínimo, máximo ou sela?

Monotonicidade não determina sozinha se o ponto crítico é mínimo, máximo ou
sela.

Como o funcional cresce na convenção adotada, um atrator do fluxo pode aparecer
como máximo local de \(\mathcal F_T\) ou \(\mathcal W_T\) nessa orientação de
\(\tau\). Se se define a energia livre física com sinal oposto:

\[
\boxed{
\mathcal E_T:=-\mathcal W_T,
}
\]

o mesmo ponto aparece como mínimo local de energia livre.

Portanto, a afirmação correta não é:

\[
\text{``monotônico, logo mínimo''.}
\]

A afirmação correta é:

\[
\boxed{
\text{o tipo do extremo é determinado pela segunda variação no setor físico.}
}
\]

Se a Hessiana tem:

\[
\boxed{
\lambda<0
}
\]

em alguma direção física, o ponto é sela/instável.

Se a Hessiana é positiva no funcional de energia física, ou negativa no
funcional entrópico crescente, módulo simetrias, o ponto é estável.

---

## 9. Segunda variação: operador de Jacobi

Seja:

\[
\boxed{
\mathfrak S=(g_\ast,B_\ast,\phi_\ast)
}
\]

um ponto crítico.

Perturbe:

\[
\boxed{
g=g_\ast+h,
\qquad
B=B_\ast+\beta,
\qquad
\phi=\phi_\ast+\eta.
}
\]

Defina:

\[
\boxed{
U=(h,\beta,\eta).
}
\]

Após gauge de DeTurck para \(g\) e gauge de Hodge para \(B\), a segunda
variação tem a forma:

\[
\boxed{
\delta^2\mathcal I_T[U,U]
=
\langle U,\mathcal J_{\mathfrak S}U\rangle_{\rho_\ast}.
}
\]

Aqui:

\[
\boxed{
\mathcal I_T=\mathcal F_T
\quad\text{ou}\quad
\mathcal W_T,
}
\]

e:

\[
\boxed{
\mathcal J_{\mathfrak S}
=
D^2\mathcal I_T|_{\mathfrak S}
}
\]

é o operador de Jacobi/Hessiano.

Esquematicamente:

\[
\boxed{
\mathcal J_{\mathfrak S}
=
\begin{pmatrix}
\Delta_L^\phi+\mathcal R_{BB}+\mathcal R_{\phi\phi}
&
\mathcal C_{gB}
&
\mathcal C_{g\phi}
\\
\mathcal C_{Bg}
&
\Delta_{H,\phi}+\mathcal M_B
&
\mathcal C_{B\phi}
\\
\mathcal C_{\phi g}
&
\mathcal C_{\phi B}
&
-\Delta_\phi+\mathcal V_\phi
\end{pmatrix}.
}
\]

Onde:

- \(\Delta_L^\phi\) é o Lichnerowicz ponderado sobre perturbações métricas;
- \(\Delta_{H,\phi}\) é o Laplaciano de Hodge ponderado sobre 3-formas;
- \(-\Delta_\phi\) é o operador escalar ponderado;
- os termos \(\mathcal C\) são acoplamentos de menor ordem;
- os termos \(\mathcal R,\mathcal M,\mathcal V\) dependem de \(R,B,\nabla\phi\).

Essa é a estrutura que precisa ser diagonalizada ou estimada.

---

## 10. Espectro da segunda variação

A estabilidade linear exige:

\[
\boxed{
\operatorname{spec}
\left(
\mathcal J_{\mathfrak S}
\big|_{\mathcal H_{\rm phys}}
\right)
\subseteq
[0,\infty)
}
\]

para a convenção em que \(\mathcal I_T\) é energia livre minimizada.

Se se usa o funcional entrópico crescente sem trocar sinal, o critério troca o
sinal:

\[
\boxed{
\operatorname{spec}
\left(
\mathcal J_{\mathfrak S}^{(\mathcal W)}
\big|_{\mathcal H_{\rm phys}}
\right)
\subseteq
(-\infty,0]
}
\]

O espaço físico é o complemento dos modos puros de simetria:

\[
\boxed{
\mathcal H_{\rm phys}
=
\left(
\ker_{\rm diff}
\oplus
\ker_{\rm gauge}
\oplus
\ker_{\rm trans}
\oplus
\ker_{\rm rot}
\oplus
\ker_{\rm scale}
\oplus
\ker_{\rm moduli}
\right)^\perp.
}
\]

Portanto:

- autovalor negativo físico no funcional de energia: instável;
- autovalor zero físico não explicado: marginal/modulus não controlado;
- apenas zeros de simetria e restante positivo: estável linearmente.

---

## 11. Caso explícito: solíton gaussiano

Para o solíton gaussiano:

\[
\boxed{
g_{ij}=\delta_{ij},
\qquad
B=0,
\qquad
\phi=\frac{|x|^2}{4\sigma},
}
\]

a medida normalizada é:

\[
\boxed{
d\mu
=
(4\pi\sigma)^{-d/2}
e^{-|x|^2/(4\sigma)}\,dx.
}
\]

O operador escalar ponderado reduz ao Ornstein--Uhlenbeck:

\[
\boxed{
\mathcal J_{\rm gauss}
\sim
-\Delta
+\frac{x}{2\sigma}\cdot\nabla
+\text{constante de setor}.
}
\]

Seu espectro em \(L^2(d\mu)\) é discreto:

\[
\boxed{
\lambda_k\sim\frac{k}{2\sigma}
}
\]

até deslocamentos dependentes do setor tensorial.

Os modos zero são:

1. translações;
2. dilatação/escala \(\sigma\);
3. rotações, quando não fixadas;
4. difeomorfismos de gauge.

Depois de removidos esses modos, não há autovalores negativos no setor
gaussiano neutro.

Assim:

\[
\boxed{
\text{o solíton gaussiano neutro é linearmente estável módulo simetrias.}
}
\]

Ele não prova ainda a estabilidade de partículas carregadas, mas fornece o
exemplo explícito de Hessiana controlável.

---

## 12. Caso torsional/carregado

Para solítons com carga e spin:

\[
\boxed{
B_\ast\neq0,
\qquad
\operatorname{Im}f_\ast\neq0,
}
\]

o operador de Jacobi possui acoplamentos adicionais:

\[
\boxed{
h\leftrightarrow\beta,
\qquad
h\leftrightarrow\eta,
\qquad
\beta\leftrightarrow\eta.
}
\]

Nesses setores, a estabilidade exige verificar:

1. se \(B\) estabiliza ou desestabiliza o modo de colapso;
2. se a fase possui circulação quantizada;
3. se os modos de separação entre núcleos são positivos;
4. se os modos de rotação são apenas simetrias;
5. se há modos de decaimento topológico;
6. se a carga é conservada sob perturbações.

O texto já possui a intuição correta:

\[
\boxed{
\text{a torção de Bismut atua como pressão de cisalhamento estabilizadora.}
}
\]

Mas isso precisa aparecer no Hessiano como positividade efetiva no setor
físico:

\[
\boxed{
\langle U,\mathcal J_{\mathfrak S}U\rangle_{\rho_\ast}\ge0.
}
\]

---

## 13. Relação com o capítulo 19 original

O capítulo original `19 - Efeito Zeeman.md` não responde diretamente à
Questão 19 de auditoria.

Ele é útil para outro problema: acoplamento de spin/torção com campo externo,
quebra de degenerescência e cálculo de autovalores de energia sob perturbação
magnética.

Mas a Questão 19 pergunta sobre monotonicidade e estabilidade. Portanto, o
material relevante vem de:

1. `questão_17.md`;
2. `questão_18.md`;
3. capítulo 17 sobre monotonicidade com torção;
4. notas sobre Perelman--Bismut;
5. cálculo do Hessiano/Jacobi.

---

## 14. Relação com a ação oficial

A ação oficial permanece:

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

Os funcionais \(\mathcal F_T\) e \(\mathcal W_T\) são instrumentos auxiliares
para estabilidade geométrica e análise do fluxo. Eles não substituem a ação
fundamental.

---

## 15. Veredito

\[
\boxed{
\text{Questão 19 fechada condicionalmente ao operador de Jacobi.}
}
\]

A resposta final é:

\[
\boxed{
\text{monotonicidade não implica estabilidade por si só.}
}
\]

Ela implica estabilidade apenas se:

1. o solíton é ponto crítico real;
2. as hipóteses de monotonicidade são satisfeitas;
3. os termos de bordo desaparecem;
4. o setor topológico é preservado;
5. a segunda variação tem sinal correto;
6. os modos zero são apenas simetrias/moduli controlados;
7. não há autovalores instáveis no espectro físico.

Para o solíton gaussiano neutro, o operador reduz ao tipo
Ornstein--Uhlenbeck e a estabilidade linear fica controlada.

Para partículas carregadas/spinoriais, a estabilidade exige calcular o
operador \(\mathcal J_{\mathfrak S}\) no setor correspondente.

