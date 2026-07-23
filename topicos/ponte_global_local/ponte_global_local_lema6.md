# Ponte global--local da GDQ — Lema 6: separação dos dados transportados

> [!important] Atualização arquitetural
> A separação usa agora convergência apontada direta. Ver
> `topicos/ponte_global_local/ponte_global_local_lemas_sem_colar.md`.

## 1. Objetivo

O último lema impede que a expressão “herança espectral” seja usada para
quantidades de naturezas distintas. A ponte global--local possui quatro
mecanismos:

1. invariância homotópica e teoria do índice;
2. convergência de projetores para espectro ligado;
3. convergência de normas e formas quadráticas para acoplamentos;
4. resposta local a fontes e interfaces.

Uma quantidade pode ser protegida por um desses mecanismos e não pelos
outros.

## 2. Setor topológico

Considere uma família de operadores elípticos de Bismut com domínio APS ou
uma realização Fredholm equivalente. Enquanto:

1. o símbolo principal permanecer elíptico;
2. a classe de torção e o fibrado permanecerem na mesma classe;
3. o operador tangencial de bordo não atravessar zero;
4. não ocorrer cirurgia;

o índice é constante:

$$
\boxed{
\operatorname{Ind}_{\rm APS}D_\varepsilon^B
=\operatorname{Ind}_{\rm APS}D_P^B.
}
$$

Se autovalores do operador tangencial cruzarem zero, a mudança é medida pelo
fluxo espectral:

$$
\operatorname{Ind}D_+^B-
\operatorname{Ind}D_-^B
=\operatorname{SF}(D_s^B).
$$

Classes de Chern são transportadas por identificações de fibrados que
preservem a conexão até homotopia:

$$
c_k(E_\varepsilon)=c_k(E_P).
$$

Esses enunciados preservam inteiros e classes. Eles não determinam uma norma
contínua de acoplamento.

## 3. Setor espectral ligado

Para um cluster isolado, os Lemas 4--5 fornecem

$$
P_{a,\varepsilon}\longrightarrow P_{a,P}
$$

em norma após identificação, e

$$
\lambda_{a,j}^{(\varepsilon)}longrightarrow
\lambda_{a,j}^{(P)}.
$$

São transportados:

1. multiplicidade do cluster;
2. autovalores ligados;
3. representação das simetrias no autoespaço;
4. matrizes de operadores comprimidos ao setor.

Não são automaticamente transportados estados que se aproximem do contínuo.

## 4. Normalização de acoplamentos

Se $\Phi_{Q,\varepsilon}$ é um modo geométrico de conexão já derivado da
Hessiana, sua constante cinética efetiva é uma norma ou forma quadrática:

$$
Z_{Q,\varepsilon}
=q_\varepsilon^{(2)}
[\Phi_{Q,\varepsilon},\Phi_{Q,\varepsilon}].
$$

Depois de integrar os graus acoplados, pode aparecer um complemento de Schur:

$$
K_{Q,\varepsilon}^{\rm eff}
=K_{QQ}-K_{Q\perp}K_{\perp\perp}^{-1}K_{\perp Q}.
$$

A magnitude do acoplamento local só pode ser definida depois dessa redução:

$$
\boxed{
\frac1{e_P^2}
=\lim_{\varepsilon\to0}
\langle\Phi_{Q,\varepsilon},
K_{Q,\varepsilon}^{\rm eff}\Phi_{Q,\varepsilon}\rangle.
}
$$

A classe de Chern pode exigir que a carga seja inteira, mas não fixa sozinha
$e_P$. Se a integral divergir, o modo não está localizado e $e_P$ pode tender
a zero. Se tender a zero, a aproximação quadrática é degenerada e requer nova
análise; nenhum dos casos deve ser corrigido por normalização posterior.

## 5. Escalas dimensionais

Um autovalor geométrico adimensional não é ainda uma massa em unidades
experimentais. A conversão exige uma escala definida pela própria redução:

$$
m_a^2
=\mathfrak C_{\rm dim}
\lambda_{a,P}.
$$

$\mathfrak C_{\rm dim}$ deve vir de $\Lambda_C$, da métrica física e da
normalização da ação, ou de uma calibração explicitamente declarada. A ponte
preserva razões de autovalores quando o mesmo fator dimensional se aplica,
mas não cria uma unidade absoluta.

## 6. Resposta local e aparelho

Após o transporte do setor global, uma fonte clássica e uma interface local
produzem

$$
K_{P,\rm eff}^{(a)}
=P_{a,P}
\left(
K_P+J_{\rm app}+\mathsf R_{\rm app}
\right)P_{a,P}.
$$

$J_{\rm app}$ é fonte ou resposta linearizada, enquanto
$\mathsf R_{\rm app}$ é a impedância de interface. Eles podem deslocar e
desdobrar o espectro, mas não pertencem à identidade global do modo.

Tempos, taxas e larguras exigem ainda a mobilidade causal e a reconstrução do
registro. A Hessiana fornece rigidez; não fornece sozinha uma escala temporal.

## 7. Tabela de transporte

| Quantidade | Mecanismo | Hipótese necessária | Pode ser quantizada? | Pode depender do aparelho? |
|---|---|---|---:|---:|
| Índice | Homotopia/Fredholm/APS | gap tangencial, sem cirurgia | sim | não, enquanto o gap não fecha |
| Carga topológica | classe de Chern ou fluxo relativo | fibrado e interface preservados | sim | orientação pode ser selecionada |
| Multiplicidade ligada | projetor de Riesz | gap uniforme | inteira | não sob perturbação menor que o gap |
| Autovalor ligado | convergência em norma no cluster | localização e gap | não em geral | pode sofrer dressing |
| Massa dimensional | autovalor mais escala física | normalização dimensional | não em geral | pode receber deslocamento ambiental |
| Acoplamento | norma da Hessiana/complemento de Schur | modo localizado e integral finita | não em geral | a resposta efetiva pode depender da interface |
| Largura/taxa | dinâmica causal e canais abertos | mobilidade e reconstrução | não | sim |
| Registro | interação clássico--quântico | fonte, interface e dinâmica condicionada | resultado discreto | essencialmente |

## 8. Aplicação metodológica às questões da GDQ

### Q28 — gerações e cargas

Índice, fluxo espectral e classes de Chern pertencem ao setor topológico.
Normas de calibre e magnitudes de acoplamento pertencem ao setor de
normalização e exigem cálculo separado. O número de estômatos não pode ser
inferido de uma normalização contínua.

### Q29 — setor eletrofraco

A identidade do modo de Hopf pode ser global. Os valores de $g$, $g'$, $v$ e
as massas de $W/Z$ exigem as normas da Hessiana e a escala dimensional após o
transporte.

### Q37 — estrutura fina

A integral de circulação pode quantizar a carga. O valor de $\alpha$ exige a
normalização finita do modo eletromagnético localizado e não segue apenas do
inteiro topológico.

### Q38 — gravidade

O dado cosmológico pode fixar uma classe ou coeficiente global. A constante
gravitacional local exige o coeficiente da resposta de curvatura na ação
reduzida e a compatibilidade do contorno causal.

### Q39 — massas leptônicas

Razões espectrais podem ser transportadas se os modos permanecerem abaixo do
limiar. A escala absoluta e correções ambientais devem ser calculadas
separadamente e não absorvidas no contorno depois da comparação.

### Q40 — bárions

Índice/carga e resposta de espalhamento são setores distintos. A identidade
bariônica pode ser global, enquanto fatores de forma e momentos dependem da
solução planar e da sonda.

## 9. Critério de uma aplicação preditiva

Para cada observável, deve existir uma ficha contendo:

1. quantidade global transportada;
2. mecanismo matemático de transporte;
3. background e setor físico;
4. operador local e domínio;
5. escala ou normalização;
6. dados do aparelho;
7. parâmetros conhecidos antes da comparação;
8. erro analítico e numérico;
9. classificação do resultado.

Uma aplicação é preditiva somente se o alvo experimental não foi usado para
escolher o background, o contorno, o setor, o coeficiente dimensional ou a
normalização.

## 10. Teorema de separação

Sob BI e os Lemas 3--5:

$$
\boxed{
\begin{aligned}
\text{topologia}&\longrightarrow
(\operatorname{Ind},c_k,Q,\operatorname{SF}),\\
\text{projetores}&\longrightarrow
(m_a,\lambda_{a,j},E_a),\\
\text{formas quadráticas}&\longrightarrow
(Z_a,e_a,m_a^{\rm dim}),\\
\text{fontes e interface}&\longrightarrow
(\delta\lambda,\Gamma,\text{registro}).
\end{aligned}
}
$$

Nenhuma seta pode ser substituída por outra sem uma identidade adicional
demonstrada. Em particular:

$$
c_1\not\Rightarrow e,
\qquad
\lambda\not\Rightarrow m\text{ absoluto},
\qquad
\operatorname{Hess}\not\Rightarrow\text{tempo}.
$$

## 11. Status

$$
\boxed{
\text{Lema 6: demonstrado como separação lógica e matemática dos setores.}
}
$$

Sua aplicação quantitativa continua condicionada à Hipótese BI, ao gap do
Lema 4 e às normalizações específicas de cada questão.
