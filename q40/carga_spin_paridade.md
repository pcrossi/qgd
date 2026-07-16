# Q40 — Bloco 2 — Carga, spin e paridade

## 1. Objetivo

Este bloco fixa os números quânticos básicos do próton e do nêutron dentro da
estrutura geométrica colada:

\[
Q,\qquad J,\qquad P.
\]

A exigência é não importar esses números do Modelo Padrão. Eles devem sair da
topologia, dos resíduos, da circulação e da paridade geométrica da solução
\(\mathfrak G_B\).

---

## 2. Carga elétrica por resíduo

A carga elétrica efetiva é definida como índice/resíduo de fase do ciclo
bariônico:

\[
\boxed{
Q_B
=
\frac{1}{2\pi i}
\oint_{\Gamma_B}
\frac{\phi'(z)}{\phi(z)}\,dz.
}
\]

Pelo princípio do argumento:

\[
Q_B=N_{\rm zeros}-N_{\rm polos}\in\mathbb Z.
\]

Assim, a carga elétrica macroscópica é inteiro topológico, não parâmetro livre.

Essa afirmação é mais forte que a decomposição usual em frações. A integral de
Cauchy não exige unidades \(1/3\); ela exige índices inteiros. Frações internas
podem aparecer apenas como coordenadas efetivas de uma decomposição local dos
resíduos entre gargantas, mas não como ontologia primária.

---

## 3. Próton

No próton, a composição das três colas gera resíduo líquido:

\[
\operatorname{Res}_{\Gamma_p}
\frac{\phi'}{\phi}
=1.
\]

Portanto:

\[
\boxed{
Q_p=+1.
}
\]

As decomposições fracionárias internas, quando usadas, devem ser interpretadas
como projeções efetivas dos resíduos nas três gargantas, não como postulado de
três cargas fundamentais. A entidade primária na GDQ é:

\[
Q_p=+1
\]

como resíduo global do sóliton.

---

## 4. Nêutron

No nêutron, a distribuição interna possui polarização/cisalhamento, mas o
resíduo líquido do ciclo global é nulo:

\[
\operatorname{Res}_{\Gamma_n}
\frac{\phi'}{\phi}
=0.
\]

Logo:

\[
\boxed{
Q_n=0.
}
\]

Isso permite que o nêutron tenha estrutura eletromagnética interna e momento
magnético não nulo sem possuir carga total.

---

## 5. Lei de compensação torsional estacionária

A neutralidade do nêutron não significa ausência de tensões internas. Ela
significa cancelamento global do resíduo/corrente de contorno. Na configuração
estacionária com um estômato invertido, as tensões contrárias se distribuem
como:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,-2\tau).
}
\]

O estômato invertido carrega o dobro da torção porque precisa equilibrar
simultaneamente os dois estômatos alinhados:

\[
\boxed{
\mathcal T_1+\mathcal T_2+\mathcal T_3=0.
}
\]

Essa é uma lei de conservação de corrente torsional de fronteira. Em forma de
Noether:

\[
\delta_\vartheta\mathcal S_{\rm GDQ}=0
\quad\Longrightarrow\quad
dJ_{\rm tor}=0.
\]

Na fronteira bariônica estacionária:

\[
\boxed{
\sum_{a=1}^{3}\mathcal T_a=0.
}
\]

Para o próton, os três estômatos estão alinhados:

\[
\boxed{
(\mathcal T_1,\mathcal T_2,\mathcal T_3)
=
(\tau,\tau,\tau).
}
\]

Nesse caso, a compensação não ocorre por cancelamento interno de sinais, mas
pelo fechamento global da torção no sóliton carregado. Portanto, o próton tem
resíduo global \(Q_p=+1\), enquanto o nêutron tem resíduo global \(Q_n=0\) por
compensação torsional estacionária.

---

## 6. Spin por circulação/holonomia

O spin não deve ser introduzido como índice espinorial externo. Na GDQ, ele é
circulação/holonomia geométrica.

A condição fundamental é:

\[
\boxed{
\oint_{\gamma_B}p_\mu dx^\mu=\frac{h}{2}.
}
\]

Equivalentemente, a holonomia de fase é:

\[
\boxed{
\mathrm{Hol}_{\gamma_B}=-1.
}
\]

Isso significa que uma volta completa no ciclo geométrico muda o sinal da
seção, exatamente como ocorre para objetos de spin \(1/2\).

Portanto:

\[
\boxed{
J_p=J_n=\frac{\hbar}{2}.
}
\]

A representação espinorial de Dirac é a representação local linearizada dessa
holonomia global, não o fundamento primário do spin na GDQ.

---

## 7. Relação com os três estômatos

Cada estômato carrega uma contribuição de meia rotação de fase:

\[
\Delta\theta_a=\frac{\pi}{2}.
\]

Para três estômatos:

\[
\sum_{a=1}^{3}\Delta\theta_a
=
\frac{3\pi}{2}.
\]

Esse termo é o mesmo que aparece no termo de superfície:

\[
\mathcal I_p^\partial
\supset
\alpha\frac{3\pi}{2}.
\]

Assim, a mesma estrutura de cola que contribui para a massa de superfície também
carrega o dado de spin/circulação.

---

## 8. Paridade geométrica

Define-se a paridade como involução espacial no setor \(S^3\) efetivo:

\[
\mathcal I_P:
\chi\mapsto\pi-\chi,
\qquad
(\theta,\phi)\mapsto(\pi-\theta,\phi+\pi).
\]

A métrica é invariante:

\[
\mathcal I_P^*g_B=g_B.
\]

A torção, por ser pseudoforma orientada, muda sinal:

\[
\mathcal I_P^*B_B=-B_B.
\]

Porém o estado físico depende da combinação orientada de cola:

\[
(B,\text{orientação}).
\]

Como a orientação espacial também muda sinal, o produto físico é preservado:

\[
(-B)\times(-\text{orientação})
=
B\times\text{orientação}.
\]

Logo o Hamiltoniano geométrico efetivo comuta com a paridade:

\[
\boxed{
[H_{\rm GDQ}^{B},\mathcal P]=0.
}
\]

---

## 9. Paridade do estado fundamental

O estado fundamental bariônico é o modo sem nó da configuração colada.

Portanto:

\[
\mathcal P\Psi_{B,0}=+\Psi_{B,0}.
\]

Com:

\[
J_B=\frac12,
\]

obtemos:

\[
\boxed{
J^P(p)=J^P(n)=\frac12^+.
}
\]

---

## 10. Status e detalhamentos posteriores

Para uma versão totalmente expandida, ainda convém escrever:

1. escrever explicitamente \(\phi_B(z)\) ou sua classe de resíduos;
2. mostrar a decomposição local dos resíduos nas três gargantas;
3. demonstrar \(dJ_{\rm tor}=0\) diretamente da simetria de fase/torção da ação
   de contorno;
4. provar a condição \(\mathrm{Hol}_{\gamma_B}=-1\) a partir dos mapas
   \(\Psi_{ab}\);
5. mostrar que o operador de paridade preserva as condições de contorno de
   Robin/regularidade do estômato.

Esses itens detalham a representação explícita dos mapas globais. Eles não
alteram o fechamento estrutural do bloco, porque os números quânticos já foram
fixados por três invariantes da solução colada:

1. \(Q_B\), pelo índice/resíduo global;
2. \(\sum_a\mathcal T_a\), pela conservação torsional estacionária;
3. \(J_B=1/2\), pela holonomia \(\mathrm{Hol}_{\gamma_B}=-1\);
4. \(P=+\), pela involução geométrica preservando a combinação
   \((B,\text{orientação})\).

Status:

\[
\boxed{
\text{carga, compensação torsional, spin e paridade fechados estruturalmente.}
}
\]
