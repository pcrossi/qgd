# Q38 — Especificação do solver auditado

## 1. Objetivo

Este documento define como deve ser refeito o solver numérico de Q38 para que
ele teste a derivação da GDQ sem misturar fatores.

O solver atual V2 é útil como exploração, mas mistura:

1. Fano;
2. planificação;
3. condição de contorno;
4. imposição do meio-instantão.

O solver auditado deve separar esses elementos.

---

## 2. Variáveis que devem ficar separadas

### 2.1 Fano bulk

Usar:

\[
\chi_{\rm Fano}^{\rm bulk}
=
\frac{3\sqrt2}{5}.
\]

Não usar:

\[
0.4791
\]

como se fosse Fano fundamental, pois:

\[
0.4791
\approx
\frac{3\sqrt2/5}{\sqrt{\pi}}.
\]

### 2.2 Planificação

Introduzir:

\[
J_{\rm flat}.
\]

Testar separadamente:

1. \(J_{\rm flat}=1\);
2. \(J_{\rm flat}=\sqrt{\pi}\);
3. \(J_{\rm flat}\) calculado por média ponderada;
4. \(J_{\rm flat}\) calculado por norma do modo gravitacional.

### 2.3 Volume efetivo

Calcular:

\[
V_{\rm eff}^{\rm bulk}
=
\operatorname{Re}
\int_\gamma d\tau
\int_K
\eta_R e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y.
\]

No solver reduzido \(1D\), isso vira uma aproximação:

\[
V_{\rm eff}^{(1D)}
=
\int_{\epsilon}^{\pi-\epsilon}
e^{2A(\chi)}
e^{-f(\chi)}
\sin^2\chi\,d\chi
\times
N_{\rm int},
\]

onde \(N_{\rm int}\) deve representar a normalização dos setores internos
omitidos.

---

## 3. Fórmula de saída

O solver deve calcular primeiro:

\[
\Pi_{1,\rm bulk}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
V_{\rm eff}^{\rm bulk}.
\]

Depois:

\[
\Pi_{1,\rm obs}
=
\frac{\Pi_{1,\rm bulk}}{J_{\rm flat}}.
\]

Portanto:

\[
\boxed{
\Pi_{1,\rm obs}
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}J_{\rm flat}}
V_{\rm eff}^{\rm bulk}.
}
\]

Essa forma impede que \(J_{\rm flat}\) seja absorvido dentro de
\(\chi_{\rm Fano}\).

---

## 4. Condições de contorno a testar

O solver V2 dizia Neumann, mas implementava Dirichlet.

O solver auditado deve testar explicitamente:

### 4.1 Dirichlet instantônico

\[
f(\epsilon)=S_{\rm inst},
\qquad
f(\pi-\epsilon)=S_{\rm inst}.
\]

Interpretação:

\[
\text{a ação instantônica é fixada topologicamente nas bordas.}
\]

### 4.2 Neumann regular

\[
f'(\epsilon)=0,
\qquad
f'(\pi-\epsilon)=0.
\]

Interpretação:

\[
\text{não há fluxo térmico pela borda regular.}
\]

### 4.3 Robin térmico

\[
f'(\epsilon)+\lambda_\epsilon f(\epsilon)=j_\epsilon,
\]

\[
f'(\pi-\epsilon)-\lambda_\pi f(\pi-\epsilon)=j_\pi.
\]

Interpretação:

\[
\text{a borda possui impedância térmica/gravitacional.}
\]

A opção Robin é a mais compatível com a linguagem de Fano/impedância, mas ela
só pode ser usada como previsão se \(\lambda_\epsilon,\lambda_\pi\) vierem do
operador de contorno da GDQ.

---

## 5. Meio-instantão

O solver não deve simplesmente impor:

\[
S_{\rm inst}
=
\frac1{2\alpha}
\]

como número externo final.

Deve separar dois modos:

### Modo A — teste fenomenológico

Usar:

\[
S_{\rm inst}
=
\frac1{2\alpha}
\]

para verificar se a cadeia numérica reproduz a fórmula conhecida.

Classificação:

\[
\boxed{\text{teste de consistência, não prova.}}
\]

### Modo B — preditivo

Resolver a sela:

\[
\frac{\delta S_{\rm red}^{E}}{\delta f}=0
\]

com as condições de contorno escolhidas, e calcular:

\[
S_E[f_{\rm inst}]
=
\int d\chi\,\mathcal L_E[f_{\rm inst}].
\]

Critério:

\[
\boxed{
\frac{S_E[f_{\rm inst}]}{\hbar}
=
\frac1{2\alpha}
}
\]

deve sair da solução, não ser imposto.

---

## 6. Tabela mínima de saídas

O solver auditado deve produzir uma tabela com colunas:

1. condição de contorno;
2. \(\chi_{\rm Fano}^{\rm bulk}\);
3. \(J_{\rm flat}\);
4. \(S_{\rm inst}\) imposto ou derivado;
5. \(V_{\rm eff}^{\rm bulk}\);
6. \(\Pi_{1,\rm bulk}\);
7. \(\Pi_{1,\rm obs}\);
8. erro relativo contra o valor adimensional observado;
9. classificação: teste, hipótese, ou predição.

Valor observado usado apenas para comparação final:

\[
\Pi_{1,\rm obs}^{\rm exp}
=
\frac{GM_p^2}{\hbar c}.
\]

Se a forma metrológica por \(M_e\) for usada:

\[
\Pi_{e}^{\rm obs}
=
\frac{GM_e^2}{\hbar c}.
\]

---

## 7. Critério de fechamento de Q38

Q38 só fica fechada numericamente se o solver auditado demonstrar:

1. \(\eta_R\) fixo por convenção tensorial;
2. \(A(y,\tau)\) derivado do fundo térmico/cosmológico;
3. \(\chi_{\rm Fano}^{\rm bulk}\) derivado da impedância;
4. \(J_{\rm flat}\) derivado da projeção ou norma do modo;
5. \(S_{\rm inst}/\hbar=1/(2\alpha)\) obtido da sela;
6. \(V_{\rm eff}^{(G)}\) calculado sem usar \(G\) como entrada;
7. \(G\) comparado apenas no final.

Enquanto isso não ocorrer, o status correto permanece:

\[
\boxed{
\text{Q38 fechada estruturalmente; avaliação direta de }G\text{ em progresso.}
}
\]

---

## 8. Próxima implementação sugerida

Criar:

\[
\boxed{
\texttt{numerico/q38\_gravidade/solve\_gravity\_q38\_auditado.py}
}
\]

com quatro modos:

1. `dirichlet_fixed_instanton`;
2. `neumann_regular_fixed_instanton`;
3. `robin_impedance_fixed_instanton`;
4. `predictive_saddle`.

O quarto modo pode ser deixado inicialmente como pendente se a ação reduzida
euclidiana ainda não estiver completamente especificada.

---

## 9. Implementação executada

Implementado:

\[
\boxed{
\texttt{numerico/q38\_gravidade/solve\_gravity\_q38\_auditado.py}
}
\]

Saída gerada:

\[
\boxed{
\texttt{numerico/q38\_gravidade/saida\_gravity\_q38\_auditado.md}
}
\]

### Resultado principal

O solver auditado confirmou que:

\[
0.4791\approx\frac{3\sqrt2/5}{\sqrt{\pi}}.
\]

Portanto, o V2 não testava independentemente:

1. \(\chi_{\rm Fano}\);
2. \(J_{\rm flat}\).

Ele usava um Fano já dividido por \(\sqrt\pi\) e depois dividia novamente por
\(\sqrt\pi\), o que cancela a planificação e retorna ao cenário bulk.

### Tabela essencial

Com:

\[
\chi_{\rm Fano}^{\rm bulk}=\frac{3\sqrt2}{5},
\qquad
V_{\rm eff}=e^{-1/(2\alpha)},
\]

o solver obteve:

\[
\Pi_{1,\rm obs}
=
5.89039596\times10^{-39},
\]

contra:

\[
\Pi_{1}^{\rm exp}
=
5.90615307\times10^{-39}.
\]

Erro:

\[
\boxed{0.2668\%}
\]

quando não se aplica \(J_{\rm flat}\) como fator independente.

Ao aplicar:

\[
J_{\rm flat}=\sqrt\pi
\]

separadamente, o erro vai para:

\[
\boxed{43.7316\%}.
\]

### Consequência

O ajuste bom de Q38, no estado atual, vem da cadeia:

\[
\boxed{
\Pi_1
=
\frac{\alpha^4(1+\alpha)}
{\chi_{\rm Fano}^{\rm bulk}}
e^{-1/(2\alpha)}
}
\]

e não de uma planificação independente por \(\sqrt\pi\).

Logo, a planificação deve ser removida da fórmula principal até ser derivada
como norma/projeção de modo. Se ela for derivada, precisará alterar outro
fator de forma consistente, não ser multiplicada por fora.

### Contornos

Com a EDO reduzida de vácuo:

\[
f''+2\cot\chi\,f'=0,
\]

os contornos regulares sem fonte efetiva colapsam no mesmo perfil constante.
Portanto, esta versão do solver não testa uma dinâmica preditiva do dilaton.
Ela apenas audita normalizações globais.

---

## 10. Novo bloqueio real

Após a auditoria, o bloqueio de Q38 não é mais aritmético. O bloqueio real é:

1. derivar:

   \[
   S_{\rm inst}/\hbar=\frac1{2\alpha}
   \]

   como ação de sela da GDQ;

2. derivar:

   \[
   \chi_{\rm Fano}^{\rm bulk}=\frac{3\sqrt2}{5}
   \]

   como impedância de contorno;

3. decidir se existe ou não um \(J_{\rm flat}\) independente.

Se existir, ele não pode ser aplicado sem reavaliar a normalização completa de
\(\mathcal V_{\rm eff}^{(G)}\).

---

## 11. Derivação formal adicionada

Documento criado:

\[
\boxed{
\texttt{q38/derivacao\_inst\_fano\_planificacao.md}
}
\]

Resultado:

1. \(S_{\rm inst}/\hbar=1/(2\alpha)\) foi derivado como ação de uma sela
   relativa com carga topológica \(Q_{\rm rel}=1/2\);
2. \(\chi_{\rm Fano}^{\rm bulk}=3\sqrt2/5\) foi derivado como admitância de
   contorno entre \(N_H=3\) modos Hopf e \(N_T=5\) ciclos toroidais, com
   normalização RMS \(\sqrt2\);
3. \(J_{\rm flat}^{(0)}=1\) foi fixado para o modo gravitacional zero
   normalizado, pois o jacobiano estereográfico cancela entre medida e norma
   do modo.

Assim, \(J_{\rm flat}=\sqrt\pi\) fica rejeitado como fator universal externo
para Q38.
