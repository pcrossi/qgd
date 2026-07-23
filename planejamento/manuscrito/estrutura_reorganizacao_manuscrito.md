# Estrutura recomendada para reorganização do manuscrito GDQ

## 1. Princípio editorial

O manuscrito principal não deve ser organizado como uma sequência de perguntas.
Ele deve ser organizado como uma teoria positiva:

1. hipóteses;
2. ação;
3. variáveis fundamentais;
4. reduções;
5. teoremas;
6. consequências;
7. previsões;
8. testes.

As perguntas trabalhadas nos arquivos `questão_X.md` devem funcionar como
auditoria interna e material de defesa, não como esqueleto direto do texto
principal.

A estrutura recomendada é:

```text
manuscrito principal = teoria positiva
apêndices técnicos = provas longas e cálculos
FAQ teórica = respostas a objeções
questões_X.md = auditoria interna/rastreabilidade
```

---

## 2. Camadas documentais

### 2.1 Manuscrito principal

Função: apresentar a GDQ como teoria fechada e coerente.

Estilo:

- afirmativo;
- dedutivo;
- sem tom defensivo;
- com proposições, lemas, teoremas e corolários;
- com notas curtas para limitações reais.

Evitar:

- transformar capítulos em “pergunta/resposta”;
- excesso de justificativas históricas;
- mencionar toda auditoria no corpo do texto;
- misturar rascunhos com resultados consolidados.

### 2.2 Apêndices técnicos

Função: guardar provas, cálculos longos, derivações espectrais, detalhes de
contorno, normalizações e fórmulas auxiliares.

Exemplos:

- derivação da Hessiana;
- reconstrução OS;
- cálculo da regra de Born;
- derivação de \(6\pi^5\);
- termos de transgressão torsional;
- operadores espectrais leptônicos;
- cálculos numéricos e scripts.

### 2.3 FAQ teórica

Função: responder objeções de leitores, físicos matemáticos e revisores.

Aqui as perguntas devem aparecer explicitamente.

Exemplos:

- “A ação oficial foi alterada?”
- “Por que \(6\pi^5\) não é numerologia?”
- “A GDQ vira o Modelo Padrão?”
- “Onde entram MeV e GeV?”
- “A regra de Born foi postulada?”
- “Por que fantasmas não são necessários?”
- “O problema do sinal foi resolvido conceitualmente ou computacionalmente?”
- “Quais partes estão fechadas e quais são programa futuro?”

### 2.4 Arquivos de auditoria

Função: manter rastreabilidade.

Arquivos:

- `questoes/q02/questao_02.md`, `questoes/q03/questao_03.md`, ...
- `faltas.md`;
- `ideias/possibilidades.md`;
- adendos em `questoes/q39/associados/`, `questoes/q40/associados/`, etc.

Esses documentos não precisam ser publicados como corpo do manuscrito. Eles
servem para garantir que nenhuma objeção importante foi perdida.

---

## 3. Estrutura sugerida do manuscrito principal

## Parte I — Fundamentos

### Capítulo 1 — Motivação e problema inicial

Objetivo: explicar por que a GDQ é proposta.

Conteúdo:

1. divergência entre Feynman e Wiener;
2. necessidade de geometrizar matéria;
3. papel do fluido de Madelung;
4. causalidade complexa;
5. visão geral da teoria.

Não entrar ainda em todas as previsões.

### Capítulo 2 — Espaço geométrico fundamental

Conteúdo:

1. bulk Hermitiano/Riemanniano;
2. distinção entre bulk e espaço-tempo físico;
3. papel de \(\mathbb R^4\times T^4\);
4. compactificações globais como ferramentas de calibração;
5. cuidado com \(T^5\times S^3\): não trocar a base local oficial.

Incorporar resultados das questões 2 e 3.

### Capítulo 3 — Campos fundamentais e variáveis derivadas

Conteúdo:

1. \(g_{\mu\bar\nu}\);
2. \(f\);
3. \(\rho=e^{-(f+\bar f)/2}\);
4. \(S_R\);
5. \(\mathcal U\);
6. \(\gamma,\tau,z_\tau,\Lambda_C\);
7. torção de Bismut/Cartan como camada geométrica.

Incorporar auditorias das questões 4, 5, 10, 11, 14, 15 e 16.

### Capítulo 4 — Ação oficial da GDQ

Conteúdo:

1. escrever a ação oficial;
2. explicar que ela não muda;
3. derivar equações variacionais;
4. continuidade;
5. Hamilton-Jacobi-Bohm;
6. equação métrica;
7. papel da medida \(\mathcal U\);
8. causalidade de Sudarshan.

Este capítulo deve ser um dos mais limpos e centrais.

### Capítulo 5 — Regularidade, finitude e ausência de fantasmas

Conteúdo:

1. regularidade geométrica;
2. corte de Cartan;
3. form factor inteiro;
4. ausência de novos polos;
5. por que fantasmas/BRST são ferramenta de auditoria, não necessidade
   ontológica;
6. relação com loops sem “renormalização fundamental”.

Incorporar questões 4, 5, 32, 33, 34 e 35.

---

## Parte II — Reconstrução quântica

### Capítulo 6 — Reconstrução do espaço de Hilbert

Conteúdo:

1. medida euclidiana/complexa;
2. axiomas OS;
3. positividade;
4. reconstrução de \(\mathcal H_{\rm phys}\);
5. Hamiltoniano;
6. unitariedade.

Incorporar questões 7, 20 e 21.

### Capítulo 7 — Regra de Born e medição

Conteúdo:

1. \(\rho\) como densidade geométrica;
2. continuidade;
3. regra de Born espacial;
4. Gleason para projetores;
5. envariance como rota auxiliar;
6. problema da medida;
7. dominância espectral/difusão de nêutrons;
8. atratores solitônicos.

Incorporar questões 22 e 24.

### Capítulo 8 — Spin, estatística e férmions

Conteúdo:

1. spin como circulação;
2. holonomia de meia unidade;
3. spin-estatística;
4. exclusão de Pauli;
5. problema do sinal;
6. resolução geométrica vs resolução computacional.

Incorporar questões 1, 23, 25 e 26.

---

## Parte III — Constantes, escalas e calibração

### Capítulo 9 — Metrologia e escalas

Conteúdo:

1. massas absolutas dependem de unidade;
2. GDQ prevê razões adimensionais;
3. papel de \(M_e\) como calibração prática;
4. \(\Lambda_C\);
5. relação entre escala local e global;
6. evitar afirmações de “MeV do nada”.

Incorporar questão 36.

### Capítulo 10 — Constante de estrutura fina

Conteúdo:

1. derivação geométrica de \(\alpha\);
2. papel de \(T^5\times S^3\) como compactificação cosmológica/global;
3. distinção entre potencial local \(1/r\) e potencial global cotangente;
4. estrutura fina como geometria, não parâmetro inserido.

Incorporar questões 37 e 38 parcialmente.

### Capítulo 11 — Constante gravitacional e limite newtoniano

Conteúdo:

1. extração de \(C_R\) da ação;
2. comparação com Einstein-Hilbert;
3. \(G=c^4/(16\pi C_R)\);
4. Buckingham como avaliação, não fundamento;
5. papel de \(M_p\) sem circularidade.

Incorporar questão 38.

---

## Parte IV — Espectro de matéria

### Capítulo 12 — Léptons carregados

Conteúdo:

1. estrutura global \(T^5\times S^3\);
2. potencial cotangente em \(S^3\);
3. operador espectral;
4. domínio Reg-Reg;
5. massas como espectro global/topológico;
6. estômato finito como setor local;
7. térmico como resposta local;
8. três gerações.

Incorporar questão 39 e pasta `questoes/q39/associados/`.

### Capítulo 13 — Bárions: próton e nêutron

Conteúdo principal a partir da Q40:

1. bárion como sóliton trimodal;
2. três estômatos;
3. decomposição:

   \[
   \text{massa}=\text{bulk}+\text{superfície torsional};
   \]

4. termo de bulk:

   \[
   6\pi^5=3(2\pi^5);
   \]

5. ansatz por câmara:

   \[
   g_p^{(a)}=\sum_{A=1}^{5}d\phi_A^2,\qquad f_p^{(a)}=f_0;
   \]

6. cola global;
7. transgressão torsional;
8. massa do próton:

   \[
   \frac{M_p}{M_e}
   =
   6\pi^5
   +
   \alpha
   \left(
   \frac{3\pi}{2}
   +
   \frac{3}{4\pi^3}
   \right);
   \]

9. massa do nêutron:

   \[
   \frac{M_n}{M_e}
   =
   \frac{M_p}{M_e}
   +
   \ln(2\pi^2)\frac{3\sqrt2}{5};
   \]

10. carga por resíduos;
11. spin por circulação.

Observáveis ainda abertos devem ser marcados como subseções futuras:

- raio;
- momentos magnéticos;
- fatores de forma;
- espectro excitado;
- espalhamento;
- estabilidade global.

### Capítulo 14 — Confinamento e mass gap

Conteúdo:

1. tubos de fluxo geométricos;
2. tensão de área;
3. mass gap;
4. relação com Yang-Mills efetivo;
5. \(\alpha_s\);
6. Fredholm;
7. polarização de híperons;
8. limites: prova completa de Yang-Mills ainda não reivindicada.

Incorporar questão 30.

### Capítulo 15 — CP forte e topologia

Conteúdo:

1. relaxação topológica de \(\theta\);
2. modo CP;
3. suscetibilidade topológica;
4. massa/escala do modo, se houver;
5. EDM;
6. status: estrutural vs fenomenológico.

Incorporar questão 31.

---

## Parte V — Fenomenologia e correspondência

### Capítulo 16 — Átomos e limite clássico

Conteúdo:

1. hidrogênio;
2. potencial local \(1/r\);
3. potencial global cotangente;
4. limite plano;
5. correspondência clássica;
6. dupla fenda;
7. escolha retardada sem colapso Copenhagen clássico.

Incorporar questões 8, 37, 38 e 39 conforme necessário.

### Capítulo 17 — Fenomenologia eletrofraca e anomalias

Conteúdo:

1. setor efetivo;
2. não transformar GDQ no Modelo Padrão;
3. grupos de gauge como emergentes;
4. monopolos/Hopf como possibilidades;
5. anomalias leptônicas/hadrônicas.

Incorporar questões 27, 28, 29, 33, 34 e 35.

### Capítulo 18 — Cosmologia

Conteúdo:

1. espaço cosmológico de Einstein;
2. temperatura do espaço de Einstein;
3. \(S^1_\beta\times S^3\);
4. \(T^5\times S^3\) como ferramenta global;
5. CMB, matéria escura geométrica, tensão de Hubble;
6. separar bem cosmologia de base local.

Incorporar questões 32, 37, 38, 39.

---

## Parte VI — Status, previsões e programa futuro

### Capítulo 19 — O que está fechado

Listar de modo honesto:

1. ação oficial;
2. medida;
3. continuidade;
4. Hamilton-Jacobi-Bohm;
5. reconstrução quântica estrutural;
6. regra de Born operacional;
7. massa leptônica como espectro global;
8. massas de próton e nêutron estruturalmente;
9. regularidade/ausência de fantasmas estrutural;
10. causalidade.

### Capítulo 20 — O que ainda é programa de pesquisa

Listar:

1. solução bariônica global completa;
2. raio de carga;
3. momentos magnéticos completos;
4. fatores de forma;
5. espalhamento;
6. espectro excitado;
7. algoritmos do problema do sinal;
8. benchmarks numéricos;
9. derivação completa de todos os coeficientes efetivos;
10. cosmologia quantitativa.

Esse capítulo deve ser honesto e objetivo. Ele aumenta a credibilidade.

---

## 4. Apêndices recomendados

### Apêndice A — Ação oficial e variações

Incluir:

- variação em \(f\);
- variação em \(S_R\);
- variação em \(g\);
- derivação da continuidade;
- derivação Hamilton-Jacobi-Bohm;
- medida \(\mathcal U\).

### Apêndice B — Reconstrução OS e Born

Incluir:

- positividade;
- espaço de Hilbert;
- Hamiltoniano;
- Gleason;
- envariance.

### Apêndice C — Operadores espectrais

Incluir:

- Hessiana;
- operador leptônico;
- operador bariônico;
- condições de contorno;
- Reg-Reg vs Robin.

### Apêndice D — Massas leptônicas

Incluir:

- material consolidado de `questoes/q39/associados/`;
- solver;
- contornos;
- temperatura;
- status.

### Apêndice E — Massas bariônicas

Incluir:

- `questoes/q40/associados/adendo_volume_superficie.md`;
- `questoes/q40/associados/adendo_bulk_6pi5.md`;
- `questoes/q40/associados/adendo_reducao_variacional_bulk.md`;
- `questoes/q40/associados/adendo_ansatz_gp_fp.md`;
- `questoes/q40/associados/adendo_cola_torcao_superficie.md`;
- `questoes/q40/associados/adendo_neutron_deltaB.md`.

### Apêndice F — Constantes fundamentais

Incluir:

- \(\alpha\);
- \(G\);
- \(\Lambda_C\);
- escalas;
- calibração metrológica.

### Apêndice G — FAQ teórica

Ver seção abaixo.

---

## 5. FAQ teórica recomendada

Criar arquivo separado:

```text
FAQ_teorica_GDQ.md
```

Perguntas sugeridas:

1. A ação oficial foi alterada ao longo da teoria?
2. O que é realmente fundamental: \(\rho\), \(f\), \(g\) ou \(\mathcal U\)?
3. Por que a regra de Born não é postulada?
4. Por que fantasmas não são necessários?
5. A GDQ vira o Modelo Padrão?
6. Onde entram \(SU(3)\), \(SU(2)\), \(U(1)\)?
7. Por que \(T^5\times S^3\) não substitui \(\mathbb R^4\times T^4\)?
8. Como MeV e GeV aparecem?
9. Por que \(6\pi^5\) não é numerologia?
10. Por que volume dá massa e torção dá superfície?
11. O problema do sinal foi resolvido conceitualmente ou computacionalmente?
12. O que está fechado matematicamente?
13. O que ainda é conjectural?
14. Quais previsões podem ser testadas?
15. Quais partes dependem de simulação?

---

## 6. Como migrar os arquivos atuais

### 6.1 Questões fechadas

Para cada `questão_X.md`:

1. extrair o veredito;
2. extrair as fórmulas finais;
3. transformar em proposição/lema/corolário;
4. mover detalhes longos para apêndice;
5. deixar perguntas difíceis na FAQ.

### 6.2 Questões parcialmente fechadas

Usar estrutura:

```text
Proposição estrutural
Demonstração parcial
Status
Pendência técnica
```

Exemplo Q40:

```text
Proposição: massas bariônicas p,n.
Demonstração: bulk + superfície + cisalhamento.
Status: massas fechadas estruturalmente.
Pendência: observáveis bariônicos completos.
```

### 6.3 Questões abertas

Não esconder. Criar seção:

```text
Programa futuro
```

com linguagem precisa:

- “permanece como programa numérico”;
- “requer solução explícita”;
- “requer benchmark”;
- “ainda não é teorema completo”.

---

## 7. Ordem prática de trabalho

Recomendo reorganizar nesta ordem:

1. congelar a ação oficial;
2. limpar capítulos de fundamentos;
3. consolidar variáveis e notação;
4. mover auditorias para apêndices;
5. reescrever léptons com base na Q39;
6. reescrever bárions com base na Q40;
7. criar FAQ teórica;
8. criar capítulo “status e programa futuro”;
9. só depois revisar fenomenologia e cosmologia.

---

## 8. Regra de ouro

Sempre que uma fórmula importante aparecer, classificar explicitamente:

```text
Status: derivada / estrutural / conjectural / fenomenológica / programa futuro.
```

Exemplos:

\[
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
\]

Status:

```text
derivada estruturalmente como bulk + superfície torsional;
requer verificação formal completa da solução global colada.
```

\[
G_E^p(q^2),G_M^p(q^2)
\]

Status:

```text
programa futuro; ainda não derivado.
```

Essa regra evita exagero e aumenta a credibilidade do manuscrito.

---

## 9. Conclusão

A melhor reorganização é:

\[
\boxed{
\text{manuscrito principal dedutivo}
+
\text{apêndices técnicos}
+
\text{FAQ teórica}
+
\text{auditoria interna preservada}.
}
\]

As perguntas que trabalhamos devem orientar a blindagem lógica da teoria, mas
não devem dominar a forma do manuscrito principal.
