# Q43 — Background físico experimental para \(g-2\)

## 1. Objetivo

Este documento monta o background físico que deve alimentar a construção GDQ
de \(H_C,c,m_\perp\) para o efeito Zeeman e \(g-2\).

Ele usa artigos experimentais como fontes de dados externos. Esses dados não
alteram a ação oficial da GDQ. Eles especificam o aparelho, a fonte magnética,
o domínio físico e o observável medido.

O cálculo GDQ a fazer depois é:

\[
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle}
{\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle}.
\]

---

## 2. Background A — elétron em armadilha de Penning

### 2.1 Fonte experimental

Referência:

- X. Fan, T. G. Myers, D. B. Sukra, G. Gabrielse,
  *Measurement of the Electron Magnetic Moment*,
  arXiv:2209.13084.

Link:

- <https://arxiv.org/abs/2209.13084>

O artigo reporta:

\[
-\frac{\mu}{\mu_B}
=
\frac{g}{2}
=
1.00115965218059(13).
\]

Portanto:

\[
g_e\simeq2.00231930436118.
\]

O mesmo resumo informa que a combinação da medição com a teoria usual fornece:

\[
\alpha^{-1}=137.035999166(15).
\]

Na Q43 usamos essa informação somente como comparação metrológica externa.

### 2.2 Domínio físico

O experimento é um problema de um único elétron confinado em armadilha de
Penning. O background físico mínimo é:

\[
\mathcal B_e
=
\left(
B_0,\,
V_{\rm trap},\,
\Omega_{\rm trap},\,
\nu_c,\,
\nu_a,\,
T_{\rm app},\,
\text{correções de cavidade}
\right).
\]

Interpretação:

- \(B_0\): campo magnético axial quase uniforme;
- \(V_{\rm trap}\): potencial elétrico quadrupolar de confinamento;
- \(\Omega_{\rm trap}\): domínio efetivo da armadilha;
- \(\nu_c\): frequência ciclotrônica;
- \(\nu_a\): frequência anômala;
- \(T_{\rm app}\): temperatura efetiva do aparato;
- correções de cavidade: resposta eletromagnética do contorno.

No formalismo operacional da armadilha:

\[
\frac{g}{2}
=
\frac{\bar\nu_c+\bar\nu_a}{\bar\nu_c}.
\]

Na leitura GDQ, \(\bar\nu_c\) mede a resposta orbital/carga ao contorno
eletromagnético, enquanto \(\bar\nu_a\) mede a diferença entre transporte
orbital e resposta de circulação interna.

### 2.3 Dicionário GDQ

O background eletrônico deve produzir:

\[
\Phi_e
\longrightarrow
H_{C,e},
\qquad
c_e,
\qquad
m_{\perp,e}.
\]

Correspondência:

| Experimento | GDQ |
|---|---|
| campo axial \(B_0\) | fonte externa \(B\) conjugada ao fluxo de Noether |
| potencial da armadilha | contorno/aparelho, não ação fundamental |
| frequência ciclotrônica | resposta orbital de carga |
| frequência anômala | resposta transversal \(m_{\perp,e}\) |
| cavidade | operador de contorno/impedância do aparelho |
| correções de cavidade | parte experimental de \(\mathsf R_{\rm app}\), não \(H_C\) do objeto |

Assim, para o elétron:

\[
a_e^{\rm GDQ}
=
\frac{1}{\gamma_{0,e}}
\frac{\langle c_e,H_{C,e}^{+}m_{\perp,e}\rangle}
{\langle c_e,H_{C,e}^{+}c_e\rangle}.
\]

O termo líder já calculado:

\[
a_e^{(1)}
=\frac{\alpha}{2\pi}.
\]

O resíduo experimental:

\[
a_e-a_e^{(1)}
\simeq
-1.75755\times10^{-6}.
\]

Esse resíduo deve vir das ordens superiores de \(H_{C,e}^{+}m_{\perp,e}\).

---

## 3. Background B — múon em anel de armazenamento

### 3.1 Fonte experimental

Referência principal de detalhes:

- D. P. Aguillard et al.,
  *Detailed Report on the Measurement of the Positive Muon Anomalous Magnetic
  Moment to 0.20 ppm*,
  arXiv:2402.15410.

Link:

- <https://arxiv.org/abs/2402.15410>

O resumo informa que o experimento usa múons positivos polarizados com:

\[
p_\mu=3.1\,{\rm GeV}/c,
\]

armazenados em um anel de raio:

\[
R_{\rm ring}=7.1\,{\rm m},
\]

com campo magnético uniforme:

\[
B_0=1.45\,{\rm T}.
\]

O valor de \(a_\mu\) é determinado pela diferença entre a frequência de
precessão do spin do múon e a frequência ciclotrônica, normalizada pelo campo
medido por NMR.

O resultado reportado no relatório detalhado é:

\[
a_\mu=116\,592\,057(25)\times10^{-11},
\]

e a média mundial informada é:

\[
a_\mu({\rm exp})
=116\,592\,059(22)\times10^{-11}.
\]

### 3.2 Domínio físico

O background físico mínimo do múon é:

\[
\mathcal B_\mu
=
\left(
p_\mu,\,
R_{\rm ring},\,
B_0,\,
\omega_a,\,
\tilde\omega_p',\,
\rho_\mu(x),\,
\Delta_{\rm beam},\,
\Delta_{\rm trans}
\right).
\]

Interpretação:

- \(p_\mu\): momento do feixe;
- \(R_{\rm ring}\): raio geométrico do anel;
- \(B_0\): campo magnético de armazenamento;
- \(\omega_a\): frequência anômala de precessão;
- \(\tilde\omega_p'\): medida NMR efetiva do campo;
- \(\rho_\mu(x)\): distribuição espacial do feixe;
- \(\Delta_{\rm beam}\): correções de movimento/dispersão do feixe;
- \(\Delta_{\rm trans}\): campos transientes e correções instrumentais.

Na GDQ, esses objetos não entram como campos fundamentais novos. Eles definem
o contorno/aparelho e a fonte externa para o background do múon.

### 3.3 Dicionário GDQ

Para o múon:

\[
\Phi_\mu
\longrightarrow
H_{C,\mu},
\qquad
c_\mu,
\qquad
m_{\perp,\mu}.
\]

Correspondência:

| Experimento | GDQ |
|---|---|
| \(p_\mu=3.1\,{\rm GeV}/c\) | estado cinemático/folha efetiva do sóliton múon |
| \(R_{\rm ring}=7.1\,{\rm m}\) | domínio macroscópico do aparelho |
| \(B_0=1.45\,{\rm T}\) | fonte magnética externa |
| \(\omega_a\) | leitura de \(a_\mu\) |
| NMR \(\tilde\omega_p'\) | calibração independente do campo |
| distribuição do feixe | medida efetiva sobre trajetórias |
| correções de beam/transientes | parte de aparelho, não deformação intrínseca do lépton |

O cálculo GDQ do múon deve ser:

\[
a_\mu^{\rm GDQ}
=
\frac{1}{\gamma_{0,\mu}}
\frac{\langle c_\mu,H_{C,\mu}^{+}m_{\perp,\mu}\rangle}
{\langle c_\mu,H_{C,\mu}^{+}c_\mu\rangle}.
\]

O termo líder universal é o mesmo:

\[
a_\mu^{(1)}
=\frac{\alpha}{2\pi}.
\]

O resíduo experimental em relação ao termo líder é:

\[
a_\mu-a_\mu^{(1)}
\simeq
4.51086\times10^{-6}.
\]

Esse valor é positivo e maior em módulo que o resíduo eletrônico. Portanto,
o background do múon não é uma cópia do background do elétron.

---

## 4. Como a Q39 entra

A Q39 fornece o espectro leptônico:

\[
e,\mu,\tau.
\]

Ela não calcula \(g-2\). Ela fornece os backgrounds:

\[
\Phi_e,\Phi_\mu,\Phi_\tau.
\]

O cálculo de Zeeman/\(g-2\) é:

\[
\Phi_\ell
\longrightarrow
H_{C,\ell}^{+}m_{\perp,\ell}
\longrightarrow
a_\ell.
\]

Assim:

\[
\text{hierarquia leptônica}
\neq
\text{anomalia magnética}.
\]

Mas:

\[
\text{hierarquia leptônica}
\Rightarrow
\text{background correto da anomalia}.
\]

---

## 5. O que ainda precisa ser construído

Para transformar este background experimental em cálculo GDQ preditivo, faltam:

1. construir \(\Phi_e\) e \(\Phi_\mu\) no setor leptônico com circulação
   fixada;
2. derivar \(H_{C,e}\) e \(H_{C,\mu}\) pela segunda variação da ação oficial;
3. construir \(m_{\perp,e}\) e \(m_{\perp,\mu}\) como fonte transversal
   magnética, removida a parte protegida por Noether;
4. avaliar a pseudoinversa física \(H_C^+\);
5. separar correções de objeto e correções de aparelho;
6. aplicar os dados experimentais apenas como domínio/contorno, não como
   ajuste de \(a_\ell\).

---

## 6. Status

\[
\boxed{
\text{background físico experimental montado;}
\quad
\text{Hessiana GDQ física ainda não construída.}
}
\]

Este arquivo permite o próximo passo: construir o modelo radial/espectral do
lépton e alimentar `avaliar_hessiana_q43.py` com \(H_C,c,m_\perp\) físicos.

