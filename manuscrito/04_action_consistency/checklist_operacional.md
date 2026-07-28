---
title: "Checklist operacional — Capítulo 4"
---

# Checklist operacional — Capítulo 4

Este checklist segue o protocolo metodológico do Capítulo 27.

O capítulo deve fixar a ação oficial da GDQ, seu domínio variacional, o papel
da medida, a Hessiana física e o significado de loops sem substituir a teoria
por formalismos externos.

## 1. Objetivo do capítulo

O Capítulo 4 deve demonstrar didaticamente:

1. por que a GDQ precisa de uma ação única;
2. qual é exatamente a ação oficial preservada;
3. quais objetos são campos e quais são dados estruturais;
4. como ler cada termo da ação sem ambiguidade dimensional;
5. como a primeira variação organiza equações de bulk e termos de bordo;
6. como simetrias geram identidades de conservação;
7. por que a Hessiana física define flutuações, resposta e loops;
8. por que fantasmas/BRST/renormalização são linguagem externa ou
   representação auxiliar, não ontologia da GDQ;
9. qual setor de loop está fechado e qual permanece programa futuro.

Status do capítulo: **estruturalmente fechado como formulação da ação e do
problema perturbativo da GDQ**.

## 2. Situação do corpo principal

| Seção | Status | Observação |
|---|---|---|
| `04.1` | pronta em primeira versão | Explica por que uma ação é necessária. |
| `04.2` | pronta em primeira versão | Preserva a ação oficial e resolve a leitura dimensional. |
| `04.3` | pronta em primeira versão | Separa campos, medida, fontes, contornos e vínculos. |
| `04.4` | pronta em primeira versão | Lê termo a termo a ação oficial. |
| `04.5` | pronta em primeira versão | Formula a variação; Cap. 5 executa as contas pedagógicas. |
| `04.6` | pronta em primeira versão | Simetrias, Noether, gauge e bordos. |
| `04.7` | pronta condicionalmente | Define loops por Hessiana física e fecha setor U(1) heat-kernel declarado. |
| `04.8` | pronta em primeira versão | Declara alcance e limites. |

## 3. Notas chamadas e função lógica

| Nota | Função |
|---|---|
| `Dimensão e normalização da ação oficial` | Resolve a ambiguidade de $\Lambda_C$ como número adimensional em coordenadas normalizadas. |
| `Significado físico do termo dimensional -n` | Deriva $-n$ como zero entrópico dimensional e separa essa referência do valor on-shell de backgrounds locais ou cosmológicos. |
| `Primeira variação da ação GDQ - estrutura completa` | Dá a álgebra compacta da primeira variação. |
| `Quociente físico, fantasmas e identidades de calibre` | Explica projetor/quociente físico e rebaixa fantasmas a jacobiano auxiliar. |
| `Ausência de polo de Landau no setor U(1) efetivo` | Calcula o setor U(1) heat-kernel com saturação UV, fixação setorial de $\tau$ e condição sem polo. |
| `Hessiana, kernel de calor e propagador modificado` | Deduz $e^{-\tau L}$, separa Hessiana e gerador de calor, e mostra ausência de novos polos pelo fator inteiro. |
| `Escala de Cartan, resolução de fluxo e escalas setoriais` | Separa $\Lambda_C$, $\widehat\Lambda_\tau$, massas e escalas setoriais, evitando cortes universais indevidos. |
| `Loop geométrico de calibre pela fase toroidal` | Preserva o loop mínimo derivado da ação oficial e demonstra Ward/transversalidade no setor declarado. |

Avaliação: o capítulo está alinhado ao padrão “ação oficial → variação →
Hessiana → quociente físico → loop”.

## 4. Material legado preservado

Fontes legadas principais:

- o capítulo legado de ação funcional;
- o capítulo legado de consistência em loops.

Blocos preservados:

1. necessidade de princípio variacional único;
2. ação da GDQ como centro organizador;
3. leitura geométrica de curvatura, campo complexo e medida;
4. variações de fase, densidade e métrica;
5. preocupação com loops e consistência perturbativa;
6. objeção dos fantasmas;
7. polo de Landau;
8. separação entre escala UV e cosmologia.

Correções de status em relação ao legado:

1. a ação oficial não foi alterada;
2. $\mathcal U$ não é multiplicador indeterminado: é funcional constitutivo;
3. Perelman não é ação física;
4. $\Lambda_C$ na ação é adimensional nas coordenadas normalizadas;
5. escalas físicas devem ser escritas como $\ell_C$, $k_C$ e $E_C$;
6. propagadores de Dirac/Yang–Mills/QED são reduções ou comparações;
7. fantasmas não são ontologia GDQ;
8. antiga função beta/polo de Landau foi substituída pelo cálculo heat-kernel
   setorial;
9. finitude superficial setorial não é finitude universal em todas as ordens.

## 5. Resultados e limites

### Fixado como axiomático

1. ação oficial;
2. campos fundamentais e dados estruturais;
3. domínio de integração;
4. contorno causal $\gamma$;
5. classe variacional admissível.

### Derivado ou definido

1. dimensionalidade correta da ação em coordenadas normalizadas;
2. papel constitutivo de $\mathcal U$;
3. estrutura da primeira variação;
4. necessidade da Hessiana para resposta e loops;
5. quociente/projetor físico como substituto intrínseco de modos não físicos;
6. interpretação auxiliar de determinantes FP/fantasmas.

### Condicional ou setorial

1. ausência do polo de Landau no setor U(1) heat-kernel declarado;
2. identidades Ward/Slavnov--Taylor como covariância espectral no domínio
   apropriado;
3. finitude superficial quando o form factor vem da Hessiana e do gerador de
   calor;
4. estabilidade de fundo quando $K_{\rm phys}$ é positivo no setor.

### Não demonstrado neste capítulo

1. finitude perturbativa em todas as ordens;
2. existência universal de backgrounds materiais;
3. estabilidade de todos os setores;
4. derivação de todos os vértices;
5. completude não perturbativa da GDQ.

## 6. Scripts numéricos e simbólicos

Scripts obrigatórios para fechamento do Capítulo 4: **nenhum**.

Motivo: os cálculos principais já estão em notas analíticas. O capítulo define
o formalismo; não faz previsão metrológica.

Scripts opcionais criados em [[scripts/README|scripts/]]:

1. [[scripts/verificar_dimensao_acao_normalizada.py|verificar_dimensao_acao_normalizada.py]]  
   Reproduzir a contagem dimensional em coordenadas normalizadas.

2. [[scripts/verificar_variacao_medida.py|verificar_variacao_medida.py]]  
   Checar a identidade $\delta\mathcal U/\mathcal U=-\delta(f+\bar f)/2$ para
   métrica fixa.

3. [[scripts/verificar_projetor_fisico_linear.py|verificar_projetor_fisico_linear.py]]  
   Ilustrar $P_{\rm phys}^2=P_{\rm phys}$ em um modelo linear com modos de
   gauge e vínculos.

4. [[scripts/verificar_polarizacao_heat_kernel_toy.py|verificar_polarizacao_heat_kernel_toy.py]]  
   Reproduzir apenas a saturação de uma integral heat-kernel simples como
   ilustração, sem substituir a nota completa de polarização.

5. [[scripts/verificar_kernel_calor_propagador.py|verificar_kernel_calor_propagador.py]]  
   Checar o limite plano $G_\tau=e^{-\tau p_E^2}/(p_E^2+m^2)$ e mostrar a
   diferença contra a dupla contagem incorreta $e^{-\tau^2p_E^2}$.

6. [[scripts/verificar_hessiana_escalar_reduzida.py|verificar_hessiana_escalar_reduzida.py]]  
   Verificar numericamente o símbolo principal do setor escalar reduzido
   $L_\varphi=2(-\Delta)$ em fundo plano.

7. [[scripts/verificar_separacao_escalas.py|verificar_separacao_escalas.py]]  
   Mostrar numericamente por que $m_e$ e $1\,{\rm GeV}$ não podem ser lidos
   como cortes gaussianos duros universais, e separar massa de resolução.

8. [[scripts/verificar_loop_geometrico_fase_t4.py|verificar_loop_geometrico_fase_t4.py]]  
   Reproduzir o loop geométrico da fase toroidal, verificando $\Pi(0)=0$,
   Ward e saturação UV.

9. [[scripts/verificar_kernels_covariantes_calibre.py|verificar_kernels_covariantes_calibre.py]]  
   Comparar kernels covariantes admissíveis e separar preservação de calibre
   de igualdade numérica entre resoluções diferentes.

Classificação: teste simbólico/ilustração, não previsão física.

## 7. Pontos didáticos a revisar na leitura final

Antes de considerar o Capítulo 4 editorialmente pronto:

1. garantir que a ação oficial aparece uma única vez como fórmula central e
   preservada;
2. reforçar a diferença entre $\Lambda_C$ adimensional e escalas físicas;
3. impedir que “loop” soe como importação de QFT comum;
4. reforçar que Hessiana física depende de background, domínio, contorno e
   projetor;
5. explicar que fontes/aparelhos entram como dados de problema, não como
   alteração da ação fundamental;
6. manter o Capítulo 5 como lugar das derivações pedagógicas completas;
7. revisar links e renderização.

## 8. Veredito operacional

O Capítulo 4 está **estruturalmente montado**.

Ele cumpre a função de fixar o funcional, a classe variacional e o significado
interno de loops na GDQ.

As pendências restantes são:

1. revisão didática;
2. referências históricas adicionais;
3. scripts opcionais de ilustração;
4. desenvolvimento posterior de vértices e finitude em todas as ordens, sem
   reabrir a validade estrutural deste capítulo.

## Revisão didática de 2026-07-19

O Capítulo 4 foi conferido na fase de revisão científica/didática. A transição
do `index.md` foi corrigida: o capítulo não apenas prepara uma variação futura;
ele fixa a ação, a primeira variação e a lógica da Hessiana. O Capítulo 5
herda essa estrutura para derivar as equações hidrodinâmicas e as leis de
conservação no setor observável.

Foram reexecutados os quatro scripts do capítulo:

1. dimensão da ação em coordenadas normalizadas;
2. variação constitutiva da medida;
3. projetor físico linear;
4. saturação heat-kernel toy.

Todos permanecem classificados como testes simbólicos ou ilustrações
pedagógicas. Eles não são previsões metrológicas, não substituem as notas
analíticas e não importam uma teoria externa como ontologia da GDQ.

## Reauditoria do propagador modificado — 2026-07-21

O tratamento do propagador modificado foi tornado autocontido no Capítulo 4.
O fator $e^{-p_E^2/\widehat\Lambda_\tau^2}$ foi registrado como limite plano
do semigrupo de calor da Hessiana normalizada:

$$
\mathcal O_{\rm Hess}^{(2)}
=
\tau L_{\rm GDQ}^{(2)},
\qquad
K_\tau=e^{-\tau L_{\rm GDQ}^{(2)}}.
$$

A ausência de novos polos foi registrada como consequência de $e^{-z}\ne0$.
As pendências remanescentes são metrológicas/formais: blocos completos em
fundo geral, reflexão positiva, reconstrução lorentziana e causalidade
retardada.

## Reauditoria da escala de corte — 2026-07-21

A ambiguidade entre corte da ação, escala de resolução e massa foi tornada
explícita:

$$
\Lambda_C
\neq
\widehat\Lambda_\tau
\neq
m_i.
$$

$\Lambda_C$ é número adimensional na ação normalizada; a escala física é
restaurada por $\ell_C$, $k_C=\ell_C^{-1}$ e $E_C=\hbar c/\ell_C$.
$\widehat\Lambda_\tau=\tau^{-1/2}$ é a resolução espectral do semigrupo de
calor. Massas $m_i$ deslocam o espectro dos operadores setoriais, mas não
definem cortes universais.

## Reauditoria de calibre em loops — 2026-07-21

O fechamento de calibre em loops foi tornado autocontido pelo loop geométrico
da fase toroidal. A cadeia preservada é:

$$
\mathcal S_{\rm GDQ}
\to
S_\chi^{(2)}
\to
H_n[A]
\to
\operatorname{Tr}\log H_n[A]
\to
\Pi_{\mu\nu}^{(n)}.
$$

O setor mostra $\Pi(0)=0$, transversalidade de Ward e saturação UV. Fantasmas
continuam classificados como representação auxiliar do jacobiano de gauge, não
como ontologia da GDQ.
