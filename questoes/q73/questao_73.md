# Questão 73 — Aharonov--Bohm via GDQ: potenciais como geometria local

## 1. Enunciado

A Q73 pergunta se a GDQ resolve o efeito Aharonov--Bohm de modo mecânico,
local e topológico, evitando a leitura de “ação fantasmagórica” do potencial
vetor.

Esta questão continua a Q46:

- `questoes/q46/questao_46.md`.

A Q46 já fechou o setor ideal:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}
$$

como holonomia de uma conexão plana, localmente pura, mas globalmente não
trivial.

A Q73 acrescenta a ontologia GDQ:

$$
\boxed{
\mathbf A
\text{ não é força oculta; é representante efetivo de cisalhamento/holonomia da geometria.}
}
$$

## 2. Status curto

$$
\boxed{
\text{Q73 fechada estruturalmente como ontologia local/topológica do potencial AB.}
}
$$

O que está fechado:

1. a fase AB ideal vem de holonomia;
2. a invariância de calibre é preservada;
3. $\mathbf B=0$ fora do solenoide não implica holonomia nula;
4. $\mathbf A$ é lido como representante local de uma classe global;
5. a GDQ elimina a necessidade de sinal não local;
6. solenoides reais entram por resposta de interface $\mathsf R_{\rm sol}$.

O que permanece aplicação futura:

1. calcular $\mathsf R_{\rm sol}$ para um solenoide material específico;
2. prever desvios de visibilidade/envelope/atraso em aparato real;
3. medir esses desvios contra experimentos AB de precisão.

## 3. Domínio e topologia

O domínio exterior ao solenoide ideal é:

$$
M_{\rm ext}
=
\mathbb R^3\setminus\mathcal S.
$$

Fora do solenoide:

$$
\mathbf B=0,
\qquad
F=dA=0.
$$

Mas:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

Logo, $A$ pode ser fechado sem ser exato globalmente:

$$
dA=0,
\qquad
A\ne d\chi
\quad
\text{globalmente}.
$$

O observável é:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left[
\frac{iq}{\hbar c}
\oint_\gamma A
\right].
$$

Para uma curva que envolve o solenoide:

$$
\oint_\gamma A
=
\Phi.
$$

Portanto:

$$
\boxed{
\Delta\varphi
=
\frac{q\Phi}{\hbar c}.
}
$$

## 4. Leitura GDQ do potencial

Na linguagem efetiva comum, escreve-se:

$$
p
\mapsto
p-\frac{q}{c}A.
$$

Na GDQ, isso não é tomado como axioma primário. É a redução operacional da
geometria de fase/cisalhamento do meio Hermitiano.

O momentum local do setor Madelung pode ser escrito:

$$
\omega
=
\left(
\nabla S_R-\frac{q}{c}A
\right)\cdot dx.
$$

Ou, para a velocidade:

$$
v
=
\frac{1}{m}
\left(
\nabla S_R-\frac{q}{c}A
\right).
$$

Interpretação:

$$
\boxed{
A
\text{ é a conexão efetiva que registra o cisalhamento/arrasto holonômico do domínio.}
}
$$

O campo magnético é a curvatura/vorticidade concentrada:

$$
B=dA
$$

dentro do solenoide. Fora dele, $dA=0$, mas a classe de cohomologia não
desaparece.

## 5. Por que não há não-localidade física

O elétron nunca precisa receber uma força vinda do interior do solenoide.

O que ele percorre é um domínio exterior que já possui uma classe global de
conexão:

$$
[A]\in H^1(M_{\rm ext}).
$$

Localmente:

$$
A=d\chi_\alpha
$$

em cada carta $U_\alpha$.

Mas em duas cartas:

$$
A_N-A_S
=
d(\chi_N-\chi_S).
$$

A função de transição:

$$
g_{NS}
=
\exp\left[
\frac{iq}{\hbar c}
(\chi_N-\chi_S)
\right]
$$

carrega a informação topológica.

Assim:

$$
\boxed{
\text{o efeito é local em cartas e global por colagem.}
}
$$

Não há transmissão de energia, momento ou informação do núcleo do solenoide
para o elétron. Há holonomia do domínio perfurado.

## 6. O que “potencial real” significa na GDQ

Na GDQ, dizer que o potencial é real não significa que $A$ seja uma força
clássica local no sentido de Lorentz. Significa:

1. $A$ é parte da conexão efetiva que transporta fase/circulação;
2. sua holonomia é observável;
3. sua classe global não pode ser removida por calibre único;
4. em aparelhos reais, o material do solenoide pode induzir resposta de
   interface adicional.

Portanto:

$$
\boxed{
\text{realidade física do potencial = realidade da conexão/holonomia, não força local misteriosa.}
}
$$

## 7. Solenoide real e impedância de interface

No limite ideal:

$$
A_{\rm eff}
=
A_{\rm harm},
\qquad
dA_{\rm harm}=0,
\qquad
\oint_\gamma A_{\rm harm}=\Phi.
$$

Em um solenoide real:

$$
A_{\rm eff}
=
A_{\rm harm}
+
\delta A_{\rm surf}.
$$

A correção $\delta A_{\rm surf}$ deve vir da resposta de interface:

$$
\mathsf R_{\rm sol}
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY}.
$$

Aqui:

- $Y$ é o contorno exterior acessível ao elétron;
- $I$ são os graus internos/material do solenoide;
- $K$ é a Hessiana física reduzida do aparelho.

A fase fica:

$$
\Delta\varphi
=
\frac{q}{\hbar c}
\oint_\gamma
\left(
A_{\rm harm}
+
\delta A_{\rm surf}
\right).
$$

No solenoide ideal:

$$
\oint_\gamma\delta A_{\rm surf}=0.
$$

No solenoide real, esse termo pode alterar:

1. visibilidade;
2. envelope;
3. atraso de fase;
4. dependência com material, blindagem e geometria.

## 8. O que distingue Q73 de Q46

Q46 fechou:

$$
\text{fase ideal}
=
\text{holonomia}.
$$

Q73 fecha:

$$
\text{potencial}
=
\text{conexão/cisalhamento físico da geometria efetiva}.
$$

E abre a rota:

$$
\text{solenoide real}
\to
\mathsf R_{\rm sol}
\to
\delta A_{\rm surf}
\to
\text{correções experimentais}.
$$

## 9. Conclusão

A GDQ resolve o efeito Aharonov--Bohm sem misticismo não local.

O ponto correto não é dizer que o elétron sente uma força onde $B=0$. Ele não
sente. O ponto correto é:

$$
\boxed{
\text{o exterior do solenoide é localmente plano, mas globalmente torcido por holonomia.}
}
$$

A partícula percorre localmente uma conexão plana; a interferência mede a
colagem global dessa conexão.

Classificação final:

$$
\boxed{
\text{Q73 fechada estruturalmente; solenoides reais ficam como aplicação metrológica.}
}
$$

