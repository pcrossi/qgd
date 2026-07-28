---
title: "Vínculos covariantes e o papel opcional do algoritmo de Dirac–Bergmann"
---

# Vínculos covariantes e o papel opcional do algoritmo de Dirac--Bergmann

## 1. A pergunta

Uma ação com redundâncias e vínculos precisa necessariamente ser submetida ao
algoritmo de consistência de Dirac--Bergmann?

No programa atual da GDQ, a resposta é **não**, desde que permaneçamos na
formulação variacional covariante e construamos corretamente o espaço físico
de variações. A resposta seria diferente caso o objetivo fosse obter uma
formulação hamiltoniana canônica completa.

## 2. O que o algoritmo de Dirac--Bergmann faria

Em uma passagem para variáveis canônicas, uma transformação de Legendre
degenerada produz relações entre coordenadas e momentos que não podem ser
invertidas livremente. O algoritmo de Dirac--Bergmann organiza então:

1. vínculos primários;
2. preservação temporal desses vínculos;
3. vínculos secundários eventualmente produzidos;
4. classificação em primeira e segunda classe;
5. fixações de gauge;
6. colchetes de Dirac quando existem vínculos de segunda classe.

Esse procedimento é necessário para uma quantização canônica ou para uma
descrição hamiltoniana que pretenda representar todo o conteúdo da ação.

## 3. A rota covariante usada pela GDQ

O manuscrito não começa por uma decomposição canônica da ação oficial. Ele
começa pela primeira e pela segunda variações covariantes. Seja
$\Phi$ o conjunto dos campos e seja

$$
\mathcal C_I[\Phi]=0
$$

o conjunto de vínculos físicos, incluindo normalizações, cargas conservadas,
compatibilidades geométricas e dados de interface que pertençam ao problema.
Em torno de um background admissível $\Phi_*$, uma flutuação física deve
satisfazer

$$
D\mathcal C_I\big|_{\Phi_*}[\delta\Phi]=0.
$$

Além disso, duas flutuações relacionadas por uma redundância de gauge não
representam perturbações físicas diferentes. O espaço físico linearizado é,
portanto, o quociente

$$
\mathcal T_{\rm phys}
=
\frac{
\bigcap_I\ker D\mathcal C_I\big|_{\Phi_*}
}{
\operatorname{Im}D_{\Phi_*}^{\rm gauge}
}.
$$

Depois de escolher um representante regular desse quociente, define-se um
mapa de inclusão ou projetor $P_{\rm phys}$. A forma quadrática física é

$$
q_{\rm phys}[\psi]
=
\delta^2\mathcal S_{\rm GDQ}
\big[
P_{\rm phys}\psi,
P_{\rm phys}\psi
\big],
$$

e seu operador associado é

$$
K_{\rm phys}
=
P_{\rm phys}^{\dagger}
\operatorname{Hess}_{\Phi_*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

É nesse operador, com domínio e condições de contorno declarados, que se
analisam modos zero, direções negativas, gap e resposta linear.

## 4. Por que isso não elimina os vínculos

O projetor físico não é uma licença para descartar equações inconvenientes.
Ele somente é legítimo quando construído a partir:

- das equações linearizadas dos vínculos;
- dos geradores reais das redundâncias;
- das condições de bordo do problema variacional;
- da estrutura funcional escolhida para o operador.

Assim, “não usar Dirac--Bergmann” não significa “não verificar
consistência”. A consistência é verificada no problema covariante por:

$$
\text{equações de Euler--Lagrange}
\;+\;
\text{identidades de Noether}
\;+\;
\text{vínculos tangentes}
\;+\;
\text{bordo}
\;+\;
\text{Hessiana física}.
$$

## 5. Quando a equivalência precisaria ser demonstrada

Se futuramente for construída uma versão hamiltoniana da GDQ, não será
suficiente declarar que ela equivale à rota covariante. Será necessário:

1. realizar a decomposição temporal escolhida;
2. calcular os momentos canônicos;
3. localizar a degenerescência da transformação de Legendre;
4. executar o algoritmo de consistência;
5. comparar o espaço reduzido canônico com $\mathcal T_{\rm phys}$;
6. demonstrar que as duas formas reduzidas produzem os mesmos observáveis.

Até essa demonstração, Dirac--Bergmann permanece uma possível auditoria ou
reformulação, não um fundamento adicional da GDQ.

## 6. Status preciso

O resultado desta nota é uma **decisão metodológica condicionada à formulação
covariante vigente**:

- o algoritmo de Dirac--Bergmann não é necessário para as derivações
  variacionais e espectrais realizadas no manuscrito;
- os vínculos continuam obrigatórios e devem ser impostos antes da leitura do
  espectro físico;
- uma futura formulação hamiltoniana canônica exigirá sua própria análise de
  consistência e uma prova de equivalência.

Não há alteração da ação oficial nem introdução de nova ontologia.
