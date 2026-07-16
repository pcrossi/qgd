# Q38 — Início da avaliação direta de \(\mathcal V_{\rm eff}^{(G)}\)

## 1. Objetivo

Este documento inicia a etapa pendente da Questão 38:

\[
\boxed{
\text{avaliar diretamente }\mathcal V_{\rm eff}^{(G)}
\text{ a partir da ação oficial da GDQ.}
}
\]

A Questão 38 já está fechada estruturalmente no seguinte sentido:

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\mathcal V_{\rm eff}^{(G)},
\qquad
G
=
\frac{c^4\Lambda_C^2}
{16\pi\hbar\,\mathcal V_{\rm eff}^{(G)}}.
\]

O que falta é transformar a integral formal em avaliação geométrica controlada,
sem pós-ajuste:

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

---

## 2. Ponto de partida: termo de curvatura da ação

O termo relevante da ação oficial é:

\[
\mathcal S_{\mathcal R}
=
\frac{\hbar}{\Lambda_C^2}
\int_\gamma d\tau
\int_{\mathcal M_{\mathbb C}}
\mathcal R\,
\mathcal U
\sqrt{\det g}\,
d^{2n}z.
\]

Na decomposição local:

\[
\mathcal M_{\mathbb C}\simeq N\times K,
\]

com \(N\) a fatia física \(4D\) e \(K\) o setor interno, escrevemos o bloco
externo como:

\[
ds^2_{\rm ext}
=
e^{2A(y,\tau)}
h_{\mu\nu}(x)dx^\mu dx^\nu.
\]

A parte da curvatura que multiplica \(R[h]\) é:

\[
\mathcal R[g]
\supset
\eta_R e^{-2A(y,\tau)}R[h].
\]

A medida externa fornece:

\[
\sqrt{\det g}
\supset
e^{4A(y,\tau)}
\sqrt{-h}\sqrt{q_*}.
\]

Logo, o coeficiente do termo Einstein--Hilbert efetivo é:

\[
C_R
=
\frac{\hbar}{\Lambda_C^2}
\operatorname{Re}
\left[
\int_\gamma d\tau
\int_K
\eta_R e^{2A}
\mathcal U_*
\sqrt{q_*}\,d^4y
\right].
\]

Isso fixa o objeto a calcular.

---

## 3. Normalização de \(\eta_R\)

A primeira pendência é a normalização entre:

1. a curvatura Kähler--Ricci \(\mathcal R\) usada na ação complexa;
2. a curvatura real \(R[h]\) usada no termo Einstein--Hilbert.

Definição operacional:

\[
\boxed{
\eta_R
=
\frac{
\text{coeficiente de }R[h]\text{ na projeção real de }\mathcal R[g]
}{
R[h]
}.
}
\]

Casos possíveis:

1. se a convenção complexa já projeta exatamente para \(R[h]\), então:

   \[
   \eta_R=1;
   \]

2. se a contração Kähler usa metade da curvatura real, então:

   \[
   \eta_R=2;
   \]

3. se a projeção real inclui orientação, duplicação holomorfa ou fator de
   volume da fibra, \(\eta_R\) deve ser extraído da expansão de segunda ordem
   da métrica, não escolhido depois.

Critério de fechamento:

\[
\boxed{
\eta_R\text{ deve ser obtido por projeção tensorial, não por ajuste numérico de }G.
}
\]

---

## 4. Temperatura do espaço de Einstein versus limite plano

O ponto físico importante é:

\[
\boxed{
T^5\times S^3\text{ não é apenas uma escolha de coordenadas; é o fundo cosmológico térmico.}
}
\]

O espaço plano \(T^4\times \mathbb R^4\) deve ser tratado apenas como limite
observacional/local. Ele não contém a temperatura global do espaço de
Einstein e, portanto, não deve ser usado para determinar o valor real de
\(\mathcal V_{\rm eff}^{(G)}\).

Consequência:

1. a avaliação fundamental de \(\mathcal V_{\rm eff}^{(G)}\) deve ser feita
   no fundo cosmológico curvo;
2. a aproximação plana entra depois como mapa de leitura local;
3. o fator chamado nos scripts de “planificação estereográfica” precisa ser
   derivado como projeção entre:

   \[
   T^5\times S^3
   \longrightarrow
   \text{limite local quase plano}.
   \]

Portanto, o erro residual de \(0,34\%\) nos scripts Q38 não deve ser lido
como falha ou sucesso final. Ele indica que a ponte cosmologia--laboratório
está quase correta, mas ainda não está derivada variacionalmente.

---

## 5. Como os fatores fenomenológicos devem emergir

O Apêndice 2 usa:

\[
\Pi_1
=
\frac{GM_p^2}{\hbar c}
=
\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)}.
\]

Após a extração de \(C_R\), essa fórmula deve ser reinterpretada como avaliação
adimensional de \(\mathcal V_{\rm eff}^{(G)}\).

Como:

\[
G
\propto
\frac{1}{\mathcal V_{\rm eff}^{(G)}},
\]

os fatores acima exigem que:

\[
\mathcal V_{\rm eff}^{(G)}
\propto
\frac{\chi_{\rm Fano}}
{\alpha^4(1+\alpha)}
e^{1/(2\alpha)}
\times
\text{fator metrológico}.
\]

Assim, cada fator tem uma tarefa:

### 5.1 Origem de \(\alpha^{-4}\)

Deve vir da medida interna efetiva:

\[
\mathcal U_*\sqrt{q_*}\,d^4y,
\]

ou do determinante reduzido da forma Kähler no setor interno.

Hipótese a testar:

\[
\frac12\Omega\wedge\Omega
\quad\Rightarrow\quad
\alpha^4
\text{ no acoplamento,}
\]

logo:

\[
\alpha^{-4}
\text{ em }\mathcal V_{\rm eff}^{(G)}.
\]

O teste correto é expandir \(\Omega\) no fundo estacionário e verificar se a
quarta potência aparece no determinante, sem escolher a potência manualmente.

### 5.2 Origem de \(e^{1/(2\alpha)}\)

Deve vir do peso do setor instantônico na integral interna:

\[
\mathcal U_*\sqrt{q_*}
\sim
e^{S_{\rm inst}/\hbar},
\qquad
\frac{S_{\rm inst}}{\hbar}
=
\frac{1}{2\alpha}.
\]

No acoplamento \(G\), esse fator aparece invertido:

\[
G\sim e^{-1/(2\alpha)}.
\]

Pendência precisa:

\[
\boxed{
\text{exibir a solução de meio-instantão e calcular sua ação euclidiana.}
}
\]

### 5.3 Origem de \(\chi_{\rm Fano}\)

O fator:

\[
\chi_{\rm Fano}
=
\frac{3\sqrt2}{5}
\]

deve aparecer como impedância/admitância de contorno dentro da própria
integral:

\[
\int_K
\eta_R e^{2A}\mathcal U_*\sqrt{q_*}.
\]

Interpretação compatível:

1. \(\chi_{\rm Fano}\) mede a mistura entre canal discreto solitônico e canal
   contínuo externo;
2. na integral de \(C_R\), isso aparece como fator de transmissão do modo de
   curvatura \(R[h]\) através da fronteira do estômato;
3. a demonstração deve vir por complemento de Schur/impedância:

   \[
   Z_{\rm eff}
   =
   Z_0
   -
   J^\dagger K^{-1}J.
   \]

Critério:

\[
\boxed{
\chi_{\rm Fano}\text{ precisa sair do operador de contorno, não de comparação numérica.}
}
\]

---

## 6. Programa mínimo de cálculo

Para fechar Q38 numericamente sem circularidade:

1. escolher o background estacionário \(g_*,f_*\) no espaço de Einstein
   \(T^5\times S^3\);
2. calcular \(\eta_R\) por projeção tensorial;
3. calcular o warp \(A(y,\tau)\) do setor gravitacional;
4. montar:

   \[
   I_G(y,\tau)
   =
   \eta_R e^{2A(y,\tau)}
   \mathcal U_*(y,\tau)
   \sqrt{q_*(y,\tau)};
   \]

5. integrar:

   \[
   \mathcal V_{\rm eff}^{(G)}
   =
   \operatorname{Re}
   \int_\gamma d\tau\int_K I_G(y,\tau)d^4y;
   \]

6. obter:

   \[
   G_{\rm GDQ}
   =
   \frac{c^4\Lambda_C^2}
   {16\pi\hbar\mathcal V_{\rm eff}^{(G)}};
   \]

7. somente depois comparar:

   \[
   \frac{G_{\rm GDQ}M_p^2}{\hbar c}
   \quad
   \text{ou}
   \quad
   \frac{G_{\rm GDQ}M_e^2}{\hbar c}.
   \]

---

## 7. Status dos scripts existentes

### `solve_gravity_q38.py`

Classificação:

\[
\boxed{\text{teste negativo útil.}}
\]

Ele mostra que um ansatz simples, como \(f(y)=e^{-y}\sin^5y\), não representa
o verdadeiro vácuo gravitacional da GDQ.

### `solve_gravity_q38_v2.py`

Classificação:

\[
\boxed{\text{hipótese efetiva promissora.}}
\]

Ele encontra estabilidade numérica e erro de aproximadamente \(0,34\%\), mas
usa uma etapa interpretativa de planificação/projeção que ainda precisa ser
derivada do mapa:

\[
T^5\times S^3
\rightarrow
\text{observador local quase plano}.
\]

Portanto, o V2 deve guiar a derivação, não substituí-la.

---

## 8. Próximo passo concreto

O próximo arquivo técnico deve calcular \(\eta_R\):

\[
\boxed{
\texttt{q38/normalizacao\_eta\_R.md}
}
\]

Tarefa:

1. escrever a decomposição tensorial da métrica complexa;
2. projetar \(\mathcal R[g]\) sobre \(R[h]\);
3. determinar se \(\eta_R=1\), \(2\), ou outro fator fixo;
4. registrar que o valor não pode ser escolhido para ajustar \(G\).

Continuação criada:

\[
\boxed{
\texttt{q38/warp\_termico\_einstein.md}
}
\]

Esse arquivo registra que \(T^5\times S^3\) é o fundo cosmológico térmico da
avaliação de \(\mathcal V_{\rm eff}^{(G)}\), enquanto o espaço plano é apenas
o limite observacional/local.
