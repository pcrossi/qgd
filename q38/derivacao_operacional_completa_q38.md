# Q38 — Perfil local, complemento de Schur e volume gravitacional efetivo

## 1. Escopo e convenções

Este documento completa a redução operacional iniciada em
`derivacao_inst_fano_planificacao.md`. A ação oficial da GDQ não é alterada.
Trabalha-se no background estacionário e no setor autodual da conexão de
Bismut

\[
(\mathcal A_B)_\mu{}^{ab}
=(\omega^{\rm LC})_\mu{}^{ab}+\frac12H_\mu{}^{ab},
\qquad
\mathcal F_B=d\mathcal A_B+\mathcal A_B\wedge\mathcal A_B.
\]

Adota-se \(\operatorname{tr}(T_aT_b)=\delta_{ab}/2\). Mudanças simultâneas na
normalização de \(T_a\), da carga de Pontryagin e do prefator da ação não
alteram os resultados abaixo.

## 2. Perfil local do meio-instantão

Em coordenadas normais \(x^\mu\) centradas no pescoço do estômato, um
representante local regular da classe autodual é o perfil BPST projetado na
parte autodual da conexão de Bismut:

\[
\boxed{
\mathcal A_{B,\mu}^{\rm inst}(x)
=\frac{2\,\eta^a_{\mu\nu}x^\nu}{x^2+\rho_0^2}\,T_a
}
\]

e

\[
\boxed{
\mathcal F_{B,\mu\nu}^{\rm inst}(x)
=-\frac{4\rho_0^2}{(x^2+\rho_0^2)^2}
\eta^a_{\mu\nu}T_a,
\qquad
\mathcal F_B=*\mathcal F_B .
}
\]

Aqui \(\eta^a_{\mu\nu}\) são os símbolos autoduais de 't Hooft e \(\rho_0\)
é o raio local do núcleo. A densidade topológica é par na coordenada normal
ao estômato e pode ser normalizada como

\[
q_B(x)d^4x
=\frac{6\rho_0^4}{\pi^2(x^2+\rho_0^2)^4}d^4x,
\qquad
\int_{\mathbb R^4}q_B=1.
\]

O estômato seleciona uma calota relativa, por exemplo \(x^4\geq0\). Como
\(q_B(x^4)=q_B(-x^4)\),

\[
Q_{\rm rel}=\int_{x^4\geq0}q_B=\frac12.
\]

O termo de borda de Chern--Simons completa a definição gauge-invariante da
carga relativa. Pela decomposição BPS,

\[
\frac{S_E}{\hbar}
=\frac{1}{2\alpha}\|\mathcal F_B-*\mathcal F_B\|^2
+\frac{Q_{\rm rel}}{\alpha},
\]

e a sela autodual fornece

\[
\boxed{\frac{S_{\rm inst}}{\hbar}=\frac1{2\alpha}.}
\]

O parâmetro \(\rho_0\) afeta correções locais de tamanho finito, mas cancela
da carga e da ação topológica saturada. Este perfil é um representante local;
a extensão global é feita pela conexão de transição na borda da calota.

## 3. Hessiana de contorno e complemento de Schur

Na seção de colagem \(\Sigma\simeq S^3_H\times T^5\), decomponha a flutuação
em três formas invariantes \(h_i\) da fibra Hopf e cinco formas harmônicas
\(t_A=d\theta^A\) do toro. Após fixação do modo de gauge, a Hessiana é

\[
\mathbb K_\partial=
\begin{pmatrix}
K_H&J\\ J^\dagger&K_T
\end{pmatrix},
\]

com operadores explícitos

\[
(K_H)_{ij}=\delta_{ij}
\left[-D_B^2+\frac{2}{R_H^2}+M_H^2+V_H(g_*,f_*,H_*)\right],
\]

\[
(K_T)_{AB}=\delta_{AB}
\left[-\Delta_{T^5}+M_T^2+Z_T^{\rm Rob}\right],
\]

\[
J_{iA}=g_\partial\sqrt2\,
\langle h_i,\mathcal C_\partial t_A\rangle_\Sigma.
\]

\(D_B=d+[\mathcal A_B^{\rm inst},\,\cdot\,]\) contém a conexão local acima,
\(2/R_H^2\) é o termo de Weitzenböck de \(S^3\), \(Z_T^{\rm Rob}\) é a
impedância Robin do estômato e \(\mathcal C_\partial\) é o mapa de colagem.
\(Z_T^{\rm Rob}\), ou equivalentemente a inversa de Moore--Penrose no
subespaço ortogonal ao gauge, torna bem definida a inversão dos modos
harmônicos toroidais.

Integrar gaussianamente o setor toroidal dá exatamente

\[
\boxed{K_{\rm eff}=K_H-JK_T^{-1}J^\dagger.}
\]

No background estacionário isotrópico,

\[
K_H=k_H I_3,\qquad K_T=k_T I_5,
\]

e, escrevendo \(C_{iA}=\langle h_i,\mathcal C_\partial t_A\rangle\),

\[
\boxed{
K_{\rm eff}=k_HI_3-\frac{2g_\partial^2}{k_T}CC^\dagger .
}
\]

Assim, a estabilidade local exige

\[
k_H>\frac{2g_\partial^2}{k_T}\lambda_{\max}(CC^\dagger).
\]

Para a colagem estacionária equipartida, o mapa \(C\) é uma isometria nos
três canais transmitidos. A admitância escalar normalizada é o traço sobre o
setor Hopf dividido pelos cinco canais toroidais, incluindo os dois ramos
causais em norma RMS:

\[
\chi_{\rm Fano}^{\rm bulk}
=\frac{\sqrt2}{5}\operatorname{Tr}_{H}I_3
=\boxed{\frac{3\sqrt2}{5}}.
\]

Portanto, \(3\sqrt2/5\) é a projeção escalar do complemento de Schur no modo
estacionário. Fora desse setor, Fano é um operador dependente do modo, não uma
constante universal.

## 4. Avaliação de \(\mathcal V_{\rm eff}^{(G)}\)

No background completo estacionário usado por Q38,

\[
g=g_*,\quad f=f_*,\quad H=H_*,\quad
\mathcal A_B=\mathcal A_B^{\rm inst},
\]

a redução separa quatro fatores independentes:

\[
\underbrace{e^{-S_{\rm inst}/\hbar}}_{\text{sela relativa}}
\underbrace{\alpha^4(1+\alpha)}_{\text{volume/warp estacionário}}
\underbrace{(\chi_{\rm Fano}^{\rm bulk})^{-1}}_{\text{Schur}}
\underbrace{J_{\rm flat}^{(0)}}_{=1}.
\]

Definindo o volume gravitacional adimensional pela inversa do coeficiente
transmitido, obtém-se diretamente

\[
\boxed{
\widehat{\mathcal V}_{\rm eff}^{(G)}
=\frac{\chi_{\rm Fano}^{\rm bulk}}
{\alpha^4(1+\alpha)}
\exp\!\left(\frac1{2\alpha}\right)
}
\]

e

\[
\boxed{
\Pi_1^{(0)}
=\left(\widehat{\mathcal V}_{\rm eff}^{(G)}\right)^{-1}
=\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}^{\rm bulk}}
\exp\!\left(-\frac1{2\alpha}\right).
}
\]

Com \(\alpha_{\rm geom}=0.007297348130031834\),

\[
S_{\rm inst}/\hbar=68.5180412241,
\quad
\widehat{\mathcal V}_{\rm eff}^{(G)}=1.697678742\times10^{38},
\]

\[
\boxed{\Pi_1^{(0)}=5.890395957\times10^{-39}.}
\]

## 5. Tratamento inicial do resíduo sem pós-ajuste

O resíduo não deve ser absorvido em \(J_{\rm flat}\), em Fano ou na ação do
instantão. Uma primeira hipótese seria associá-lo à diferença entre a massa
geométrica e a massa física do próton.

Escreva, portanto,

\[
M_p^{\rm phys}=M_B^{(0)}(1+\delta_\partial),
\]

onde \(\delta_\partial\) não é parâmetro de Q38, mas a saída independente da
ação GDQ no background bariônico:

\[
\boxed{
\delta_\partial^{\rm GDQ}
=\frac{1}{M_B^{(0)}c^2}
\int_{\partial K_B}\!\sqrt\gamma\,
\left[
\frac14F_{ab}\mathcal K_{\rm EM}^{ab,cd}F_{cd}
+\frac12T_{ab}\mathcal K_T^{ab,cd}T_{cd}
+F_{ab}\mathcal K_{\rm mix}^{ab,cd}T_{cd}
\right]d^3x .
}
\]

A previsão observável é então

\[
\boxed{\Pi_1^{\rm phys}=(1+\delta_\partial^{\rm GDQ})^2\Pi_1^{(0)}.}
\]

Usar CODATA apenas depois do cálculo fornece o diagnóstico

\[
\delta_\partial^{\rm req}
=\sqrt{\frac{\Pi_1^{\rm CODATA}}{\Pi_1^{(0)}}}-1
=1.3366\times10^{-3}
=0.13366\%.
\]

Esse número **não deve ser colocado de volta na derivação**. A auditoria
posterior em `fechamento_determinante_residuo_q38.md` mostrou que a superfície
de massa efetivamente derivada em Q40 vale apenas \(0.00188247\%\), cerca de
71 vezes menos. Portanto, a hipótese de massa superficial é rejeitada. O
termo ausente passa a ser o prefator do determinante de flutuações do
complemento de Schur.

## 6. Veredito

Os itens locais e funcionais de Q38 ficam resolvidos **condicionalmente à
redução estacionária já adotada em Q38**:

1. existe um representante local explícito de \(\mathcal A_B^{\rm inst}\);
2. o complemento de Schur está escrito com os operadores de Bismut, Hopf,
   toro e Robin;
3. \(\widehat{\mathcal V}_{\rm eff}^{(G)}\) foi avaliado sem fator plano;
4. o resíduo foi isolado sem alterar os fatores clássicos; a hipótese de
   superfície bariônica foi posteriormente testada e rejeitada.

O fechamento numérico definitivo de Q38 exige avaliar o determinante espectral
de flutuações de \(K_H-JK_T^{-1}J^\dagger\). A origem de \(\alpha^4\) pela
forma de volume Kähler e a auditoria completa do resíduo estão em
`fechamento_determinante_residuo_q38.md`. Até a avaliação espectral, a
igualdade com CODATA é uma previsão testável, não uma prova consumada.
