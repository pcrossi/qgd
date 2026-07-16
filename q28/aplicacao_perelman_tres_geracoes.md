# Q28 — Aplicação do teorema de Perelman à estabilidade geracional

## 1. Questão precisa

Queremos saber se os resultados de Perelman demonstram

$$
N_G=3.
$$

O artigo fornece monotonicidade, rigidez dos casos de igualdade, controle de
soluções antigas, necks e fluxo com cirurgia em dimensão três. É necessário
separar:

$$
\text{dimensão da variedade}=3
$$

de

$$
\text{número de componentes geracionais}=3.
$$

Esses números não são o mesmo invariante.

## 2. Resultado de monotonicidade aplicável

Para o funcional de Perelman,

$$
\mathcal W(g,f,\tau),
$$

a evolução satisfaz uma identidade do tipo

$$
\frac{d\mathcal W}{dt}
=2\tau
\int_M
\left|
\operatorname{Ric}
+\nabla^2f
-\frac{g}{2\tau}
\right|^2
\mathcal U,dV
\geq0.
$$

A igualdade ocorre somente quando

$$
\operatorname{Ric}
+\nabla^2f
=\frac{g}{2\tau},
$$

isto é, num sóliton gradiente encolhedor.

Aplicado à GDQ no setor em que a redução Ricci--Bismut preserva a mesma
estrutura de Lyapunov, isso fornece:

$$
\boxed{
\text{cada setor topológico admissível converge, quando converge, para um
sóliton crítico; breathers não triviais são excluídos.}
}
$$

Esse é um teorema de seleção e estabilidade, não de contagem de setores.

## 3. Neckpinches e cirurgia

Perelman descreve regiões singulares como uniões de necks e capped necks. A
cirurgia corta essas gargantas, cola calotas e continua o fluxo. O número de
cirurgias é finito em cada intervalo temporal finito sob as hipóteses do
programa.

Isso permite à GDQ formular a cadeia

$$
\text{background inicial}
\longrightarrow
\text{neckpinches}
\longrightarrow
\text{cirurgia}
\longrightarrow
\text{componentes estáveis}.
$$

Porém o artigo usa expressões equivalentes a “vários necks” e permite regiões
possivelmente desconectadas. Ele não fixa seu número em três.

## 4. Invariantes preservados pela cirurgia

Denote por

$$
Q_G(\Sigma_a)
$$

a carga topológica geracional de uma componente. Para que uma cirurgia não
apague ou crie gerações arbitrariamente, a GDQ precisa demonstrar:

$$
\frac{dQ_G}{d\tau}=0
$$

no fluxo regular e

$$
Q_G^{\rm antes}
=\sum_bQ_{G,b}^{\rm depois}
$$

na cirurgia.

O índice APS local calculado fornece uma candidata:

$$
Q_G(\Sigma_a)
=\operatorname{ind}_{\rm APS}D_{G,a}^+
=1.
$$

Se existem $N_G$ componentes primitivas, então

$$
Q_G^{\rm total}=N_G.
$$

Assim, a quantidade que Perelman pode preservar para a GDQ é o índice total.
Mas seu valor inicial ainda precisa ser calculado.

## 5. Teorema condicional GDQ--Perelman

Considere um background GDQ que satisfaça:

1. a redução Ricci--Bismut possui funcional de Lyapunov do tipo Perelman;
2. o fluxo é não colapsado nas escalas relevantes;
3. as singularidades admissíveis são neckpinches cirúrgicos;
4. o índice geracional total é preservado pelo fluxo e pela colagem;
5. o dado inicial possui

   $$
   Q_G^{\rm total}=3;
   $$

6. cada componente final primitiva possui índice local unitário.

Então

$$
\boxed{
N_G
=\sum_a\operatorname{ind}_{\rm APS}D_{G,a}^+
=Q_G^{\rm total}
=3.
}
$$

Além disso, a monotonicidade de $\mathcal W$ seleciona soluções solitônicas em
cada classe e exclui ciclos não triviais do fluxo.

Esse teorema é correto, mas a hipótese 5 não pode ser usada como derivação de
si mesma.

## 6. O que o corpus fornece para o valor inicial

O corpus contém três estruturas diferentes que não devem ser identificadas
sem um mapa:

1. três dimensões espaciais;
2. três câmaras/estômatos do bárion;
3. três gerações fermiônicas observadas.

Perelman trabalha com o primeiro item. A Q40 constrói o segundo. A Q28 procura
derivar o terceiro.

Nenhum teorema atual demonstra

$$
\text{três dimensões}
\Longrightarrow
\text{três câmaras bariônicas}
\Longrightarrow
\text{três gerações}.
$$

Usar essa cadeia sem um mapa seria circular.

## 7. O cálculo global necessário

O valor inicial deve vir de uma avaliação independente:

$$
\boxed{
Q_G^{\rm total}
=
\operatorname{Ind}
\slashed D_{B,A}^{+,\rm global}.
}
$$

Pela fórmula APS/Bismut,

$$
Q_G^{\rm total}
=
\int_{M_{\rm global}}
\widehat A(TM)
\operatorname{ch}(E_G)
-\sum_a\bar\eta_a.
$$

Perelman garante que esse valor, uma vez calculado e preservado, organiza os
limites estáveis. Ele não fornece o valor numérico da integral para o fibrado
GDQ.

## 8. Conclusão

$$
\boxed{
\text{Perelman fecha estabilidade, convergência e cirurgia; não fixa sozinho
}N_G=3.
}
$$

$$
\boxed{
N_G=3\text{ será teorema quando o índice global inicial da GDQ for calculado
e resultar em }3.
}
$$

Referências internas ao OCR:

- [[../manuscrito/ref/Perelman - The entropy formula for the Ricci flow (2002)/pages/page-5/markdown|Perelman, fluxo gradiente e monotonicidade]];
- [[../manuscrito/ref/Perelman - The entropy formula for the Ricci flow (2002)/pages/page-31/markdown|Perelman, soluções antigas em dimensão três]];
- [[../manuscrito/ref/Perelman - The entropy formula for the Ricci flow (2002)/pages/page-37/markdown|Perelman, quadro global e cirurgia]].

## 9. Status

$$
\boxed{
\text{aplicação de Perelman concluída; índice global inicial permanece o
único dado de contagem não calculado.}
$$
