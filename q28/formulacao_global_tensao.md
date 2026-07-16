# Q28 — Formulação global da tensão e regra de não circularidade

## 1. Separação dos níveis

A estrutura deve ser formulada em dois níveis matematicamente distintos.

### Nível global

O problema cosmológico fornece o domínio, sua orientação, sua colagem e sua
carga topológica:

$$
\mathfrak B_{\rm global}
=\left(
K_8,
[g]_{\partial},
[\mathcal U]_{\partial},
\Gamma_{\mathbb Z_6},
A
\right).
$$

Aqui

$$
A
=-\frac1{8\pi^2}
\int_{T^4}\operatorname{tr}(F\wedge F)
$$

é uma carga global conservada. Ela representa a tensão/torção total do tecido
espacial no setor relevante, não uma variável local contínua.

### Nível local

Dado $\mathfrak B_{\rm global}$, a ação oficial determina os campos locais:

$$
(g_A,f_A,\mathcal U_A,F_A)
=\operatorname*{Crit}_{\mathfrak B_{\rm global}}
\mathcal S_{\rm GDQ}.
$$

As variações locais obedecem

$$
\delta A=0.
$$

Isso não é uma restrição artificial: números característicos não mudam sob
deformações suaves que preservam o domínio e as condições de bordo.

## 2. Teorema condicional local-global

O resultado da Q28 deve ser enunciado assim.

> **Teorema local-global da contagem geracional.** Considere um background
> global GDQ com colagem $\mathbb Z_6$, winding mínimo
> $\nu(g)=1$ e carga topológica toroidal $A$. Se a Hessiana local possui índice
> APS unitário por componente e permanece estável durante o fluxo admissível,
> então o índice geracional global é

$$
\boxed{
N_G
=\frac{A\nu(g)}6
=\frac A6.
}
$$

Consequentemente,

$$
N_G=3
\Longleftrightarrow
A=18.
$$

Esse teorema deriva a transmissão da carga global para a contagem local. Ele
não afirma que a ação local determina o valor cosmológico de $A$.

## 3. Problema global remanescente

A pergunta correta não é mais

$$
\text{“por que a minimização local escolhe }A=18\text{?”}
$$

pois foi demonstrado que ela não escolhe. A pergunta correta é

$$
\boxed{
\text{“quais condições cosmológicas de contorno da GDQ fixam }A=18\text{?”}
}
$$

Essa questão deve ser respondida no setor cosmológico/global, usando dados
como:

1. topologia e orientação do espaço de Einstein;
2. tensão espacial total e sua lei de conservação;
3. regularidade global da colagem entre os ciclos toroidais e $S^3$;
4. condição causal inicial/final;
5. eventual decomposição obrigatória da carga em componentes mínimas.

## 4. Princípio de conservação

Se o domínio global não sofre uma cirurgia que atravesse uma singularidade
admissível, então

$$
\frac{dA}{d\tau}=0.
$$

O fluxo da ação oficial pode redistribuir a densidade

$$
\operatorname{tr}(F\wedge F),
$$

mas preserva sua integral. Assim, a tensão global fixa o setor; a dinâmica
local determina como essa tensão é distribuída e observada.

## 5. Regra para evitar loops

A partir deste ponto, não devem ser repetidas tentativas de obter $A=18$ por:

1. holonomias toroidais constantes;
2. Hessiana do background produto;
3. minimização homogênea da conexão;
4. variação do raio de $S^3$;
5. anisotropia homogênea de $T^5$;
6. redistribuição suave do dilatão e da medida.

Essas rotas já foram calculadas e produzem curvatura nula ou monotonicidade em
$|A|$.

Uma nova tentativa só é válida se introduzir um dado global previamente não
avaliado e derivado independentemente, como uma condição cosmológica de
contorno ou uma cirurgia que altere a classe topológica.

## 6. Classificação correta da Q28

A Q28 possui dois status diferentes:

$$
\boxed{
\text{setor local e transmissão índice--representações: fechado.}
}
$$

$$
\boxed{
\text{seleção cosmológica de }A=18:\text{ aberta e transferida ao problema
global de contorno.}
}
$$

Portanto, não se deve chamar toda a Q28 de “não resolvida”, nem declarar três
gerações como derivadas sem a condição global. A formulação honesta é:

$$
\boxed{
\text{a GDQ deriva }N_G=A/6;
\text{ o valor }N_G=3\text{ requer demonstrar }A=18
\text{ no background cosmológico.}
}
$$

## 7. Próximo trabalho único

O próximo trabalho permitido é construir o funcional/carga global da tensão
no background cosmológico e calcular

$$
A[\mathfrak B_{\rm cosmológico}].
$$

Até esse cálculo existir, a análise local da Q28 deve ser considerada
encerrada e congelada.

## 8. Resultado do cálculo cosmológico isotrópico

O cálculo explícito está em `q28/tensao_global_cosmologica.md`. Como

$$
H^4(T^5,\mathbb Z)\cong\mathbb Z^5,
$$

a classe $a_4$ é dual a um vetor integral axial. A invariância sob as
inversões orientadas de dois ciclos do toro força todas as suas componentes a
zero. Portanto,

$$
\boxed{
A[T^5\times S^3,\text{ isotropia global completa}]=0.
}
$$

Assim, a cosmologia completamente isotrópica não produz $A=18$. No background
físico de Einstein, porém, o ciclo térmico reduz a simetria para a isotropia de
$T^4$ e deixa um setor invariante unidimensional:

$$
a_4=A\,\operatorname{PD}(e^5),
\qquad
A\in\mathbb Z.
$$

A condição térmica escolhe a direção e a topologia quantiza o coeficiente,
mas nenhuma delas determina sua magnitude. Continua faltando uma identidade
global de localização, uma cirurgia com multiplicidade calculada ou uma
condição inicial topológica que fixe $A$ sem usar $N_G=3$.
