# Q38 — Redução radial condicional do setor quadrático \(Q_{\rm rel}=1/2\)

> **Correção de status.** Este documento reduz o funcional quadrático/BPS
> usado nos adendos instantônicos. A equivalência desse funcional com a ação
> oficial linear em \(\mathcal R_B\) ainda não foi demonstrada. Ver
> questoes/q38/associados/auditoria_final_acao_instanton_q38.md.

## 1. Setor reduzido

No background steady já obtido, o setor instantônico **proposto** foi escrito
por completamento de quadrado:

\[
\frac{S_E}{\hbar}
=\frac{1}{2\alpha}
\|\mathcal F_B-*\mathcal F_B\|_{\mathcal U_*}^2
+\frac{Q_{\rm rel}}{\alpha}
+S_{\rm br}[g,f,H].
\]

Aqui (S_{\rm br}) contém a retroação de (g,f,H=d^c\omega). No background
estacionário, sua primeira variação se anula. Para a sela autodual,

\[
\mathcal F_B=*\mathcal F_B,
\qquad
Q_{\rm rel}=\frac12,
\]

portanto

\[
\boxed{
\frac{S_{\rm red}^{(Q=1/2)}}{\hbar}
=\frac1{2\alpha}+S_{\rm br}^{(2)}+O(\delta\Phi^3).
}
\]

## 2. Perfil radial

Use

\[
\mathcal A_\mu^{\rm inst}
=\frac{2\eta^a_{\mu\nu}x^\nu}{r^2+\rho^2}T_a,
\]

com densidade normalizada

\[
q_\rho(r)
=\frac{6\rho^4}{\pi^2(r^2+\rho^2)^4}.
\]

No espaço completo,

\[
2\pi^2\int_0^\infty r^3q_\rho(r)dr=1.
\]

Dentro de uma bola de raio (R), a carga acumulada é

\[
Q_{B^4}(R,\rho)
=\frac{R^4(R^2+3\rho^2)}{(R^2+\rho^2)^3}.
\]

Na meia-bola,

\[
Q_{B^4_+}^{\rm bulk}(R,\rho)
=\frac12
\frac{R^4(R^2+3\rho^2)}{(R^2+\rho^2)^3}.
\]

Para (R<\infty), essa integral de bulk isolada não vale exatamente (1/2).
A carga relativa inclui a transgressão da borda:

\[
Q_{\rm rel}
=Q_{B^4_+}^{\rm bulk}
+Q_{\rm CS}^{\partial},
\]

com

\[
Q_{\rm CS}^{\partial}(R,\rho)
=\frac12\left[
1-rac{R^4(R^2+3\rho^2)}{(R^2+\rho^2)^3}
\right].
\]

Logo,

\[
\boxed{Q_{\rm rel}(R,\rho)=\frac12}
\]

para qualquer (R>0) e (\rho>0).

## 3. Variação do módulo de tamanho

Substituindo a solução autodual e a transgressão completa,

\[
\boxed{
S_{\rm red}^{(Q=1/2)}(\rho)
=\frac{\hbar}{2\alpha}
}
\]

no setor clássico topológico. Portanto,

\[
\boxed{
\frac{dS_{\rm red}}{d\rho}=0,
\qquad
\frac{d^2S_{\rm red}}{d\rho^2}=0.
}
\]

O funcional quadrático proposto não seleciona classicamente um raio
instantônico isolado: nele, \(\rho\) é um módulo coletivo exato. Esse resultado
só se transfere à ação oficial se a equivalência auditada acima for provada.

## 4. Condição natural de borda

A variação do termo de Pontryagin é uma forma exata:

\[
\delta\int_U\operatorname{tr}(F\wedge F)
=2\int_{\partial U}\operatorname{tr}(\delta A\wedge F).
\]

A variação do termo relativo de Chern--Simons cancela essa contribuição quando
o mapa de cola e a conexão de referência são mantidos fixos. Assim, a condição
natural não é um número Robin escolhido externamente; é

\[
\boxed{
\delta(\mathcal A_B-\mathcal A_{B,*})\big|_{\partial U}=0
}
\]

na classe relativa. Para as flutuações físicas ortogonais aos modos de gauge,
essa condição define a extensão auto-adjunta relativa do operador.

## 5. Hessiana e modo zero

O modo de tamanho é

\[
Z_\rho=\frac{\partial\mathcal A^{\rm inst}}{\partial\rho}.
\]

Como a ação é constante em (\rho),

\[
\boxed{
\mathbb L_{B,\rm inst}Z_\rho=0.
}
\]

Ele deve ser removido do determinante primado e integrado separadamente. O
prefator correto possui a forma

\[
\boxed{
\mathcal P_{\rm GDQ}
=\int_{\mathcal I_\rho}d\rho\,
\sqrt{G_{\rho\rho}(\rho)}
\,J_{\rm outros}(\rho)
\left[
\frac{\det{}'\mathbb L_{B,\rm inst}(\rho)}
{\det\mathbb L_{B,0}}
\right]^{-1/2}.
}
\]

A métrica do módulo é derivada da medida oficial:

\[
G_{\rho\rho}
=\left\langle Z_\rho,Z_\rho\right\rangle_{\mathcal U_*}.
\]

Com \(\operatorname{tr}(T_aT_b)=\delta_{ab}/2\),

\[
\operatorname{tr}(Z_{\rho,\mu}Z_\rho{}^\mu)
=\frac{24\rho^2r^2}{(r^2+\rho^2)^4}.
\]

Na meia-bola de raio \(R\), e tomando \(\mathcal U_*\) constante no núcleo
local,

\[
G_{\rho\rho}(R,\rho)
=\mathcal U_*
\int_{B^4_+(R)}
\operatorname{tr}(Z_\rho^2)d^4x.
\]

A integral radial é elementar e fornece

\[
\boxed{
G_{\rho\rho}(R,\rho)
=4\pi^2\mathcal U_*
\frac{R^6}{(R^2+\rho^2)^3}.
}
\]

No limite de meia-espaço,

\[
G_{\rho\rho}(\infty,\rho)=4\pi^2\mathcal U_*.
\]

Assim, a medida do módulo de tamanho é

\[
\boxed{
d\mu_\rho
=2\pi\sqrt{\mathcal U_*}
\frac{R^3}{(R^2+\rho^2)^{3/2}}d\rho.
}
\]

Se a geometria da calota restringe \(0<\rho<R\), sua integral é

\[
\boxed{
\int_0^R d\mu_\rho
=\sqrt2\,\pi R\sqrt{\mathcal U_*}.
}
\]

Portanto, a medida de \(\rho\) está determinada no núcleo local. Ainda devem
ser incluídos os demais modos coletivos e a variação de \(\mathcal U_*\) no
colar não homogêneo.

## 6. Consequência para o determinante espectral

Não existe um único determinante a ser avaliado em um (\rho_0) clássico,
porque (\rho) não foi estabilizado classicamente. Existe uma integral sobre
o espaço de módulos. O domínio (mathcal I_\rho) deve vir da geometria da
cirurgia:

\[
0<\rho<\rho_{\max}(R,\epsilon_{\rm stoma}).
\]

O limite superior e a métrica (G_{\rho\rho}) são calculáveis pela ação e
pela geometria do estômato, mas ainda requerem a imersão explícita do perfil
no colar global. Sem essa imersão, substituir (\rho) por um valor que reproduza
o resíduo seria pós-ajuste.

## 7. Resultado

A redução radial resolve três questões:

1. a carga relativa é exatamente (1/2), incluindo a transgressão;
2. a condição de borda é a cola relativa fixa;
3. (\rho) é um modo zero coletivo, não um parâmetro a ser extremizado para
   obter um mínimo isolado.

Assim, o próximo objeto não é (dS/d\rho=0) — que já se anula
identicamente —, mas a medida completa do módulo e o determinante primado ao
longo de (mathcal I_\rho).
