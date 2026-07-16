# Redução da Hessiana torsional para o canal macroscópico GDQ

## 1. Objetivo

Este documento constrói o primeiro background local capaz de fornecer
\(Z_t\), \(Z_x\), \(c_A\) e \(\gamma_A\) diretamente do setor torsional da
ação GDQ.

A construção usa:

1. o bulk local oficial \(\mathbb R^4\times T^4\);
2. a decomposição oficial

   \[
   H=d\mathcal A+H_{\rm top};
   \]

3. o termo de Bismut

   \[
   \mathcal R_B
   =\mathcal R_{LC}-\frac1{12}H_{ABC}H^{ABC}
   +\text{divergência};
   \]

4. uma 2-forma harmônica do toro interno;
5. propagação ao longo de uma direção física aberta.

O resultado é um canal torsional gapless cuja impedância é uma norma ponderada
da ação oficial.

---

## 2. Convenção torsional vigente

Nas Questões 2, 12 e 19, o setor de torção é escrito como

\[
\boxed{H=d\mathcal A+H_{\rm top},}
\]

onde \(\mathcal A\) é um potencial de 2-forma e \(H_{\rm top}\) representa uma
classe fechada não exata.

O termo local é

\[
S_H
=-\frac1{12}
\int H_{ABC}H^{ABC}\,d\mu.
\]

Usando a norma de formas

\[
|H|^2_{\rm form}
=\frac1{3!}H_{ABC}H^{ABC},
\]

temos

\[
-\frac1{12}H_{ABC}H^{ABC}
=-\frac12|H|^2_{\rm form}.
\]

Essa é a normalização canônica de uma 3-forma de campo.

---

## 3. Célula do aparelho

Considere localmente

\[
\Omega_A
=\mathbb R_t\times\mathbb R_{+,x}
\times\Sigma_2\times T^4,
\]

onde:

- \(t\) é o tempo físico reconstruído;
- \(x\ge0\) é a direção aberta do canal;
- \(\Sigma_2\) representa duas direções físicas transversais integradas;
- \(T^4\) é o setor interno oficial.

A soma das dimensões é

\[
1+1+2+4=8.
\]

O background é aproximadamente produto na célula:

\[
g_*simeq
-c_{m phys}^2dt^2+dx^2+g_{\Sigma_2}+g_{T^4}
\]

depois da reconstrução lorentziana. A medida ponderada varia lentamente na
direção do canal:

\[
\left|\partial_x\log(\mathcal U_*\sqrt{g_*})\right|
L_{\rm cel}\ll1.
\]

Essa é a aproximação local/WKB. Não se afirma que um toro plano compacto com
\(f\) constante seja shrinker global.

---

## 4. Forma harmônica interna

Escolha

\[
\omega_I\in\mathcal H^2(T^4),
\]

com

\[
d\omega_I=0,
\qquad
d^\dagger\omega_I=0,
\qquad
\Delta_{T^4}\omega_I=0.
\]

Como

\[
b_2(T^4)=6,
\]

existem seis direções harmônicas reais antes das seleções adicionais de
quiralidade, polarização e acoplamento ao objeto.

Normalize localmente:

\[
\boxed{
\int_{T^4}
|\omega_I|^2
\mathcal U_*\sqrt{g_{T^4}}\,d^4y
=N_I.
}

\]

Pode-se escolher \(N_I=1\) como normalização modal, mas o valor físico deve
manter a normalização compatível com a carga e com o acoplamento torsional.

---

## 5. Ansatz do canal torsional

Considere uma flutuação do potencial de 2-forma:

\[
\boxed{
\delta\mathcal A
=y(x,t)\,\omega_I.
}

Então:

\[
\delta H
=d\delta\mathcal A
=dy\wedge\omega_I,
\]

isto é,

\[
\boxed{
\delta H
=(\partial_ty)dt\wedge\omega_I
+(\partial_xy)dx\wedge\omega_I.
}

Como \(\omega_I\) é harmônica, não aparece termo de massa proveniente do
Laplaciano interno.

---

## 6. Redução do termo quadrático

Para uma métrica produto e formas em fatores ortogonais:

\[
|dy\wedge\omega_I|^2
=|dy|^2|\omega_I|^2.
\]

Na assinatura física:

\[
|dy|^2
=-\frac1{c_{m phys}^2}(\partial_ty)^2
+(\partial_xy)^2.
\]

Portanto:

\[
-\frac12|\delta H|^2
=\frac{|\omega_I|^2}{2c_{m phys}^2}
(\partial_ty)^2
-\frac{|\omega_I|^2}{2}(\partial_xy)^2.
\]

Integrando \(T^4\), \(\Sigma_2\) e o contorno de escala da ação, obtemos

\[
\boxed{
S_{H,I}^{(2)}
=\frac12\int dt\,dx
\left[
Z_t^{(I)}(\partial_ty)^2
-Z_x^{(I)}(\partial_xy)^2
\right].
}

---

## 7. Coeficientes diretamente da ação oficial

No termo torsional da ação oficial, o fator \(\tau\) que multiplica
\(\mathcal R_B\) cancela \(d\tau/\tau\). Defina o funcional de projeção física
do contorno causal:

\[
\mathfrak C_\gamma[Q]
:=
\operatorname{Phys}
\int_\gamma Q(z_\tau)\,d\tau,
\]

onde \(\operatorname{Phys}\) significa a combinação real/causal selecionada
pela reconstrução OS e pela orientação de \(\gamma\). Não se deve inserir um
resíduo adicional que não exista na ação.

Então:

\[
\boxed{
Z_x^{(I)}
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma
\left[
\int_{\Sigma_2\times T^4}
\mathcal U_*|\omega_I|^2
\sqrt{g_\perp}\,d^6z
\right].
}

Para a métrica local isotrópica:

\[
\boxed{
Z_t^{(I)}
=\frac{Z_x^{(I)}}{c_{\mathrm{phys}}^2}.
}
\]

Em coordenada temporal \(x^0=c_{\mathrm{phys}}t\), os dois coeficientes são a mesma
norma geométrica.

Se o background for anisotrópico, a forma geral é

\[
Z_t^{(I)}
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma
\left[
\int\mathcal U_*
\langle dt\wedge\omega_I,
dt\wedge\omega_I\rangle_{\rm phys}
dV_\perp
\right],
\]

\[
Z_x^{(I)}
=\frac{\hbar}{\Lambda_C^2}
\mathfrak C_\gamma
\left[
\int\mathcal U_*
\langle dx\wedge\omega_I,
dx\wedge\omega_I\rangle_{\rm phys}
dV_\perp
\right].
\]

---

## 8. Velocidade e impedância

Comparando com

\[
S^{(2)}
=\frac{\zeta_A}{2}
\int dt\,dx
\left[
\frac1{c_A^2}(\partial_ty)^2
-(\partial_xy)^2
\right],
\]

resulta:

\[
\boxed{\zeta_A=Z_x^{(I)},}
\]

\[
\boxed{c_A^2=\frac{Z_x^{(I)}}{Z_t^{(I)}}.}
\]

O DtN do domínio semi-infinito fornece

\[
\boxed{
\gamma_A
=\frac{\zeta_A}{c_A}
=\sqrt{Z_t^{(I)}Z_x^{(I)}}.
}

No background local isotrópico:

\[
c_A=c_{\rm phys},
\qquad
\gamma_A=\frac{Z_x^{(I)}}{c_{\rm phys}}.
\]

---

## 9. Prova de ausência de gap na ordem quadrática

O operador reduzido é

\[
\mathcal O_I
=-Z_t^{(I)}\partial_t^2
+Z_x^{(I)}\partial_x^2
+m_I^2.
\]

O termo de massa transversal é proporcional ao autovalor interno:

\[
m_I^2\propto
\langle\omega_I,\Delta_{T^4}\omega_I\rangle.
\]

Como \(\omega_I\) é harmônica:

\[
\boxed{m_I^2=0.}
\]

A dispersão é

\[
\boxed{\omega^2=c_A^2k^2.}
\]

Logo o canal possui o contínuo gapless necessário ao limite ôhmico, desde que
a direção \(x\) seja realmente aberta ou suficientemente longa para que o
espectro seja quase contínuo.

---

## 10. Gauge e modos físicos

O potencial de 2-forma possui transformação

\[
\mathcal A\longmapsto\mathcal A+d\Lambda.
\]

O ansatz \(y\omega_I\) não é gauge puro se \([\omega_I]\ne0\) em
\(H^2(T^4)\) e \(y\) varia nas direções externas. Seu campo

\[
H=dy\wedge\omega_I
\]

é não nulo e gauge-invariante.

Ainda assim, a redução completa deve impor gauge de Lorenz para 2-formas ou a
projeção de Hodge equivalente, removendo:

- componentes exatas;
- modos longitudinais;
- redundâncias de \(\Lambda\);
- zero modes que não acoplam ao contorno.

---

## 11. Positividade física e reconstrução OS

O funcional auxiliar de Perelman--Bismut contém o sinal

\[
-\frac1{12}|H|^2.
\]

Esse sinal, isoladamente, não deve ser interpretado como energia euclidiana
positiva ou negativa: \(\mathcal F_T\) e \(\mathcal W_T\) são funcionais de
fluxo/entropia, não o Hamiltoniano físico.

A ação causal efetiva da Questão 2 produz, após a escolha de assinatura, a
forma padrão

\[
\frac12Z_t\dot y^2-\frac12Z_x(y')^2.
\]

Para que o canal seja admissível, é obrigatório verificar:

\[
\boxed{Z_t^{(I)}>0,\qquad Z_x^{(I)}>0.}
\]

Essa positividade deve seguir da reconstrução OS e do produto interno físico.
Se a projeção de \(\gamma\) produzir sinal contrário, o modo não pertence ao
setor físico estável e não pode ser usado como canal do aparelho.

---

## 12. Seleção da direção que acopla ao objeto

Há seis formas harmônicas em \(T^4\), mas o acoplamento de Stern--Gerlach
seleciona somente combinações com sobreposição não nula:

\[
\boxed{
g_I
\propto
\int_\Sigma
\mathcal T_Q^{AB}
(dX\wedge\omega_I)_{AB\cdots}
d\mu_\Sigma.
}

A matriz de Gram torsional é

\[
\boxed{
G_{IJ}^{\rm int}
=\langle\omega_I,\omega_J\rangle_{\mathcal U_*}.
}

O vetor de acoplamentos \(g_I\) seleciona a direção física normalizada

\[
\omega_{\rm SG}
=\frac{g^I\omega_I}
{\sqrt{g^IG_{IJ}^{\rm int}g^J}}.
\]

Assim, a direção torsional do aparelho não precisa ser escolhida manualmente:
ela é determinada pela projeção da fonte clássica e do perfil do objeto no
espaço harmônico interno.

---

## 13. Taxa informacional resultante

Substituindo a impedância na fórmula do detector clássico:

\[
\Gamma_A
=\frac{g_X^2}{8\gamma_Ak_BT_A},
\]

obtemos

\[
\boxed{
\Gamma_A
=\frac{g_X^2}
{8k_BT_A\sqrt{Z_t^{(\rm SG)}Z_x^{(\rm SG)}}}.
}

No caso local isotrópico:

\[
\boxed{
\Gamma_A
=\frac{g_X^2c_{\rm phys}}
{8k_BT_AZ_x^{(\rm SG)}}.
}

Agora todos os coeficientes pertencem a projeções da ação ou a dados legítimos
do aparelho. O número ainda não pode ser avaliado porque faltam o background,
a normalização física de \(\gamma\) e o perfil de sobreposição \(g_X\).

---

## 14. Correções ao limite ideal

### 14.1 Peso lentamente variável

Se

\[
w(x)=\mathcal U_*(x)\sqrt{g_*(x)}
\]

não for constante, o operador longitudinal é

\[
\boxed{
L_xy
=-\frac1w\partial_x(wZ_x\partial_xy).
}

O DtN torna-se dependente da frequência e o espectro é colorido.

### 14.2 Canal finito

Para comprimento \(L_A\), o espectro é discreto, com espaçamento

\[
\Delta\omega\sim\frac{\pi c_A}{L_A}.
\]

O limite ôhmico requer tempos menores que o tempo de retorno ou mecanismos de
absorção na extremidade.

### 14.3 Forma interna não harmônica

Se

\[
\Delta_{T^4}\omega_I=\lambda_I\omega_I,
\qquad\lambda_I>0,
\]

então surge gap:

\[
m_I^2\propto\lambda_I.
\]

O canal deixa de ser ôhmico abaixo da frequência de corte.

### 14.4 Mistura métrica--dílaton--torção

Em background com \(H_*\ne0\), a Hessiana não é bloco diagonal. Deve-se usar o
complemento de Schur:

\[
K_H^{\rm eff}
=K_H-J_{Hg,f}K_{g,f}^{-1}J_{g,fH}.
\]

Essa mistura pode alterar \(Z_t,Z_x\), abrir gap ou criar dispersão.

---

## 15. O que foi derivado

1. ansatz torsional intrínseco no bulk oficial;
2. redução do termo \(-H^2/12\) para um campo propagante 1D;
3. fórmulas de \(Z_t\) e \(Z_x\) como normas da ação;
4. velocidade \(c_A^2=Z_x/Z_t\);
5. impedância \(\gamma_A=\sqrt{Z_tZ_x}\);
6. gap nulo pela harmonicidade em \(T^4\);
7. seleção da polarização por matriz de Gram e sobreposição;
8. taxa informacional em função das projeções GDQ;
9. correções por peso, tamanho finito, gap e mistura de setores.

---

## 16. O que permanece

1. escolher e resolver \(g_*,f_*,H_*\) da célula macroscópica;
2. avaliar a projeção causal \(\mathfrak C_\gamma\);
3. demonstrar positividade OS para o modo torsional;
4. calcular a matriz \(G_{IJ}^{\rm int}\) no background físico;
5. calcular \(g_X\) com o perfil do estômato;
6. incluir a mistura com métrica e dílaton;
7. testar um canal finito e colorido.

## 17. Próximo passo

O próximo cálculo deve construir um background produto local explícito com
raios do \(T^4\), normalizar as seis formas harmônicas e calcular a matriz de
Gram. Isso permitirá determinar a dependência de \(Z_x\) nos raios internos e
identificar quais combinações podem acoplar ao setor de Hopf.

Esse cálculo foi realizado em `gram_torcional_t4_interface.md`. A matriz de
Gram foi obtida para raios arbitrários e o espaço harmônico foi decomposto nos
tripletos auto-dual e anti-auto-dual. A verificação algébrica está em
`interface_medida/test_gram_t4.py`.

## 18. Status

\[
\boxed{
\text{Hessiana torsional reduzida e canal gapless derivados
estruturalmente da ação oficial;}
\quad
\text{normalização causal e background material permanecem abertos.}
}
\]
