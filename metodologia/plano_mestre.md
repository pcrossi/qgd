# Plano mestre — metodologia reutilizável GDQ

## 1. Objetivo

Construir um protocolo único para resolver problemas físicos na GDQ usando a
ação oficial, backgrounds, fontes clássicas, projetores, Hessianas,
multiplicadores, DtN/Schur e observáveis.

O método deve ser reaproveitável em:

1. Stern--Gerlach;
2. Zeeman e $g-2$;
3. dupla fenda e decoerência;
4. espalhamento;
5. fatores de forma;
6. confinamento;
7. poços, barreiras e ressonâncias;
8. interação clássico--quântico;
9. calibrações de aparelho;
10. testes de correspondência.

---

## 2. Pipeline universal

O pipeline é:

$$
\mathcal S_{\rm GDQ}
\to
\Phi_*
\to
C_a[\Phi]=0
\to
P_{\rm phys}
\to
K_{\rm phys}
\to
J_{\rm app}
\to
\delta\Phi
\to
\mathsf R_{\rm app}
\to
\mathcal O_{\rm obs}.
$$

Com:

$$
K_{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

E:

$$
\delta\Phi
=
K_{\rm phys}^{-1}J_{\rm app}.
$$

Quando houver graus internos de aparelho ou bulk não observados:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

---

## 3. Módulo A — Background

### 3.1 Entradas

Definir:

1. espaço usado;
2. domínio;
3. campo estacionário $\Phi_*=(g_*,J_*,H_*,f_*,\mathcal U_*)$;
4. contornos;
5. topologia;
6. setor de carga;
7. simetrias preservadas;
8. simetrias quebradas pela fonte.

### 3.2 Saída mínima

Um background só pode ser usado se houver:

$$
\delta\mathcal S_{\rm GDQ}[\Phi_*]=0
$$

ou uma justificativa explícita de que se trata de background efetivo/condicional.

### 3.3 Classificação

Cada background deve ser classificado como:

1. solução derivada;
2. solução condicional;
3. fundo efetivo;
4. fixture numérico;
5. ansatz exploratório.

---

## 4. Módulo B — Vínculos e multiplicadores

### 4.1 Tipos de vínculo

Registrar:

1. carga;
2. fluxo;
3. normalização;
4. fase/circulação;
5. Noether;
6. contorno;
7. calibre;
8. regularidade;
9. topologia.

### 4.2 Forma geral

Usar:

$$
\mathcal S_{\rm aug}
=
\mathcal S_{\rm GDQ}
+\sum_a \lambda_a C_a[\Phi].
$$

Os multiplicadores $\lambda_a$ não são novos campos fundamentais. Eles impõem
dados do setor, do aparelho ou do contorno.

### 4.3 Saída mínima

Listar:

$$
C_a[\Phi]=0,
\qquad
\lambda_a,
\qquad
\delta C_a,
\qquad
\delta^2 C_a.
$$

---

## 5. Módulo C — Projetor físico

### 5.1 Objetivo

Remover:

1. difeomorfismos puros;
2. modos de gauge;
3. modos nulos de simetria;
4. variações incompatíveis com vínculos;
5. perturbações fora do domínio.

### 5.2 Forma

O projetor físico é:

$$
P_{\rm phys}
=
I
-G(G^\dagger G)^{-1}G^\dagger
-C^\dagger(CC^\dagger)^{-1}C
$$

quando a decomposição linear for regular.

Aqui:

- $G$ gera modos de gauge;
- $C$ lineariza os vínculos.

### 5.3 Saída mínima

Verificar:

$$
P_{\rm phys}^2=P_{\rm phys},
\qquad
P_{\rm phys}^\dagger=P_{\rm phys},
\qquad
CP_{\rm phys}=0.
$$

---

## 6. Módulo D — Hessiana física

### 6.1 Definição

Calcular:

$$
K
=
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm aug}.
$$

Depois projetar:

$$
K_{\rm phys}
=
P_{\rm phys}KP_{\rm phys}.
$$

### 6.2 Domínio

Declarar:

1. espaço funcional;
2. regularidade;
3. condições de bordo;
4. produto interno;
5. medida;
6. auto-adjunticidade;
7. gap ou tratamento de modos zero.

### 6.3 Saída mínima

Listar:

$$
K_{\rm phys},
\qquad
\operatorname{Dom}(K_{\rm phys}),
\qquad
\Delta_{\rm gap},
\qquad
\ker K_{\rm phys}.
$$

---

## 7. Módulo E — Fonte clássica ou contorno do aparelho

### 7.1 Princípio

Aparelhos entram como fontes, vínculos ou contornos clássicos:

$$
J_{\rm app}^{\rm clássico}.
$$

Eles não substituem a ação oficial.

### 7.2 Tipos de fonte

1. campo magnético;
2. gradiente de campo;
3. barreira;
4. detector;
5. sonda eletromagnética;
6. loop de Wilson efetivo;
7. potencial externo;
8. condição térmica;
9. condição de regularidade.

### 7.3 Resposta

Calcular:

$$
\delta\Phi_{\rm app}
=
K_{\rm phys}^{-1}J_{\rm app}.
$$

Se houver modos internos do aparelho:

$$
\mathsf R_{\rm app}
=
K_{\partial\partial}
-K_{\partial I}K_{II}^{-1}K_{I\partial}.
$$

---

## 8. Módulo F — Observável

### 8.1 Regra

O observável deve ser extraído de:

1. fluxo conservado;
2. carga de Noether;
3. forma quadrática de resposta;
4. autovalor;
5. fase/resíduo;
6. razão adimensional;
7. integral de superfície;
8. visibilidade/contraste;
9. seção eficaz;
10. fator de forma.

### 8.2 Forma genérica

Resposta linear:

$$
\mathcal O^{(1)}
=
\langle W,\delta\Phi\rangle.
$$

Resposta quadrática:

$$
\mathcal O^{(2)}
=
\langle J,K_{\rm phys}^{-1}J\rangle.
$$

Impedância:

$$
\mathcal O_{\rm DtN}
=
\langle \phi_\partial,\mathsf R_{\rm app}\phi_\partial\rangle.
$$

---

## 9. Módulo G — Numérico

### 9.1 Script mínimo

Todo script deve declarar:

1. equação;
2. domínio;
3. contorno;
4. parâmetros universais;
5. parâmetros de aparelho;
6. operador;
7. observável;
8. classificação do resultado.

### 9.2 Saídas mínimas

Salvar:

1. `.md` com resumo;
2. `.csv` ou `.npz` com dados;
3. parâmetros congelados;
4. tabela de convergência;
5. erro ou sensibilidade;
6. veredito conservador.

### 9.3 Validação

Exigir pelo menos uma destas:

1. limite analítico;
2. refinamento de malha;
3. simetria conservada;
4. positividade;
5. monotonicidade;
6. comparação com caso sem fonte;
7. comparação com resultado experimental.

---

## 10. Módulo H — Status final

Classificar o resultado como:

1. fechado;
2. fechado estruturalmente;
3. fechado condicionalmente;
4. parcialmente resolvido;
5. aberto;
6. programa futuro.

Para fechar, registrar:

1. hipótese;
2. domínio;
3. derivação;
4. cálculo;
5. teste;
6. limitação;
7. arquivo canônico;
8. atualização de `memory.md` quando material.

---

## 11. Aplicações imediatas

| Questão | Background | Fonte/contorno | Operador | Observável |
|---|---|---|---|---|
| Q42 | spin/Hopf | gradiente SG | DtN de interface | canais $\pm$ |
| Q43 | background leptônico | campo magnético | Hessiana magnética | $g$, $g-2$ |
| Q44 | Madelung/fendas | detector | DtN/Schur | visibilidade |
| Q40 | bárion | sonda EM | Hessiana de superfície | fatores de forma |
| Q30 | setor cor | loop/contorno | conexão efetiva | lei de área |
| Q25 | benchmark fermiônico | ensemble/aparelho | Schur térmico | correlação |

---

## 12. Ordem de expansão da pasta

1. Criar templates simbólicos.
2. Criar templates numéricos.
3. Mapear Q40--Q44 para o pipeline.
4. Criar checklists.
5. Converter scripts existentes para o padrão.
6. Criar biblioteca comum opcional.
7. Atualizar `memory.md` com a metodologia como decisão arquitetural.
