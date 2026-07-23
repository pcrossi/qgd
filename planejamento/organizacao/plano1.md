# Plano de Implementação: Refutação Integral da Auditoria da GDQ

Este documento estabelece o roteiro de guerra para resolver, derivar e refutar rigorosamente **todas** as objeções levantadas pelo `RELATORIO_AUDITORIA_COMPLETA_GDQ`. O objetivo não é responder com argumentos retóricos, mas sim com **matemática estrita, sem circularidade e sem pular etapas**.

A estratégia será dividida em 5 Fases Sequenciais. Nenhuma fase posterior será iniciada até que a fase atual esteja matematicamente blindada.

---

## FASE 1: A Fundação Axiomática (A "Prioridade 1" Expandida)
**Objetivo:** Eliminar as críticas 3.1, 3.2, 3.5 e 3.6 (Dimensionalidade, Kähler vs Bismut, Assinatura).

1. **Definição da Variedade Base e Dimensão:**
   - **Ação:** Fixar definitivamente se a teoria opera em dimensão real $8$ (Complexa $4$) ou $10$ (Bola Real). 
   - **Solução:** Vamos provar matematicamente a seleção de $n=4$ usando cancelamento de anomalias, não por leis de potência empíricas.
2. **Geometria de Bismut-Cartan-Kähler:**
   - **Ação:** Definir inequivocamente a conexão. Se a variedade tem torção não nula, ela **não pode** usar a conexão de Levi-Civita pura de Kähler. 
   - **Solução:** Construiremos a GDQ sobre uma **Variedade Hermitiana com Conexão de Bismut**, provando como a 3-forma de torção $H$ atua fisicamente como a fase de Madelung.
3. **Continuação Analítica e Assinatura:**
   - **Ação:** Refutar a crítica de que a métrica Riemanniana de Perelman não gera o espaço Lorentziano.
   - **Solução:** Implementar a rotação de Wick rigorosa e usar o teorema de Osterwalder-Schrader para provar que a evolução temporal difusiva $\tau$ mapeia perfeitamente no tempo físico $t$ preservando a causalidade (Crítica 3.5).

---

## FASE 2: O Teorema Perelman-Madelung e a Ação Unificada
**Objetivo:** Eliminar as críticas 3.3 e 3.4 (Mapeamento não provado e Equações não derivadas da Ação).

1. **Prova Formal do Mapeamento Perelman-Madelung:**
   - **Ação:** Parar de usar as relações $\rho = e^{-f}$ e $\rho = e^{S_I/\hbar}$ de forma intercambiável sem prova.
   - **Solução:** Escrever o Teorema de Representação que liga o funcional global $W$ de Perelman à densidade local conjugada de probabilidade.
2. **Cálculo Variacional Integral do Capítulo 4:**
   - **Ação:** A crítica 3.4 aponta que nossa Ação não gera a equação de continuidade correta nem a de Hamilton-Jacobi sem truques.
   - **Solução:** Recalcular as equações de Euler-Lagrange do zero, incluindo:
     - Termos de bordo.
     - Vínculos e Multiplicadores de Lagrange (para a incompressibilidade).
     - Variação exata da medida.

---

## FASE 3: Eliminação da Circularidade Numérica (Scripts e Constantes)
**Objetivo:** Refutar as críticas 3.8, 3.9 e 7 (Ajuste retrospectivo e Numerologia).

1. **Cálculo de $\alpha$ e $G$ sem "Alvos":**
   - **Ação:** Os scripts atuais (`calculo_alpha_gdq.py`) forçam a resposta a bater com $137.03599$. 
   - **Solução:** Criar um operador espectral (um Laplaciano sobre a variedade definida na Fase 1) e calcular seu autovalor fundamental numericamente usando métodos de elementos finitos ou Monte Carlo não viciado. Se o número derivado for $\sim 137$, a prova é absoluta.
2. **Massas das Partículas (Hierarquia e Taxonomia):**
   - **Ação:** Abandonar o uso de massas empíricas (diferença nêutron-próton) para calcular o elétron. Abandonar a fórmula de Koide injetada à força.
   - **Solução:** Modelar o elétron, múon e tau como modos de vibração topológicos puros (solítons de Ricci 3D). Resolver a equação de autovalores para suas massas. 

---

## FASE 4: Construção do Modelo Padrão e Spin
**Objetivo:** Eliminar as críticas das seções 4 (Capítulos 09, 14, 25, 27).

1. **Derivação Rigorosa do Spin 1/2:**
   - **Ação:** Provar que a "circulação inteira" gera de fato a representação espinorial de $Spin(3,1)$.
   - **Solução:** Construir espinores, a Álgebra de Clifford associada à variedade hermitiana da GDQ, e recuperar a Equação de Dirac como um limite do fluxo geométrico.
2. **Confinamento e Gap de Massa (Yang-Mills):**
   - **Ação:** A crítica diz que assumir densidade constante torna $V = \sigma r$ uma tautologia.
   - **Solução:** Formular o campo de calibre não-abeliano rigorosamente. Provar matematicamente que o gap de massa surge da geometria do fluxo sem impor área transversal finita *a priori*.

---

## FASE 5: A Defesa Final (Navier-Stokes e Previsão Falsificável)
**Objetivo:** Refutar o Apêndice 12 (Crítica 5) e fornecer o critério de falsificação (Crítica 10).

1. **A Resolução Real de Navier-Stokes:**
   - **Ação:** A auditoria destruiu nossa prova mostrando que usamos a Desigualdade de Grönwall circularmente (assumindo limite de vorticidade para provar limite de vorticidade).
   - **Solução:** Derivar uma "estimativa a priori" para a componente solenoidal que seja **independente de $\epsilon$** sem usar a suposição de vorticidade limitada. Usaremos estimativas dispersivas estritas de Strichartz em variedades de Bismut.
2. **O Critério de Falsificabilidade:**
   - **Ação:** Publicar uma previsão cega.
   - **Solução:** Usar a GDQ fechada para prever o valor de um desvio espectroscópico (ex: Raio do Próton Muônico, ou uma fase CP da matriz PMNS) que ainda não tenha sido fixado ou que discorde sutilmente do Modelo Padrão, mas que seja testável em colisores na próxima década.

---

## Regras de Engajamento para a IA (O Novo Padrão)
A partir de agora, em cada sessão de trabalho:
1. **Nenhum valor experimental** será inserido nas equações para "fazer bater".
2. **Toda afirmação "prova-se que"** deve ser seguida pela matemática explícita, linha por linha.
3. Se o formalismo não produzir o resultado esperado da física clássica/quântica, nós **alteraremos a geometria base da teoria**, e não daremos um "jeitinho" na matemática.
