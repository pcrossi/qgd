# Relatório final local — Q39: hierarquia leptônica

## 1. Resultado consolidado

A análise numérica da Questão 39 fica consolidada em três níveis:

1. limite espectral global;
2. efeito local do estômato finito;
3. correção térmica efetiva do estômato.

O fechamento correto é:

\[
\boxed{
\text{Q39 está fechada no espectro global Reg-Reg; o setor térmico foi avaliado em aproximação líder de Einstein por }-H^{-1}J^{(\beta)}.
}
\]

---

## 2. Limite espectral global

Script:

- `solve_hierarchy_q39.py`

Saída:

- `saida_solve_hierarchy.md`

No limite Regularidade-Regularidade, o espectro analítico de Rosen-Morse é:

\[
\lambda_n=(s+n)^2-\frac{b^2}{(s+n)^2}.
\]

Com:

\[
n_e=0,\qquad n_\mu=1,\qquad n_\tau=17,
\]

obtém-se:

\[
\frac{M_\mu}{M_e}\approx 206.7679,
\]

\[
\frac{M_\tau}{M_e}\approx 3477.1465.
\]

Esse é o núcleo forte da Q39: o espectro global reproduz as razões leptônicas sem depender do truncamento local do estômato.

---

## 3. Comparação de contornos

Script:

- `compare_boundaries_q39.py`

Saída:

- `saida_compare_boundaries.md`

Resultado regenerado:

| Contorno | \(M_\mu/M_e\) | Desvio | \(M_\tau/M_e\) | Desvio |
|---|---:|---:|---:|---:|
| Robin-Robin | 208.158808 | \(+0.673\%\) | 3502.038295 | \(+0.716\%\) |
| Robin-Regularidade | 207.460940 | \(+0.335\%\) | 3489.539602 | \(+0.356\%\) |
| Regularidade-Robin | 207.460427 | \(+0.335\%\) | 3489.539071 | \(+0.356\%\) |
| Regularidade-Regularidade | 206.767399 | \(\approx 0\%\) | 3477.131776 | \(-0.001\%\) |

Interpretação:

1. Regularidade-Regularidade é o limite global Rosen-Morse.
2. Robin-Regularidade representa um único estômato físico.
3. Robin-Robin representa dois estômatos e dobra aproximadamente o deslocamento.

Conclusão:

\[
\boxed{
\text{para um único estômato físico, o contorno adequado é Robin-Regularidade.}
}
\]

---

## 4. Setor térmico efetivo

Script:

- `thermal_solver_q39.py`

Saída:

- `saida_thermal_solver.md`

Partindo do caso Robin-Regularidade em \(T=0\):

\[
\frac{M_\mu}{M_e}=207.460940,
\]

\[
\frac{M_\tau}{M_e}=3489.539601.
\]

O solver efetivo encontra:

\[
\Delta_\epsilon
=
2.37946518\times10^{-4}\ {\rm rad},
\]

\[
\Delta_b
=
4.51750951\times10^{-2}.
\]

Com esses parâmetros:

\[
\frac{M_\mu}{M_e}=206.768339,
\]

\[
\frac{M_\tau}{M_e}=3477.149462.
\]

Isso mostra que o desvio local do estômato pode ser compensado por um vestimento térmico efetivo pequeno em escala angular absoluta, mas ainda não prova que esse vestimento é preditivo.

Ponto crítico:

\[
\boxed{
\Delta_\epsilon\ \text{e}\ \Delta_b\ \text{ainda são obtidos por busca numérica contra o alvo.}
}
\]

Portanto, eles devem ser tratados como alvo quantitativo para a avaliação
direta de \(H\) e \(J^{(\beta)}\) a partir do operador GDQ com contorno
Robin-Regularidade.

---

## 5. Classificação dos arquivos

| Arquivo | Status | Uso |
|---|---|---|
| `solve_hierarchy_q39.py` | oficial | teste espectral e convergência |
| `compare_boundaries_q39.py` | oficial | seleção do contorno físico |
| `thermal_solver_q39.py` | efetivo | quantificação do vestimento térmico necessário |
| `saida_solve_hierarchy.md` | saída oficial | registro do espectro global e Robin-Robin |
| `saida_compare_boundaries.md` | saída oficial | comparação dos contornos |
| `saida_thermal_solver.md` | saída efetiva | ajuste térmico do estômato |
| `STATUS.md` | controle | status auditável e pendências |
| `RELATORIO_FINAL.md` | referência local | síntese da Q39 numérica |

---

## 6. Pendências restantes

Foi adicionada a derivação variacional formal dos parâmetros térmicos em:

- `DERIVACAO_VARIACIONAL_TERMICA.md`
- `FECHAMENTO_Q39.md`

A forma GDQ obtida é:

\[
\begin{pmatrix}
\Delta_\epsilon\\
\Delta_b
\end{pmatrix}
=
-
H^{-1}
\begin{pmatrix}
J_\epsilon^{(\beta)}\\
J_{\ln b}^{(\beta)}
\end{pmatrix}.
\]

Com isso, a pendência foi reduzida a uma tarefa concreta: derivar os
coeficientes sublíderes que completam a fonte térmica de Einstein. A avaliação
direta líder já fornece:

\[
\eta_{\rm lead}=(1.5,3.0),
\]

com resposta:

\[
(\Delta_\epsilon,\Delta_b)_{\rm lead}
\approx
(2.4514\times10^{-4},4.6517\times10^{-2}),
\]

contra o alvo inverso:

\[
(\Delta_\epsilon,\Delta_b)_{\rm alvo}
\approx
(2.3795\times10^{-4},4.5175\times10^{-2}).
\]

Para fechamento preditivo forte, faltam:

1. derivar os coeficientes sublíderes
   \(\eta_{\rm req}\approx(1.471445,2.929056)\);
2. verificar unicidade local da solução térmica;
3. repetir o solver térmico para \(N=4000,8000,16000\);
4. documentar a estabilidade dos parâmetros térmicos sob refinamento de malha.

---

## 7. Conclusão operacional

Q39 pode ser usada como template dos demais blocos numéricos porque já separa:

1. limite analítico;
2. discretização;
3. estudo de contorno;
4. correção efetiva;
5. pendência variacional.

A formulação recomendada para o manuscrito/controle é:

\[
\boxed{
\text{A hierarquia leptônica emerge do espectro global de Rosen-Morse; o estômato finito induz deslocamento local controlado; a compensação térmica líder é dada pela resposta GDQ }-H^{-1}J^{(\beta)}\text{ com fatores de Einstein }(3/2,3).
}
\]
