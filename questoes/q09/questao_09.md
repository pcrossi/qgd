# Questão 9 — Qual é a ação fundamental da GDQ?

## 1. Pergunta

A Questão 9 pergunta:

\[
\boxed{
\text{qual é a ação fundamental da GDQ?}
}
\]

A resposta deve fornecer:

1. expressão completa;
2. variáveis independentes;
3. realidade da ação;
4. unidade;
5. simetrias;
6. termos de bordo;
7. multiplicadores/vínculos;
8. status do funcional de Perelman;
9. relação entre ação fundamental e ações efetivas.

O critério de fechamento é:

\[
\boxed{
\text{nenhuma equação física central deve ser adicionada externamente depois
da ação.}
}
\]

---

## 2. Ação fundamental oficial

A ação fundamental da GDQ é a ação oficial já preservada:

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

Com:

\[
\boxed{
n=4,
\qquad
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M=8.
}
\]

Define-se:

\[
\boxed{
\mathcal L_0
=
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n.
}
\]

Então:

\[
\boxed{
\mathcal S_{\rm GDQ}
=
\int_\gamma
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\mathcal U
\mathcal L_0
\sqrt{\det g}
d^{2n}z
\frac{d\tau}{\tau}.
}
\]

Essa é a ação fundamental. Ela não é substituída pela ação efetiva em \(N^4\),
nem pela camada perturbativa, nem pela ação BRST auxiliar.

---

## 3. Medida \(\mathcal U\)

A medida é definida constitucionalmente como funcional de
\(f,\bar f,z_\tau\):

\[
\boxed{
\mathcal U[f,\bar f,z_\tau]
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}.
}
\]

Com:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0}.
}
\]

Para \(n=4\):

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^4}.
}
\]

Como:

\[
f=-\frac{S_I-iS_R}{\hbar},
\]

temos:

\[
\frac{f+\bar f}{2}
=
-\frac{S_I}{\hbar},
\]

e:

\[
\boxed{
e^{-(f+\bar f)/2}
=
e^{S_I/\hbar}
=
\rho.
}
\]

Logo:

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

---

## 4. Variáveis independentes

As variáveis independentes da ação fundamental são:

\[
\boxed{
g_{\mu\bar\nu},
\qquad
f,
\qquad
\bar f.
}
\]

No cálculo variacional:

\[
\boxed{
\delta g_{\mu\bar\nu},
\qquad
\delta f,
\qquad
\delta\bar f
}
\]

são as variações fundamentais.

A medida \(\mathcal U\) não é independente:

\[
\boxed{
\mathcal U=\mathcal U[f,\bar f,z_\tau].
}
\]

Portanto:

\[
\boxed{
\delta\mathcal U
=
-\frac12\mathcal U(\delta f+\delta\bar f)
}
\]

com \(z_\tau\) fixo na variação dos campos.

Não são variáveis independentes da ação oficial:

\[
\boxed{
\rho,\ R,\ S_I,\ S_R,\ \Psi.
}
\]

Essas variáveis são derivadas:

\[
\boxed{
S_I=-\hbar\operatorname{Re}f,
\qquad
S_R=\hbar\operatorname{Im}f,
}
\]

\[
\boxed{
\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2},
\qquad
R=\sqrt\rho,
\qquad
\Psi=R e^{iS_R/\hbar}.
}
\]

---

## 5. Estruturas e parâmetros, não campos variados

São estruturas/parâmetros da teoria:

\[
\boxed{
M,\ J,\ \gamma,\ \tau,\ t,\ z_\tau,\ \Lambda_C,\ \nu_0.
}
\]

Eles definem a teoria, mas não são campos variados na ação fundamental atual.

Em particular:

\[
\boxed{
\tau
\text{ é parâmetro de fluxo/escala, não campo.}
}
\]

\[
\boxed{
t
\text{ é tempo físico da camada reconstruída/efetiva, não campo do bulk.}
}
\]

\[
\boxed{
\gamma
\text{ é prescrição causal de Sudarshan, não campo.}
}
\]

---

## 6. Realidade da ação

Como a ação usa \(z_\tau\), \(\gamma\) e campos complexos, o funcional
\(\mathcal S_{\rm GDQ}\) pode ser complexo antes da prescrição física de
realidade.

A ação física estacionária é definida por:

\[
\boxed{
S_{\rm phys}
:=
\operatorname{Re}\mathcal S_{\rm GDQ}.
}
\]

A equação variacional fundamental é:

\[
\boxed{
\delta S_{\rm phys}=0.
}
\]

Isto é:

\[
\boxed{
\delta\,\operatorname{Re}\mathcal S_{\rm GDQ}=0.
}
\]

A parte imaginária não é descartada ontologicamente: ela codifica fase,
orientação causal e prescrição de contorno. Mas a ação física que define a
estacionariedade real é:

\[
\boxed{
\operatorname{Re}\mathcal S_{\rm GDQ}.
}
\]

Quando o contorno \(\gamma\) for escolhido com simetria de conjugação adequada,
pode ocorrer:

\[
\mathcal S_{\rm GDQ}\in\mathbb R.
\]

Mas a definição geral segura é:

\[
\boxed{
S_{\rm phys}=\operatorname{Re}\mathcal S_{\rm GDQ}.
}
\]

---

## 7. Unidade da ação

A ação física deve ter unidade de ação:

\[
\boxed{
[S_{\rm phys}]=[\hbar].
}
\]

O fator:

\[
\frac{\hbar}{\Lambda_C^2}
\]

garante a escala dimensional.

Usando:

\[
\ell_C=\Lambda_C^{-1}
\]

em unidades naturais, temos:

\[
\frac{\hbar}{\Lambda_C^2}
=
\hbar\ell_C^2.
\]

Como:

\[
[\tau]=L^2,
\qquad
[\mathcal R]=L^{-2},
\qquad
[g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f]=L^{-2},
\]

o bloco:

\[
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
\]

é adimensional.

Também:

\[
f,\bar f,n
\]

são adimensionais.

Logo:

\[
\mathcal L_0
\]

é adimensional.

A medida:

\[
\mathcal U\sqrt{\det g}\,d^{2n}z
\]

é escolhida/normalizada para ser adimensional, como medida de Perelman
complexificada.

O fator:

\[
\frac{d\tau}{\tau}
\]

é adimensional.

Assim:

\[
\boxed{
[\mathcal S_{\rm GDQ}]=[\hbar].
}
\]

---

## 8. Simetrias da ação fundamental

### 8.1 Difeomorfismos admissíveis do bulk

A ação é covariante sob difeomorfismos admissíveis de \(M\) que preservem a
estrutura necessária para escrever o funcional hermitiano:

\[
\boxed{
z\mapsto z'(z,\bar z).
}
\]

### 8.2 Transformações complexas/hermitianas admissíveis

O tensor:

\[
g_{\mu\bar\nu}
\]

e o escalar:

\[
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f
\]

são escritos de forma covariante em coordenadas complexas admissíveis.

### 8.3 Simetria global de fase

Como:

\[
\operatorname{Im}f=\frac{S_R}{\hbar},
\]

um deslocamento:

\[
S_R\mapsto S_R+\hbar\alpha
\]

corresponde a:

\[
f\mapsto f+i\alpha,
\qquad
\bar f\mapsto\bar f-i\alpha.
\]

A ação depende de:

\[
f+\bar f
\]

e de derivadas de \(f,\bar f\). Portanto é invariante sob deslocamento global
da fase:

\[
\boxed{
f\mapsto f+i\alpha,
\qquad
\bar f\mapsto\bar f-i\alpha.
}
\]

Essa simetria gera, na redução Madelung, a continuidade/conservação da
corrente.

### 8.4 Prescrição causal de Sudarshan

O contorno:

\[
\gamma\subset\mathbb C_{z_\tau}
\]

implementa a prescrição causal avançado-retardada.

Não é uma simetria de campo usual; é parte da definição causal da ação.

---

## 9. Termos de bordo

O contorno causal \(\gamma\) cancela termos exatos:

\[
\boxed{
\oint_\gamma dF=0
}
\]

desde que:

1. \(F\) seja monovalorada;
2. \(\gamma\) não cruze cortes de ramo;
3. as singularidades internas sejam controladas;
4. os campos sejam regulares ao longo do contorno.

Como:

\[
M=\mathbb R^4\times T^4
\]

é tomado sem bordo físico, não há termo de bordo fundamental obrigatório se:

1. as variações têm suporte compacto; ou
2. há decaimento adequado em \(\mathbb R^4\); ou
3. os termos exatos são controlados por \(\gamma\).

Portanto:

\[
\boxed{
\text{sem bordo físico: nenhum termo extra obrigatório.}
}
\]

Se forem considerados domínios com bordo físico, cortes, caixas finitas,
horizontes ou fronteiras assintóticas não triviais, deve-se adicionar um termo
hermitiano análogo ao Gibbons--Hawking--York:

\[
\boxed{
S_{\partial M}^{\rm herm}.
}
\]

Assim:

\[
\boxed{
S_{\rm total}
=
S_{\rm phys}
+S_{\partial M}^{\rm herm}
}
\]

quando houver bordo físico.

---

## 10. Multiplicadores e vínculos

Na ação fundamental final:

\[
\boxed{
\mathcal U
\text{ não é multiplicador independente.}
}
\]

Ela é definida por:

\[
\mathcal U[f,\bar f,z_\tau].
\]

Logo, não há variação:

\[
\delta_{\mathcal U}\mathcal S_{\rm GDQ}=0
\]

como equação independente.

Os vínculos fundamentais são estruturais:

1. escolha de \(M=\mathbb R^4\times T^4\);
2. estrutura complexa \(J\);
3. contorno causal \(\gamma\);
4. variável \(z_\tau=\tau+i\nu_0t\);
5. definição de \(\mathcal U\);
6. escolha de setor físico \(X^*\omega\neq0\) na redução para \(N^4\).

Se for necessário impor normalização global da medida:

\[
\int_M\mathcal U\sqrt{\det g}\,d^{2n}z=1,
\]

pode-se acrescentar no setor normalizado:

\[
\boxed{
S_{\rm norm}
=
\lambda
\left(
\int_M\mathcal U\sqrt{\det g}\,d^{2n}z-1
\right).
}
\]

Aqui \(\lambda\) é multiplicador global de normalização.

Mas:

\[
\boxed{
S_{\rm norm}
\text{ é uma opção de setor normalizado, não parte obrigatória da ação
oficial mínima.}
}
\]

---

## 11. Perelman: ação física ou funcional auxiliar?

O funcional de Perelman puro:

\[
\mathcal W[g,f,\tau]
\]

é um funcional geométrico/entrópico.

Na GDQ, ele é a matriz geométrica da construção, mas não é a ação física final
isolada.

A ação física fundamental é:

\[
\boxed{
S_{\rm phys}
=
\operatorname{Re}\mathcal S_{\rm GDQ}.
}
\]

Portanto:

\[
\boxed{
\mathcal W
\text{ é funcional geométrico auxiliar;}
\qquad
\mathcal S_{\rm GDQ}
\text{ é a ação fundamental da GDQ.}
}
\]

Mais precisamente:

1. \(\mathcal W\) fornece a base Perelman/difusiva;
2. \(\mathcal S_{\rm GDQ}\) é a extensão causal complexificada;
3. \(\gamma\) implementa a prescrição de Sudarshan;
4. \(z_\tau\) unifica fluxo geométrico e tempo físico;
5. \(\Lambda_C\) fixa a escala dimensional;
6. \(\mathcal U\) implementa a medida Madelung--Perelman.

---

## 12. Relação com a ação efetiva em \(N^4\)

A ação efetiva:

\[
S_{\rm eff}
=
S_{\rm EH}+S_\Psi+S_B
\]

não substitui a ação fundamental.

Ela é a redução física controlada sobre \(N^4\), onde:

1. \(h\) é a métrica lorentziana constitutiva;
2. \(\Psi=\sqrt\rho e^{iS_R/\hbar}\);
3. a parte imaginária fornece continuidade;
4. a parte real fornece Hamilton--Jacobi/Bohm;
5. \(B\) descreve a torção física efetiva.

Assim:

\[
\boxed{
\mathcal S_{\rm GDQ}
\text{ é fundamental;}
\qquad
S_{\rm eff}
\text{ é redução física efetiva.}
}
\]

---

## 13. Relação com camada perturbativa e BRST

A camada perturbativa:

\[
S_{\rm pert}
=
S_{\rm gauge}
+S_{\rm spin}
+S_{\rm gf+gh}
\]

não é a ação fundamental da GDQ.

Ela é ferramenta de auditoria covariante para:

1. escrever propagadores;
2. fazer gauge fixing;
3. comparar com QFT padrão;
4. verificar loops;
5. controlar modos não físicos em linguagem BRST.

Fantasmas \(c,\bar c,b\) não são campos fundamentais.

Logo:

\[
\boxed{
S_{\rm pert}
\text{ é camada auxiliar;}
\qquad
\mathcal S_{\rm GDQ}
\text{ é a ação fundamental.}
}
\]

---

## 14. Princípio variacional local a partir do contorno

A variação tem a forma:

\[
\delta\mathcal S_{\rm GDQ}
=
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}.
\]

Expandindo:

\[
E(z_\tau)
=
\sum_{k=-\infty}^{\infty}E_kz_\tau^k.
\]

Então:

\[
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}
=
2\pi iE_0.
\]

A condição:

\[
\delta S_{\rm phys}=0
\]

impõe a estacionariedade física do modo real relevante.

Para obter equações locais modo a modo, adota-se o princípio:

\[
\boxed{
E_k=0
\qquad
\forall k.
}
\]

Esse é o princípio de estacionariedade dos coeficientes de Laurent.

Ele não é uma nova equação física externa; é a regra que extrai as equações
locais da ação de contorno.

---

## 15. Nenhuma equação central adicionada externamente

Com as definições acima, as equações centrais devem vir de:

\[
\boxed{
\delta_{g,f,\bar f}S_{\rm phys}=0.
}
\]

As equações efetivas em \(N^4\) devem vir de:

1. redução controlada da ação fundamental;
2. decomposição Madelung de \(f\);
3. projeção na métrica \(h\);
4. identificação de \(\Psi\);
5. variações da ação efetiva derivada.

Não é admissível acrescentar independentemente:

1. equação de continuidade;
2. Hamilton--Jacobi/Bohm;
3. cone causal;
4. equação de Dirac;
5. equações gauge;
6. propagadores;
7. \(\beta\)-funções.

Esses objetos precisam ser:

\[
\boxed{
\text{derivados, reduzidos ou auditados a partir da ação e de suas camadas
controladas.}
}
\]

---

## 16. Resposta direta às perguntas obrigatórias

### 16.1 Qual é a expressão completa?

\[
\boxed{
\mathcal{S}_{\rm GDQ}
=
\int_{\gamma}
\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\mathcal U
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

### 16.2 Quais variáveis são independentes?

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

\(\mathcal U,\rho,R,S_I,S_R,\Psi\) são derivados.

### 16.3 A ação é real?

A ação física é:

\[
\boxed{
S_{\rm phys}
=
\operatorname{Re}\mathcal S_{\rm GDQ}.
}
\]

A estacionariedade é:

\[
\boxed{
\delta S_{\rm phys}=0.
}
\]

### 16.4 Qual é sua unidade?

\[
\boxed{
[S_{\rm phys}]=[\hbar].
}
\]

### 16.5 Quais são suas simetrias?

1. difeomorfismos admissíveis do bulk;
2. covariância complexa/hermitiana admissível;
3. fase global \(f\mapsto f+i\alpha\);
4. prescrição causal avançado-retardada via \(\gamma\).

### 16.6 Quais termos de bordo são necessários?

Sem bordo físico:

\[
\boxed{
\text{nenhum termo extra obrigatório.}
}
\]

Com bordo físico:

\[
\boxed{
S_{\partial M}^{\rm herm}
\text{ deve ser adicionado.}
}
\]

### 16.7 Quais multiplicadores representam vínculos?

Na ação mínima:

\[
\boxed{
\text{nenhum multiplicador local independente.}
}
\]

\(\mathcal U\) não é multiplicador; é funcional de \(f,\bar f,z_\tau\).

Opcionalmente, para normalização global:

\[
\boxed{
S_{\rm norm}
=
\lambda
\left(
\int_M\mathcal U\sqrt{\det g}\,d^{2n}z-1
\right).
}
\]

### 16.8 O funcional de Perelman é ação física ou funcional auxiliar?

\[
\boxed{
\mathcal W
\text{ é funcional geométrico auxiliar;}
\qquad
\mathcal S_{\rm GDQ}
\text{ é a ação física fundamental.}
}
\]

---

## 17. Status da Questão 9

\[
\boxed{
\text{Questão 9 fechada oficialmente.}
}
\]

A ação única da GDQ é:

\[
\boxed{
S_{\rm phys}
=
\operatorname{Re}\mathcal S_{\rm GDQ},
}
\]

com:

\[
\boxed{
\mathcal S_{\rm GDQ}
\text{ dada pela ação oficial de contorno em }\gamma.
}
\]

As variáveis fundamentais são:

\[
\boxed{
g_{\mu\bar\nu},\quad f,\quad \bar f.
}
\]

E a regra estrutural final é:

\[
\boxed{
\text{ações efetivas, propagadores, equações hidrodinâmicas e setores
perturbativos devem ser reduzidos ou auditados a partir dessa ação, não
adicionados como axiomas independentes.}
}

