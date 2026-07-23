Compreendido. A correção de `ex1.md` está irretocável e impõe o rigor metodológico e a sobriedade indispensáveis à física teórica. Remover o excesso de entusiasmo e a linguagem superlativa não é um preciosismo, mas uma defesa contra o autoengano no desenvolvimento teórico.

Aqui está o inventário de **"O que já temos"**, reajustado estritamente sob os critérios realistas e científicos impostos pela crítica:

---

### O Estado Atual do Projeto GDQ (Inventário Realista)

**Resumo Executivo:**
> Atualmente existe um repositório extenso de hipóteses, analogias, reproduções de resultados conhecidos e propostas fenomenológicas. Ainda não existe uma formulação mínima validada da GDQ. O próximo passo é congelar uma versão candidata dos axiomas e verificar se dela pode ser derivada uma ação consistente.

#### 1. Candidatos Geométricos e Ação (Fases 1 e 2)
* **O que temos:** Uma *proposta candidata* de geometria (variedade hermitiana com conexão de Bismut e torção) e uma *proposta candidata* de ação baseada no funcional de Perelman estendido (Capítulo 4).
* **Limitação:** A ação proposta no Capítulo 4 falha em derivar, de forma fechada, as equações declaradas. A escolha da geometria ainda está sujeita a testes de consistência. Não temos a ação mínima validada.

#### 2. O Mapeamento Perelman–Madelung (Fase 3)
* **O que temos:** Uma exploração conceitual que conecta o fluxo geométrico de Ricci à informação de Fisher e às equações de Madelung/Bohm.
* **Limitação:** Esta conexão possui antecedentes na literatura que precisam ser devidamente mapeados para delimitar a real originalidade da GDQ. Além disso, o teste do mapeamento não precisa resultar em bijeção; o desenvolvimento rigoroso poderá revelar que existe apenas correspondência parcial ou até incompatibilidade.

#### 3. Os Scripts e Simulações (Fase 0)
Temos códigos que demonstram consistência lógica de matrizes ou visualizam hipóteses, mas cada um tem limitações específicas que os desqualificam, no estado atual, como "provas":
* `calculo_alpha_gdq.py`: Injeta explicitamente o alvo (137.03599) na construção.
* `calculo_alpha_gdq_2.py`: Não injeta o alvo diretamente, mas seleciona fatores geométricos cuja necessidade não foi derivada da teoria.
* `monte_carlo_alpha_gdq.py`: Verifica apenas uma razão volumétrica esperada do domínio programado, não a constante $\alpha$ propriamente dita.
* **Simulação da Dupla Fenda:** É uma visualização de superposição de pacotes gaussianos com amortecimento assumido, e não uma simulação completa das equações diferenciais acopladas da GDQ.

#### 4. O Repositório Fenomenológico (Extensões)
* **O que temos:** Um volume massivo de material distribuído (spin, matriz PMNS, espalhamento Klein-Nishina, cosmologia, anomalias, etc.) que propõe modelos geométricos para problemas da física de partículas e relatividade.
* **Limitação:** Todo este corpus deve ser rebaixado, neste momento, à categoria de "repositório amplo de hipóteses fenomenológicas". Eles dependem de uma base que ainda será construída e validada.

---

### Próximo Passo Operacional

Concordo integralmente com a restrição: o trabalho imediato é criar `01_axiomas.md` **sem preencher lacunas com escolhas silenciosas**. Tudo o que for inserido no documento deve ser rotulado estritamente como "Definição" ou "Axioma", sem assumir que "já provamos que funciona".

Quer dar início à redação do documento `01_axiomas.md`, focando exclusivamente em listar a variedade candidata, a conexão candidata e os campos fundamentais, para testarmos se podemos derivar uma ação consistente disso?