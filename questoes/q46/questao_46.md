# Questão 46 — Aharonov--Bohm

## 1. Enunciado

A questão pergunta:

1. se a fase padrão é apenas recuperada por acoplamento mínimo;
2. qual mecanismo local adicional é previsto;
3. se há observável diferente da eletrodinâmica convencional;
4. se a invariância de calibre é preservada.

O capítulo legado associado é:

- `pt-br/40 - O Efeito Aharonov-Bohm.md`.

Adendo técnico:

- `questoes/q46/associados/holonomia_ab_gdq.md`.

## 2. Status curto

$$
\boxed{
\text{Q46 fechada estruturalmente no setor ideal de holonomia.}
}
$$

O que está fechado:

1. a fase Aharonov--Bohm padrão como holonomia de uma conexão plana e não
   globalmente exata;
2. a invariância de calibre;
3. a leitura GDQ da fase como memória topológica/geométrica do domínio
   perfurado;
4. a separação entre fase ideal e possíveis correções locais de interface.

O que fica para `ideias/possibilidades.md`:

1. comparação com solenoides reais;
2. cálculo da impedância $\mathsf R_{\rm sol}$ pela Hessiana oficial;
3. desvios de envelope, visibilidade ou atraso de fase para aparato concreto.

## 3. Domínio físico

O domínio exterior ao solenoide é:

$$
M_{\rm ext}
=
\mathbb R^3\setminus\mathcal S.
$$

Fora do solenoide ideal:

$$
B=0,
\qquad
F=dA=0.
$$

Mas o domínio é multiplamente conexo:

$$
\pi_1(M_{\rm ext})\simeq\mathbb Z.
$$

Assim, $A$ pode ser localmente puro calibre e ainda assim globalmente
observável:

$$
dA=0,
\qquad
A\ne d\chi
\quad
\text{globalmente}.
$$

## 4. A fase padrão é apenas recuperada por acoplamento mínimo?

Não apenas.

O acoplamento mínimo:

$$
p\mapsto p-\frac{q}{c}A
$$

é a linguagem efetiva que recupera a fórmula operacional. Na GDQ, a razão mais
profunda é que $A$ representa a conexão efetiva de uma classe geométrica
global no domínio perfurado.

O observável não é o valor local de $A$, mas a holonomia:

$$
\operatorname{Hol}_\gamma(A)
=
\exp\left[
\frac{iq}{\hbar c}\oint_\gamma A
\right].
$$

Para uma curva $\gamma$ que envolve o solenoide:

$$
\oint_\gamma A=\Phi.
$$

Logo:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}.
$$

Para o elétron:

$$
\Delta\varphi
=
-\frac{e\Phi}{\hbar c},
$$

com o sinal dependendo da orientação.

Portanto, a fase padrão é recuperada, mas não como postulado de acoplamento
mínimo. Ela é a holonomia do setor efetivo de conexão da GDQ.

## 5. Papel de Mayer--Vietoris

O exterior pode ser coberto por dois patches:

$$
M_{\rm ext}=U_N\cup U_S.
$$

Em cada patch:

$$
A_N=d\chi_N,
\qquad
A_S=d\chi_S.
$$

Na interseção:

$$
A_N-A_S=d(\chi_N-\chi_S).
$$

A transição:

$$
g_{NS}
=
\exp\left[
\frac{iq}{\hbar c}(\chi_N-\chi_S)
\right]
$$

carrega a informação global. A fase AB mede exatamente a falha de trivializar
essa conexão em um único patch global.

Em termos físicos:

$$
\text{campo local nulo}
\ne
\text{holonomia global nula}.
$$

## 6. Qual mecanismo local adicional é previsto?

O mecanismo adicional da GDQ não altera a fase topológica ideal. Ele fornece
uma ontologia geométrica para o potencial: $A$ é o representante efetivo de
cisalhamento/holonomia da geometria no exterior do solenoide.

No limite ideal:

$$
A_{\rm eff}=A_{\rm harm},
\qquad
dA_{\rm harm}=0,
\qquad
\oint_\gamma A_{\rm harm}=\Phi.
$$

Em solenoides reais, o contorno material pode gerar uma resposta de interface:

$$
\mathsf R_{\rm sol}
=
K_{YY}-K_{YI}K_{II}^{-1}K_{IY},
$$

e:

$$
A_{\rm eff}
=
A_{\rm harm}
+\delta A_{\rm surf}.
$$

Aqui $\delta A_{\rm surf}$ seria calculado pela Hessiana oficial com o
contorno do solenoide. Esse termo é o candidato GDQ para correções locais de
visibilidade, envelope ou atraso de fase em aparatos reais.

## 7. Há observável diferente da eletrodinâmica convencional?

No experimento ideal, não.

A previsão estrutural coincide com a eletrodinâmica convencional:

$$
\Delta\varphi
=
\frac{q\Phi}{\hbar c}.
$$

A diferença da GDQ é ontológica e geométrica: a fase é holonomia de uma
conexão efetiva da malha, não ação à distância misteriosa do potencial.

Observáveis diferentes só aparecem fora do limite ideal, por exemplo:

1. correção de visibilidade por impedância do contorno;
2. alteração de envelope por $\delta A_{\rm surf}$;
3. atraso dispersivo dependente da interface;
4. dependência com blindagem, raio, material ou resposta dinâmica do
   solenoide.

Esses efeitos exigem $\mathsf R_{\rm sol}$ calculado da Hessiana oficial para
um aparato real. Portanto, ficam em `ideias/possibilidades.md`, sem reabrir a
Q46 estrutural.

## 8. A invariância de calibre é preservada?

Sim.

Sob:

$$
A\mapsto A+d\chi,
$$

temos:

$$
\oint_\gamma A
\mapsto
\oint_\gamma A+\oint_\gamma d\chi.
$$

Se $\chi$ é globalmente bem definida:

$$
\oint_\gamma d\chi=0.
$$

Logo:

$$
\operatorname{Hol}_\gamma(A+d\chi)
=
\operatorname{Hol}_\gamma(A).
$$

Se a transformação é grande ou multivalorada, a condição física é:

$$
\frac{q}{\hbar c}\oint_\gamma d\chi
\in
2\pi\mathbb Z.
$$

Assim, a fase física é preservada módulo $2\pi$.

## 9. Respostas diretas às perguntas obrigatórias

1. A fase padrão não é apenas “colocada” por acoplamento mínimo. O acoplamento
   mínimo é a linguagem efetiva; a origem GDQ é a holonomia de uma conexão
   plana e globalmente não trivial.
2. O mecanismo local adicional é a resposta de cisalhamento/impedância da
   interface do solenoide, expressável por DtN/Schur da Hessiana física.
3. No limite ideal, não há observável diferente: a fase é a mesma. Diferenças
   possíveis pertencem a solenoides reais e exigem cálculo de $\mathsf R_{\rm sol}$.
4. A invariância de calibre é preservada porque a holonomia de laço fechado é
   invariante sob transformações pequenas e sob transformações grandes módulo
   $2\pi$.

## 10. Veredito

$$
\boxed{
\text{Q46 fechada estruturalmente.}
}
$$

A GDQ recupera o efeito Aharonov--Bohm como holonomia geométrica:

$$
\operatorname{Hol}_\gamma
=
\exp\left[
\frac{iq\Phi}{\hbar c}
\right].
$$

O fechamento não depende de postular uma força local onde $F=0$. A física
local é plana em curvatura, mas globalmente não trivial em cohomologia.

