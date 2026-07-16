# Plano numérico das pendências da GDQ

## 1. Objetivo

Este documento organiza as pendências numéricas que restam depois da
consolidação estrutural das questões já trabalhadas.

A regra de uso é:

\[
\boxed{
\text{o cálculo numérico não deve substituir a prova estrutural; ele deve avaliá-la.}
}
\]

Ou seja, um solver só entra depois de estarem definidos:

1. operador;
2. domínio;
3. condição de contorno;
4. medida;
5. normalização;
6. observable comparável.

Também vale a regra global:

\[
\boxed{
\text{não alterar a ação oficial da GDQ e não importar o Modelo Padrão como postulado.}
}
\]

---

## 2. Status geral

As questões 39 e 40 saíram do bloco de faltas estruturais.

Q39 está fechada estruturalmente como espectro global de massa de repouso.
O que resta é refinamento numérico/local:

1. resposta térmica do estômato finito;
2. comparação entre contornos globais e contornos locais;
3. derivação variacional dos coeficientes efetivos;
4. exclusão fina de modos por monodromia/topologia.

Q40 está fechada estruturalmente para próton e nêutron.
O que resta é fenomenologia numérica:

1. fatores de forma;
2. espalhamento;
3. modos excitados;
4. observáveis fracos;
5. estabilidade quantitativa.

Q28 e Q29 estão fechadas como estrutura condicional/efetiva.
O que resta é cálculo explícito:

1. classes características;
2. \(\eta\)-invariantes;
3. normas internas dos geradores;
4. acoplamentos \(g_s,g,g'\);
5. \(v\);
6. Yukawas.

---

## 3. Ordem recomendada dos próximos passos

### Passo 1 — Atualizar os documentos de controle

Antes de novos cálculos, atualizar:

1. `faltas_plano.md`;
2. `constantes_status.md`.

Motivo: esses arquivos ainda carregam linguagem anterior em que Q28/Q29 eram
próximos gargalos. Agora o próximo bloco real é:

\[
\boxed{
Q34/Q35\text{ pelo teste }U(1)\rightarrow Q28/Q29/Q30/Q31\text{ numérico}
\rightarrow fenomenologia numérica.
}
\]

---

### Passo 2 — Q30: confinamento, Wilson loops e mass gap

Produto esperado:

`questão_30_yang_mills.md`

Status:

\[
\boxed{\text{fechada estruturalmente no setor efetivo GDQ--}SU(3)_C}
\]

Documentos:

1. `questão_30_yang_mills.md`;
2. `q30/conexao_su3_wilson_gap.md`.

Pendência numérica:

1. avaliar explicitamente a conexão de cor:

   \[
   A\in\Omega^1(N,\mathfrak{su}(3));
   \]

2. calcular holonomias/Wilson loops:

   \[
   W(C)=\operatorname{Tr}\,\mathcal P\exp\left(i\oint_C A\right);
   \]

3. avaliar numericamente:

   \[
   \langle W(C)\rangle\sim e^{-\sigma\,\operatorname{Area}(C)};
   \]

4. extrair a tensão:

   \[
   \sigma_{\rm conf};
   \]

5. montar a Hessiana confinante:

   \[
   \mathcal H_{\rm conf}=-\Delta_A+V_{\rm geom};
   \]

6. estimar o primeiro autovalor positivo:

   \[
   \Delta_{\rm YM}>0.
   \]

Critério de fechamento:

\[
\boxed{
\text{valor numérico de }\sigma\text{ + valor numérico de }\lambda_1\text{ + convergência.}
}
\]

---

### Passo 3 — Q31: CP forte e setor torsional

Produto esperado:

`questão_31.md` e `q31/cp_forte_torcao_su3.md`.

Status:

\[
\boxed{
\text{Q31 fechada estruturalmente; avaliação funcional e numérica posterior.}
}
\]

Pendências numéricas:

1. normalizar o modo torsional \(a\);
2. derivar o termo cinético canônico:

   \[
   \frac12 f_B^2(\partial a)^2;
   \]

3. verificar a fórmula:

   \[
   f_B
   =
   M_P
   \sqrt{\frac{3}{\sqrt{6\pi^5}}};
   \]

4. calcular a susceptibilidade topológica efetiva:

   \[
   \chi_{\rm top};
   \]

5. obter:

   \[
   m_a^2f_B^2=\chi_{\rm top};
   \]

6. estimar o EDM residual do nêutron.

Critério de fechamento:

\[
\boxed{
\text{valor de }\chi_{\rm top}^{\rm GDQ}
\text{ + }f_B\text{ canônico + EDM residual + teste cosmológico.}
}
\]

---

### Passo 4 — Q28/Q29: constantes de gauge e setor eletrofraco

Esta etapa não reabre Q28/Q29. Ela apenas transforma a estrutura condicional em
cálculo.

Pendências de Q28:

1. calcular:

   \[
   c_2(E_C),\quad c_3(E_C),\quad c_2(E_W),\quad c_1(L_Y);
   \]

2. avaliar o operador tangencial APS:

   \[
   \mathcal D_a
   =
   \slashed D_{\partial_a}
   +\frac18B_{ijk}^{(a)}\gamma^{ijk}
   -iA_i^{(a)}\gamma^i;
   \]

3. calcular:

   \[
   \eta_a(0),\qquad h_a;
   \]

4. verificar:

   \[
   n_a=-\frac12(\eta_a(0)+h_a)=1;
   \]

5. obter:

   \[
   N_{\rm ger}=\sum_{a=1}^3 n_a=3.
   \]

Pendências de acoplamento:

\[
\frac1{g_s^2}
=
\mathcal N_C\int_{\mathcal I}\|\xi_C\|^2d\mu_g,
\]

\[
\frac1{g^2}
=
\mathcal N_W\int_{\mathcal I}\|\xi_W\|^2d\mu_g,
\]

\[
\frac1{g'^2}
=
\mathcal N_Y\int_{\mathcal I}\|\xi_Y\|^2d\mu_g.
\]

Pendências de Q29:

1. calcular o modo:

   \[
   \Phi_{\rm EW}\sim(1,2)_{1/2};
   \]

2. calcular os coeficientes variacionais:

   \[
   S_{\rm eff}
   =
   S_0+\frac12a_2|\varphi|^2+\frac14a_4|\varphi|^4+\cdots;
   \]

3. obter:

   \[
   v^2=-\frac{2a_2}{a_4};
   \]

4. calcular:

   \[
   m_W=\frac{gv}{2},
   \qquad
   m_Z=\frac v2\sqrt{g^2+g'^2};
   \]

5. calcular:

   \[
   \tan\theta_W=\frac{g'}{g};
   \]

6. calcular Yukawas como integrais de sobreposição:

   \[
   y_{ij}
   =
   \mathcal N_Y
   \int_{\mathcal I}
   \langle\psi_{L,i},\Phi_{\rm EW}\psi_{R,j}\rangle d\mu_g.
   \]

Critério de fechamento:

\[
\boxed{
\text{obter }g_s,g,g',\theta_W,v\text{ e pelo menos a estrutura de Yukawas sem ajuste externo.}
}
\]

---

## 4. Bloco Q39 — massas leptônicas

Status:

\[
\boxed{\text{fechada estruturalmente no espectro global; setor térmico preditivo pendente.}}
\]

O resultado primário deve continuar sendo o espectro global regular:

\[
\chi\in[0,\pi],
\qquad
\text{regularidade natural nos dois polos}.
\]

Esse caso dá:

\[
r_2\simeq206.766,
\qquad
r_3\simeq3477.10,
\]

compatível com a rota analítica de Rosen--Morse.

### Pendências numéricas restantes

1. Documentar definitivamente que o contorno Robin-local representa o
   estômato físico finito, não a definição primária da massa de repouso.

2. Separar três objetos:

   \[
   \text{massa global},
   \qquad
   \text{deslocamento local de contorno},
   \qquad
   \text{resposta térmica do espaço de Einstein}.
   \]

3. A correção térmica já foi formalizada como ciclo \(S^1_\beta\), não como
   alteração da ação:

   \[
   \beta=\frac{\hbar}{k_BT_{\rm E}},
   \]

   onde \(T_{\rm E}\) é propriedade do espaço cosmológico de Einstein.

4. A primeira avaliação direta da Hessiana fria \(H\) e das fontes térmicas
   \(J^{(\beta)}\) já foi implementada em:

   ```text
   numerico/q39_leptons/evaluate_H_J_q39.py
   ```

   A forma usada foi:

   \[
   (\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}.
   \]

   Com sinal fermiônico e fatores líderes de Einstein:

   \[
   \eta_{\rm lead}=(3/2,3),
   \]

   obteve-se:

   \[
   (\Delta_\epsilon,\Delta_b)_{\rm lead}
   \approx
   (2.4514\times10^{-4},4.6517\times10^{-2}),
   \]

   contra:

   \[
   (\Delta_\epsilon,\Delta_b)_{\rm alvo}
   \approx
   (2.3795\times10^{-4},4.5175\times10^{-2}).
   \]

5. A pendência atual é derivar os coeficientes sublíderes:

   \[
   \eta_{\rm req}\approx(1.471445,2.929056),
   \]

   a partir da curvatura finita do espaço de Einstein, do tamanho finito do
   estômato ou de \(S_\partial^{\rm GDQ}\).

5. Transformar `compare_boundaries_q39.py` e o solver térmico em testes
   reproduzíveis:

   - entrada fixa;
   - tabela de saída;
   - erro relativo;
   - comentário físico do domínio;
   - nenhuma calibração escondida por CODATA.

Critério de fechamento numérico:

\[
\boxed{
\text{solver global reproduz massa; solver local explica deslocamento; setor térmico líder foi avaliado; fechamento metrológico exige derivar }\eta_{\rm req}.
}
\]

---

## 5. Bloco Q40 — próton, nêutron e observáveis bariônicos

Status:

\[
\boxed{\text{fechada estruturalmente; fenomenologia numérica posterior.}}
\]

### Pendências numéricas

1. Calcular densidades:

   \[
   \rho_E^p,\quad \rho_M^p,\quad \rho_E^n,\quad \rho_M^n.
   \]

2. Avaliar fatores de forma:

   \[
   G_E^B(q^2)
   =
   \int_{\epsilon_B}^{\pi}
   \rho_E^B(\chi)j_0(qC_rR_B\chi)d\chi,
   \]

   \[
   G_M^B(q^2)
   =
   \int_{\epsilon_B}^{\pi}
   \rho_M^B(\chi)j_0(qC_rR_B\chi)d\chi.
   \]

   Para o nêutron, o perfil elétrico líder já foi derivado como:

   \[
   H_n(\xi,\tau_n)
   =
   |\mu_n|
   [K_{\tau_n}(\xi,\xi_+)-K_{\tau_n}(\xi,\xi_-)],
   \]

   e implementado em `numerico/q40_barions/solve_hn_variational_q40.py`.

   A curva variacional foi comparada com a parametrização de Galster no script:

   ```text
   numerico/q40_barions/compare_ge_neutron_q40.py
   ```

   Saída:

   ```text
   numerico/q40_barions/saida_compare_ge_neutron_q40.md
   ```

   Resultado: a baixa transferência \(q\le2\,{\rm fm}^{-1}\) fica controlada
   em escala, enquanto a região intermediária exige o operador de
   sonda/magnetização ou filtro assintótico da casca composta.

   O mesmo comparador inclui agora o operador líder de superfície:

   \[
   F_\Sigma(q)=\left(1+\frac{q^2}{\Lambda_\Sigma^2}\right)^{-2},
   \qquad
   \Lambda_\Sigma=\frac{\sqrt{12}}{r_p}.
   \]

   Esse fator preserva \(G_E^n(0)\) e a inclinação no zero, mas reduz o RMS
   relativo contra Galster de \(18.6\%\) para \(12.7\%\) em
   \(q\le2\,{\rm fm}^{-1}\), e de \(50.7\%\) para \(33.0\%\) em
   \(q\le4\,{\rm fm}^{-1}\). A pendência restante é substituir esse filtro
   líder pela Hessiana eletromagnética/magnética completa da sonda.

   A formulação dessa pendência está em:

   ```text
   q40/adendo_operador_sonda_em.md
   ```

   O próximo script recomendado é:

   ```text
   numerico/q40_barions/solve_probe_response_q40.py
   ```

   Ele deve montar a Hessiana reduzida:

   \[
   H_\Sigma=
   \begin{pmatrix}
   H_{EE} & H_{EM} & H_{ET}\\
   H_{ME} & H_{MM} & H_{MT}\\
   H_{TE} & H_{TM} & H_{TT}
   \end{pmatrix},
   \]

   resolver \(H_\Sigma\delta\Phi=J_{\rm em}\) e projetar
   \(G_E^{n,\rm phys}(q^2)\). O critério de aceite é preservar
   \(G_E^n(0)=0\) e a inclinação já derivada, enquanto reduz a discrepância
   intermediária sem ajuste escalar livre.

   Esse script foi implementado. Saída:

   ```text
   numerico/q40_barions/saida_probe_response_q40.md
   ```

   Figuras:

   ```text
   numerico/figs/neutron_ge_probe_response_q40.png
   numerico/figs/neutron_probe_filters_q40.png
   ```

   Resultado: a Hessiana EMT mínima preserva carga e raio, mas quase não reduz
   o RMS contra Galster além do filtro escalar. Portanto, a próxima etapa não é
   aumentar a mistura perturbativa \(E\)-\(M\)-\(T\), mas derivar a impedância
   coletiva de superfície:

   \[
   \mathcal I_\Sigma(q)
   =
   \left.
   \frac{\delta^2\mathcal S_{\rm GDQ}^{\partial}}
   {\delta a_{\rm em}(q)\,\delta a_{\rm em}(-q)}
   \right|_{\mathfrak G_n}.
   \]

   Diagnóstico criado:

   ```text
   numerico/q40_barions/diagnose_surface_impedance_q40.py
   ```

   Saída:

   ```text
   numerico/q40_barions/saida_required_impedance_q40.md
   ```

   Figuras:

   ```text
   numerico/figs/neutron_required_impedance_q40.png
   numerico/figs/neutron_impedance_diagnostic_curve_q40.png
   ```

   Resultado diagnóstico: uma impedância coletiva começando em \(q^4\) reduz o
   RMS relativo contra Galster para \(5.49\%\) em \(0.25\le q\le2.0\) e
   \(4.18\%\) em \(0.25\le q\le4.0\). Isso indica que o termo faltante é
   coletivo de superfície e de ordem geométrica, não uma correção perturbativa
   proporcional a \((\alpha_{\rm tor}^{(2)})^2\).

   Derivação variacional consolidada:

   ```text
   q40/adendo_impedancia_variacional.md
   ```

   Resultado:

   \[
   \mathcal I_\Sigma(q)
   =
   -
   J_\Sigma^\dagger(q)K_\Sigma^{-1}(q)J_\Sigma(q).
   \]

   Assim, a forma \(q^4\), o sinal de amolecimento e a preservação de carga/raio
   são consequências da eliminação variacional dos modos coletivos de
   superfície.

   Refinamento reduzido executado:

   ```text
   numerico/q40_barions/refine_collective_modes_q40.py
   ```

   Saída:

   ```text
   numerico/q40_barions/saida_collective_modes_q40.md
   ```

   Figuras:

   ```text
   numerico/figs/neutron_collective_modes_curve_q40.png
   numerico/figs/neutron_collective_modes_impedance_q40.png
   ```

   Resultado:

   \[
   j_0=1.712091781054,\quad
   j_1=1.341454657186,\quad
   j_2=1.063840998206.
   \]

   O refinamento preserva \(G_E^n(0)\) e \(\langle r_n^2\rangle\), e reduz o
   RMS relativo contra Galster para \(5.491\%\) em \(0.25\le q\le2.0\) e
   \(4.178\%\) em \(0.25\le q\le4.0\).

   Status:

   \[
   \boxed{\text{Q40 fechada estruturalmente e no refinamento reduzido de superfície.}}
   \]

3. Comparar:

   \[
   G_E^p,\quad G_M^p,\quad G_E^n,\quad G_M^n
   \]

   com dados de espalhamento elástico.

4. Resolver numericamente o potencial efetivo bariônico:

   \[
   V_{\rm eff}^{B}(\chi).
   \]

5. Calcular fases parciais:

   \[
   \delta_\ell(E).
   \]

6. Obter seções de choque.

7. Calcular modos radiais/torsionais além do \(\Delta(1232)\).

8. Derivar \(G_F\) e \(g_A\) da cola fraca/torsional para o decaimento do
   nêutron.

9. Se for permitido violar setor bariônico, calcular:

   \[
   \Gamma_p\sim e^{-S_{\rm inst}/\hbar}.
   \]

Critério de fechamento numérico:

\[
\boxed{
\text{fatores de forma + fases parciais + observáveis fracos sem parâmetros livres novos.}
}
\]

---

## 6. Bloco Q38 — constante gravitacional

Status:

\[
\boxed{\text{fechada estruturalmente; integral efetiva pendente.}}
\]

Pendência central:

\[
\mathcal V_{\rm eff}^{(G)}
=
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y
\right].
\]

Tarefa numérica:

1. escolher background estacionário real da GDQ;
2. fixar \(\eta_R\);
3. avaliar \(\mathcal V_{\rm eff}^{(G)}\);
4. verificar:

   \[
   G
   =
   \frac{c^4\Lambda_C^2}
   {16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}};
   \]

5. demonstrar o limite de Poisson:

   \[
   \nabla^2\Phi=4\pi G\rho.
   \]

Critério de fechamento:

\[
\boxed{
\text{coeficiente Einstein--Hilbert extraído diretamente da ação efetiva.}
}
\]

---

## 7. Bloco Q37 — constante de estrutura fina

Status:

\[
\boxed{\text{rota estrutural avançada; normalização final pendente.}}
\]

Pendência numérica/geométrica:

1. derivar a métrica espectral no espaço de conexões:

   \[
   G_*^{ab};
   \]

2. fixar o gerador eletromagnético:

   \[
   Q=T_3+Y;
   \]

3. calcular:

   \[
   \frac1{g_{\rm em}^2}=v_av_bG_*^{ab};
   \]

4. obter:

   \[
   \alpha=\frac{g_{\rm em}^2}{4\pi};
   \]

5. verificar o papel de \(T^5\times S^3\) apenas como ciclo interno/global de
   calibração, sem substituir a base local da ação.

Critério de fechamento:

\[
\boxed{
\alpha\text{ calculado por norma geométrica, sem seleção posterior de fatores.}
}
\]

---

## 8. Padrão dos scripts numéricos

Todo script novo deve seguir este padrão mínimo:

1. cabeçalho dizendo qual questão resolve;
2. lista de parâmetros de entrada;
3. separação entre constantes derivadas e constantes calibradas;
4. função que monta operador/matriz;
5. função que aplica condição de contorno;
6. solver;
7. estudo de convergência;
8. tabela final;
9. erro relativo;
10. veredito físico;
11. salvamento opcional de CSV/JSON.

O script deve imprimir explicitamente:

\[
\text{domínio},\quad
\text{contorno},\quad
\text{medida},\quad
\text{normalização}.
\]

Nenhum script deve usar dado experimental como entrada sem marcar isso como
calibração.

---

## 9. Prioridade prática

A ordem mais eficiente agora é:

1. atualizar `faltas_plano.md` e `constantes_status.md`;
2. usar o teste \(U(1)\) comum a Q34/Q35 já registrado em
   `q34/polarizacao_U1_heat_kernel.md`:
   \[
   \Pi_{\mu\nu}^{(\tau)}(q);
   \]
3. preparar cálculo numérico de Q30/Q31 para \(\sigma\), \(\lambda_1\), \(g_s\),
   \(\chi_{\rm top}\), \(f_B\) e EDM residual;
4. organizar os scripts de Q39 como testes de referência;
5. iniciar pacote numérico de Q40;
6. voltar para Q28/Q29 para cálculo explícito de índice, acoplamentos e
   eletrofraco.

Resumo:

\[
\boxed{
\text{Q32 está estruturalmente fechada; Q34/Q35 estão fechadas no teste }
U(1)\text{; Q34 também está fechada estruturalmente no setor não abeliano.}
\text{ Restam coeficientes/jacobianos e avaliação numérica das }\Lambda_s
\text{ setoriais.}
}
\]
