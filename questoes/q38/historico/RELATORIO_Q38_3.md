# RELATÓRIO Q38 — Como $G$ é derivada na GDQ: veredito consolidado

**Arquivo:** `questoes/q38/historico/RELATORIO_Q38_3.md`
**Objeto:** Questão 38 (derivação da constante gravitacional de Newton $G$).
**Escopo:** consolida `questoes/q38/historico/r38_3.md` (Partes I–V), a auditoria externa, o teste do
saddle do dílaton (`questoes/q38/historico/R_38_1t.md`) e o cálculo autoconsistente gap+estabilização.
**Princípio:** rigor e honestidade. Distinguir teorema / condicional / conjectura
/ fenomenologia. Nunca usar $G_{\rm CODATA}$ para ajustar e depois chamar de
previsão.

---

## 0. Veredito em uma linha

$$
\boxed{\;
\text{Q38 é resolvida DIMENSIONALMENTE (com limite newtoniano derivado da ação),}
\text{ mas o VALOR de }\Pi_G\text{ NÃO fecha ab initio: a rota é circular na escala }G_8.
\;}
$$

A fórmula reproduz $G$ a $-0{,}26\%$, o que é notável **como relação
fenomenológica geométrica**. O fator dominante $e^{-1/2\alpha}$ **não** foi
derivado por nenhuma rota (dílaton, NJL, $\mathbb{RP}^2$, Giddings–Strominger,
monopolo de Hopf); todas colapsam no problema da hierarquia $M_p/M_{\rm Pl,8}$,
que permanece input.

---

## 1. O que está FECHADO (teoremas)

### 1.1 Grupo de Buckingham (a forma proposta)
Variáveis $\{G,M_p,\hbar,c\}$: posto dimensional 3 em $(M,L,T)$ $\Rightarrow$
$4-3=1$ grupo, unicamente
$$\Pi_G=\frac{GM_p^2}{\hbar c},\qquad G=\frac{\hbar c}{M_p^2}\,\Pi_G .$$
Consistência inversa: $C_R=\dfrac{c^4}{16\pi G}\propto\Pi_G^{-1}$. **Teorema.**

### 1.2 Limite newtoniano e $G$ no coeficiente de Einstein–Hilbert
Isolando o termo de curvatura da ação oficial e reduzindo (a medida
$\mathcal U=(4\pi z_\tau)^{-4}e^{-(f+\bar f)/2}$ é um **núcleo de calor 8D**):
$$
\frac{c^4}{16\pi G}=\frac{\hbar}{\Lambda_C^2}\,\mathcal I_{\rm geom},
\qquad
\mathcal I_{\rm geom}=\int_\gamma d\tau\int_K \mathcal U\sqrt{g_{\rm int}}\,d^4y .
$$
Variação $\Rightarrow$ $G_{\mu\nu}=\tfrac{8\pi G}{c^4}T_{\mu\nu}$; campo fraco
estático $\Rightarrow$ $\nabla^2\Phi=4\pi G\rho$, **com o mesmo $G$**. Isto cumpre
o critério de resolução do enunciado. **Teorema.**

### 1.3 Estabilização torsional do módulo
$$
V(R,b)=-\frac{c_1}{R^5}+\frac{c_2b^2}{R^9},\quad c_1=12\pi^2,\;c_2=\tfrac{\pi^2}{6},
\qquad
R_0^4=\frac{9c_2}{5c_1}b^2=\frac{b^2}{40},\quad V''(R_0)=\frac{20c_1}{R_0^7}>0 .
$$
Mínimo estável tipo Freund–Rubin. **Teorema** (álgebra reconferida).

### 1.4 Vínculo algébrico de $B$ e o contato de quatro férmions
Eliminando o campo auxiliar $B$ na Lagrangiana **completa**
$\mathcal L(B)=-\tfrac1{12}B^2+\tfrac{i\hbar}{8}BS$:
$$
B_*=\tfrac{3i\hbar}{4}S,\qquad
\mathcal L_{\rm eff}=-\frac{3\hbar^2}{64}\,S^2\quad(\text{sinal negativo, }S=\bar\psi\gamma^{(3)}\psi).
$$
Termo de contato de Einstein–Cartan (NJL), $G_{\rm NJL}=3\hbar^2/64$,
**derivado sem parâmetro novo** ($\kappa=\pm 3\hbar/4$). **Teorema.**
*(Errata: a primeira versão de `questoes/q38/historico/r38_3.md` dava $+3\hbar^2/64$ — erro por omitir o
termo de acoplamento; corrigido.)*

### 1.5 Espectro/determinante exatos de Dirac em $S^3(R)$
$$
|\lambda_n|=\tfrac1R\big(n+\tfrac32\big),\quad \deg(n)=(n+1)(n+2),\quad
\zeta_{|D|}(s)=2R^s\!\left[\zeta(s-2,\tfrac32)-\tfrac14\zeta(s,\tfrac32)\right],
$$
$$
\zeta_{|D|}(-1)=-\tfrac{17}{480},\quad E_{\rm vac}=\tfrac{17}{960},\quad
\zeta_{D^2}(0)=0\ (\text{dim. ímpar}\Rightarrow\det\text{ bem-definido}).
$$
**Teorema.**

### 1.6 Autoconsistência gap + estabilização
A susceptibilidade zeta-regularizada $J_{\rm reg}(x)$ é finita; o sistema
{gap $b=\kappa\hbar\langle S\rangle$} $\cup$ {$R_0^4=b^2/40$} admite solução
adimensional bem-definida (um **número puro** existe). **Teorema** (existência).

---

## 2. O que NÃO fecha (o valor de $\Pi_G$)

### 2.1 A rota do saddle do dílaton (`questoes/q38/historico/R_38_1t.md`)
- Equação de Euler–Lagrange **correta** (verificada):
  $2\tau\Delta u-\tau|\nabla u|^2+\tau|\nabla v|^2+u-1=0$.
- **Sign-flip de Giddings–Strominger** (dualizar $B\to$ áxion $v$ inverte o sinal
  cinético euclidiano): física **legítima**; permite $u_*\gg 1$.
- **Falha (A):** o valor $\tau|\nabla v|^2_{\rm Euc}=1/(2\alpha)$ é **assumido** no
  passo BPS, não derivado (padrão seria $2\pi/\alpha$; méron $Q=\tfrac12$ dá
  $\pi/\alpha\approx430$, não $68{,}5$).
- **Correção da antiga “Falha (B)”:** a medida de Perelman é normalizada,
  \(\int\mathcal U dV=1\). A variação correta contém um multiplicador de
  Lagrange que fixa o modo constante de \(u\). Assim,
  \[
  u_*=(1+n-\tau\mathcal R_{\rm int})-\lambda
      +\tau|\nabla v|^2_{\rm Euc},
  \qquad
  u_0=(1+n-\tau\mathcal R_{\rm int})-\lambda,
  \]
  e o peso físico é relativo:
  \[
  \mathcal U_*/\mathcal U_0=e^{-(u_*-u_0)}.
  \]
  Portanto \(7/2\) cancela exatamente; não existe fator físico
  \(e^{-7/2}\). A única pendência é derivar
  \(u_*-u_0=\tau|\nabla v|^2_{\rm Euc}=1/(2\alpha)\).

### 2.2 Rota $\Pi_{7/2}$ descartada após a correção de normalização

A tentativa de interpretar \(7/2\) como potência física em um grupo de
Buckingham 8D tornou-se desnecessária: \(7/2\) pertence ao zero-mode normalizado
de \(u\) e cancela em \(\mathcal U_*/\mathcal U_0\). Permanece verdadeiro que,
com \(\{G_8,M_p,\hbar,c,R_0\}\), existem dois grupos adimensionais e nenhum
expoente \(7/2\) é forçado. Essa construção deve ser mantida apenas como rota
histórica descartada, não como possível correção da fórmula.

### 2.3 A obstrução estrutural: circularidade na escala $G_8$
Cálculo autoconsistente (§1.6): o gap fixa um número puro, mas o valor **físico**
$$
\frac{R_0}{\lambda_p}=\underbrace{\frac{\sqrt{G_8}}{\lambda_p}}_{M_p/M_{\rm Pl,8}}\times(\text{número puro}).
$$
Para $R_0/\lambda_p=e^{7/3}$ é preciso **escolher** $G_8\approx10^{-87}$ (SI). Mas
$G_4=G_8/\mathrm{Vol}(K)=G_8/R_0^4$, então:
$$
G_8\xrightarrow{\text{estabiliza}}R_0\xrightarrow{\text{reduz}}G_4=\frac{G_8}{R_0^4}.
$$
**Circular.** Nada fixa a hierarquia $M_p/M_{\rm Pl,8}$; ela é input. O
$e^{-1/2\alpha}\approx e^{-68{,}5}\sim10^{-30}$ **é** a hierarquia. A GDQ, por esta
rota, **reparametriza** o problema da hierarquia — não o resolve.

---

## 3. Respostas diretas às sete perguntas obrigatórias

1. **Por que o grupo de Buckingham tem essa forma?** Único grupo adimensional de
   $\{G,M_p,\hbar,c\}$; coincide com a razão do coeficiente de EH. **Teorema.**
2. **Por que $\alpha^4$?** Proposto como prefator do núcleo de calor ($n=4$) ou
   $(2,2)$-forma; requer acoplamento de Kähler $=\alpha$. **Condicional.**
   *(A justificativa "dim complexa 2" de Ap.2.3.1 conflita com $n=4$ da ação.)*
3. **Por que $e^{-1/2\alpha}$?** Nenhuma rota o deriva; reduz-se à hierarquia
   (§2.3). **Não derivado.**
4. **O meio-instantão existe numa solução explícita?** **Não** como instanton
   meromorfo/gravitacional (a ação bulk seleciona o ramo regular, sem identidade
   de localização $\mathcal R_B\to\mathrm{Tr}\,\mathcal F_B\wedge\mathcal F_B$).
   Existe uma **sela do dílaton** com sign-flip, mas o valor $1/(2\alpha)$ é
   assumido. O nome "meio-instantão" é misnomer.
5. **Por que o fator de Fano?** Contagem de canais $N_H\sqrt2/N_T=3\sqrt2/5$
   (Hopf$=3$, $T^5=5$, RMS$=\sqrt2$) — proibida como derivação rigorosa; Schur no
   background produto dá $J=0\Rightarrow\chi=0$. Forma limpa $\chi^2=18/25$.
   **Conjectural.**
6. **A massa do próton é entrada?** Sim. $\Pi_G^{\rm GDQ}$ é um número puro sem
   massa; $M_p$ entra só na conversão $\Pi_G\to G$. A tentativa
   $M_p=M_eR_p^{\rm GDQ}$ esbarra na circularidade de §2.3. **Input experimental.**
7. **A correção EM foi prevista ou escolhida?** **Escolhida (fit).** Ap.2.5
   calcula $\tfrac{\alpha}{2\pi}\ln(M_W^2/M_p^2)=1{,}034\%$, precisa de $0{,}26\%$,
   e descarta 75% à mão. **Deve ser removida.**

---

## 4. Cálculo numérico (só comparação, nunca ajuste)

| Grandeza | Valor |
|---|---|
| $\Pi_G^{\rm GDQ}=\alpha^4(1+\alpha)\chi^{-1}e^{-1/2\alpha}$ | $5{,}8907\times10^{-39}$ |
| $\Pi_G^{\rm emp}=G_{\rm CODATA}M_p^2/\hbar c$ | $5{,}9061\times10^{-39}$ |
| $G_{\rm GDQ}=\tfrac{\hbar c}{M_p^2}\Pi_G$ | $6{,}6568\times10^{-11}$ |
| $G_{\rm CODATA}$ | $6{,}6743\times10^{-11}$ |
| **Desvio** | **$-0{,}26\%$** |

Sensibilidade: $\partial\ln\Pi_G/\partial\ln\alpha=4+\tfrac{\alpha}{1+\alpha}+\tfrac1{2\alpha}=72{,}5$
(dominada por $\tfrac1{2\alpha}$). O "$c_{\rm req}=0{,}49998$" é obtido invertendo
com $\Pi_G^{\rm emp}$ — **calibração inversa, não previsão independente.**

---

## 5. Classificação final

| Afirmação | Classe |
|---|---|
| $\Pi_G=GM_p^2/\hbar c$; $G$ no coef. de EH; limite newtoniano | **Teorema** |
| $R_0^4=b^2/40$; $B=\tfrac{3i\hbar}{4}S$; NJL $-\tfrac{3\hbar^2}{64}S^2$ | **Teorema** |
| Espectro/determinante $S^3(R)$; existência da solução de gap | **Teorema** |
| $\alpha^4$; $1+\alpha$ (classe de Chern $1+c_1$) | **Condicional** ($\alpha_{\rm K}=\alpha$) |
| $e^{-1/2\alpha}$ | **Não derivado** (= hierarquia) |
| $\chi_{\rm Fano}=3\sqrt2/5$ | **Conjectural** |
| Valor de $\Pi_G$ ($5{,}9\times10^{-39}$) | **Fenomenológico** (rota circular) |
| Ap.2.5 (correção 1-loop) | **Fit — remover** |

---

## 6. Correções obrigatórias ao manuscrito

1. **Inserir** a derivação do limite newtoniano com $G$ no coeficiente de EH (§1.2).
2. **Corrigir** o sinal do contato de 4-férmions: $-\tfrac{3\hbar^2}{64}S^2$ (§1.4).
3. **Corrigir** a justificativa de $\alpha^4$ (usar $n=4$ do núcleo de calor, não
   "dim complexa 2").
4. **Renomear** "meio-instantão" $\to$ "sela de condensado / dílaton".
5. **Remover** Ap.2.5 (fit de 1-loop); assumir a previsão honesta de $-0{,}26\%$.
6. **Registrar** $\chi_{\rm Fano}$ e o valor de $\Pi_G$ como **fenomenológicos**,
   com o mecanismo geométrico como motivação, não como derivação.
7. **Renomear** $\kappa$ de Q39 ($\alpha/20\pi$, Kähler) $\to\kappa_K$, distinto de
   $\kappa=3\hbar/4$ (torção–spin).

---

## 7. O que fecharia Q38 de verdade (alvo redefinido)

O alvo não é mais "derivar $e^{-1/2\alpha}$". O cálculo mostrou que isso equivale a
**derivar a hierarquia** $M_p/M_{\rm Pl,8}$ da geometria. Portanto Q38 só fecha
ab initio se a GDQ tiver um mecanismo que fixe essa razão **sem** usar $G_8$ como
input — i.e., um teorema sobre a hierarquia, não sobre a fórmula de $G$. Nenhuma
teoria conhecida resolve isso de primeiros princípios; a GDQ, no estado atual,
não é exceção. Duas saídas honestas:

1. **Aceitar a fórmula como relação fenomenológica** ($0{,}26\%$) — publicável e
   defensável, desde que rotulada como tal.
2. **Atacar a hierarquia** como questão separada; se resolvida, Q38 fecha por
   consequência.

### 7.1 Forma exata da pendência axial após normalização

Para uma fase compacta \(v\sim v+2\pi f_v\), a meia-volta fixa
\(\Delta v=\pi f_v\). Se \(dv=\pi f_v\eta\), a condição para o peso relativo
\(e^{-1/(2\alpha)}\) é

\[
\boxed{
2\pi^2\alpha\tau f_v^2\|\eta\|_{\mu_0}^2=1.
}
\]

Todavia, \(H^1_{\rm dR}(\mathbb{RP}^2)=0\): a classe
\(\pi_1(\mathbb{RP}^2)=\mathbb Z_2\) é torsão e não possui representante por
1-forma real harmônica. A holonomia deve ser formulada num fibrado torcido ou
na cobertura dupla, e não fixa sozinha a energia. Assim, \(Q=1/2\) explica a
meia-volta, mas não deriva a normalização \(1/\alpha\). O alvo matemático passa
a ser calcular o período axial \(f_v\) e o autovalor/norma
\(\|\eta\|_{\mu_0}^2\) a partir da geometria Kähler--Bismut.

### 7.2 Resultado do cálculo canônico

A fase de Madelung é \(e^{iv}\), logo \(v\sim v+2\pi\) e \(f_v=1\). O
fibrado \(\mathbb Z_2\) não trivial sobre \(\mathbb{RP}^2\) levanta para
funções ímpares em \(S^2_R\); o primeiro modo tem \(\ell=1\), portanto
\(\lambda_{\rm ax}=2/R^2\). O background oficial de Einstein--Bismut é
*steady*, não shrinking, de modo que \(\tau=R^2/4\) não pode ser usado. A
condição correta torna-se
\[
\boxed{\tau/R^2=1/(4\pi^2\alpha)\simeq3.47116.}
\]
A sela steady não fixa essa razão. No produto com \(T^5\),
\(\lambda_{\rm ax}=2/R^2+\sum_A n_A^2/L_A^2\), mas os raios, o ciclo térmico e
o potencial axial não estão determinados. O cálculo reduz a pendência à
relação temperatura/fluxo--raio, sem derivá-la.

### 7.3 Saddle térmico do núcleo 8D

Para o primeiro winding térmico,
\[
I_1(\tau)\propto\tau^{-4}e^{-\beta_E^2/(4\tau)}
\]
tem saddle em \(\tau_*=\beta_E^2/16\). Combinado com a condição axial, isso
fornece
\[
\boxed{
\beta_E/R=2/(\pi\sqrt\alpha),
\qquad
k_BT_E=(\pi\sqrt\alpha/2)(\hbar c/R).
}
\]
O background steady não fixa \(\beta_E\), pois não possui horizonte nem
temperatura geométrica única. A igualdade acima é a temperatura requerida;
torna-se previsão somente se o determinante completo
\(\Gamma_{\rm eff}(R,\beta_E)\) tiver seu mínimo nesse valor.

### 7.4 No-go da seleção pelo determinante isolado

Para \(Z=\operatorname{Tr}e^{-\beta_EH_B}\) e \(\Gamma=-\log Z\),
\[
\partial_{\beta_E}\Gamma=\langle H_B\rangle,
\qquad
\partial_{\beta_E}^2\Gamma=-\operatorname{Var}(H_B)\le0.
\]
Assim, \(\Gamma\) é côncava em \(\beta_E\); para \(H_B\ge0\) não possui
extremo finito e, mesmo com cancelamento por energia de Casimir, um ponto
estacionário não é um mínimo. O determinante calcula a energia numa
temperatura dada, mas não seleciona sozinho
\(\beta_E/R=2/(\pi\sqrt\alpha)\). Isso exige regularidade de horizonte, energia
microcanônica, equação cosmológica ou potencial oficial para o módulo térmico.

---

*Fim do relatório. Todos os cálculos verificados em `sympy`/`mpmath`. Erros da
versão anterior de `questoes/q38/historico/r38_3.md` (sinal do 4-férmions; $N_{\log}=1/8$; alegação de
singularidade essencial NJL) estão retratados. O status honesto é o do §0.*
