# Status numérico — Questão 39: hierarquia leptônica

## 1. Veredito atual

A Questão 39 é o bloco numérico mais maduro da pasta `numerico/`.

Status:

\[
\boxed{
\text{Q39 concluída: espectro global Reg-Reg fechado e setor térmico líder avaliado por }-H^{-1}J^{(\beta)}.
}
\]

Em termos práticos:

1. o limite global Regularidade-Regularidade reproduz o espectro analítico de Rosen-Morse e as razões leptônicas;
2. o truncamento por estômato finito desloca as razões de massa de forma estável;
3. o solver térmico mostra quais correções efetivas seriam necessárias para recuperar o alvo físico;
4. a avaliação direta de \(H\) e \(J^{(\beta)}\) foi implementada em primeira aproximação; o sinal fermiônico e os fatores líderes de Einstein \((3/2,3)\) reproduzem o sinal e a ordem de grandeza, restando cerca de \(3\%\) de coeficientes sublíderes.

Portanto, Q39 está concluída como referência metodológica para os demais
blocos numéricos. O refinamento metrológico dos coeficientes sublíderes de
heat-kernel/curvatura ou de \(S_\partial^{\rm GDQ}\) fica registrado como
trabalho posterior, não como bloqueio da questão.

---

## 2. Arquivos da pasta

### Script oficial de referência espectral

Arquivo:

- `solve_hierarchy_q39.py`

Função:

- define os parâmetros geométricos base;
- calcula o limite analítico Rosen-Morse;
- resolve o problema discreto no domínio de estômato duplo;
- gera `saida_solve_hierarchy.md`.

Status:

\[
\boxed{\text{oficial como teste espectral e estudo de convergência do operador radial.}}
\]

Observação:

o domínio usado no estudo discreto principal é

\[
[\epsilon_{\rm eff},\pi-\epsilon_{\rm eff}],
\]

isto é, um domínio com dois polos truncados. Esse caso é útil como teste simétrico, mas não é a melhor representação de um único estômato físico.

---

### Script oficial comparativo de contornos

Arquivo:

- `compare_boundaries_q39.py`

Função:

- compara quatro domínios:
  1. Robin-Robin;
  2. Robin-Regularidade;
  3. Regularidade-Robin;
  4. Regularidade-Regularidade.

Status:

\[
\boxed{\text{oficial para decidir qual contorno representa melhor a topologia física.}}
\]

Resultado essencial:

| Caso | Interpretação | Resultado |
|---|---|---|
| Reg-Reg | limite global Rosen-Morse | coincide com as razões analíticas |
| Robin-Reg | um estômato físico | desvio local de cerca de \(+0.33\%\) |
| Reg-Robin | estômato no antipolo | mesmo desvio de \(+0.33\%\) |
| Robin-Robin | dois estômatos | desvio dobrado, cerca de \(+0.67\%\) |

Conclusão física:

\[
\boxed{
\text{o contorno Robin-Regularidade é o melhor representante de um único estômato físico.}
}
\]

---

### Script térmico efetivo

Arquivo:

- `thermal_solver_q39.py`

Função:

- parte do caso Robin-Regularidade;
- busca \(\Delta_\epsilon\) e \(\Delta_b\) que compensam o deslocamento local do estômato;
- gera `saida_thermal_solver.md`.

Status:

\[
\boxed{\text{engenharia inversa numérica do equilíbrio térmico; ainda não é derivação fechada.}}
\]

Resultado salvo atualmente:

\[
\Delta_\epsilon \approx 2.37946518\times 10^{-4}\ {\rm rad},
\]

\[
\Delta_b \approx 4.51750951\times 10^{-2}.
\]

Interpretação:

1. \(\Delta_\epsilon>0\) indica expansão térmica efetiva do estômato;
2. \(\Delta_b\) indica vestimento térmico efetivo do acoplamento;
3. a solução reproduz numericamente as razões de massa, mas usa ajuste por busca numérica.

Pendência:

\[
\boxed{
\text{avaliar diretamente }H\text{ e }J^{(\beta)}\text{ no operador GDQ Robin-Regularidade.}
}
\]

---

## 3. Equações usadas como definição operacional

O problema radial regularizado é formulado para

\[
\psi(\chi)=\frac{\phi(\chi)}{\sin^s\chi}.
\]

O operador discreto implementado é equivalente à forma:

\[
-\psi''-2s\cot\chi\,\psi'
+\left(s^2-2b\cot\chi\right)\psi
=\lambda\psi.
\]

Os autovalores analíticos de referência são:

\[
\lambda_n=(s+n)^2-\frac{b^2}{(s+n)^2}.
\]

A identificação leptônica usada é:

\[
n_e=0,\qquad n_\mu=1,\qquad n_\tau=17.
\]

As razões de massa são:

\[
\frac{M_\mu}{M_e}
=
\sqrt{\frac{\lambda_1}{\lambda_0}},
\qquad
\frac{M_\tau}{M_e}
=
\sqrt{\frac{\lambda_{17}}{\lambda_0}}.
\]

---

## 4. Parâmetros geométricos atualmente usados

A implementação atual usa:

\[
\alpha=\frac{1}{137.03599907},
\]

\[
\epsilon=\frac{5\alpha}{\pi},
\]

\[
\Delta\epsilon_{\rm geom}
=
\frac49\alpha^2-\frac{\pi}{2}\alpha^3,
\]

\[
\epsilon_{\rm eff}
=
\epsilon-\Delta\epsilon_{\rm geom},
\]

\[
s=\epsilon_{\rm eff},
\]

\[
b=
\frac{\alpha}{20\pi}
\left[
1+
\left(
\frac32-\frac{4}{15}\alpha
\right)
\alpha\ln\frac1\epsilon
\right].
\]

Essas fórmulas devem ser mantidas separadas em duas classes:

1. parte geométrica estrutural já adotada no modelo;
2. vestimentos efetivos que ainda exigem derivação variacional completa.

---

## 5. O que está fechado

Está fechado numericamente:

1. o solver reproduz o limite analítico Reg-Reg;
2. a discretização converge;
3. o efeito do estômato finito é estável;
4. o desvio escala com o número de contornos truncados;
5. o contorno de um único estômato deve ser Robin-Regularidade, não Robin-Robin;
6. a compensação térmica necessária pode ser estimada numericamente.

---

## 6. O que falta para fechamento final

Foi adicionada a derivação variacional formal em:

- `DERIVACAO_VARIACIONAL_TERMICA.md`
- `FECHAMENTO_Q39.md`

Com isso, a origem GDQ dos parâmetros térmicos fica:

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
\end{pmatrix},
\]

onde \(H\) é a Hessiana fria do funcional de borda e \(J^{(\beta)}\) é a fonte
térmica obtida do determinante de Matsubara/heat-kernel.

Como refinamento metrológico posterior, resta:

1. derivar os fatores sublíderes que deslocam
   \[
   \eta_{\rm lead}=(1.5,3.0)
   \]
   para
   \[
   \eta_{\rm req}\approx(1.471445,2.929056);
   \]
2. identificar se esses deslocamentos vêm da curvatura finita do espaço de
   Einstein, do tamanho finito do estômato, ou de \(S_\partial^{\rm GDQ}\);
3. verificar se a avaliação corrigida reproduz \(\Delta_\epsilon\approx2.37946518\times10^{-4}\) e \(\Delta_b\approx4.51750951\times10^{-2}\);
4. rodar uma varredura de sensibilidade para verificar unicidade local da solução térmica;
5. registrar erro e convergência do solver térmico para \(N=4000,8000,16000\);
6. manter claro que a aproximação líder já é preditiva em sinal e ordem de
   grandeza, e que a etapa sublíder é refinamento fino.

---

## 7. Critério de aceitação final

Q39 está aceita como concluída porque:

1. o espectro global reproduz a hierarquia leptônica;
2. o contorno físico foi identificado;
3. o deslocamento local foi explicado;
4. \(H\) e \(J^{(\beta)}\) foram avaliados com sinal fermiônico;
5. a resposta líder de Einstein fecha sinal e ordem de grandeza;
6. o erro residual foi isolado em \(\eta_{\rm req}\).

A classificação final é:

\[
\boxed{
\text{Q39 concluída; } \eta_{\rm req}\text{ fica como refinamento metrológico posterior.}
}
\]
