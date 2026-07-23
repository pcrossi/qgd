# Questão 2 — Definição matemática completa da GDQ

## 1. Escopo e resposta

Na auditoria original, a Questão 2 perguntava qual é a dimensão da variedade
fundamental. Durante a reconstrução, a questão foi ampliada para incluir:

1. variedade fundamental;
2. dimensões real e complexa;
3. geometria hermitiana e torção;
4. espaço-tempo físico;
5. emergência da assinatura lorentziana;
6. estrutura spin e circulação meio-inteira;
7. ação efetiva;
8. causalidade;
9. setores de matéria, torção e gauge;
10. formulação do problema espectral.

A resposta final é:

\[
\boxed{
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M=8,
\qquad
\dim_{\mathbb C}M=4.
}
\]

O bulk \(M\) permanece riemanniano. O espaço-tempo físico é uma variedade
quadridimensional \(N\), imersa em \(M\), cuja métrica lorentziana é uma
relação constitutiva construída a partir da métrica induzida e de uma
1-forma global do toro.

A Questão 2 está concluída no nível de definição axiomática de uma teoria
efetiva. A determinação numérica de massas, cargas e constantes de
acoplamento permanece como problema espectral posterior.

---

## 2. Variedade fundamental

### 2.1 Definição

Adota-se:

\[
M=\mathbb R^4\times T^4,
\qquad
T^4=S^1_1\times S^1_2\times S^1_3\times S^1_4.
\]

Consequentemente:

\[
\dim_{\mathbb R}M
=4+4=8.
\]

Equipando os fatores reais aos pares com a estrutura complexa padrão:

\[
\dim_{\mathbb C}M=4.
\]

Essa dimensão é uma definição da teoria. Uma futura explicação dinâmica de
por que a natureza seleciona quatro dimensões complexas é uma questão
diferente.

### 2.2 Propriedades globais

\(M\) é:

- suave;
- conexa;
- orientável;
- sem bordo;
- não compacta, devido a \(\mathbb R^4\);
- paralelizável;
- capaz de receber métricas riemannianas completas.

Somente o setor \(T^4\) é compacto. A teoria não deve voltar a chamar o bulk
inteiro de compacto.

---

## 3. Estrutura hermitiana de Bismut

O dado geométrico fundamental é:

\[
(M,g,J,B,\nabla^B),
\]

onde:

- \(g\) é uma métrica riemanniana completa;
- \(J\) é uma estrutura complexa integrável;
- \(g(JV,JW)=g(V,W)\);
- \(\omega_H(V,W)=g(JV,W)\) é a forma hermitiana fundamental;
- \(B\in\Omega^3(M)\) é uma 3-forma real;
- \(\nabla^B g=0\);
- \(\nabla^B J=0\);
- a torção de \(\nabla^B\) é totalmente antissimétrica.

Uma convenção possível é:

\[
B=d^c\omega_H.
\]

Quando se impõe o setor pluriclosed:

\[
dB=0.
\]

É necessário manter uma convenção única para o sinal de \(d^c\) e de \(B\).

### Consequência

Geometria Kähler estrita e torção de Bismut não nula não devem ser alegadas
simultaneamente para o mesmo setor, pois:

\[
d\omega_H=0
\quad\Longrightarrow\quad
B=0
\]

na convenção usual. A formulação final é hermitiana torsional, não
necessariamente Kähler estrita.

---

## 4. Existência de estrutura spin

Os fibrados tangentes de \(\mathbb R^4\) e \(T^4\) são triviais. Logo:

\[
TM\simeq M\times\mathbb R^8.
\]

Todas as classes de Stiefel–Whitney positivas se anulam. Em particular:

\[
\boxed{
w_2(TM)=0.
}
\]

Portanto, \(M\) admite estrutura spin.

As estruturas spin formam um espaço afim sobre:

\[
H^1(M,\mathbb Z_2)
\simeq H^1(T^4,\mathbb Z_2)
\simeq(\mathbb Z_2)^4.
\]

Existem:

\[
2^4=16
\]

estruturas spin inequivalentes.

---

## 5. Setor antiperiódico e circulação

Escolhe-se o primeiro círculo como ciclo interno ativo:

\[
\theta_1\sim\theta_1+2\pi.
\]

O setor fermiônico mínimo é:

\[
\boxed{
\boldsymbol\varepsilon_F=(1,0,0,0).
}
\]

Uma seção espinorial satisfaz:

\[
\psi(\theta_1+2\pi)=-\psi(\theta_1).
\]

Após duas voltas:

\[
\psi(\theta_1+4\pi)=\psi(\theta_1).
\]

Os modos permitidos são:

\[
\psi_n(\theta_1)
\propto e^{i(n+1/2)\theta_1}.
\]

Assim:

\[
p_{\theta_1}
=\hbar\left(n+\frac12\right)
\]

e:

\[
\boxed{
\oint p_{\theta_1}\,d\theta_1
=h\left(n+\frac12\right).
}
\]

### Interpretação correta

A circulação meio-inteira é uma consequência da estrutura spin
antiperiódica escolhida. A soma de Poisson usada no manuscrito transfere
corretamente a monodromia \(\pi\) para o espectro \(n+1/2\), mas não seleciona
por si mesma a monodromia.

A escolha entre as 16 estruturas spin é um axioma do setor físico enquanto
não houver uma demonstração de seleção dinâmica.

---

## 6. Espaço-tempo físico

Seja \(N\) uma variedade real quadridimensional e:

\[
X:N\longrightarrow M
\]

uma imersão.

A métrica induzida é:

\[
q_{\mu\nu}
=g_{AB}(X)
\partial_\mu X^A
\partial_\nu X^B.
\]

Como \(g\) é positiva definida e \(X\) é uma imersão:

\[
q=X^*g
\]

também é positiva definida. Portanto, uma métrica lorentziana não pode ser
obtida pela simples restrição de \(g\).

---

## 7. Forma-relógio e domínio físico

Escolha no toro:

\[
\omega=d\theta_1,
\qquad
d\omega=0.
\]

Seu pullback é:

\[
u=X^*\omega.
\]

Uma forma não nula no toro pode ter pullback nulo. Consequentemente, o setor
físico deve ser definido por:

\[
\boxed{
\mathcal C
=
\left\{
X\in{\rm Imm}(N,M):
X^*\omega\neq0
\text{ em todo ponto}
\right\}.
}
\]

Essa é uma restrição cinemática/topológica. A ação não produz
automaticamente uma barreira infinita em \(u=0\).

---

## 8. Teorema de lorentzianização

Defina:

\[
s=q^{-1}(u,u)
=q^{\mu\nu}u_\mu u_\nu.
\]

No setor \(\mathcal C\):

\[
s>0.
\]

A métrica física é:

\[
\boxed{
h_{\mu\nu}
=q_{\mu\nu}
-2\frac{u_\mu u_\nu}{s}.
}
\]

### 8.1 Inversa

Definindo:

\[
u^\mu=q^{\mu\nu}u_\nu,
\]

tem-se:

\[
\boxed{
h^{\mu\nu}
=q^{\mu\nu}
-2\frac{u^\mu u^\nu}{s}.
}
\]

A contração fornece:

\[
h_{\mu\alpha}h^{\alpha\nu}
=\delta_\mu^\nu.
\]

### 8.2 Assinatura

Num referencial \(q\)-ortonormal adaptado a \(u\):

\[
q=\operatorname{diag}(1,1,1,1),
\qquad
u=(u_0,0,0,0).
\]

Logo:

\[
h=\operatorname{diag}(-1,1,1,1).
\]

Portanto:

\[
\boxed{
\operatorname{sign}(h)=(-,+,+,+).
}
\]

### 8.3 Determinante

Pelo lema do determinante para uma modificação de posto um:

\[
\det h
=\det q
\left(
1-2\frac{s}{s}
\right).
\]

Assim:

\[
\boxed{
\det h=-\det q\neq0.
}
\]

### Consequência lógica

O bulk permanece riemanniano. A assinatura lorentziana pertence à métrica
constitutiva de \(N\). Não ocorre uma transição singular de assinatura no
bulk e a existência do tempo não depende de \(\nabla f\).

---

## 9. Background Minkowski explícito

Considere no bulk:

\[
g
=\sum_{A=0}^3dY^A{}^2
+\sum_{a=1}^4R_a^2d\theta_a^2.
\]

Escolha:

\[
N=\mathbb R_t\times\mathbb R^3
\]

e a imersão:

\[
Y^0=bt,
\qquad
Y^i=x^i,
\qquad
\theta_1=\Omega t,
\]

com:

\[
b^2+R_1^2\Omega^2=1,
\qquad
b\neq0,
\qquad
\Omega\neq0.
\]

Então:

\[
q=dt^2+d\mathbf x^2,
\qquad
u=\Omega dt,
\]

e:

\[
\boxed{
h=-dt^2+d\mathbf x^2.
}
\]

O enrolamento em \(S^1\) não fecha a curva física porque \(Y^0=bt\) não é
periódico.

### Hiperbolicidade global

Para uma curva causal:

\[
-\dot t^2+|\dot{\mathbf x}|^2\leq0,
\]

logo:

\[
\left|\frac{d\mathbf x}{dt}\right|\leq1.
\]

Uma curva causal inextensível não pode terminar em \(t\) finito, pois teria
posição espacial convergente e seria extensível. Portanto, cada curva causal
inextensível cruza cada folha \(t=\mathrm{constante}\) exatamente uma vez.

Assim:

\[
\boxed{
(N,h)\text{ é globalmente hiperbólico}.
}
\]

---

## 10. Escalas

Devem ser distinguidas:

\[
\Lambda_e=m_ec^2,
\]

\[
\Lambda_C=\text{corte da EFT de Cartan},
\]

\[
\Lambda_{\rm Pl}
=\sqrt{\frac{\hbar c^5}{G}}.
\]

A hierarquia é:

\[
\boxed{
\Lambda_e\ll\Lambda_C\ll\Lambda_{\rm Pl}.
}
\]

Os comprimentos associados são:

\[
\ell_X=\frac{\hbar c}{\Lambda_X}.
\]

Em particular:

\[
\boxed{
\ell_C=\frac{\hbar c}{\Lambda_C}.
}
\]

Valores eletrônicos, bariônicos e de Planck não podem compartilhar o mesmo
símbolo.

---

## 11. Origem da energia barotrópica

A medida de Perelman é:

\[
\rho=e^{-f}
\]

à parte da normalização do kernel de calor.

O termo \(f\rho\) do funcional produz:

\[
f\rho=-\rho\ln\rho.
\]

Logo, a entropia de Boltzmann–Gibbs é:

\[
S_{\rm BG}
=-\int\rho\ln\rho\,dV.
\]

A energia livre de Helmholtz é:

\[
\mathcal F
=\mathcal E-\Theta_gS_{\rm BG}.
\]

Portanto:

\[
-\Theta_gS_{\rm BG}
=\Theta_g\int\rho\ln\rho\,dV.
\]

Em torno de uma densidade \(\rho_0\), a forma relativa é:

\[
\boxed{
\mathcal F_{\rm ent}
=K_0
\int
\left[
\rho\ln\frac{\rho}{\rho_0}
-\rho+\rho_0
\right]dV,
}
\]

com:

\[
\boxed{
K_0=\Theta_g=\frac1{2\epsilon}>0.
}
\]

Sua primeira variação é:

\[
\frac{\delta\mathcal F_{\rm ent}}{\delta\rho}
=K_0\ln\frac{\rho}{\rho_0}.
\]

Sua segunda variação é:

\[
\delta^2\mathcal F_{\rm ent}
=K_0
\int\frac{(\delta\rho)^2}{\rho}\,dV>0.
\]

Consequentemente, o equilíbrio é restaurador e estável.

---

## 12. Relação entre \(\epsilon\) e o fluxo

Defina:

\[
\widehat\tau=\frac{\tau}{\ell_C^2}.
\]

No pareamento entre o setor de Fisher do funcional de Perelman e a
normalização hidrodinâmica usada no manuscrito:

\[
\boxed{
\epsilon^2=2\widehat\tau
=\frac{2\tau}{\ell_C^2}.
}
\]

Ou:

\[
\epsilon
=\frac{\sqrt{2\tau}\Lambda_C}{\hbar c}.
\]

Essa relação é uma convenção de redução numa janela de renormalização. Na
ação física local, \(\tau\) e \(\epsilon\) são tratados como constantes
dentro da janela. Sua mudança entre janelas é uma evolução de escala, não
um campo externo local.

---

## 13. Ação efetiva causal

As variáveis mínimas são:

\[
X^A,\qquad
\Psi,\qquad
\mathcal A,
\]

e um fluxo topológico \(B_{\rm top}\).

Defina:

\[
B=d\mathcal A+B_{\rm top}.
\]

A ação é:

\[
\boxed{
S=S_{\rm EH}+S_\Psi+S_B.
}
\]

### Gravidade

\[
S_{\rm EH}
=\frac1{16\pi G}
\int_N
R[h[X]]
\sqrt{-h[X]}\,d^4x.
\]

### Matéria

\[
S_\Psi
=-\int_N
\left[
\hbar^2h^{\mu\nu}
\partial_\mu\Psi^*
\partial_\nu\Psi
+m_0^2c^2|\Psi|^2
+U_{\rm bar}(|\Psi|^2)
\right]
\sqrt{-h}\,d^4x,
\]

\[
U_{\rm bar}(\rho)
=K_0
\left[
\rho\ln\frac{\rho}{\rho_0}
-\rho+\rho_0
\right].
\]

O termo \(m_0^2c^2|\Psi|^2\) fornece a energia de repouso. Não se deve
adicionar manualmente outro termo \(+\rho\) às equações de Friedmann.

### Torção

\[
S_B
=-\frac1{12}
\int_N
B_{\mu\nu\lambda}B^{\mu\nu\lambda}
\sqrt{-h}\,d^4x.
\]

As equações são:

\[
dB=0,
\qquad
d(*_hB)=0.
\]

---

## 14. Madelung e potencial de Bohm

Escreva:

\[
\Psi=\sqrt\rho\,e^{iS/\hbar}.
\]

A variação de \(\Psi^*\) gera uma equação complexa de segunda ordem. Sua
parte imaginária é:

\[
\boxed{
\nabla_\mu
\left(
\rho\nabla^\mu S
\right)=0.
}
\]

Sua parte real é:

\[
\boxed{
h^{\mu\nu}
\partial_\mu S\partial_\nu S
+m_0^2c^2
+U_{\rm bar}'(\rho)
-\hbar^2
\frac{\Box_h\sqrt\rho}{\sqrt\rho}
=0.
}
\]

O termo:

\[
-\hbar^2
\frac{\Box_h\sqrt\rho}{\sqrt\rho}
\]

é o potencial quântico covariante de Bohm.

No limite não relativístico:

\[
\omega^2
=c_s^2k^2
+\frac{\hbar^2}{4m_0^2}k^4.
\]

O termo \(k^4\) é uma aproximação hidrodinâmica. A equação fundamental
continua sendo de segunda ordem e tem símbolo:

\[
h^{\mu\nu}k_\mu k_\nu.
\]

### Consequência causal

A velocidade de grupo da aproximação truncada não deve ser usada no
ultravioleta. A velocidade frontal é determinada pelo símbolo da equação
fundamental e coincide com o cone de \(h\).

---

## 15. Variação completa da imersão

Defina:

\[
\mathcal E^{\mu\nu}
=
\frac2{\sqrt{-h}}
\frac{\delta S}{\delta h_{\mu\nu}}.
\]

Então:

\[
\delta_XS
=\frac12
\int_N
\sqrt{-h}\,
\mathcal E^{\mu\nu}
\delta_Xh_{\mu\nu}\,d^4x.
\]

Com:

\[
h_{\mu\nu}
=q_{\mu\nu}
-2\frac{u_\mu u_\nu}{s},
\]

obtém-se:

\[
\delta h_{\mu\nu}
=\delta q_{\mu\nu}
-\frac2s
\left(
\delta u_\mu u_\nu
+u_\mu\delta u_\nu
\right)
+\frac{2u_\mu u_\nu}{s^2}\delta s,
\]

\[
\delta s
=\delta q^{-1}(u,u)
+2q^{-1}(u,\delta u).
\]

Como \(d\omega=0\):

\[
\delta u
=d(\omega_A\delta X^A).
\]

Esse termo é exato, mas não é apenas borda: após integração por partes, ele
gera uma corrente longitudinal.

A equação correta é mantida na forma:

\[
\boxed{
\frac{\delta S[h(q[X],u[X])]}{\delta X^A}=0.
}
\]

Ela contém a projeção extrínseca, a variação do projetor temporal e a
corrente associada a \(u\). Só em backgrounds especiais reduz-se à equação
usual de Regge–Teitelboim.

---

## 16. Torção cosmológica

Em FLRW:

\[
h=-dt^2+a(t)^2\gamma_{ij}dx^idx^j.
\]

Para:

\[
B_{ijk}=b_0\varepsilon_{ijk},
\]

tem-se:

\[
|B|^2=\frac{6b_0^2}{a^6}.
\]

O tensor de energia da 3-forma fornece:

\[
\boxed{
\rho_B=\frac{b_0^2}{2a^6},
\qquad
P_B=\rho_B,
\qquad
w_B=1.
}
\]

Logo:

\[
\dot\rho_B+6H\rho_B=0.
\]

A torção é um fluido rígido. Ela não deve ser apresentada como energia
escura com \(w=-3\).

---

## 17. Friedmann e Jeans

As equações cosmológicas assumem:

\[
H^2+\frac{K}{a^2}
=\frac{8\pi G}{3}
\left(
\rho_\Psi+\rho_B
\right),
\]

\[
\frac{\ddot a}{a}
=-\frac{4\pi G}{3}
\left[
\rho_\Psi+3P_\Psi
+\rho_B+3P_B
\right].
\]

\(\rho_\Psi\) e \(P_\Psi\) devem ser calculadas diretamente da ação.

No limite não relativístico, sub-horizonte e de campo fraco:

\[
\ddot\delta
+2H\dot\delta
+\left[
\frac{c_s^2k^2}{a^2}
+\frac{\hbar^2k^4}{4m_0^2a^4}
-4\pi G\rho_{\rm bg}
\right]\delta
=0.
\]

A escala de Jeans é:

\[
\boxed{
k_J^2
=
\frac{
-c_s^2a^2
+\sqrt{
c_s^4a^4
+\frac{4\pi G\hbar^2}{m_0^2}
\rho_{\rm bg}a^4
}
}{
\hbar^2/(2m_0^2)
}.
}
\]

Essa equação é válida no regime de redução declarado, não como equação
fundamental ultravioleta.

---

## 18. Setor gauge

O pullback:

\[
X^*d\theta_a
\]

é fechado e produz somente conexão plana. Para campos locais não triviais,
introduz-se uma conexão de Ehresmann:

\[
\Theta^a
=d\theta^a+g_aA^a.
\]

Sob:

\[
\theta^a\mapsto\theta^a-\lambda^a(x),
\]

tem-se:

\[
A^a
\mapsto
A^a+\frac1{g_a}d\lambda^a.
\]

A curvatura é:

\[
F^a=dA^a.
\]

As translações do toro geram inicialmente:

\[
U(1)^4.
\]

A ação reduzida é:

\[
S_{\rm gauge}
=-\frac14
\int_N
G_{ab}
F^a_{\mu\nu}F^{b\,\mu\nu}
\sqrt{-h}\,d^4x.
\]

O eletromagnetismo é uma combinação:

\[
A_{\rm em}=v_aA^a.
\]

A direção \(v_a\) e sua normalização devem ser determinadas pelo background
espectral.

---

## 19. Setor espinorial

No espaço físico spin, o operador de Dirac com torção e gauge é:

\[
\boxed{
\slashed D_{B,A}
=\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18
B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA^a_\mu
\right).
}
\]

A ação é:

\[
S_{\rm spin}
=\int_N
\bar\psi
\left(
i\hbar\slashed D_{B,A}
-mc
\right)
\psi
\sqrt{-h}\,d^4x.
\]

O símbolo principal satisfaz:

\[
(\gamma^\mu k_\mu)^2
=h^{\mu\nu}k_\mu k_\nu.
\]

Matéria escalar, gravidade, torção, gauge e espinores compartilham o cone de
\(h\) quando todos são acoplados covariantemente à mesma métrica.

---

## 20. Espectro do toro

Para:

\[
g_{T^4}
=\sum_aR_a^2d\theta_a^2,
\]

os modos são:

\[
\psi_{\mathbf n}
\propto
\exp
\left[
i\sum_a
\left(
n_a+\frac{\varepsilon_a}{2}
\right)\theta_a
\right].
\]

Os momentos internos são:

\[
p_a
=\frac{\hbar}{R_a}
\left(
n_a+\frac{\varepsilon_a}{2}
\right).
\]

Os autovalores satisfazem:

\[
\boxed{
|\lambda_{\mathbf n}|
=
\sqrt{
\sum_a
\frac{
(n_a+\varepsilon_a/2)^2
}{R_a^2}
}.
}
\]

As massas reduzidas são:

\[
m_{\mathbf n}^2c^2
=m_8^2c^2
+\hbar^2|\lambda_{\mathbf n}|^2.
\]

No modo mínimo antiperiódico, se \(m_8=0\):

\[
\boxed{
m_{\min}c^2
=\frac{\hbar c}{2R_1}.
}
\]

Isso deriva geometricamente uma escala de massa em função de \(R_1\). Para
predizer o elétron, \(R_1\) deve ser obtido da estabilização de
Ricci–Bismut, e não escolhido a partir de \(m_e\).

---

## 21. Cargas e constante de estrutura fina

Os números de carga da rede dual são:

\[
Q_a
=n_a+\frac{\varepsilon_a}{2}.
\]

Para a direção eletromagnética:

\[
q_{\mathbf n}
=g_{\rm em}v_aQ_a.
\]

A constante de estrutura fina é:

\[
\boxed{
\alpha
=\frac{g_{\rm em}^2}{4\pi\hbar c}.
}
\]

Na redução toroidal:

\[
\frac1{g_{4,a}^2}
\propto
\frac{\operatorname{Vol}(T^4)}
{\kappa_8^2}
R_a^2,
\]

com o fator exato dependente da normalização da ação octodimensional.

Para calcular \(\alpha\), são necessários:

1. background estacionário;
2. raios \(R_a\);
3. métrica interna \(G_{ab}\);
4. normalização \(\kappa_8\);
5. direção \(v_a\).

A fórmula antiga baseada em \(T^5\times S^3\), ordem \(1920\) e uma
“característica de Euler \(5\)” não pertence à geometria final e não deve ser
usada como demonstração.

---

## 22. Estatística fermiônica

Circulação meio-inteira e transformação por \(4\pi\) demonstram a estrutura
spin, mas não bastam para obter anticomutação.

Na EFT local, causal, com energia positiva e covariância local de Lorentz, o
teorema spin–estatística exige:

\[
\{
\widehat\psi_\alpha(t,\mathbf x),
\widehat\psi_\beta^\dagger(t,\mathbf y)
\}
=
\delta_{\alpha\beta}
\delta^{(3)}(\mathbf x-\mathbf y),
\]

\[
\{
\widehat\psi_\alpha,
\widehat\psi_\beta
\}=0.
\]

Logo:

\[
(\widehat a_j^\dagger)^2=0.
\]

O princípio de exclusão decorre da quantização fermiônica local. Não deve ser
atribuído apenas à circulação clássica ou à sequência de Mayer–Vietoris.

---

## 23. Problema espectral final

As previsões quantitativas exigem encontrar:

\[
(g_*,B_*,f_*,R_{a,*})
\]

tal que:

\[
\delta\mathcal W_B[g,B,f]=0.
\]

Depois devem ser calculados:

\[
\operatorname{Spec}(\slashed D_{B_*}),
\qquad
\operatorname{Spec}(\Delta_{B_*}),
\qquad
G_{ab,*},
\qquad
\kappa_{8,*}.
\]

As previsões assumem a forma:

\[
m_j^2c^2
=m_8^2c^2
+\hbar^2
\lambda_j(\slashed D_{B_*}^2),
\]

\[
q_j
=g_{\rm em}v_aQ_{j,a},
\]

\[
\alpha
=\frac{g_{\rm em}^2}{4\pi\hbar c}.
\]

---

## 24. Consequências lógicas

Da formulação seguem:

1. o bulk não é o espaço-tempo físico;
2. a métrica positiva do bulk não muda de assinatura;
3. o tempo físico é definido pela reflexão constitutiva na direção \(u\);
4. a assinatura não desaparece quando \(\nabla f=0\);
5. a forma-relógio e o eletromagnetismo são setores distintos;
6. torção de 3-forma não é o tensor de Maxwell;
7. o termo de Bohm decorre da decomposição de um campo complexo causal;
8. o termo \(k^4\) é efetivo, não fundamental;
9. a torção cosmológica espacial possui \(w=1\);
10. a estrutura spin antiperiódica produz circulação meio-inteira;
11. massas e cargas tornam-se problemas espectrais;
12. valores experimentais não podem ser usados como entradas numa alegação
    de derivação de primeiros princípios.

---

## 25. Status oficial

### Demonstrado

- \(M=\mathbb R^4\times T^4\);
- dimensões \(8\) real e \(4\) complexa;
- propriedades globais do bulk;
- existência de estrutura spin;
- 16 estruturas spin;
- setor antiperiódico;
- circulação \(n+1/2\);
- métrica lorentziana constitutiva;
- inversa, assinatura e determinante;
- background Minkowski globalmente hiperbólico;
- ação efetiva causal;
- energia barotrópica convexa;
- origem do potencial de Bohm;
- setor torsional saudável;
- formulação de gauge;
- operador de Dirac;
- cone causal comum na EFT;
- espectro do toro plano;
- formulação do problema quantitativo.

### Axiomático

- escolha de \(M\);
- escolha do ciclo-relógio;
- restrição \(X^*\omega\neq0\);
- escolha da estrutura spin antiperiódica;
- manutenção do produto global em vez de uma fibração toroidal não trivial.

### Ainda não calculado

- seleção dinâmica dos axiomas discretos;
- background não trivial completo de Ricci–Bismut;
- raios internos estabilizados;
- \(\Lambda_C\);
- massas observadas;
- direção eletromagnética;
- cargas físicas;
- \(g_{\rm em}\) e \(\alpha\);
- soluções cosmológicas não triviais da equação de imersão.

---

## 26. Veredito

### Questão original

\[
\boxed{
\dim_{\mathbb R}M=8,
\qquad
\dim_{\mathbb C}M=4.
}
\]

Está concluída.

### Questão ampliada

\[
\boxed{
\text{A definição matemática da GDQ está concluída como EFT axiomática.}
}
\]

A teoria possui agora uma referência única e internamente coerente para sua
variedade, assinatura, spin, ação e causalidade.

\[
\boxed{
\text{A predição numérica das constantes permanece aberta como problema
espectral de Ricci–Bismut.}
}
\]

Essa limitação não reabre a definição da teoria; delimita a próxima etapa de
pesquisa.
