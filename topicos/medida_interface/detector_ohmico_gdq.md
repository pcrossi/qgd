# Detector ôhmico idealizado derivado de um canal geométrico GDQ

## 1. Objetivo

Este documento inicia a Rota B da teoria da interface. O aparelho idealizado é
formado por:

1. um ponteiro bistável \(X(t)\);
2. o acoplamento torsional ao canal de Hopf do objeto;
3. um canal geométrico semi-infinito que transporta energia e informação para
   os graus macroscópicos do aparelho;
4. uma condição de radiação retardada no infinito.

A vantagem dessa escolha é que o operador Dirichlet--to--Neumann do canal pode
ser calculado exatamente. Ele produz dissipação ôhmica sem inserir um termo de
atrito manualmente.

O modelo continua sendo uma redução quadrática da ação oficial. Ele não é uma
nova ação fundamental da GDQ.

---

## 2. Redução modal do canal do aparelho

Considere uma coordenada longitudinal \(x\ge0\) no canal de saída e uma
perturbação física normalizada \(y(x,t)T_y\) do background do aparelho.

Depois da reconstrução do tempo físico, a projeção quadrática da ação oficial
assume a forma normal

\[
\boxed{
S_{\rm canal}^{(2)}
=\frac{\zeta_A}{2}
\int dt\int_0^\infty dx
\left[
\frac1{c_A^2}(\partial_ty)^2
-(\partial_xy)^2
\right].
}
\]

Os coeficientes são projeções dos símbolos temporal e espacial da Hessiana
física:

\[
\boxed{
\frac{\zeta_A}{c_A^2}
=\langle T_y,K_tT_y\rangle_{\mathcal U_*},
}
\]

\[
\boxed{
\zeta_A
=\langle T_y,K_xT_y\rangle_{\mathcal U_*}.
}
\]

Em termos da ação oficial, esses produtos internos contêm o prefator
\(\hbar/\Lambda_C^2\), a medida \(\mathcal U_*\sqrt{g_*}\), a integração na
seção transversal do canal e as projeções físicas de gauge.

Portanto, \(\zeta_A\) e \(c_A\) não são constantes universais: dependem do
background e da seção transversal do aparelho.

---

## 3. Equação bulk e condição de colagem

A equação do canal é

\[
\boxed{
\frac1{c_A^2}\partial_t^2y-\partial_x^2y=0.
}
\]

O ponteiro é o valor de bordo do modo:

\[
\boxed{y(0,t)=X(t).}
\]

Essa identificação é o limite de colagem rígida. Uma interface de impedância
finita pode ser introduzida posteriormente por um termo de cola derivado.

No infinito impõe-se a condição causal de radiação: somente ondas que saem da
interface em direção ao aparelho macroscópico são admitidas.

---

## 4. DtN retardado do canal

Use a convenção de Fourier

\[
y(x,t)=\int\frac{d\omega}{2\pi}
e^{-i\omega t}y_\omega(x).
\]

A solução que satisfaz radiação de saída é

\[
\boxed{
y_\omega(x)=X_\omega e^{i\omega x/c_A}.
}
\]

Logo:

\[
\partial_xy_\omega(0)
=\frac{i\omega}{c_A}X_\omega.
\]

O fluxo canônico do canal sobre a interface é, com orientação escolhida de
modo que a potência radiada seja positiva,

\[
\Pi_A(\omega)
=-\zeta_A\partial_xy_\omega(0).
\]

Assim, o DtN retardado é

\[
\boxed{
\Lambda_A^{\rm ret}(\omega)
=-i\omega\frac{\zeta_A}{c_A}.
}
\]

Defina

\[
\boxed{\gamma_A=\frac{\zeta_A}{c_A}>0.}
\]

Então:

\[
\boxed{
\Lambda_A^{\rm ret}(\omega)=-i\gamma_A\omega.
}
\]

Essa é uma impedância exatamente ôhmica. A dissipação foi produzida pelo DtN
retardado de um domínio aberto, não por um termo de atrito acrescentado ao
bulk.

---

## 5. Balanço de energia

A energia do canal é

\[
E_A
=\frac{\zeta_A}{2}
\int_0^\infty dx
\left[
\frac1{c_A^2}(\partial_ty)^2
+(\partial_xy)^2
\right].
\]

Para a solução de saída, o fluxo médio de potência na interface é

\[
\boxed{
\mathcal P_{\rm out}
=\gamma_A\,\dot X^2\ge0.
}

Portanto, o sinal da impedância é fixado pela exigência física de energia
fluindo do ponteiro para o canal macroscópico.

---

## 6. Equação efetiva do ponteiro

O potencial condicionado ao canal \(\kappa=\pm1\) é

\[
U_\kappa(X)
=-\frac A2X^2+\frac B4X^4-g_X\kappa X.
\]

Incluindo a inércia do modo coletivo e o DtN:

\[
\boxed{
M_X\ddot X+\gamma_A\dot X+U_\kappa'(X)=\xi_A(t).
}

A mobilidade no limite superamortecido é

\[
\boxed{\mathcal M_X=\gamma_A^{-1}=\frac{c_A}{\zeta_A}.}
\]

Agora a mobilidade causal foi obtida diretamente do canal aberto.

---

## 7. Flutuação--dissipação

Se o canal do aparelho está em equilíbrio à temperatura \(T_A\), a relação de
flutuação--dissipação no limite clássico fornece

\[
\boxed{
\langle\xi_A(t)\xi_A(t')\rangle
=2\gamma_Ak_BT_A\,\delta(t-t').
}

No domínio de frequências, a forma quântica simetrizada é

\[
\boxed{
S_\xi^{\rm sym}(\omega)
=\gamma_A\hbar|\omega|
\coth\left(\frac{\hbar|\omega|}{2k_BT_A}\right),
}

salvo fatores de dois definidos pela convenção unilateral ou bilateral do
espectro.

No limite \(k_BT_A\gg\hbar|\omega|\):

\[
S_\xi^{\rm sym}(\omega)\to2\gamma_Ak_BT_A.
\]

O limite \(T_A\to0\) não pode ser avaliado pela fórmula clássica branca; deve
usar o espectro quântico completo.

---

## 8. Linearização perto de um registro

Seja \(X_\kappa^*\) o mínimo favorecido, definido por

\[
U_\kappa'(X_\kappa^*)=0.
\]

Defina a rigidez local

\[
\boxed{k_\kappa=U_\kappa''(X_\kappa^*)>0.}
\]

Para \(x=X-X_\kappa^*\):

\[
M_X\ddot x+\gamma_A\dot x+k_\kappa x=\xi_A.
\]

A susceptibilidade retardada é

\[
\boxed{
G_X^{\rm ret}(\omega)
=\frac1{k_\kappa-M_X\omega^2-i\gamma_A\omega}.
}

No regime superamortecido e de baixa frequência:

\[
\tau_{\rm relax}
=\frac{\gamma_A}{k_\kappa}.
\]

---

## 9. Registro normalizado e taxa informacional

### 9.1 Dinâmica linear usada para leitura

Antes da saturação completa da bacia, considere a aproximação local

\[
\gamma_A dX_t
=(-kX_t+g_X\kappa)dt
+\sqrt{2\gamma_Ak_BT_A}\,dW_t.
\]

Dividindo pela amplitude de ruído, o incremento de inovação mensurável é

\[
\boxed{
dY_t
=\frac{\gamma_A dX_t+kX_tdt}
{\sqrt{2\gamma_Ak_BT_A}}
=\frac{g_X}{\sqrt{2\gamma_Ak_BT_A}}
\kappa dt+dW_t.
}
\]

Comparando com a normalização usada no teorema de captura,

\[
dY_t=2\sqrt{\Gamma_A}\,\kappa dt+dW_t,
\]

obtemos

\[
\boxed{
\Gamma_A
=\frac{g_X^2}{8\gamma_Ak_BT_A}
=\frac{g_X^2c_A}{8\zeta_Ak_BT_A}.
}
\]

Esta é a primeira taxa informacional explícita da teoria de interface para um
detector GDQ idealizado.

### 9.2 Interpretação

- maior acoplamento \(g_X\) aumenta a taxa quadraticamente;
- maior ruído térmico reduz a informação;
- maior impedância \(\gamma_A\) reduz a taxa para a normalização adotada;
- a rigidez \(k\) cancela no registro de inovação ideal porque o drift
  conhecido é subtraído causalmente;
- com largura de banda finita ou ruído adicional de leitura, \(k\) reaparece.

### 9.3 Domínio de validade

A fórmula exige:

1. regime térmico clássico;
2. ruído branco ôhmico;
3. observação ideal de \(X_t\);
4. canal QND conservado;
5. dinâmica linear no intervalo de aquisição;
6. ausência de ruído técnico adicional.

Ela diverge formalmente quando \(T_A\to0\), sinalizando apenas a falha da
aproximação clássica. O cálculo de baixa temperatura requer filtragem com o
espectro quântico colorido.

---

## 10. Tempo de leitura e erro

Para taxa constante, a informação acumulada é

\[
\mathcal I(t)=\Gamma_At.
\]

O erro ideal é

\[
\boxed{
P_{\rm erro}(t)
=\Phi(-2\sqrt{\Gamma_At}).
}

Para um erro máximo \(\epsilon\):

\[
\boxed{
t_{\rm leitura}
\ge
\frac{[\Phi^{-1}(\epsilon)]^2}{4\Gamma_A}.
}

Substituindo a taxa:

\[
\boxed{
t_{\rm leitura}
\ge
\frac{2\gamma_Ak_BT_A}{g_X^2}
[\Phi^{-1}(\epsilon)]^2.
}

O aparelho deve ainda satisfazer

\[
\tau_{\rm escape}\gg t_{\rm leitura}
\gg\tau_{\rm relax}
\]

para registrar com pequena ambiguidade e preservar o resultado.

---

## 11. Taxa de decoerência e eficiência

O canal aberto carrega informação sobre \(\kappa\). Se toda a informação
irradiada for observada e não houver canais perdidos, o detector é ideal e a
taxa de perda de coerência está ligada à taxa informacional por uma eficiência
\(\eta=1\), conforme a convenção usada na equação condicionada.

Com perdas, defina

\[
0<\eta\le1,
\qquad
\Gamma_{\rm info}=\eta\Gamma_{\rm deph}.
\]

Na GDQ, \(\eta\) deve ser calculada como a fração do fluxo espectral total que
alcança o canal monitorado:

\[
\boxed{
\eta
=\frac{\mathcal P_{\rm monitorada}}
{\mathcal P_{\rm total}}.
}
\]

Não se deve tomar \(\eta=1\) para um aparelho real sem inventariar os canais de
perda.

---

## 12. Relação com o Stern--Gerlach espacial

O canal de medida acima registra \(\kappa\). A separação espacial continua
governada por

\[
\boldsymbol F_\kappa
=\kappa\mu_{\rm GDQ}
\boldsymbol\nabla|\boldsymbol B_A|.
\]

Para tempo de trânsito \(t_m=L/v\), em gradiente aproximadamente constante:

\[
\Delta z_\kappa
=\kappa
\frac{\mu_{\rm GDQ}}{2m}
\frac{\partial B}{\partial z}
\left(\frac L v\right)^2.
\]

O experimento completo exige simultaneamente:

1. separação espacial maior que a largura do feixe;
2. informação acumulada suficiente;
3. transição não adiabática pequena;
4. estabilidade do registro na tela.

---

## 13. Critérios de consistência experimental

Defina:

- \(\sigma_z\): largura transversal do feixe;
- \(t_m\): tempo no ímã;
- \(P_{\rm LZ}\): probabilidade de transição não adiabática;
- \(\epsilon\): erro de leitura;
- \(\tau_{\rm escape}\): vida do registro.

Um regime de boa medição exige:

\[
\boxed{|\Delta z_+-\Delta z_-|\gg\sigma_z,}
\]

\[
\boxed{\Gamma_At_m\gg1,}
\]

\[
\boxed{P_{\rm LZ}\ll1,}
\]

\[
\boxed{\tau_{\rm escape}\gg t_{\rm leitura}.}
\]

Esses quatro números adimensionais separam deflexão, aquisição de informação,
adiabaticidade e memória.

---

## 14. O que foi calculado

### 14.1 Resultado exato no modelo idealizado

1. DtN retardado:

   \[
   \Lambda_A^{\rm ret}=-i\omega\zeta_A/c_A;
   \]

2. coeficiente de atrito:

   \[
   \gamma_A=\zeta_A/c_A;
   \]

3. mobilidade:

   \[
   \mathcal M_X=c_A/\zeta_A;
   \]

4. ruído térmico pela flutuação--dissipação;
5. susceptibilidade retardada do ponteiro;
6. taxa informacional clássica:

   \[
   \Gamma_A=g_X^2/(8\gamma_Ak_BT_A);
   \]

7. tempo e erro de leitura.

### 14.2 Quantidades ainda não numéricas

Os números exigem:

- background do aparelho;
- modo transversal \(T_y\);
- projeções \(\zeta_A,c_A\);
- acoplamento \(g_X\);
- temperatura e geometria experimentais.

---

## 15. Limitações do detector idealizado

1. o canal é unidimensional e sem dispersão;
2. o espectro é exatamente ôhmico;
3. a colagem \(y(0)=X\) é rígida;
4. o ruído técnico é ignorado;
5. o regime de baixa temperatura requer extensão quântica;
6. o material real pode possuir gaps, bandas e memória;
7. a tela de detecção não foi microscopicamente modelada;
8. \(\mu_{\rm GDQ}\) e \(g_X\) ainda dependem do perfil torsional.

Essas limitações não invalidam o resultado estrutural. Elas delimitam o
primeiro detector calculável da teoria.

---

## 16. Próximo passo

O próximo passo deve ser duplo:

1. construir um teste numérico deste detector, verificando o filtro, a taxa
   \(\Gamma_A\), o erro e as escalas temporais;
2. procurar no manuscrito um background macroscópico simples que permita
   avaliar \(\zeta_A/c_A\) pela ação oficial, substituindo a impedância
   abstrata por uma projeção geométrica concreta.

O teste foi implementado em
`interface_medida/test_detector_ohmico_gdq.py`, com saída consolidada em
`interface_medida/saida_detector_ohmico_gdq.md`. A busca do background foi
documentada em `topicos/medida_interface/auditoria_background_macroscopico_interface.md`: o manuscrito
contém a arquitetura NESS e o DtN microscópico, mas ainda não contém uma
solução macroscópica global com Hessiana e espectro contínuo calculados.

## 17. Status

\[
\boxed{
\text{Rota B fechada analiticamente para um canal GDQ idealizado;}
\quad
\text{avaliação material e geométrica permanece aberta.}
}
\]
