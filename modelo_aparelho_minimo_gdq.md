# Modelo mínimo GDQ do aparelho de medida

## 1. Objetivo

Este documento constrói o segundo bloco da teoria da interface
clássico--quântico: um aparelho mínimo capaz de correlacionar um canal do
objeto com um registro macroscópico.

O aparelho reduzido contém:

\[
\boxed{
\text{modo de ponteiro }X
+\text{modos internos }y_\nu
+\text{orientação Hopf }P.
}
\]

O modelo não é uma nova ação fundamental. Ele deve ser obtido pela expansão e
projeção modal da ação oficial em torno de um background GDQ macroscópico.

O resultado estrutural é uma cadeia:

\[
\mathcal S_{\rm GDQ}
\longrightarrow
\mathcal S_{\rm red}[P,X,y_\nu]
\longrightarrow
G_A^{\rm ret}
\longrightarrow
\mathcal K_X,\ \xi_X
\longrightarrow
\text{registros metastáveis}.
\]

---

## 2. Background conjunto

Considere uma solução estacionária do sistema objeto--aparelho antes da
ativação do protocolo:

\[
\Phi_*=(\Phi_{Q*},\Phi_{A*}),
\qquad
\left.\frac{\delta\mathcal S_{\rm GDQ}}
{\delta\Phi}\right|_{\Phi_*}=0.
\]

As perturbações físicas do aparelho, depois da remoção de difeomorfismos,
calibre e isometrias globais, são decompostas como

\[
\delta\Phi_A
=X(t)T_X
+\sum_\nu y_\nu(t)T_\nu
+\delta\Phi_A^\perp.
\]

Aqui:

- \(T_X\) é o modo coletivo legível, denominado ponteiro;
- \(T_\nu\) são modos internos não observados;
- \(\delta\Phi_A^\perp\) contém modos mais altos a serem eliminados;
- todos os vetores tangentes pertencem ao subespaço físico gauge-fixado.

O ponteiro pode representar:

- magnetização coletiva;
- posição de um domínio;
- diferença de carga entre dois eletrodos;
- intensidade em duas regiões do detector;
- modo mecânico de uma tela ou amplificador.

Para Stern--Gerlach completo, o ponteiro final mais natural é uma variável
espacial ou de registro do detector. A magnetização é um modelo intermediário
conveniente para derivar a resposta do eletroímã, mas não deve ser confundida
automaticamente com a mancha observada.

---

## 3. Coeficientes como variações da ação oficial

Seja \(\mathbb H_A\) a Hessiana física do aparelho:

\[
\mathbb H_A
=\Pi_{\rm phys}
\left.\frac{\delta^2\mathcal S_{\rm GDQ}}
{\delta\Phi_A^2}\right|_{\Phi_{A*}}
\Pi_{\rm phys}.
\]

O coeficiente quadrático do modo coletivo é

\[
\boxed{a_2=\langle T_X,\mathbb H_AT_X\rangle.}
\]

As interações superiores são projeções das variações da mesma ação:

\[
\boxed{
a_3=D^3\mathcal S_{\rm GDQ}[T_X,T_X,T_X],
}
\]

\[
\boxed{
a_4=D^4\mathcal S_{\rm GDQ}[T_X,T_X,T_X,T_X].
}
\]

Essas expressões devem incluir a variação da medida \(\mathcal U\sqrt g\), das
conexões e dos vínculos de normalização.

Se os modos \(\delta\Phi_A^\perp\) forem eliminados, os coeficientes físicos
recebem complementos de Schur não lineares. Portanto, \(a_4\) efetivo não é,
em geral, apenas a quarta derivada nua ao longo de \(T_X\).

---

## 4. Emergência de dois registros

### 4.1 Simetria do aparelho não ativado

Para um detector com dois registros equivalentes, deve existir uma simetrização
do protocolo que troque:

\[
X\longmapsto-X.
\]

Nesse caso, no ponto não enviesado:

\[
a_3=0.
\]

O potencial efetivo de menor ordem é

\[
U_A(X)
=U_0+\frac{a_2}{2}X^2+rac{a_4}{4!}X^4+O(X^6).
\]

Para dois registros espontaneamente estáveis, exige-se:

\[
\boxed{a_2<0,\qquad a_4>0.}
\]

Definindo

\[
A=-a_2>0,
\qquad
B=\frac{a_4}{6}>0,
\]

temos a forma normal:

\[
\boxed{
U_A(X)=U_0-\frac A2X^2+\frac B4X^4.
}
\]

Os registros são

\[
\boxed{X_\pm=\pm\sqrt{A/B}.}
\]

A barreira entre eles é

\[
\boxed{\Delta U_A=\frac{A^2}{4B}.}
\]

### 4.2 Interpretação

A existência de dois registros não é consequência do potencial Zeeman do
objeto. Ela é propriedade do aparelho preparado próximo de uma bifurcação ou
com dois setores macroscópicos de leitura.

O objeto fornece um viés condicionado; o aparelho fornece amplificação e
memória.

---

## 5. Acoplamento objeto--ponteiro

No setor de Hopf, defina a variável axial

\[
s_{\boldsymbol n}(P)
=\boldsymbol n(P)\cdot\boldsymbol n_A,
\qquad
-1\le s_{\boldsymbol n}\le1,
\]

onde \(\boldsymbol n_A\) é determinado pelo campo clássico do aparelho.

A contração torsão--curvatura derivada no documento anterior, ao ser projetada
no modo \(T_X\), fornece o acoplamento líder

\[
\boxed{
U_{QA}(P,X)=-g_X X\,s_{\boldsymbol n}(P).
}
\]

O coeficiente não é livre conceitualmente:

\[
\boxed{
g_X
=-D^2S_{\rm int}[T_X,T_s],
}

onde \(T_s\) é a deformação localizada do objeto induzida pela orientação de
Hopf. Em forma espectral, \(g_X\) é uma integral de sobreposição entre:

1. perfil torsional do objeto;
2. perfil do campo clássico;
3. modo coletivo do aparelho;
4. medida oficial.

Para um canal axial \(s=\pm1\), o potencial condicionado é

\[
\boxed{
U_\pm(X)
=-\frac A2X^2+\frac B4X^4\mp g_XX.
}
\]

---

## 6. Estrutura das bacias condicionadas

Os pontos estacionários satisfazem

\[
BX^3-AX\mp g_X=0.
\]

O valor crítico do viés, no qual uma das bacias metastáveis desaparece, é

\[
\boxed{
g_c=\frac{2A^{3/2}}{3\sqrt{3B}}.
}

Existem três regimes:

### 6.1 Viés fraco: \(|g_X|\ll g_c\)

As duas bacias persistem. O canal do objeto altera suas profundidades e as
taxas de captura, mas flutuações do aparelho continuam relevantes.

Esse regime é apropriado para medição fraca e para estudar competição entre
informação adquirida e perturbação.

### 6.2 Viés próximo do limiar: \(|g_X|\lesssim g_c\)

Uma bacia torna-se pouco estável. Pequena diferença microscópica pode produzir
grande ganho macroscópico.

Esse é o regime natural de um amplificador de medição.

### 6.3 Viés acima do limiar: \(|g_X|>g_c\)

Para cada canal fixo, resta apenas a bacia favorecida. O registro torna-se
quase determinístico condicionado ao canal.

Esse fato não deriva as probabilidades dos canais. Ele apenas amplifica uma
correlação já estabelecida na etapa de pré-medição.

---

## 7. Pré-medição e registro são etapas diferentes

### 7.1 Pré-medição coerente

A interação inicial deve correlacionar os canais intrínsecos com estados do
ponteiro:

\[
c_+|+\rangle|X_0\rangle
+c_-|-\rangle|X_0\rangle
\longrightarrow
c_+|+\rangle|X_+^{\rm pre}\rangle
+c_-|-\rangle|X_-^{\rm pre}\rangle.
\]

Na GDQ, essa escrita é uma abreviação operacional para duas soluções
correlacionadas do problema de interface. Ela não deve ser usada como ponto de
partida ontológico.

### 7.2 Amplificação e registro

Os modos internos do aparelho dispersam a coerência relativa entre os dois
setores e estabilizam:

\[
X_+^{\rm pre}\to X_+,
\qquad
X_-^{\rm pre}\to X_-.
\]

Portanto:

\[
\boxed{
\text{dois canais vêm do objeto; dois registros vêm do aparelho.}
}
\]

---

## 8. Banho geométrico do aparelho

Considere modos internos \(y_\nu\) que diagonalizam o bloco do complemento
ortogonal ao modo coletivo. O modo \(T_X\) é escolhido por legibilidade
macroscópica e não precisa ser autovetor da Hessiana completa; por isso podem
existir termos cruzados entre \(X\) e \(y_\nu\).
Após reconstrução do tempo físico, a forma reduzida esperada é

\[
L_A^{(2)}
=\frac{M_X}{2}\dot X^2-U_A(X)
+\sum_\nu\frac{m_\nu}{2}
(\dot y_\nu^2-\omega_\nu^2y_\nu^2)
+X\sum_\nu c_\nu y_\nu.
\]

Essa expressão é a forma normal lorentziana da expansão modal. Seus
coeficientes devem vir da reconstrução Osterwalder--Schrader e das projeções da
ação oficial:

\[
M_X=\langle T_X,K_tT_X\rangle,
\]

\[
m_\nu\omega_\nu^2
=\langle T_\nu,\mathbb H_AT_\nu\rangle,
\]

\[
\boxed{
c_\nu
=\langle T_X,\mathbb H_AT_\nu\rangle.
}
\]

Se \(T_X\) também for escolhido como autovetor da Hessiana completa, então
\(c_\nu=0\) na ordem quadrática. Nesse caso, dissipação exige acoplamentos
não lineares provenientes de \(D^3\mathcal S_{\rm GDQ}\) e ordens superiores.

A forma exata do acoplamento depende da parametrização dos campos; a expressão
acima registra a estrutura modal, não um novo postulado fundamental.

---

## 9. Eliminação dos modos internos

As equações dos modos do banho são

\[
m_\nu\ddot y_\nu+m_\nu\omega_\nu^2y_\nu=-c_\nu X.
\]

Usando a solução retardada e substituindo na equação de \(X\), obtém-se uma
equação de Langevin generalizada:

\[
\boxed{
M_X\ddot X(t)
+U_\pm'(X(t))
+\int_0^t\Gamma_X(t-s)\dot X(s)\,ds
=\xi_X(t).
}
\]

Para um banho harmônico discreto, o kernel é

\[
\boxed{
\Gamma_X(t)
=\sum_\nu\frac{c_\nu^2}{m_\nu\omega_\nu^2}
\cos(\omega_\nu t).
}
\]

O termo \(\xi_X(t)\) depende das condições iniciais dos modos \(y_\nu\). Em
estado térmico, sua correlação clássica de alta temperatura satisfaz

\[
\boxed{
\langle\xi_X(t)\xi_X(t')\rangle
=k_BT\,\Gamma_X(|t-t'|),
}

com fatores de convenção dependentes da definição do kernel. No regime
quântico do banho, a relação contém o fator espectral
\(\hbar\omega\coth(\hbar\omega/2k_BT)\).

Essa relação deve ser derivada da distribuição estacionária do aparelho, não
imposta se o background estiver fora de equilíbrio.

---

## 10. Densidade espectral e kernel retardado

Defina

\[
\boxed{
J_A(\omega)
=\frac\pi2
\sum_\nu\frac{c_\nu^2}{m_\nu\omega_\nu}
\delta(\omega-\omega_\nu).
}

Então

\[
\Gamma_X(t)
=\frac2\pi\int_0^\infty
\frac{J_A(\omega)}{\omega}
\cos(\omega t)\,d\omega.
\]

O kernel de resposta do ponteiro é

\[
\boxed{
G_X^{\rm ret}(\omega)
=\left[
-M_X\omega^2
+U_\pm''(X_*)
-\Sigma_A^{\rm ret}(\omega)
\right]^{-1}.
}

A parte imaginária de \(\Sigma_A^{\rm ret}\) controla dissipação. A parte real
desloca a rigidez e deve ser incluída ao determinar \(A\), \(B\) e o limiar.

---

## 11. Limite Markoviano

Se o espectro do aparelho for suficientemente denso e a memória decair numa
escala muito menor que a evolução do ponteiro:

\[
\Gamma_X(t)\simeq2\gamma_X\delta(t).
\]

A equação reduz-se a

\[
\boxed{
M_X\ddot X+\gamma_X\dot X+U_\pm'(X)=\xi_X(t).
}

No limite superamortecido:

\[
\boxed{
\dot X
=-\mathcal M_XU_\pm'(X)+\zeta_X(t),
\qquad
\mathcal M_X=\gamma_X^{-1}.
}

Agora a mobilidade causal, ausente numa Hessiana puramente estática, aparece
como momento de baixa frequência do espectro do aparelho.

---

## 12. Tempos físicos do aparelho

Perto de uma bacia \(X_*\), a taxa linear de relaxação superamortecida é

\[
\boxed{
\tau_{\rm relax}^{-1}
=\mathcal M_XU_\pm''(X_*).
}

Para escapar termicamente de uma bacia, a aproximação de Kramers fornece

\[
\Gamma_{\rm escape}
\sim
\frac{\sqrt{|U''(X_b)|U''(X_*)}}{2\pi\gamma_X}
\exp\left(-\frac{\Delta U}{k_BT}\right),
\]

onde \(X_b\) é o topo da barreira.

Um registro confiável exige:

\[
\boxed{
\tau_{\rm escape}\gg
\tau_{\rm leitura}\gg
\tau_{\rm relax}.
}

Essas desigualdades oferecem um critério físico para separar uma interação
reversível de uma medição com registro persistente.

---

## 13. Ligação com \(\kappa_H^{\rm SG}\) e \(\Gamma_{\rm SG}\)

O complemento de Schur dinâmico do aparelho é

\[
K_Q^{\rm eff}(\omega)
=K_Q-J_{QX}G_X^{\rm ret}(\omega)J_{XQ}.
\]

Expandindo em baixa frequência:

\[
K_Q^{\rm eff}(\omega)
=K_Q^{\rm eff}(0)
-i\omega\,mathcal D_{\rm SG}
+O(\omega^2).
\]

Então:

- a parte estática de \(K_Q^{\rm eff}(0)\) contribui para
  \(\kappa_H^{\rm SG}\);
- a parte dissipativa \(\mathcal D_{\rm SG}\) contribui para
  \(\Gamma_{\rm SG}\);
- ambas provêm do mesmo espectro, mas são momentos espectrais distintos.

Esquematicamente:

\[
\boxed{
\kappa_H^{\rm SG}
\sim J_{QX}^2\operatorname{Re}G_X^{\rm ret}(0),
}
\]

\[
\boxed{
\Gamma_{\rm SG}
\sim\frac{J_{QX}^2}{\hbar^2}
\lim_{\omega\to0}
\frac{\operatorname{Im}G_X^{\rm ret}(\omega)}{\omega}.
}

Os fatores exatos dependem da normalização dos modos e do observável do
aparelho.

---

## 14. O que este modelo ainda não demonstra

Este documento não deriva ainda:

1. o modo \(T_X\) de um eletroímã ou detector concreto;
2. os sinais \(a_2<0\) e \(a_4>0\) para um background real;
3. a densidade espectral \(J_A(\omega)\) a partir do material;
4. o valor de \(g_X\);
5. a regra de Born para a captura individual;
6. uma quebra fundamental da unitariedade;
7. dois resultados a partir do potencial Zeeman isolado.

Ele demonstra quais quantidades devem ser avaliadas e como a amplificação,
a dissipação e a memória podem emergir da mesma ação depois da redução modal.

---

## 15. Próximo cálculo intrínseco

O próximo passo é escolher o modo coletivo mais simples e calculável. Há duas
opções complementares:

### Rota A — Ponteiro abstrato universal

Manter \(T_X\) genérico e derivar as condições espectrais suficientes para
Born, captura e estabilidade. Essa rota fecha a teoria matemática geral, mas
não produz números de um aparelho específico.

### Rota B — Detector Stern--Gerlach concreto

Escolher:

1. geometria do eletroímã;
2. material ou modo mecânico do detector;
3. corrente clássica;
4. temperatura;
5. perfil de campo;
6. modo legível.

Então calcular \(T_X,A,B,g_X,J_A(\omega)\) e as escalas temporais.

A ordem recomendada é concluir primeiro a Rota A e depois usar a Rota B como
teste quantitativo.

## 16. Status

\[
\boxed{
\text{Modelo mínimo do aparelho fechado estruturalmente como redução modal;}
\quad
\text{coeficientes de um aparelho real permanecem por calcular.}
}
\]
