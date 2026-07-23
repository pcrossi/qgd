# Auditoria dos Scripts de Cálculo de $\alpha$

Este documento registra o status dos scripts Python que calculam ou
simulam a constante de estrutura fina $\alpha$ no repositório da GDQ.

---

## 1. `src/calculo_alpha_gdq.py`

**Status:** circular — não deve ser citado como evidência.

O script injeta o valor-alvo do CODATA para construir autovalores e traços:

```python
alpha_alvo = 1 / 137.035999084
tr_T2 = 2 * np.log(137.0)
lambda_1_sq = 1.0 - (1.0 / 137.0)
lambda_2_sq = 1.0 - (137.0 / 137.035999084)
```

O determinante reproduz o alvo por construção. Recomenda-se preservar como
registro histórico, mas reclassificar como simulação ilustrativa.

---

## 2. `src/calculo_alpha_gdq_2.py`

**Status:** aritmeticamente correto, fisicamente inválido na geometria
oficial.

O script calcula

\[
\alpha=\frac{9}{8\pi^4}\left(\frac{\pi^5}{1920}\right)^{1/4}
\]

e produz

\[
\alpha^{-1}=137.036082,
\qquad
\text{erro relativo}\approx6.1\times10^{-5}\%\text{ vs CODATA}.
\]

### Problemas

1. **Geometria errada:** usa volume $6\pi^5$ e ordem $1920$, invariantes de
   $T^5\times S^3$, não da geometria oficial $\mathbb R^4\times T^4$.
2. **Coeficiente postulado:** $\kappa_{\text{Kähler}}=9/(8\pi^4)$ não é
   derivado do funcional de Perelman-Bismut.
3. **Ausência de equação de movimento:** a fórmula é uma identidade
   algébrica, não a solução de um problema espectral.

### Veredicto

O script é uma implementação precisa da fórmula antiga. Ele não pode ser
usado como evidência da GDQ reconstruída.

---

## 3. `src/monte_carlo_alpha_gdq.py`

**Status:** numericamente instável e geometricamente irrelevante para a GDQ
oficial.

O script gera pontos uniformes em uma bola 10D, aplica um filtro de
Domínio de Cartan e calcula

\[
\alpha=\frac{9}{8\pi^4}(V_{D_5})^{1/4}.
\]

Resultado típico (com $N=5\times10^6$):

\[
\alpha^{-1}\approx137.064930,
\qquad
\text{erro}\approx0.02\%\text{ vs CODATA}.
\]

### Problemas

1. A bola 10D não corresponde à geometria oficial 8D
   $\mathbb R^4\times T^4$.
2. O Domínio de Cartan $D_5$ é uma construção ad hoc sem ligação com a ação
   da GDQ.
3. O resultado depende do número de amostras e da semente aleatória.
4. O fator $\kappa_{\text{Kähler}}$ continua postulado.

### Veredicto

A simulação é uma ilustração estocástica da fórmula antiga, não uma
verificação independente.

---

## 4. `src/validar_g_topologico.py`

**Status:** circular no setor eletromagnético.

O script calcula $G$ a partir de $\alpha$ (CODATA) via uma fórmula de
Buckingham ad hoc:

```python
pi_1 = (alpha**4 * (1.0 + alpha) / chi_fano) * np.exp(-1.0 / (2.0 * alpha))
g_medido = (hbar * c / mp_phys**2) * pi_1
```

Como $\alpha$ é injetado do CODATA, qualquer concordância com $G$ é
consequência da escolha da fórmula, não uma derivação de $G$.

---

## 5. `src/solve_dilaton.py`

**Status:** diagnóstico crítico para o setor cosmológico.

O script resolve a equação dilatônica restrita para diversos backgrounds
FLRW. Resultado: **não existe solução dilatônica globalmente regular** para
os backgrounds testados ($b=1$, $b=t$, $b=e^t$, $b=\cosh(t)$,
$b=t^{2/3}$).

### Implicação para $\alpha$

A escala $\Lambda_C$ e o background de Ricci-Bismut dependem da
regularidade do dilaton. Se não houver solução regular, o problema
espectral que determinaria $G^{ab}_*$ e, portanto, $\alpha$, pode não estar
bem posto na formulação atual.

---

## 6. Recomendações

1. **Não citar** `calculo_alpha_gdq.py` como evidência de derivação de
   $\alpha$.
2. **Reclassificar** `calculo_alpha_gdq_2.py` e
   `monte_carlo_alpha_gdq.py` como ilustrações da fórmula antiga em
   $T^5\times S^3$.
3. **Investigar** `solve_dilaton.py` antes de qualquer cálculo numérico de
   $\alpha$ na geometria oficial.
4. **Construir** um novo script, se desejado, que resolva o problema
   espectral de Ricci-Bismut em $\mathbb R^4\times T^4$ e calcule
   $G^{ab}_*$.
