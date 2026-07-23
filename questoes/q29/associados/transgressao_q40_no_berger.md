# Q29 — Transgressão documentada da Q40 no ansatz de Berger

## 1. Dependência geométrica disponível

O termo usado anteriormente foi escrito como

$$
V_\partial
=\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3}\right).
$$

Para Berger, a contribuição Chern--Simons permanece topológica:

$$
V_{\rm CS}=\alpha\frac{3\pi}{2}.
$$

Ela não depende de $R$ ou $q$ e, portanto, não estabiliza o squashing.

A correção espectral foi definida por

$$
\lambda_{\rm throat}^{(3)}
=\frac{3}{\operatorname{Vol}(S^3)\operatorname{Vol}(S^1)}.
$$

Como

$$
\operatorname{Vol}(S^3_{R,q})=2\pi^2R^3q,
\qquad
\operatorname{Vol}(S^1)=2\pi,
$$

sua extensão direta é

$$
\boxed{
V_\partial(R,q)
=\alpha\left[
\frac{3\pi}{2}
+\frac{3}{4\pi^3R^3q}
\right].
}
$$

## 2. Teste variacional

Esse termo foi somado ao funcional homogêneo de Berger e as equações
$\partial_RV=\partial_qV=0$ foram resolvidas a partir de múltiplas sementes.
Os extremos continuam saddles: nenhuma solução apresentou Hessiana positiva.

Isso era esperado estruturalmente. Para $q\to\infty$,

$$
V_{\rm CS}=\text{constante},
\qquad
V_{\rm throat}\sim q^{-1},
$$

enquanto o bulk contém a direção runaway proporcional a $-q^2/R^2$. Portanto,
a transgressão documentada não cresce o suficiente para confinar o squashing.

## 3. Consequência para a quártica da Q29

O coeficiente

$$
\alpha\left(\frac{3\pi}{2}+\frac{3}{4\pi^3}\right)
$$

foi usado anteriormente como rigidez positiva multiplicando a variação de
área do modo $\ell=1$. A presente auditoria mostra que sua interpretação como
energia elástica métrica não segue apenas da fórmula topológica/espectral da
Q40. Os próprios documentos da Q40 registram que falta derivar essa expressão
diretamente da ação oficial ou de uma ação efetiva derivada.

Portanto, a positividade da quártica de interface da Q29 deve ser classificada
como **condicional à existência da rigidez métrica de interface**, não como
consequência já encerrada da transgressão topológica.

## 4. O termo que realmente seria necessário

Uma estabilização de Berger exige uma contribuição que cresça com a deformação,
por exemplo uma Hessiana de cisalhamento obtida da ação oficial,

$$
V_{\rm shear}
=\frac12\mu_\partial
\int_{S^3}|h^{\rm TF}|^2dA+\cdots,
$$

mas $\mu_\partial$ não pode ser introduzido por analogia elástica. Ele deve ser
o complemento de Schur dos modos métrico-dilatônicos/torsionais de interface.

## 5. Veredito

$$
\boxed{
\text{a transgressão Q40 disponível não estabiliza Berger.}
}
$$

A rota somente permanece aberta se a Hessiana oficial de interface produzir
uma rigidez de cisalhamento adicional positiva.

O vínculo de Noether foi posteriormente reintroduzido com a densidade
torsional como variável independente. A Hessiana KKT projetada coincide
exatamente com a Hessiana reduzida usada aqui; ver
`questoes/q29/associados/noether_berger_hessiana_vinculada.md`.
