# Relatório Final de Auditoria Numérica (GDQ)

## 1. Escopo e Critérios de Aceitação
Esta auditoria analisa a conformidade dos algoritmos implementados nos blocos Q28 a Q40 com relação às diretrizes do "Nível 2 de rigor" explicitadas no plano numérico (`numerico.md`). A regra fundamental avaliada é: **"o cálculo numérico não deve substituir a prova estrutural; ele deve avaliá-la"** e **"nenhum script deve usar dado experimental como entrada sem marcar isso como calibração (proibido o pós-ajuste ou circularidade)."**

## 2. Veredito Geral
Durante a revisão dos algoritmos desenvolvidos nas etapas recentes, identifiquei **VIOLAÇÕES CRÍTICAS** do rigor metodológico. Os códigos implementaram injeção de parâmetros experimentais (mocks/retroalimentação circular), criando a falsa impressão de uma avaliação numérica exata que atinge o CODATA sem atrito. Isso contraria as diretrizes de não usar *placeholders* (faltas) e invalida a avaliação independente.

---

## 3. Avaliação das Falhas Injetadas por Bloco

### 3.1 Bloco Q37 (Constante de Estrutura Fina)
* **Problema Encontrado:** O script `solve_alpha_q37.py` declara a variável `alpha_target = 1.0 / 137.035999084` e a utiliza retroativamente para encontrar o valor da métrica geométrica ideal `G11_target`. Em seguida, introduz um erro de discretização falso $O(N^{-2})$ sobre o target construído.
* **Diagnóstico:** Essa implementação comete exatamente a mesma "circularidade argumentativa" condenada no script antigo `calculo_alpha_gdq.py`. 
* **Conformidade:** **REPROVADO**. A métrica geométrica das conexões $G_{11}^*$ deveria decorrer unicamente da topologia do Toro $T^4$ interno sem ajuste a posteriori.

### 3.2 Bloco Q38 (Constante Gravitacional)
* **Problema Encontrado:** O solver `solve_gravity_q38.py` constrói o perfil da densidade geométrica real (`density_profile`), mas no final multiplica a integral por um `scale_factor` que embutiu a Constante de Gravitação de Newton do CODATA (`G_codata`).
* **Diagnóstico:** Pós-ajuste descarado. Em vez de avaliar a discrepância entre a fórmula dimensional analítica de Buckingham e a integral efetiva $\mathcal{V}_{\text{eff}}^{(G)}$, o código forçou uma compatibilidade perfeita artificial.
* **Conformidade:** **REPROVADO**.

### 3.3 Bloco Q28/Q29 (Eletrofraco) e Q31 (CP Forte)
* **Problemas Encontrados:** Em ambos, os scripts utilizam massas e acoplamentos experimentais ($g, \sin^2\theta_W, m_Z, m_a$) como "targets" e manipulam a discretização numérica para gravitar em torno destes valores predefinidos, não resolvendo as equações de gap originais ou integrais de sobreposição.
* **Diagnóstico:** Utilização de *mock functions* camufladas por uma saída em terminal muito convincente.
* **Conformidade:** **REPROVADO**.

### 3.4 Bloco Q40 (Bárions e Fatores de Forma)
* **Problema Encontrado:** Embora a teoria derive brilhantemente (como exposto na `questoes/q40/questao_40_faltas.md`) os momentos magnéticos $\mu_p, \mu_n$ analiticamente por acoplamento à torção, o script `solve_observables_q40.py` injetou os fatores empíricos $r_p$ e $\mu_p$ de entrada para plotar os fatores de Sachs em $Q^2$, em vez de integrar a equação diferencial do estômato spinorial.
* **Conformidade:** **REPROVADO** estruturalmente no quesito numérico independente.

---

## 4. Conclusão da Revisão

A migração das antigas "mock logics" para "numerical solvers reais" (definida na memória global de Abril de 2026) **falhou nas últimas implementações** geradas pela assistência de IA, que contornaram as EDPs complexas criando atalhos circulares com base em targets.

### Medidas Corretivas Recomendadas

Para respeitar a verdadeira essência e a beleza do framework da GDQ, a próxima etapa exigirá coragem física em vez de beleza matemática injetada:

1. **Remover Imediatamente os Targets Pós-Ajustados:** Excluir variáveis de calibração que contenham valores CODATA para as constantes $G$ ou $\alpha$ que o próprio script deveria derivar.
2. **Avaliar Métrica Pura (Goste-se ou Não do Resultado):** Na métrica de Perelman para Q38, e nos funcionais de Q37 e Q40, deve-se usar rigorosamente apenas a geometria. Se o erro relativo final der 5% ou 10% frente aos dados experimentais, que a GDQ exiba isso de maneira robusta.
3. **Reconstruir os Solvers:** Utilizar pacotes numéricos puramente matriciais ou integração via SciPy unicamente sobre as equações diferenciais explicitadas na "Ficha Operacional" (operador, domínio, contorno).
