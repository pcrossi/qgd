---
title: "Auditoria do termo canônico rho d_t S_R"
---

# Auditoria do termo canônico $\rho\,\partial_tS_R$

## Enunciado

Queremos verificar se o pullback temporal da ação oficial implica diretamente

$$
\Theta_{\Sigma}=\int_{\Sigma}\rho\,\delta S_R\,d\Sigma
$$

e, por consequência, uma ação reduzida contendo

$$
\int dt\int_{\Sigma_t}\rho\,\partial_tS_R\,d\Sigma_t.
$$

A resposta direta é negativa: a ação oficial produz um momento proporcional à
derivada normal da fase. A igualdade com $\rho$ exige uma condição dinâmica ou
uma polarização adicional, que deve ser derivada.

## Corrente obtida da ação oficial

Com

$$
f=-\ln\rho+\frac{i}{\hbar}S_R,
$$

a medida $\mathcal U$ não depende de $S_R$. A variação da fase fornece

$$
\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

Se $n$ é o vetor normal unitário selecionado pela forma-relógio sincronizada,
o potencial pré-simplético da fase numa folha $\Sigma$ é

$$
\Theta_{\Sigma,S}
=\int_\Sigma\Pi_{S_R}\,\delta S_R\,d\Sigma,
$$

onde

$$
\Pi_{S_R}
=n_\mu\widehat J_S^\mu
=\frac{2\tau}{\hbar\Lambda_C^2}
\mathcal U\,n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

Usando

$$
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n},
$$

obtemos

$$
\Pi_{S_R}
=\rho\,
\frac{2\tau}{\hbar\Lambda_C^2(4\pi z_\tau)^n}
n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R.
$$

Portanto,

$$
\boxed{\Pi_{S_R}\neq\rho\quad\text{em geral}.}
$$

## Por que a normalização interna não basta

Se $K$ representa as direções internas, a densidade de carga transportada ao
laboratório é o pushforward

$$
\varrho_{\rm lab}(x)=\int_K\Pi_{S_R}(x,y)\,dV_K,
$$

enquanto o marginal geométrico é obtido do pushforward de $\mathcal U$. A
normalização da distribuição condicional interna não elimina o fator
$n\cdot dS_R$. Uma fase constante fornece $\Pi_{S_R}=0$ mesmo quando
$\rho>0$ e a medida interna está normalizada. Logo,

$$
\boxed{
\int_K\mathcal U\,dV_K=1
\quad\not\Rightarrow\quad
\varrho_{\rm lab}=\rho_{\rm lab}.
}
$$

## Condição exata de fechamento

A identidade canônica requer, depois do pushforward causal e interno,

$$
\boxed{\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}.}
$$

No caso fatorado, isso equivale à condição ponderada

$$
\frac{2\tau}{\hbar\Lambda_C^2(4\pi z_\tau)^n}
\left\langle
n_\mu g^{\mu\bar\nu}\partial_{\bar\nu}S_R
\right\rangle_K=1.
$$

Também é preciso escolher uma polarização física que elimine ou relacione o
momento conjugado da amplitude $u=-\ln\rho$. Essa condição deve seguir de uma
estrutura interna da GDQ, como um vínculo causal de fluxo, uma redução de
Routh em carga de Noether fixa, uma polarização de contorno derivada ou uma
identidade da solução estacionária completa.

## Forma de primeira ordem

A ação de segunda ordem pode ser reescrita em forma hamiltoniana por
transformação de Legendre, sem acrescentar uma nova ação fundamental:

$$
I_{\rm red}
=\int dt\int_{\Sigma_t}
\left(
\Pi_{S_R}^{\rm lab}\,\partial_tS_R
-\mathcal H_{\rm red}
\right)d\Sigma_t.
$$

O termo de Madelung aparece exatamente se a dinâmica ou o vínculo físico
selecionar

$$
\Pi_{S_R}^{\rm lab}=\rho_{\rm lab}.
$$

A transformação de Legendre explica como um termo linear temporal pode surgir
de uma ação originalmente quadrática, mas não prova sozinha a identificação
do momento com a densidade.

## Redução de Routh e desigualdade variacional

Há uma rota mais forte que não precisa supor previamente uma fase
monoenergética. Suponha que o pullback sincronizado e a integração interna
reduzam o Hamiltoniano temporal a

$$
H_t[\Pi,\rho]
=\int_\Sigma\frac{\Pi^2}{2A\rho}\,d\Sigma,
\qquad A>0
$$

com $A$ constante. Defina

$$
Q_S=\int_\Sigma\Pi\,d\Sigma,
\qquad
N_\rho=\int_\Sigma\rho\,d\Sigma.
$$

Por Cauchy--Schwarz,

$$
Q_S^2
\leq
\left(\int_\Sigma\frac{\Pi^2}{\rho}\,d\Sigma\right)
\left(\int_\Sigma\rho\,d\Sigma\right),
$$

e, portanto,

$$
H_t\geq\frac{Q_S^2}{2A N_\rho}.
$$

A igualdade ocorre se, e somente se,

$$
\Pi=\frac{Q_S}{N_\rho}\rho
$$

quase em toda parte. Assim, se a carga de fase primitiva e a normalização da
densidade forem derivadas independentemente como

$$
Q_S=N_\rho=1,
$$

o minimizador satisfará

$$
\Pi=\rho.
$$

Essa é uma prova variacional condicional legítima. Para aplicá-la à GDQ ainda
é necessário demonstrar diretamente no pullback que:

1. $A$ é constante no suporte físico;
2. lapse, shift e modos internos não produzem termos cruzados;
3. não existe fuga de fluxo pelo bordo;
4. $\rho>0$ no suporte conectado;
5. $Q_S=1$ é fixado independentemente como setor primitivo, e não escolhido
   depois para obter a igualdade;
6. o background é o minimizador do setor convexo.

Se $A=A(x)$, o minimizador é proporcional a $A(x)\rho(x)$, não a $\rho(x)$.
Se $Q_S=1$ for apenas uma renormalização escolhida depois de $N_\rho=1$, o
argumento será circular.

## Por que o ansatz estacionário não basta

O ansatz $S_R=-Et+\sigma$ fornece $\Pi=Z_E\rho$ somente quando a frequência,
o lapse e o pushforward são uniformes. Igualar depois $Q_S=N_\rho=1$ fixa
$Z_E=1$, mas não prova que a carga de fase seja primitivamente unitária. Além
disso, as cargas de translação temporal e de deslocamento da fase são cargas
de Noether distintas. Portanto, essa rota define um setor on shell possível,
mas não constitui a prova geral procurada.

## Cálculo ADM e teste de preservação

Suponha provisoriamente que o pushforward causal seja local em $t$. Com

$$
ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)
$$

e $D_tS_R=\partial_tS_R-N^i\partial_iS_R$, o setor de fase assume a forma

$$
L_S=\frac A2N\sqrt h\,\rho
\left[-(D_tS_R/N)^2+h^{ij}\partial_iS_R\partial_jS_R\right].
$$

Logo,

$$
\Pi_{S_R}=-A\sqrt h\,\rho\frac{D_tS_R}{N}.
$$

A igualdade densitizada desejada equivale a

$$
\Pi_{S_R}=\sqrt h\rho
\quad\Longleftrightarrow\quad
-A\frac{D_tS_R}{N}=1.
$$

O setor de amplitude também possui cinética temporal regular:

$$
L_\rho=\frac{A\hbar^2}{2}N\sqrt h
\left[-\frac{(D_t\rho/N)^2}{\rho}+\frac{|D\rho|^2}{\rho}\right],
$$

com momento independente

$$
p_\rho=-A\hbar^2\sqrt h\frac{D_t\rho/N}{\rho}.
$$

Assim, a Hessiana temporal em $(\partial_tS_R,\partial_t\rho)$ é regular para
$A\rho\neq0$. A condição

$$
C:=\Pi_{S_R}-\sqrt h\rho=0
$$

não é vínculo primário da ação oficial. Suas equações hamiltonianas mostram
que $\dot C=0$ impõe uma condição adicional envolvendo $p_\rho$, expansão da
folha, shift e fluxo espacial da fase; ela não se anula identicamente sobre
$C=0$.

No setor estacionário comóvel,

$$
N^i=0,
\quad D_iS_R=0,
\quad\dot\rho=\dot h=0,
\quad p_\rho=0,
$$

$C=0$, uma vez selecionado inicialmente, é preservado. A desigualdade de
Routh mostra que essa folha é o minimizador no setor uniforme de carga fixa,
mas não deriva sua normalização inicial.

## Obstrução causal ao cálculo de $A$

O corpus define $z_\tau=\tau+i\nu_0t$, mas não fornece um mapa completo

$$
\gamma:t\longmapsto\tau_\gamma(t)
$$

nem uma identidade que determine

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)
$$

em função de $dt$. A sincronização fixa a direção, a unidade e a orientação do
relógio local, mas não esse Jacobiano causal. O projetor de Laurent histórico
normaliza um coeficiente já constante; ele não demonstra a fatorização do
momento de fase. Por isso $A$ ainda não pode ser avaliado sem completar o
pullback causal.

## Veredito final

$$
\boxed{
\text{A corrente de fase e o potencial pré-simplético estão derivados.}
}
$$

$$
\boxed{
C_3\text{ estacionário: }\Pi_{S_R}=\rho
\text{ pode ser selecionada e é preservada condicionalmente.}
}
$$

$$
\boxed{
\text{Dinâmica geral: }\Pi_{S_R}=\rho
\text{ não é vínculo nem identidade da ação oficial.}
}
$$

Uma derivação geral exigiria que o pullback causal produzisse uma redução
degenerada ou uma polarização física que eliminasse metade dos dados
canônicos. Essa estrutura não está demonstrada na formulação vigente.

## Auditoria da tentativa Killing--Perelman

Uma proposta posterior tentou fechar as duas condições restantes por
isometria de Killing e monotonicidade de Perelman. Ela preserva uma ideia
útil, mas não constitui prova.

Primeiro, de $\mathcal L_Kg=0$ não segue

$$
\Delta\kappa=0.
$$

A equação de Killing controla a métrica ao longo de $K$; ela não fornece uma
equação elíptica para o Jacobiano independente
$\kappa=d\tau_\gamma/dt$. Além disso, mesmo que
$\tau_\gamma(t)=at+b$, teríamos

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)
=\frac{a}{at+b}\,dt,
$$

que não é constante. Um coeficiente constante em $d\tau/\tau$ exigiria uma
lei exponencial para $\tau_\gamma$, não uma lei afim. Essa lei precisa vir da
dinâmica causal, não da isometria plana isolada.

Segundo, a monotonicidade de um funcional auxiliar de Perelman em $\tau$ não
implica que o momento físico $p_\rho$ decaia em $t$. Ela também não demonstra:

1. convergência de todo dado inicial para um único sóliton;
2. identificação do sóliton com o mínimo do Hamiltoniano de Routh;
3. saturação da desigualdade de Cauchy--Schwarz;
4. relaxamento físico de um aparelho;
5. equivalência entre o fluxo geométrico em $\tau$ e dissipação temporal em
   $t$.

A parte válida da proposta continua sendo a desigualdade de Routh. Ela prova
a forma do minimizador se o sistema já estiver no setor convexo declarado;
não prova que Perelman selecione dinamicamente esse setor.

## Auditoria da rota escala--eliminação adiabática

Uma segunda proposta substituiu Killing--Perelman por um homomorfismo de
relógios e por eliminação adiabática. Ela melhora a separação entre $\tau$ e
$t$, mas ainda não fecha a prova.

Se for demonstrado ou adotado que o mapa causal é um homomorfismo contínuo

$$
\gamma:(\mathbb R,+)\longrightarrow(\mathbb R_+,\times),
$$

então

$$
\gamma(t+s)=\gamma(t)\gamma(s)/\gamma(0)
$$

implica rigorosamente

$$
\tau_\gamma(t)=\tau_0e^{\kappa t}
$$

e

$$
\gamma^*\left(\frac{d\tau}{\tau}\right)=\kappa\,dt.
$$

O resultado matemático é correto. Contudo, a invariância de $d\tau/\tau$ e a
homogeneidade dos tiques não demonstram, sozinhas, que o mapa físico deve
preservar a lei de grupo. Essa compatibilidade de composição precisa ser
derivada da construção causal ou declarada como condição do relógio. Ela
também não fixa o valor de $\kappa$ nem, sozinha, todos os fatores de $A$.

A equação efetiva

$$
\dot p_\rho=-\Gamma p_\rho-\frac{\delta H_t}{\delta\rho}
$$

não segue ainda da ação oficial. Para obtê-la por eliminação do aparelho é
necessário calcular seu funcional de influência e demonstrar positividade do
kernel dissipativo, ruído compatível com flutuação--dissipação, separação de
escalas, aproximação markoviana e gap do setor rápido. Além disso,
$p_\rho\to0$ e $N^i\to0$ não implicam por si mesmos que a distribuição
$\Pi_{S_R}$ minimize $H_t$ a carga fixa. É preciso derivar uma equação fechada
para esse modo ou um funcional de Lyapunov cuja igualdade selecione Routh.

Assim, a parte causal é um teorema condicional simples; a parte dissipativa é
um programa calculável da teoria da medida, não uma prova já concluída.

## Teorema exato no espaço de estados Kähler

Existe uma origem intrínseca e exata para o par $(\rho,S_R)$ no espaço de
estados. Defina

$$
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
$$

Então

$$
\delta\Psi
=e^{iS_R/\hbar}
\left(
\frac{\delta\rho}{2\sqrt\rho}
+\frac{i\sqrt\rho}{\hbar}\delta S_R
\right),
$$

e, portanto,

$$
\hbar\operatorname{Im}(\bar\Psi\,\delta\Psi)
=\rho\,\delta S_R.
$$

Integrando na folha física,

$$
\boxed{
\Theta_{\rm state}
=\hbar\operatorname{Im}\langle\Psi,\delta\Psi\rangle
=\int_\Sigma\rho\,\delta S_R\,d\Sigma.
}
$$

Logo,

$$
\boxed{
\Omega_{\rm state}
=\delta\Theta_{\rm state}
=\int_\Sigma\delta\rho\wedge\delta S_R\,d\Sigma.
}
$$

O mesmo resultado aparece diretamente na geometria ponderada do alvo. Com
$u=-\ln\rho$ e $v=S_R/\hbar$, a métrica

$$
G=\rho(du^2+dv^2)
$$

tem forma compatível

$$
\omega_T=\rho\,du\wedge dv
=-\frac1\hbar d\rho\wedge dS_R.
$$

Assim, $(\rho,S_R)$ são coordenadas de Darboux naturais no espaço de estados
normalizados, após remover a fase constante.

## Teorema de não identificação automática

O resultado anterior não coincide automaticamente com a forma covariante da
ação oficial. Esta última é

$$
\Omega_{\rm GDQ}
=\int_\Sigma
\left(
\delta\Pi_{S_R}\wedge\delta S_R
+\delta p_\rho\wedge\delta\rho
+\text{setor métrico}
\right).
$$

$\Omega_{\rm state}$ vive no espaço de configurações normalizadas;
$\Omega_{\rm GDQ}$ vive no fibrado cotangente dos dados de Cauchy. Além disso,
a Hessiana da ação oficial nas velocidades é não degenerada, enquanto uma
ação first-order $\rho\dot S_R-H$ possui Hessiana temporal degenerada. Uma
derivada total ou um termo de bordo não muda esse posto.

Portanto, sob os axiomas vigentes, não se pode concluir

$$
\Omega_{\rm GDQ}^{\rm phys}=\Omega_{\rm state}
$$

sem derivar uma subvariedade dinâmica invariante que elimine o par da
amplitude e relacione $\Pi_{S_R}$ a $\rho$. A geometria Kähler demonstra
exatamente o par canônico candidato; a ação oficial não demonstra ainda que
todo o seu espaço de Cauchy se reduza a esse par.
