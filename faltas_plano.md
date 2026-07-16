# Plano de ação para zerar `faltas.md`

## 1. Objetivo

Usar `faltas.md` como backlog mestre e transformar cada item em uma destas
classes:

1. **Resolvido estruturalmente** — já há resposta dedutiva suficiente.
2. **Resolvido, falta referência** — já foi feito em outro arquivo, mas
   `faltas.md` ainda não aponta corretamente.
3. **Pendente estrutural** — falta uma prova ou construção interna essencial.
4. **Dependente** — só fecha depois de outra questão.
5. **Trabalho posterior** — simulação, benchmark, comparação fenomenológica ou
   cálculo numérico.
6. **Correção editorial** — ajustar linguagem, status ou evitar afirmação forte.

Regra de trabalho:

\[
\boxed{
\text{não alterar a ação oficial; não importar o Modelo Padrão como postulado.}
}
\]

Regra arquitetural global--local:

\[
\boxed{
\text{não redeterminar localmente uma quantidade espectral global herdada.}
}
\]

Antes de iniciar um cálculo, classificar o observável por espaço, fonte,
contorno, escala e estatuto, conforme
`teorema_heranca_espectral_global_local_gdq.md`. A ponte foi demonstrada sem
colar cosmológico--local e aplicada ao background gaussiano $C_3$. Para Q40,
a pendência compartilhada foi eliminada. Para Q39 resta somente identificar
o cluster leptônico $n=0,1,17$ com o cluster físico transportado. Resposta
local, dressing, cirurgia e taxas permanecem problemas planares.

---

## 2. Ordem recomendada

A ordem deve seguir risco estrutural, não numeração.

### Fase A — Limpeza de status e referências

Objetivo: impedir que `faltas.md` contradiga documentos já atualizados.

1. **Q40 — Próton e nêutron**
   - Status atual correto:
     \[
     \boxed{\text{fechada estruturalmente}}
     \]
   - Ação:
     manter `faltas.md`, `numerico.md` e `questão_40.md` sincronizados
     com este status; Q40 não pertence mais ao bloco de faltas estruturais.
   - Referências:
     - `questão_40.md`
     - `q40/solucao_global_colada.md`
     - `q40/carga_spin_paridade.md`
     - `q40/raios_momentos_form_factors.md`
     - `q40/espectro_espalhamento_estabilidade.md`
     - `q40/adendo_observaveis_criticos.md`
   - Restante:
     fatores de forma numéricos, fases parciais, \(G_F\), \(g_A\),
     \(S_{\rm inst}\) e a separação dos terceiros jatos causais nos dois
     invariantes $C_S$ e $C_T$ para observáveis polarizados. A combinação
     $2|C_S|^2+6|C_T|^2$ já está fechada pela lei GDQ de relaxamento e fixa a
     meia-vida. O antineutrino já é caracterizado como onda torsional neutra.
   - Classe:
     **resolvido estruturalmente / trabalho posterior**.

2. **Q39 — Massas leptônicas**
   - Status atual:
     \[
     \boxed{\text{fechada como espectro global de massa de repouso}}
     \]
   - Ação:
     manter como fechada estruturalmente; pendências viram refinamento.
   - Restante:
     coeficientes efetivos de correção, resposta térmica local, exclusão
     detalhada de modos por monodromia.
   - Classe:
     **resolvido estruturalmente / refinamento posterior**.

3. **Q36 — Escala dimensional**
   - Status:
     \[
     \boxed{\text{fechada por calibração metrológica}}
     \]
   - Ação:
     auditar linguagem para remover qualquer promessa de massa absoluta
     ab initio.
   - Classe:
     **resolvido / auditoria editorial**.

4. **Q33 — Escala de corte**
   - Status:
     estruturalmente respondida.
   - Ação:
     marcar capítulo 33 original como correção futura, não como lacuna da
     resposta.
   - Classe:
     **resolvido estruturalmente / correção editorial**.

---

## 3. Fase B — Pendências estruturais centrais

Estas são as que realmente seguram blocos grandes.

### B1. Q28 — Grupo efetivo do Modelo Padrão

Status:

$$
\boxed{
\text{setor local calculado; carga cosmológica global pendente}
}
$$

Por que é central:

Q28 destravou a formulação condicional de Q29, Q30, Q31, Q34 e parte de Q35.
O que ainda falta não é a estrutura do grupo efetivo, mas o cálculo explícito
das classes características, \(\eta\)-invariantes e normas internas.

Ações já consolidadas:

1. definir o fibrado interno efetivo:
   \[
   E_{\rm int}=E_C\oplus E_W\oplus L_Y;
   \]
2. construir a conexão efetiva;
3. formular a redução global para:
   \[
   \frac{SU(3)_C\times SU(2)_L\times U(1)_Y}{\Gamma};
   \]
4. aproveitar \(\mathfrak{su}(3)\) por potenciais de
   Killing:
   \[
   \{P_A,P_B\}_{\rm Poisson}=f_{ABC}P_C;
   \]
5. estruturar representações e hipercargas;
6. formular cancelamento de anomalias;
7. formular três gerações por índice APS/Bismut.

Ações ainda pendentes:

1. não repetir os cálculos locais de Berry/Hessiana já encerrados;
2. formular a tensão global como condição cosmológica de contorno;
3. calcular $A[\mathfrak B_{\rm cosmológico}]$ e testar se $A=18$;
4. calcular $g_s,g,g'$ como normas/rigidezes internas;
5. avaliar classes globais adicionais nos ciclos apropriados.

Produto sugerido:

`questão_28_final.md` e adendos em `q28/`.

Classe:

**resolvido estruturalmente como teorema condicional / cálculo explícito posterior**.

---

### B2. Q29 — Quebra eletrofraca

Status:

\[
\boxed{\text{fechada de acordo com \texttt{bkp/29-0.md}}}
\]

Ações já consolidadas:

1. identificar modo efetivo:
   \[
   \Phi_{\rm EW}\sim(1,2)_{1/2};
   \]
2. derivar potencial efetivo;
3. demonstrar instabilidade quadrática e estabilidade quartica;
4. obter as relações:
   \[
   m_W=\frac{gv}{2},
   \qquad
   m_Z=\frac v2\sqrt{g^2+g'^2},
   \qquad
   \tan\theta_W=\frac{g'}{g};
   \]
5. formular Yukawas como integrais de sobreposição.

Correção obrigatória:

\[
v_K\simeq72{,}85\,{\rm MeV}\neq246\,{\rm GeV}.
\]

Produto sugerido:

`questão_29_final.md` e adendos em `q29/`.

Classe:

**resolvido / avaliação numérica posterior que não reabre a questão**.

A predição absoluta de $\alpha$ deve ser administrada como programa futuro
autônomo. Por decisão explícita do usuário, $1/128$ não integra o programa
atual; usa-se $\alpha^{-1}\simeq137$ na ponte constitutiva de baixa energia.

---

### B3. Q30 — Confinamento e mass gap

Status:

\[
\boxed{\text{fechada estruturalmente no setor efetivo GDQ--}SU(3)_C}
\]

Ações consolidadas:

1. manter a prova variacional de tensão/área constante;
2. separar \(\alpha_s^{\rm eff}=3/(8\pi)\) de running completo;
3. usar Q28 para construir:
   \[
   A_C\in\Omega^1(N,\mathfrak{su}(3));
   \]
4. definir Wilson loops como holonomias de \(A_C\);
5. obter lei de área por \(\sigma>0\);
6. formular Hessiana confinante e cota de gap:
   \[
   \lambda_1\ge c_D\Lambda_0+c_\sigma\sigma>0.
   \]

Produto sugerido:

`questão_30_yang_mills.md` e `q30/conexao_su3_wilson_gap.md`.

Classe:

**resolvido estruturalmente / cálculo explícito e numérico posterior**.

---

### B4. Q38 — Constante gravitacional \(G\)

Status:

\[
\boxed{\text{fechada como problema global no espaço cosmológico de Einstein}}
\]

Trabalhos posteriores, sem reabrir a questão:

1. avaliar:
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
   \right];
   \]
2. fixar \(\eta_R\);
3. obter limite fraco:
   \[
   \nabla^2\Phi=4\pi G\rho;
   \]
4. derivar \(\alpha^4\), \(\chi_{\rm Fano}\) e \(e^{1/(2\alpha)}\) sem ajuste.

Produto sugerido:

`q38/avaliacao_Veff_G.md`

Classe:

**resolvido globalmente / projeções locais e comparação fenomenológica
posteriores**.

Não exigir que a avaliação em um infinitésimo da fibra determine o valor
global de $G$. O setor local pode verificar transporte, limite fraco e
compatibilidade, mas não contém sozinho a informação cosmológica global.

---

## 4. Fase C — Setores de campos, loops e causalidade

### C1. Q32 — Propagador modificado

Status:

\[
\boxed{\text{fechada estruturalmente; coeficientes completos e OS ficam para cálculo posterior}}
\]

Ações:

1. usar a separação:
   \[
   \mathcal O_{\rm Hess}^{(2)}=\tau L_{\rm GDQ}^{(2)};
   \]
2. usar o gerador normalizado:
   \[
   L_{\rm GDQ}^{(2)}=\tau^{-1}\mathcal O_{\rm Hess}^{(2)};
   \]
3. fixar o gauge Hermitiano/DeTurck;
4. registrar que o kernel completo é:
   \[
   e^{-\tau L_{\rm GDQ}^{(2)}};
   \]
5. deixar reflexão positiva completa e causalidade retardada explícita como
   verificação posterior.

Produto sugerido:

`q32/reducao_hessiana_gauge_fixada.md`

Classe:

**resolvida estruturalmente / cálculo funcional posterior**.

---

### C2. Q34 — Calibre em loops

Status:

\[
\boxed{\text{fechada no setor geométrico declarado de 34-0}}
\]

Ações:

1. usar o teste mínimo \(U(1)\);
2. usar o heat-kernel covariante;
3. usar o cálculo já registrado em:
   \[
   \boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}};
   \]
4. usar a extensão não abeliana registrada em:
   \[
   \boxed{\texttt{q34/slavnov\_taylor\_geometrico.md}};
   \]
5. manter Slavnov--Taylor como identidade geométrica:
   \[
   \mathcal S(\Gamma)=0;
   \]
6. explicar fantasmas como auditoria, não ontologia no setor não abeliano.

Dependência:

Q28 para o setor gauge completo.

Produto sugerido:

`q34/loop_U1_teste_minimo.md`, `q34/polarizacao_U1_heat_kernel.md` e
`q34/slavnov_taylor_geometrico.md`

Classe:

**fechada; Bismut, topologia e setor não abeliano são extensões posteriores**.

---

### C3. Q35 — Polo de Landau

Status:

\[
\boxed{\text{fechada condicionalmente no setor }U(1)}
\]

Ações:

1. usar a polarização \(U(1)\) já calculada em:
   \[
   \boxed{\texttt{q34/polarizacao\_U1\_heat\_kernel.md}};
   \]
2. usar a identificação setorial registrada em:
   \[
   \boxed{\texttt{q35/tau\_geometrico\_setorial.md}};
   \]
3. usar $\Lambda_{\rm EM}=1{,}90727017413475\Lambda_C$;
4. estender para setores não abelianos quando necessário;
5. manter como tese efetiva:
   \[
   \alpha(\mu)\to\alpha_*<\infty
   \]
   por saturação heat-kernel, ou:
   \[
   \mu\gtrsim\Lambda_C
   \Rightarrow
   \text{regime pontual deixa de ser físico}.
   \]

Produto sugerido:

`q35/U1_sem_polo_Landau.md` e `q35/tau_geometrico_setorial.md`

Classe:

**fechada condicionalmente no setor $U(1)$; extensões não reabrem a questão**.

---

## 5. Fase D — Medição, sinal e spin refinado

### D1. Q24 — Assintoticidade da medição

Status:

\[
\boxed{\text{dominância espectral existe; ponte com registros pendente}}
\]

Ações:

1. conectar operador espectral \(\mathcal H\) a registros \(R_i\);
2. provar estabilidade de ponteiros;
3. estimar supressão de termos fora da diagonal;
4. conectar bacias geométricas à regra de Born da Q22.

Produto sugerido:

`questão_24_registros.md`

Classe:

**pendente estrutural médio**.

---

### D2. Q25 — Problema do sinal

Status:

\[
\boxed{\text{resolução geométrica feita; algoritmo posterior}}
\]

Ações:

1. manter como resolvido conceitualmente;
2. mover algoritmo, variância, benchmarks e Hubbard 2D para trabalho posterior;
3. se desejar, criar especificação de matriz transmissão/reflexão.

Produto sugerido:

`q25/especificacao_algoritmica.md`

Classe:

**trabalho posterior computacional**.

---

### D3. Q26 — Hopf e resíduos para spin

Status:

\[
\boxed{\text{spin fechado pela rota spinorial; Hopf/resíduos são refinamento}}
\]

Ações:

1. manter como refinamento interpretativo;
2. conectar Hopf, resíduos e integração no toro;
3. evitar substituir a prova por fibrado spinorial.

Produto sugerido:

`q26/hopf_residuos_refinamento.md`

Classe:

**refinamento posterior**.

---

## 6. Fase E — Constantes, CP forte e fenomenologia

### E1. Constantes fundamentais

Status:

\[
\boxed{\text{programa aberto}}
\]

Ações:

1. listar constantes por categoria:
   - já derivadas estruturalmente;
   - calibradas;
   - estimadas;
   - abertas;
2. separar teorema, hipótese efetiva e heurística;
3. remover scripts que injetam alvo sem declarar.

Produto sugerido:

`constantes_status.md`

Classe:

**programa aberto / auditoria transversal**.

---

### E2. Q31 — CP forte

Status:

\[
\boxed{\text{fechada estruturalmente no setor efetivo GDQ--}SU(3)_C}
\]

Ações:

1. calcular \(\chi_{\rm top}\);
2. conectar \(f_B\) ao termo cinético canônico por cálculo funcional explícito;
3. decidir numericamente se \(a\) é polo propagante ou modo relaxacional;
4. calcular EDM residual;
5. validar a cosmologia superamortecida.

Produto sugerido:

`q31/cp_forte_torcao_su3.md`

Classe:

**resolvido estruturalmente / cálculo funcional e numérico posterior**.

---

## 7. Prioridade prática imediata

Para avançar sem dispersão:

1. Manter `faltas.md`, `faltas_plano.md`, `constantes_status.md` e
   `numerico.md` sincronizados.
2. Executar o teste \(U(1)\) comum a Q34/Q35 para loops e tradução
   perturbativa externa.
3. Manter Q28/Q29/Q30/Q31 como cálculo explícito posterior de índices, normas,
   acoplamentos, \(\sigma\) e gap.
4. Manter Q39/Q40 como refinamento numérico/fenomenológico, não como lacuna
   estrutural.

Ordem curta:

\[
\boxed{
Q34/Q35\text{ via }\Pi_{\mu\nu}^{(\tau)}
\to Q28/Q29/Q30/Q31\text{ numérico}
\to Q39/Q40\text{ fenomenológico}.
}
\]

---

## 8. Critério de encerramento de cada item

Um item pode sair de `faltas.md` quando tiver:

1. documento de resposta;
2. status explícito;
3. equações principais;
4. dependências declaradas;
5. separação entre estrutural e fenomenológico;
6. indicação de trabalho posterior, se houver.

Modelo:

```md
Status: resolvido estruturalmente.

Resposta:
...

Referências:
- questão_X.md
- qX/adendo_...

Trabalho posterior:
- simulação;
- comparação experimental;
- refinamento numérico.
```

---

## 9. Veredito

\[
\boxed{
\text{A estrutura geral está formada. A tarefa atual é zerar inconsistências de status e dependências.}
}
\]

O maior bloco estrutural remanescente foi reduzido: Q32 está fechada
estruturalmente; Q34 está fechada no setor geométrico declarado após derivar o
loop da ação oficial e testar kernels covariantes; Q35 está fechada
condicionalmente no setor $U(1)$, sem incluir $1/128$ no programa atual.
Restam ainda extensões topológicas, índice, normas
internas, \(v\), acoplamentos, Yukawas, \(\sigma\), gap numérico,
\(\chi_{\rm top}\), \(f_B\) canônico e EDM residual.
