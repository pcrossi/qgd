# Q30 — Três lemas da equivalência operacional GDQ--Yang--Mills

## 1. Dados e domínio

Trabalha-se no setor físico tubular já reduzido, com:

1. elongações excluídas, $S=0$;
2. carga torsional e orientação preservadas;
3. mapa topológico bijetivo

$$
\Theta:
\mathfrak T_{\rm GDQ}\longrightarrow\mathfrak T_{\rm YM};
$$

4. operador regular de Heaviside

$$
P_\mu=-\Delta+\mu^2,
\qquad \mu>0;
$$

5. remoção de $\mu$ somente depois da subtração do modo constante.

Yang--Mills é tomado axiomaticamente por sua álgebra física de holonomias e
por um estado de vácuo positivo, normalizado, invariante e único no setor em
questão.

## 2. Álgebra de geradores

Antes do traço, sejam $U_C$ os transportes paralelos associados a caminhos.
As relações geométricas são

$$
U_{C_1\circ C_2}=U_{C_1}U_{C_2},
\qquad
U_{C^{-1}}=U_C^*,
\qquad
U_{\mathrm{id}}=1.
$$

Depois do fechamento e do traço, obtêm-se os observáveis de Wilson/holonomia.
As relações de traço e representação são preservadas porque o mapa não altera
a representação interna, apenas transporta a classe do caminho.

Defina nos geradores

$$
\boxed{
\mathfrak H_\Theta(U_C^{\rm YM})
:=U_{\Theta^{-1}C}^{\rm GDQ}.
}
$$

Nos observáveis de resposta, use o cálculo funcional

$$
\boxed{
\mathfrak H_\Theta[F(P_\mu^{\rm YM})]
:=F(P_\mu^{\rm GDQ,red}).
}
$$

No setor confinante, os dois lados são identificados pela mesma função de
transferência

$$
F_\mu(k^2)
=-\frac{8\pi\sigma}{(k^2+\mu^2)^2}.
$$

## 3. Lema 1 — Boa definição no quociente

> **Lema 1.** $\mathfrak H_\Theta$ independe do representante topológico e
> de gauge escolhido.

### Prova

Se $C\sim C'$ no quociente de Yang--Mills, então representam a mesma classe
$[C]=[C']$. Como $\Theta$ é definida nas classes,

$$
\Theta^{-1}[C]=\Theta^{-1}[C'].
$$

Logo, os transportes GDQ correspondentes diferem, no máximo, por conjugação
nos extremos:

$$
U_{\Theta^{-1}C'}
=g^{-1}U_{\Theta^{-1}C}g.
$$

Para laços fechados, o traço elimina a conjugação:

$$
\operatorname{tr}(g^{-1}Ug)=\operatorname{tr}U.
$$

Para operadores, uma troca de frame atua por conjugação unitária,
$P_\mu\mapsto VP_\mu V^{-1}$. O cálculo funcional satisfaz

$$
F(VP_\mu V^{-1})=VF(P_\mu)V^{-1}.
$$

Portanto, classes e observáveis gauge-invariantes têm imagem única.

$$
\boxed{\mathfrak H_\Theta\text{ é bem definido no quociente.}}
$$

## 4. Lema 2 — Preservação das relações

> **Lema 2.** $\mathfrak H_\Theta$ preserva unidade, produto, involução,
> composição de caminhos e relações funcionais de Heaviside.

### Prova

Como $\Theta$ preserva composição e orientação,

$$
\begin{aligned}
\mathfrak H_\Theta(U_{C_1\circ C_2})
&=U_{\Theta^{-1}(C_1\circ C_2)}\\
&=U_{\Theta^{-1}C_1\circ\Theta^{-1}C_2}\\
&=U_{\Theta^{-1}C_1}U_{\Theta^{-1}C_2}\\
&=\mathfrak H_\Theta(U_{C_1})
\mathfrak H_\Theta(U_{C_2}).
\end{aligned}
$$

Além disso,

$$
\mathfrak H_\Theta(1)=1,
$$

$$
\mathfrak H_\Theta(U_C^*)
=U_{\Theta^{-1}(C^{-1})}
=U_{(\Theta^{-1}C)^{-1}}
=\mathfrak H_\Theta(U_C)^*.
$$

Para o cálculo funcional, com $P_\mu$ positivo e auto-adjunto,

$$
(FG)(P_\mu)=F(P_\mu)G(P_\mu),
$$

$$
\overline F(P_\mu)=F(P_\mu)^*.
$$

Logo, toda relação algébrica satisfeita pelos geradores é enviada à mesma
relação. Pela propriedade universal da álgebra apresentada por geradores e
relações, o mapa se estende unicamente a um $*$-homomorfismo:

$$
\boxed{
\mathfrak H_\Theta:
\mathfrak A_{\rm YM}\longrightarrow\mathfrak A_{\rm GDQ}^{\rm red}.
}
$$

## 5. Lema 3 — Fidelidade, sobrejetividade e estado

> **Lema 3.** No setor físico reduzido, $\mathfrak H_\Theta$ é um
> $*$-isomorfismo e transporta o estado axiomático de Yang--Mills.

### Prova da bijetividade

Como $\Theta$ é bijetivo, existe $\Theta^{-1}$. Para $\mu>0$, $P_\mu$ não
possui modo zero e a função operacional confinante é não nula no espectro.
Define-se o mapa inverso nos geradores por

$$
\mathfrak K_\Theta(U_D^{\rm GDQ})
:=U_{\Theta D}^{\rm YM}
$$

e pela função operacional inversa no setor de resposta. Então

$$
\mathfrak K_\Theta\circ\mathfrak H_\Theta
=\operatorname{id}_{\mathfrak A_{\rm YM}},
$$

$$
\mathfrak H_\Theta\circ\mathfrak K_\Theta
=\operatorname{id}_{\mathfrak A_{\rm GDQ}^{\rm red}}.
$$

No limite $\mu\to0^+$, toma-se o quociente pelo modo constante, já que
$V\mapsto V+V_0$ não altera os observáveis. Assim, a inversa sobrevive no
espaço físico quocientado.

### Prova para o estado

Defina o estado transportado na álgebra de Yang--Mills por

$$
\widetilde\omega_{\rm YM}(O)
:=\omega_{\rm GDQ}(\mathfrak H_\Theta O).
$$

Ele é normalizado:

$$
\widetilde\omega_{\rm YM}(1)=1,
$$

e positivo:

$$
\widetilde\omega_{\rm YM}(O^*O)
=\omega_{\rm GDQ}
\left[
(\mathfrak H_\Theta O)^*(\mathfrak H_\Theta O)
\right]\ge0.
$$

Como $\Theta$ preserva orientação, composição e a ação das simetrias no setor
reduzido, $\widetilde\omega_{\rm YM}$ é invariante pelas mesmas simetrias do
estado axiomático. Pela hipótese axiomática de unicidade do vácuo nesse setor,

$$
\widetilde\omega_{\rm YM}=\omega_{\rm YM}.
$$

Portanto,

$$
\boxed{
\omega_{\rm GDQ}\circ\mathfrak H_\Theta
=\omega_{\rm YM}.
}
$$

## 6. Teorema de equivalência

Reunindo os três lemas:

> **Teorema de equivalência operacional.** Dado o mapa topológico bijetivo
> $\Theta$, a equivalência regular de Heaviside e a unicidade do estado de
> vácuo axiomático, o setor tubular físico reduzido da GDQ e o setor
> confinante de Yang--Mills possuem álgebras de observáveis
> $*$-isomorfas e estados entrelaçados.

Assim, para quaisquer observáveis $O_1,\ldots,O_n$ da álgebra,

$$
\boxed{
\langle O_1\cdots O_n\rangle_{\rm YM}
=
\left\langle
\mathfrak H_\Theta(O_1)\cdots
\mathfrak H_\Theta(O_n)
\right\rangle_{\rm GDQ}.
}
$$

Os correladores superiores seguem do isomorfismo; não precisam ser
reconstruídos individualmente.

## 7. Hipóteses usadas

1. bijetividade topológica de $\Theta$ no setor considerado;
2. mesma representação interna para as relações de holonomia;
3. positividade e auto-adjuncidade de $P_\mu$ para $\mu>0$;
4. quociente pelo modo constante quando $\mu\to0$;
5. positividade, invariância e unicidade do estado axiomático de vácuo;
6. positividade do estado GDQ na thimble física escolhida.

A hipótese 6 é exatamente onde a construção global da thimble entra. Se a
positividade do estado GDQ ainda for apenas setorial, o teorema permanece
setorial/condicional nessa mesma extensão, sem afetar os dois primeiros lemas.

## 8. Classificação

- Lema 1: demonstrado a partir de $\Theta$ e invariância por conjugação;
- Lema 2: demonstrado por composição e cálculo funcional;
- Lema 3 algébrico: demonstrado para $\mu>0$ e no quociente físico;
- igualdade do estado: condicional à unicidade axiomática e positividade da
  thimble GDQ;
- equivalência: fechada condicionalmente no setor físico declarado.

