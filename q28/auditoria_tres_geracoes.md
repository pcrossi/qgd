# Q28 — Auditoria topológica da afirmação de três gerações

## 1. Pergunta

Os rascunhos anteriores usavam

$$
N_G=|h^{1,1}-h^{2,1}|=3
$$

e associavam esse número a

$$
T^5\times S^3.
$$

É necessário verificar se essa igualdade decorre da topologia declarada.

## 2. Cohomologia real pelo teorema de Künneth

O polinômio de Poincaré do toro é

$$
P_{T^5}(t)=(1+t)^5.
$$

Para a 3-esfera,

$$
P_{S^3}(t)=1+t^3.
$$

Logo,

$$
P_{T^5\times S^3}(t)
=(1+t)^5(1+t^3).
$$

Os números de Betti são

$$
\boxed{
(b_0,b_1,\ldots,b_8)
=(1,5,10,11,10,11,10,5,1).
}
$$

A característica de Euler é

$$
\chi(T^5\times S^3)
=\sum_{k=0}^8(-1)^kb_k
=0.
$$

Nenhum desses invariantes fornece automaticamente $N_G=3$.

## 3. Problema com os números de Hodge

Os números

$$
h^{p,q}
$$

dependem de uma estrutura complexa e, em geral, de propriedades adicionais
como Kähleridade para possuírem as interpretações usadas em compactificações
complexas usuais.

A topologia real de $T^5\times S^3$, sozinha, não determina

$$
h^{1,1}
$$

nem

$$
h^{2,1}.
$$

Mesmo que uma estrutura complexa Hermitiana seja escolhida, seus números de
Hodge precisam ser calculados para essa estrutura concreta. Portanto,

$$
\boxed{
|h^{1,1}-h^{2,1}|=3
}
$$

não é atualmente um teorema da geometria global declarada.

## 4. O que o cálculo local realmente permite

O protótipo APS demonstrou:

$$
\operatorname{ind}_{\rm APS}D_{G,a}^+=1
$$

para cada estômato elementar orientado da classe mínima.

Consequentemente, se o background possuir $N_G$ componentes estáveis
equivalentes,

$$
\operatorname{Ind}_{G_{\rm gauge}}
=N_G\mathcal E_{\rm gen}.
$$

O índice local determina a contribuição por estômato. Ele não determina o
número de estômatos.

## 5. Teorema ainda necessário

Para derivar três gerações, a GDQ deve demonstrar uma destas alternativas:

1. **teorema de estabilidade:** a ação oficial possui exatamente três classes
   estáveis de estômatos geracionais;
2. **índice global:** um operador global calculado possui índice total três;
3. **Morse/monodromia:** somente três componentes do espaço de módulos têm
   Hessiana não negativa e holonomia admissível;
4. **estrutura complexa concreta:** construir a estrutura Hermitiana global,
   calcular seus grupos de cohomologia relevantes e demonstrar que o índice é
   três.

Não é suficiente usar a trimodalidade bariônica $n_B=3$: ela conta câmaras de
um bárion, não gerações leptônicas ou famílias quirais, salvo se um mapa entre
os dois problemas for demonstrado.

## 6. Status

$$
\boxed{
\text{a contribuição local unitária está provada; }N_G=3
\text{ permanece como teorema global aberto.}
}
$$

Esse resultado negativo remove uma justificativa não demonstrada e deixa a
pendência em forma matematicamente precisa.
