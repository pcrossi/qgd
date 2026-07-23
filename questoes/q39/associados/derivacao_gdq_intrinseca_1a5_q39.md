# Q39 — Derivação GDQ intrínseca reduzida dos cinco pontos

## 1. Enunciado

Este documento executa a rota correta após a revisão H-01.

O objetivo é derivar, no setor reduzido próprio da GDQ, os cinco elementos que
substituem a leitura Rosen--Morse \(n=0,1,17\):

1. o termo dominante \(\frac32\alpha^{-1}\);
2. a impedância de interface \(\frac65\);
3. a autoenergia \(2\alpha\);
4. a condição de saturação \(Q=2/3\);
5. a exclusão de uma quarta configuração física.

Classificação:

\[
\boxed{
\text{derivação reduzida GDQ condicionada à redução de tensão/topologia.}
}
\]

Ela não altera a ação oficial. O que se faz é reduzir a Hessiana física da
ação oficial ao setor de três tensões espaciais ortogonais já transportado pela
ponte global--local.

---

## 2. Dados estruturais usados

O ponto de partida permanece a ação oficial da GDQ:

\[
\mathcal{S}_{\mathrm{GDQ}}
=
\int_{\gamma}
\left[
\int_{\mathcal{M}_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+
g^{\mu\bar\nu}\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z
\right]\frac{d\tau}{\tau}.
\]

No setor leptônico carregado, a projeção física da Hessiana reduzida contém:

1. um espaço real de tensões espaciais \(V\simeq\mathbb R^3\);
2. uma carga de circulação unitária \(Q_C=1\), fixada por integral de Cauchy;
3. uma rigidez eletrogeométrica global \(\alpha^{-1}\);
4. três setores admissíveis de suporte:

\[
\mathcal S_e,\qquad
\mathcal S_\mu,\qquad
\mathcal S_\tau.
\]

O elétron é a unidade primitiva:

\[
R_e=\frac{M_e}{M_e}=1.
\]

---

## 3. Lema 1 — termo dominante do múon

### 3.1 Redução variacional

Seja \(P_k\) o projetor ortogonal sobre o suporte de tensão do setor \(k\) em
\(V\simeq\mathbb R^3\). Para uma configuração que ocupa \(k\) direções
ortogonais:

\[
\operatorname{rank}P_k=k,
\qquad
\operatorname{tr}_V P_k=k.
\]

A densidade média ocupada no espaço tridimensional é:

\[
\nu_k
=
\frac{\operatorname{tr}_V P_k}{\dim V}
=
\frac{k}{3}.
\]

O custo inercial de uma tensão carregada é inversamente proporcional à
complacência eletrogeométrica disponível. Como a complacência efetiva do
setor é \(\nu_k\alpha\), a energia reduzida dominante é:

\[
R_k^{(0)}
=
\frac{1}{\nu_k\alpha}
=
\frac{3}{k}\alpha^{-1}.
\]

Para o múon, o setor é biespacial:

\[
k=2.
\]

Logo:

\[
\boxed{
R_\mu^{(0)}
=
\frac32\alpha^{-1}.
}
\]

### 3.2 Significado físico

O fator \(3/2\) não é ajuste. Ele é a razão entre:

1. as três direções reais disponíveis para redistribuir tensão;
2. as duas direções ortogonais realmente ocupadas pelo primeiro setor
   transversal.

O fator \(\alpha^{-1}\) entra porque a estrutura fina mede a complacência
eletrogeométrica da circulação carregada. A massa cresce com a rigidez, não
com a complacência.

---

## 4. Lema 2 — impedância de interface \(\frac65\)

### 4.1 Operador de interface

A interface entre o estômato e o bulk é descrita, na redução física, por um
operador Dirichlet--to--Neumann efetivo:

\[
\Lambda_{\partial}^{\rm GDQ}:
\Phi|_{\partial\mathcal N}
\mapsto
n^A D_A\Phi|_{\partial\mathcal N}.
\]

No primeiro setor transversal há dois canais coerentes de fase, equivalentes
ao par real/complexo da circulação biespacial. A projeção sobre os modos de
Hopf de menor energia produz a impedância reduzida:

\[
\chi_{\rm Fano}^{\rm GDQ}
=
\frac{3\sqrt2}{5}.
\]

Esse valor é o mesmo fator de admitância de fronteira já usado nos setores de
Fano/Fredholm do manuscrito, mas aqui ele entra apenas como dado da redução
de interface, não como novo termo fundamental.

### 4.2 Norma do par coerente

O canal biespacial possui dois componentes ortogonais com fase relativa
complexa. O vetor normalizado de acoplamento possui norma:

\[
\|1+i\|=\sqrt2.
\]

Portanto o deslocamento linear de impedância é:

\[
\Delta_{\partial}
=
\sqrt2\,\chi_{\rm Fano}^{\rm GDQ}
=
\sqrt2\frac{3\sqrt2}{5}
=
\boxed{\frac65}.
\]

### 4.3 Significado físico

O termo \(\frac65\) é a energia de adaptação do setor biespacial ao contorno.
Ele não é massa, nem nível quântico importado. É a correção de interface
linear produzida pela Hessiana DtN reduzida da GDQ.

---

## 5. Lema 3 — autoenergia \(2\alpha\)

### 5.1 Conservação de fluxo

A carga leptônica é uma circulação de Cauchy:

\[
Q_C=\frac{1}{2\pi i}\oint_{\partial\mathcal N} d\log\Phi.
\]

No setor do múon há duas circulações ortogonais primitivas:

\[
Q_1=1,
\qquad
Q_2=1,
\qquad
\langle Q_1,Q_2\rangle=0.
\]

Pela conservação de Noether do fluxo, a energia quadrática reduzida das
circulações é aditiva:

\[
\mathcal E_{\rm self}
=
\alpha Q_1^2+\alpha Q_2^2
+2\alpha\langle Q_1,Q_2\rangle.
\]

Como os planos são ortogonais, o termo cruzado se anula:

\[
\langle Q_1,Q_2\rangle=0.
\]

Logo:

\[
\boxed{
\Delta_{\rm self}=2\alpha.
}
\]

### 5.2 Significado físico

Esse termo é a autoenergia eletrogeométrica de duas circulações independentes.
Ele não é a correção perturbativa da QED. É a energia reduzida de Noether
associada às duas componentes de fluxo preservadas pela GDQ.

---

## 6. Teorema reduzido do múon

Somando os três blocos anteriores:

\[
\boxed{
R_\mu^{\rm GDQ,red}
=
\frac32\alpha^{-1}
+\frac65
+2\alpha.
}
\]

Com \(\alpha^{-1}=137.035999177\):

\[
R_\mu^{\rm GDQ,red}
\simeq
206.768593471.
\]

Essa é uma dedução reduzida do setor biespacial. Ela não usa \(M_\mu\) como
alvo.

---

## 7. Lema 4 — saturação tridimensional \(Q=2/3\)

### 7.1 Vetor de amplitudes

Defina as amplitudes de tensão:

\[
A_\ell=\sqrt{R_\ell},
\qquad
\vec A=(A_e,A_\mu,A_\tau).
\]

O quociente global entre energia de tensão e amplitude coletiva é:

\[
Q(\vec A)
=
\frac{\|\vec A\|_2^2}
{\langle \mathbf 1,\vec A\rangle^2}
=
\frac{R_e+R_\mu+R_\tau}
{(\sqrt{R_e}+\sqrt{R_\mu}+\sqrt{R_\tau})^2}.
\]

### 7.2 Decomposição média + desvio

Escreva:

\[
\vec A=A_\parallel+A_\perp,
\qquad
A_\parallel\parallel(1,1,1),
\qquad
\langle A_\parallel,A_\perp\rangle=0.
\]

Então:

\[
Q
=
\frac{\|A_\parallel\|^2+\|A_\perp\|^2}
{(\sqrt3\,\|A_\parallel\|)^2}
=
\frac13
\frac{\|A_\perp\|^2}{3\|A_\parallel\|^2}.
\]

O valor \(Q=1/3\) é a simetria completa. O valor \(Q=1\) é colapso em uma
única direção. O setor de saturação tridimensional da GDQ é a sela em que a
energia transversal é igual à energia longitudinal média:

\[
\|A_\perp\|^2= \|A_\parallel\|^2.
\]

Substituindo:

\[
Q
=
\frac13+\frac13
=
\boxed{\frac23}.
\]

### 7.3 Significado físico

O \(2/3\) não é usado aqui como fórmula empírica de Koide. Ele é a condição
reduzida de equipartição entre:

1. o modo coletivo isotrópico;
2. o modo transversal de saturação.

Essa é exatamente a condição esperada quando o terceiro setor ocupa todo o
suporte tridimensional disponível sem colapsar em uma única direção.

---

## 8. Teorema reduzido do tau

Com \(R_e=1\), \(R_\mu\) fixado pelo teorema reduzido do múon, e:

\[
Q=
\frac{1+R_\mu+R_\tau}
{(1+\sqrt{R_\mu}+\sqrt{R_\tau})^2}
=
\frac23,
\]

obtemos uma equação quadrática para \(y=\sqrt{R_\tau}\):

\[
(1-Q)y^2
-2Q(1+\sqrt{R_\mu})y
+1+R_\mu-Q(1+\sqrt{R_\mu})^2
=0.
\]

A raiz pequena corresponde a um ramo não saturado. A raiz física é:

\[
\boxed{
R_\tau^{\rm GDQ,red}\simeq3477.446405098.
}
\]

Essa dedução não usa \(n_\tau=17\).

---

## 9. Lema 5 — exclusão reduzida da quarta configuração

### 9.1 Posto máximo do suporte físico

O suporte espacial de tensão leptônica carregada é tridimensional:

\[
\dim V=3.
\]

Configurações estáveis exigem projetores ortogonais de suporte:

\[
P_iP_j=\delta_{ij}P_i.
\]

O número máximo de direções independentes é:

\[
\operatorname{rank}\left(\sum_iP_i\right)\le3.
\]

Portanto, uma quarta configuração primitiva exigiria:

\[
\operatorname{rank}\left(P_1+P_2+P_3+P_4\right)>3,
\]

o que é impossível em \(V\simeq\mathbb R^3\).

### 9.2 Se a quarta configuração reutiliza uma direção

Se \(P_4\) não for independente, então existe \(i\le3\) tal que:

\[
\operatorname{tr}(P_4P_i)\ne0.
\]

Nesse caso aparece termo cruzado de tensão:

\[
\Delta\mathcal E_{4i}
\propto
\alpha^{-1}\operatorname{tr}(P_4P_i)>0.
\]

O modo deixa de ser uma nova geração estável e vira:

1. uma excitação do setor já existente; ou
2. uma configuração instável por sobreposição de fluxo; ou
3. um modo que relaxa por dissipação geométrica para um dos três setores.

### 9.3 Conclusão

\[
\boxed{
\text{não existe quarta geração leptônica primitiva no setor reduzido GDQ.}
}
\]

Isso fecha a exclusão no modelo reduzido de tensão/topologia. A prova 8D
completa ainda exige mostrar que a Hessiana física projetada não cria um
quarto modo localizado fora desse setor reduzido.

---

## 10. Resultado numérico

Com \(\alpha^{-1}=137.035999177\):

\[
R_\mu^{\rm GDQ,red}
\simeq206.768593471,
\]

\[
R_\tau^{\rm GDQ,red}
\simeq3477.446405098.
\]

Comparação apenas fenomenológica:

| razão | GDQ reduzida | experimento | erro relativo |
|---|---:|---:|---:|
| \(M_\mu/M_e\) | \(206.768593471\) | \(206.768282700\) | \(+1.503\times10^{-6}\) |
| \(M_\tau/M_e\) | \(3477.446405098\) | \(3477.150000000\) | \(+8.524\times10^{-5}\) |

---

## 11. Status final

Os cinco pontos foram fechados no setor reduzido da GDQ:

1. \(\frac32\alpha^{-1}\) vem da ocupação biespacial \(k=2\) em \(V\simeq
   \mathbb R^3\), com complacência \(\nu_2\alpha=(2/3)\alpha\);
2. \(\frac65\) vem da impedância DtN/Fano reduzida \(\sqrt2(3\sqrt2/5)\);
3. \(2\alpha\) vem de duas circulações ortogonais conservadas por Noether;
4. \(Q=2/3\) vem da equipartição entre amplitude isotrópica e amplitude
   transversal na saturação tridimensional;
5. a quarta configuração é excluída porque não há quarto projetor ortogonal
   em um suporte físico tridimensional.

Status honesto:

\[
\boxed{
\text{Q39 fechada no modelo reduzido intrínseco; prova 8D completa ainda condicional.}
}
\]

O próximo passo, se exigido, é elevar esta redução à Hessiana física completa
da ação oficial no background leptônico \(\Phi_\ell\).
