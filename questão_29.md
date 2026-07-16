# Questão 29 — Como ocorre a quebra eletrofraca?

## 1. Status

A Questão 29 não deve ser fechada como uma derivação completa e independente
enquanto a Questão 28 permanecer aberta.

O motivo é estrutural: a quebra eletrofraca só faz sentido depois de estar
definido, no setor efetivo, o fibrado interno com grupo

\[
SU(2)_L\times U(1)_Y
\]

e com campos, hipercargas e representações já estabelecidos. Sem isso, qualquer
discussão sobre \(W^\pm\), \(Z\), fóton, ângulo de Weinberg e massas fermiônicas
apenas reproduz a estrutura do Modelo Padrão, em vez de derivá-la da GDQ.

Portanto, a resposta correta é:

\[
\boxed{
\text{a Questão 29 pode ser formulada de modo consistente, mas seu fechamento
pleno é condicional à Questão 28.}
}
\]

---

## 2. Separação entre a ação oficial da GDQ e o setor eletrofraco efetivo

A ação oficial da GDQ permanece intocada:

\[
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
+
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+
\frac{f+\bar f}{2}
-
n
\right]
\mathcal U
\sqrt{\det g}
d^{2n}z
\right]
\frac{d\tau}{\tau}.
\]

A quebra eletrofraca não deve ser inserida como novo postulado fundamental no
bulk. Ela deve aparecer como setor efetivo após:

1. reconstrução do espaço de Hilbert físico;
2. emergência do espaço-tempo lorentziano efetivo \((N,h)\);
3. definição do fibrado espinorial;
4. definição do fibrado interno efetivo;
5. redução do grupo efetivo para \(SU(2)_L\times U(1)_Y\);
6. identificação de um modo geométrico com os números quânticos do Higgs.

Assim, a GDQ não deve ser convertida no Modelo Padrão por hipótese. O Modelo
Padrão deve aparecer, no máximo, como limite efetivo recuperado.

---

## 3. Existe Higgs ou substituto?

A resposta tecnicamente segura é:

\[
\boxed{
\text{existe um modo de ordem eletrofraco efetivo, equivalente ao Higgs no
limite de baixa energia.}
}
\]

Na linguagem do Modelo Padrão, esse modo é um dupleto escalar complexo

\[
H
\in
(1,2)_{1/2}
\quad
\text{sob}
\quad
SU(3)_C\times SU(2)_L\times U(1)_Y.
\]

Na linguagem da GDQ, esse campo não precisa ser ontologicamente elementar. Ele
pode ser interpretado como um modo coletivo geométrico, por exemplo uma
flutuação conformal/torsional estável do setor interno:

\[
\Phi_{\rm EW}
\sim
\text{modo normal geométrico do par }
(g_{\mu\bar\nu},f,\bar f)
\text{ projetado no fibrado efetivo.}
\]

Para reproduzir a física eletrofraca, esse modo deve transformar como:

\[
\boxed{
\Phi_{\rm EW}\sim (1,2)_{1/2}.
}
\]

Essa é a condição mínima. Se o modo geométrico não tiver exatamente esses
números quânticos efetivos, ele não reproduz a quebra eletrofraca observada.

---

## 4. Qual é o potencial?

No nível efetivo, o potencial deve ter a forma de Landau-Higgs:

\[
\boxed{
V_{\rm eff}(\Phi)
=
-\mu_{\rm EW}^2\,\Phi^\dagger\Phi
+
\lambda_{\rm EW}
(\Phi^\dagger\Phi)^2
+
\cdots
}
\]

com

\[
\mu_{\rm EW}^2>0,
\qquad
\lambda_{\rm EW}>0.
\]

O mínimo ocorre em

\[
\Phi^\dagger\Phi
=
\frac{v^2}{2},
\]

ou, em calibre unitário,

\[
\boxed{
\Phi(x)
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0\\
v+\eta(x)
\end{pmatrix}.
}
\]

Na GDQ, esse potencial não deve ser tratado como novo potencial fundamental
arbitrário. Ele deve ser a expansão efetiva da ação geométrica em torno de um
atrator estável:

\[
V_{\rm eff}(\Phi)
\sim
\mathcal S_{\rm GDQ}
\big|_{\text{modo }\Phi}
\quad
\text{expandida perto do ponto crítico.}
\]

Isto significa que, para fechar a questão como teorema, é preciso mostrar que a
segunda variação da ação tem uma direção instável no ponto simétrico e que a
quarta variação estabiliza a bacia:

\[
\delta^2\mathcal S_{\rm GDQ}[\Phi=0]<0,
\qquad
\delta^4\mathcal S_{\rm GDQ}[\Phi=0]>0.
\]

Sem esse cálculo variacional/espectral, o potencial acima é uma forma efetiva
necessária, não uma derivação final.

---

## 5. Como \(W^\pm\), \(Z\) e fóton adquirem suas massas?

Assumindo que o setor efetivo \(SU(2)_L\times U(1)_Y\) foi derivado, a derivada
covariante do modo eletrofraco é:

\[
D_\mu\Phi
=
\left(
\partial_\mu
-ig\,W_\mu^i\frac{\sigma_i}{2}
-ig'YB_\mu
\right)\Phi,
\qquad
Y=\frac12.
\]

O termo cinético efetivo

\[
(D_\mu\Phi)^\dagger(D^\mu\Phi)
\]

gera as massas dos bósons vetoriais quando

\[
\langle\Phi\rangle
=
\frac{1}{\sqrt2}
\begin{pmatrix}
0\\
v
\end{pmatrix}.
\]

As combinações carregadas são:

\[
\boxed{
W_\mu^\pm
=
\frac{1}{\sqrt2}
\left(
W_\mu^1
\mp
iW_\mu^2
\right).
}
\]

Suas massas são:

\[
\boxed{
m_W
=
\frac{gv}{2}.
}
\]

Os campos neutros se misturam:

\[
\begin{pmatrix}
Z_\mu\\
A_\mu
\end{pmatrix}
=
\begin{pmatrix}
\cos\theta_W & -\sin\theta_W\\
\sin\theta_W & \cos\theta_W
\end{pmatrix}
\begin{pmatrix}
W_\mu^3\\
B_\mu
\end{pmatrix}.
\]

O bóson \(Z\) adquire massa:

\[
\boxed{
m_Z
=
\frac{v}{2}\sqrt{g^2+g'^2}.
}
\]

O fóton permanece sem massa:

\[
\boxed{
m_\gamma=0.
}
\]

Geometricamente, a direção não quebrada é a combinação que preserva a carga
elétrica:

\[
\boxed{
Q=T_3+Y.
}
\]

Assim, a quebra é:

\[
\boxed{
SU(2)_L\times U(1)_Y
\longrightarrow
U(1)_{\rm EM}.
}
\]

Na interpretação da GDQ, as direções \(W^1,W^2,W^3,B\) são modos de conexão
efetivos do fibrado interno. O condensado geométrico \(\langle\Phi\rangle\)
torna três direções de conexão massivas e deixa uma direção exatamente
desimpedida, identificada com o fóton.

---

## 6. Qual é o ângulo de Weinberg?

O ângulo de Weinberg é definido por:

\[
\boxed{
\tan\theta_W
=
\frac{g'}{g}.
}
\]

Também:

\[
\boxed{
e
=
g\sin\theta_W
=
g'\cos\theta_W.
}
\]

e

\[
\boxed{
\cos\theta_W
=
\frac{m_W}{m_Z}.
}
\]

Na GDQ, para não importar o Modelo Padrão por hipótese, os acoplamentos \(g\) e
\(g'\) devem ser obtidos como normas geométricas dos modos internos:

\[
\boxed{
\frac1{g_a^2}
\sim
\int_{\mathcal I}
\|\xi_a\|_g^2\,d\mu_g,
}
\]

ou por fórmula espectral equivalente do operador geométrico efetivo. Logo:

\[
\boxed{
\tan\theta_W
=
\left(
\frac{
\int_{\mathcal I}\|\xi_{SU(2)}\|_g^2\,d\mu_g
}{
\int_{\mathcal I}\|\xi_Y\|_g^2\,d\mu_g
}
\right)^{1/2}
}
\]

em uma normalização apropriada dos geradores.

Essa é a forma correta da resposta dentro da GDQ: \(\theta_W\) não deve ser
escolhido; ele deve sair da razão entre as rigidezes/normas geométricas das
duas direções de calibre.

---

## 7. Como férmions adquirem massa?

No limite efetivo, as massas fermiônicas vêm de acoplamentos de Yukawa:

\[
\mathcal L_Y
=
-
y_d\,\bar Q_L\Phi d_R
-
y_u\,\bar Q_L\tilde\Phi u_R
-
y_e\,\bar L_L\Phi e_R
+
\text{h.c.},
\]

com

\[
\tilde\Phi=i\sigma_2\Phi^*.
\]

Após a quebra eletrofraca:

\[
\boxed{
m_f
=
\frac{y_f v}{\sqrt2}.
}
\]

Na GDQ, isso só é aceitável como descrição efetiva. A versão geométrica deve
substituir a escolha livre de \(y_f\) por elementos de matriz entre modos
espinoriais:

\[
\boxed{
y_{ij}
\sim
\int_{\mathcal I}
\bar\psi_i\,
\Phi_{\rm EW}\,
\psi_j\,
d\mu_g.
}
\]

Ou seja, os Yukawas devem ser integrais de sobreposição entre:

1. modos espinoriais do operador de Dirac-Bismut;
2. modo eletrofraco efetivo \(\Phi_{\rm EW}\);
3. medida geométrica interna induzida pela GDQ.

Sem esse cálculo, as massas fermiônicas continuam parâmetros efetivos.

---

## 8. Qual é a escala \(v\)?

Fenomenologicamente, a escala eletrofraca é:

\[
\boxed{
v
=
\left(\sqrt2\,G_F\right)^{-1/2}
\approx
246{,}22\ {\rm GeV}.
}
\]

Essa escala fixa:

\[
m_W=\frac{gv}{2},
\qquad
m_Z=\frac{v}{2}\sqrt{g^2+g'^2},
\qquad
m_f=\frac{y_fv}{\sqrt2}.
\]

Na GDQ, \(v\) deveria ser obtido como autovalor geométrico do modo de ordem
eletrofraco:

\[
\boxed{
v^2
\sim
2\,\|\Phi_{\rm EW}^{(0)}\|^2
}
\]

com \(\Phi_{\rm EW}^{(0)}\) solução estacionária de um problema variacional:

\[
\boxed{
\frac{\delta \mathcal S_{\rm GDQ}^{\rm eff}}
{\delta \Phi_{\rm EW}}
=0.
}
\]

Mais explicitamente, a escala deveria surgir de:

\[
\boxed{
v^2
=
\mathcal N
\int_{\mathcal I}
|\Phi_{\rm EW}^{(0)}|^2\,d\mu_g,
}
\]

onde \(\mathcal N\) é fixado pela normalização dos termos cinéticos efetivos dos
bósons de calibre.

---

## 9. Correção aritmética obrigatória

A fórmula usada no texto:

\[
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\]

não produz \(246\,{\rm GeV}\).

Usando

\[
M_e\simeq0{,}511\,{\rm MeV},
\qquad
\alpha^{-1}\simeq137{,}036,
\]

temos:

\[
\frac{M_e}{\alpha}
=
M_e\alpha^{-1}
\simeq
70{,}03\,{\rm MeV}.
\]

Além disso:

\[
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\simeq
1{,}039.
\]

Logo:

\[
\boxed{
v_K
\simeq
72{,}85\,{\rm MeV},
}
\]

não

\[
246\,{\rm GeV}.
\]

O erro é de escala:

\[
\frac{246\,{\rm GeV}}{72{,}85\,{\rm MeV}}
\approx
3377.
\]

Portanto, essa fórmula deve ser removida como derivação da escala eletrofraca.
Ela pode, no máximo, ser reinterpretada como uma escala geométrica leptônica ou
um parâmetro auxiliar de baixa energia, mas não como o valor esperado do Higgs.

---

## 10. O que pode ser aproveitado do texto original

Pode ser aproveitado:

1. a ideia de que a quebra eletrofraca é uma transição geométrica efetiva;
2. a ideia de que o Higgs pode ser um modo coletivo, não necessariamente
   elementar;
3. a ideia de que \(g\), \(g'\), \(\theta_W\) e \(v\) devem ser extraídos de
   rigidezes geométricas;
4. a associação da quiralidade à orientação complexa/torsional;
5. a interpretação do fóton como direção de calibre não quebrada.

Não pode ser aproveitado como prova:

1. a escala \(v_K=M_e/\alpha(\cdots)\);
2. a afirmação direta de \(v_K\approx246\,{\rm GeV}\);
3. a dedução baseada em \(\mathcal M_{\mathbb C}^3\), pois a estrutura oficial
   usa \(n=4\);
4. a identificação de vetores de Killing com o Modelo Padrão sem representar
   corretamente \(SU(2)_L\times U(1)_Y\);
5. qualquer escolha manual de \(g\), \(g'\), \(Y\), \(y_f\) ou \(v\).

---

## 11. Resposta direta às perguntas obrigatórias

### 1. Existe Higgs ou substituto?

Sim, no setor efetivo deve existir um modo de ordem \(\Phi_{\rm EW}\) com os
números quânticos de um dupleto:

\[
\Phi_{\rm EW}\sim(1,2)_{1/2}.
\]

Ele pode ser interpretado na GDQ como modo geométrico coletivo, não
necessariamente como campo fundamental independente.

### 2. Qual é o potencial?

Efetivamente:

\[
V_{\rm eff}
=
-\mu_{\rm EW}^2\Phi^\dagger\Phi
+
\lambda_{\rm EW}
(\Phi^\dagger\Phi)^2
+
\cdots.
\]

Na GDQ, esse potencial deve ser derivado da expansão da ação efetiva ao redor
do atrator geométrico.

### 3. Como \(W^\pm\), \(Z\) e fóton adquirem massas?

Pelo termo:

\[
(D_\mu\Phi)^\dagger(D^\mu\Phi)
\]

após

\[
\langle\Phi\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}0\\v\end{pmatrix}.
\]

Então:

\[
m_W=\frac{gv}{2},
\qquad
m_Z=\frac{v}{2}\sqrt{g^2+g'^2},
\qquad
m_\gamma=0.
\]

### 4. Qual é o ângulo de Weinberg?

\[
\tan\theta_W=\frac{g'}{g},
\qquad
e=g\sin\theta_W=g'\cos\theta_W.
\]

Na GDQ, \(g\) e \(g'\) devem vir de normas geométricas dos modos de calibre.

### 5. Como férmions adquirem massa?

Por acoplamentos efetivos de Yukawa:

\[
m_f=\frac{y_fv}{\sqrt2}.
\]

Na GDQ, os \(y_f\) devem ser integrais de sobreposição de modos geométricos e
espinoriais, não parâmetros arbitrários.

### 6. Qual é a escala \(v\)?

Fenomenologicamente:

\[
v\simeq246{,}22\,{\rm GeV}.
\]

Na GDQ, ainda falta derivar essa escala como autovalor geométrico. A fórmula
atual com \(M_e/\alpha\) está aritmeticamente errada para esse fim.

---

## 12. Condições para fechar definitivamente a Questão 29

Para fechar a Questão 29 como teorema da GDQ, faltam quatro passos:

1. concluir a Questão 28, derivando o setor efetivo
   \(SU(2)_L\times U(1)_Y\);
2. identificar um modo geométrico \(\Phi_{\rm EW}\sim(1,2)_{1/2}\);
3. derivar o potencial efetivo por segunda e quarta variações da ação;
4. calcular \(v\), \(g\), \(g'\) e \(y_f\) como autovalores, normas ou integrais
   geométricas.

Até isso ser feito:

\[
\boxed{
\text{a Questão 29 está formulada corretamente, mas não está fechada
oficialmente como derivação completa.}
}
\]

