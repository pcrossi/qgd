# Q24 — Resultado único por bacias reais da microgeometria

## 1. Objetivo

Provar, no domínio apropriado da GDQ, que um evento de medição produz um único
registro real.

A prova não usa colapso fundamental nem altera a ação oficial. Ela usa:

1. a Hessiana física GDQ com contorno do aparelho;
2. a decomposição espectral em setores de registro;
3. a existência de bacias de atração no espaço real de microgeometrias do
   aparelho e ambiente.

O resultado é um teorema condicional:

\[
\boxed{
\text{se o espaço microgeométrico }A+E\text{ possui bacias Morse estáveis,
então quase todo evento termina em um único }R_i.
}
\]

---

## 2. Espaço de configurações real do aparelho

Seja:

\[
\boxed{
\mathcal C_{A+E}
=
\{(g,f,\bar f;\xi_{\rm app})\text{ compatíveis com o contorno do aparelho}\}/\mathcal G
}
\]

o espaço físico de microgeometrias do aparelho e ambiente, depois da remoção
dos modos de gauge/difeomorfismos \(\mathcal G\).

O acoplamento com o sistema define um funcional efetivo aberto:

\[
\boxed{
\mathfrak F_{\rm meas}[\Phi]
=
\operatorname{Re}\mathcal S_{\rm GDQ}^{S+A+E}[\Phi]
\quad
\text{restrito à janela de medição.}
}
\]

Aqui \(\Phi\in\mathcal C_{A+E}\). Fontes e contornos do aparelho entram como
dados de problema, não como nova ação fundamental.

---

## 3. Hipóteses dinâmicas mínimas

### H1 — Regularidade

\(\mathcal C_{A+E}\) é uma variedade de Banach/Hilbert localmente modelada no
setor físico projetado, e \(\mathfrak F_{\rm meas}\) é \(C^2\) no domínio
relevante.

### H2 — Funcional de Lyapunov

A dinâmica aberta reduzida satisfaz:

\[
\boxed{
\frac{d}{d\tau}\mathfrak F_{\rm meas}[\Phi(\tau)]
\le0.
}
\]

Na forma de fluxo gradiente:

\[
\boxed{
\dot\Phi
=
-\mathsf M(\Phi)\nabla\mathfrak F_{\rm meas}[\Phi],
\qquad
\mathsf M\ge0.
}
\]

### H3 — Registros como mínimos hiperbólicos

Cada registro \(R_i\) corresponde a um ponto crítico hiperbólico estável:

\[
\boxed{
\nabla\mathfrak F_{\rm meas}(R_i)=0,
\qquad
\operatorname{Hess}_{R_i}^{\rm phys}\mathfrak F_{\rm meas}>0.
}
\]

### H4 — Separação por selas

As fronteiras entre bacias são variedades estáveis de pontos críticos
instáveis ou selas:

\[
\boxed{
\partial\mathcal B_i
\subset
\bigcup_\alpha W^s(S_\alpha).
}
\]

### H5 — Medida física regular

A medida inicial da microgeometria real do aparelho, condicionada ao estado
preparado, é absolutamente contínua em relação à medida física induzida por
\(\mathcal U_*\):

\[
\boxed{
d\mu_{\rm init}
=
\varpi(\Phi)\,d\mu_{\mathcal U},
\qquad
\varpi\in L^1.
}
\]

---

## 4. Definição das bacias

A bacia do registro \(R_i\) é:

\[
\boxed{
\mathcal B_i
=
\left\{
\Phi_0\in\mathcal C_{A+E}:
\lim_{\tau\to\infty}\Phi(\tau;\Phi_0)=R_i
\right\}.
}
\]

Pela estabilidade hiperbólica, cada \(\mathcal B_i\) é aberta no domínio
físico.

Como os registros são separados pelo gap espectral da Q24:

\[
\boxed{
R_i\ne R_j
\Rightarrow
\mathcal B_i\cap\mathcal B_j=\varnothing.
}
\]

Logo:

\[
\boxed{
\mathcal C_{A+E}^{\rm reg}
=
\bigcup_i\mathcal B_i
\;\dot\cup\;
\mathcal N,
}
\]

onde \(\mathcal N\) é o conjunto que cai em selas, modos neutros não
resolvidos ou fronteiras de bacia.

---

## 5. Medida nula das fronteiras

Pelo teorema da variedade estável para fluxos hiperbólicos, a variedade
estável de uma sela possui codimensão pelo menos 1 no espaço físico.

Assim:

\[
\boxed{
\mu_{\mathcal U}(W^s(S_\alpha))=0.
}
\]

Como:

\[
\mathcal N
\subset
\bigcup_\alpha W^s(S_\alpha),
\]

segue:

\[
\boxed{
\mu_{\rm init}(\mathcal N)=0.
}
\]

Portanto, para quase toda microgeometria inicial:

\[
\boxed{
\Phi_0\in\mathcal B_i
\text{ para um único }i.
}
\]

Isso é o resultado único no setor aberto: cada evento real pertence a uma
bacia e converge para um registro.

---

## 6. Probabilidades das bacias

A probabilidade do registro \(i\) é a medida da bacia:

\[
\boxed{
\mathbb P(R_i)
=
\mu_{\rm init}(\mathcal B_i).
}
\]

Pela construção da Q24, o aparelho implementa o projetor \(P_i\) da Q22:

\[
\boxed{
P_i
\longleftrightarrow
\Pi_i
\longleftrightarrow
\mathcal B_i.
}
\]

Logo a medida inicial condicionada satisfaz:

\[
\boxed{
\mu_{\rm init}(\mathcal B_i)
=
\operatorname{Tr}(\rho_SP_i).
}
\]

No caso puro discreto:

\[
\boxed{
\mathbb P(R_i)=|c_i|^2.
}
\]

Born não foi inserido como peso geométrico ad hoc. Ele entra como medida
operacional já derivada na Q22; a Q24 prova que o aparelho realiza essa
decomposição por bacias físicas.

---

## 7. Teorema

Sob H1--H5, para quase toda condição inicial da microgeometria real do
aparelho/ambiente, existe um único índice \(i\) tal que:

\[
\boxed{
\lim_{\tau\to\infty}\Phi(\tau)=R_i.
}
\]

Além disso:

\[
\boxed{
\mathbb P(R_i)
=
\operatorname{Tr}(\rho_SP_i).
}
\]

Portanto:

\[
\boxed{
\text{resultado único}
=
\text{seleção quase certa de uma bacia real da microgeometria }A+E.
}
\]

---

## 8. Interpretação física

Antes da medição, vários registros são possibilidades dinâmicas. Durante a
interação, o aparelho altera o contorno e deforma o funcional efetivo. A
microgeometria concreta do aparelho/ambiente não é um vetor abstrato sem
estado; ela possui flutuações e condições iniciais reais. Essas condições
iniciais colocam o sistema em uma bacia específica:

\[
\Phi_0\in\mathcal B_k.
\]

O fluxo dissipativo aberto então conduz:

\[
\Phi(\tau)\to R_k.
\]

Assim, o colapso não é uma regra cinemática fundamental. É a estabilização de
um atrator real no setor aberto da medição.

---

## 9. Limites da prova

Esta prova depende das hipóteses H1--H5. Para um aparelho concreto, ainda é
preciso demonstrar:

1. existência dos mínimos \(R_i\);
2. hiperbolicidade da Hessiana física;
3. gap setorial;
4. ausência de componentes neutras não resolvidas;
5. regularidade da medida inicial.

Quando esses itens forem verificados, o resultado único deixa de ser hipótese
ontológica naquele aparelho e vira teorema dinâmico aplicado.

---

## 10. Status

\[
\boxed{
\text{resultado único provado condicionalmente pelo teorema de bacias reais.}
}
\]

Isso melhora o status anterior da Q24:

\[
\text{hipótese dinâmica de bacia}
\quad\longrightarrow\quad
\text{teorema condicional de bacias}.
\]

A condição restante não é conceitual; é verificar H1--H5 para cada classe de
aparelho.
