# Q28 — Ação on-shell nos setores topológicos

## 1. Forma quadrática induzida pela ação oficial

Na fibração métrica derivada anteriormente, a parte fisicamente positiva da
forma quadrática da conexão é, após fixar a orientação euclidiana estável,

$$
I_A
=C_{\rm GDQ}
\int_{T^4}
w\operatorname{tr}(F\wedge *_4F),
$$

onde

$$
C_{\rm GDQ}>0,
\qquad
w=r^5\mathcal U_B>0.
$$

O quinto ciclo e a fibra $S^3$ fornecem fatores positivos de volume e de
normalização, que foram absorvidos em $C_{\rm GDQ}$.

## 2. Limite topológico

Em quatro dimensões,

$$
0\le
\int_{T^4}
w\operatorname{tr}
\left[(F\mp *_4F)\wedge *_4(F\mp *_4F)\right].
$$

Para peso constante no background homogêneo, segue

$$
\int_{T^4}
w\operatorname{tr}(F\wedge *_4F)
\ge
8\pi^2w|A|,
$$

com

$$
A
=-\frac{1}{8\pi^2}
\int_{T^4}\operatorname{tr}(F\wedge F).
$$

A igualdade é atingida por conexões auto-duais ou anti-auto-duais, conforme a
orientação. Assim,

$$
\boxed{
I_A^{\rm on\mbox{-}shell}
=8\pi^2C_{\rm GDQ}w|A|
}
$$

no setor homogêneo mínimo.

## 3. Seleção entre setores

Se a colagem $\mathbb Z_6$ restringe

$$
A\in6\mathbb Z,
$$

então a sequência de ações mínimas é proporcional a

$$
0,6,12,18,24,\ldots
$$

O mínimo absoluto é

$$
A=0.
$$

Se uma condição global excluir o setor trivial, o mínimo orientado positivo é

$$
A=6,
$$

que forneceria

$$
N_G=1,
$$

e não três.

Portanto,

$$
\boxed{
\text{a forma quadrática homogênea da ação oficial não seleciona }A=18.
}
$$

## 4. Consequência lógica

O resultado não invalida a relação

$$
N_G=\frac{A}{6}.
$$

Ele mostra que a cardinalidade três não pode ser obtida apenas minimizando a
energia de uma conexão homogênea em todos os setores topológicos. Uma das
seguintes informações adicionais, já pertencente à geometria global, é
necessária:

1. uma condição de contorno que fixe diretamente $A=18$;
2. três componentes topológicas obrigatórias, cada uma com carga mínima
   $A=6$;
3. retroação dos módulos $r$, $G_{ij}$ e $f$ que torne a ação on-shell não
   linear em $A$ e possua extremo estável em $18$;
4. uma restrição de regularidade que exclua $A=0,6,12$;
5. uma lei causal de conservação que determine o setor inicial.

As opções 1 e 2 só constituem derivação se a condição ou as três componentes
forem obtidas independentemente do número de gerações observado.

## 5. Equações para a retroação completa

O próximo teste não deve variar apenas $A_i^{\ a}$. Deve resolver
simultaneamente

$$
D_i\left(r^5\mathcal U_BF^{ij}\right)=0,
$$

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta r}=0,
$$

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta G_{ij}}=0,
$$

$$
\frac{\delta\mathcal S_{\rm GDQ}}{\delta f}=0.
$$

Somente depois de eliminar os módulos,

$$
(r,G,f)=(r_A,G_A,f_A),
$$

obtém-se a função efetiva correta

$$
I_{\rm eff}(A)
=\mathcal S_{\rm GDQ}[A,r_A,G_A,f_A].
$$

Um fechamento preditivo de três gerações exige demonstrar

$$
I_{\rm eff}'(18)=0,
\qquad
I_{\rm eff}''(18)>0,
$$

na continuação discreta apropriada, ou provar que apenas $A=18$ pertence ao
domínio global admissível.

## 6. Status

A comparação on-shell foi concluída para a aproximação homogênea. Seu
resultado é negativo para a seleção espontânea de três gerações. A pendência
foi reduzida à retroação completa dos módulos ou a uma condição global
independentemente derivada.
