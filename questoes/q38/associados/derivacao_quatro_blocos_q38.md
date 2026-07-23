# Q38 — execução dos quatro blocos a partir da ação oficial da GDQ

## 0. Convenções e objetivo

A ação usada é exclusivamente

\[
\mathcal S_{\rm GDQ}=\int_\gamma\!\left[\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}\left\{
\tau\left(\mathcal R+g^{\mu\bar\nu}\partial_\mu f
\partial_{\bar\nu}\bar f\right)+\frac{f+\bar f}{2}-n
\right\}\mathcal U\,dV_g\right]\frac{d\tau}{\tau}.
\]

Escrevemos \(\sigma=(f+\bar f)/2\), \(n=4\) e
\(\mathcal U=(4\pi\tau)^{-4}e^{-\sigma}\). A conexão de Bismut só pode
entrar por \(\mathcal R\) se esta for, por definição da GDQ, a curvatura
escalar dessa conexão. Nenhum termo de Yang--Mills ou Pontryagin é acrescentado
à ação.

O objetivo é determinar o que os quatro blocos produzem logicamente e quais
quantidades permanecem livres.

---

## 1. Bloco I — redução 8D e equações do background

### 1.1 Ansatz dimensionalmente consistente

Usamos

\[
\mathcal M_8=N_4\times I_r\times S^3,
\]

\[
ds_8^2=e^{2A(r,\tau)}h_{\mu\nu}(x)dx^\mu dx^\nu
+dr^2+R(r,\tau)^2d\Omega_3^2.
\]

Definimos \(B=\log R\). Para o background externo plano, os componentes da
curvatura de Levi--Civita são

\[
\operatorname{Ric}_{\mu\nu}
=-\left(A''+4A'^2+3A'B'\right)g_{\mu\nu},
\]

\[
\operatorname{Ric}_{rr}
=-4(A''+A'^2)-3(B''+B'^2),
\]

e, nas direções de \(S^3\),

\[
\operatorname{Ric}_{ab}
=\frac{2(1-R'^2)-RR''-4RR'A'}{R^2}\,g_{ab}.
\]

Para \(\sigma=\sigma(r,\tau)\),

\[
\nabla_\mu\nabla_\nu\sigma=A'\sigma' g_{\mu\nu},
\quad
\nabla_r\nabla_r\sigma=\sigma'',
\quad
\nabla_a\nabla_b\sigma=\frac{R'}R\sigma'g_{ab}.
\]

Adotando fluxo de Ricci--Bismut na gauge gradiente

\[
\partial_\tau g_{IJ}
=-2\left(\operatorname{Ric}_{IJ}-\frac14H_{IKL}H_J{}^{KL}
+\nabla_I\nabla_J\sigma\right),
\]

e fluxo interno

\[
H=\frac{2k}{R^3}\operatorname{vol}_{S^3},
\qquad
H_{acd}H_b{}^{cd}=\frac{8k^2}{R^6}g_{ab},
\]

obtemos, componente a componente,

\[
\boxed{
\dot A=A''+4A'^2+3A'\frac{R'}R-A'\sigma'.
}
\]

No gauge radial \(g_{rr}=1\), a equação \(rr\) não é uma evolução
independente: ela é o vínculo

\[
\boxed{
4(A''+A'^2)+3\left(\frac{R''}R\right)-\sigma''=0,
}
\]

onde foi usado \(B''+B'^2=R''/R\). A equação da esfera é

\[
\boxed{
\dot R=R''+4A'R'
+\frac{2(R'^2-1)}R
+\frac{2k^2}{R^5}-R'\sigma'.
}
\]

Os sinais de \(\sigma\) mudam se o parâmetro de fluxo for definido no sentido
reverso ou se a difeomorfia de Perelman for movida para o outro lado. Essa
convenção deve ser mantida junto com a orientação de \(\gamma\).

### 1.2 Equação da medida

A conservação local de \(\mathcal U dV\) fornece a equação de calor conjugada.
Na convenção acima, sua forma reduzida é

\[
\boxed{
\dot\sigma=-\Delta_8\sigma+|\nabla\sigma|^2-\mathcal R_B
+\frac4\tau,
}
\]

\[
\Delta_8\sigma=\sigma''+
\left(4A'+3\frac{R'}R\right)\sigma'.
\]

Um multiplicador dependente de \(\tau\) pode ser somado para impor a
normalização global; ele fixa apenas o modo espacial constante de \(\sigma\).

### 1.3 Dados necessários e resultado

O sistema exige, além da ação:

- valor/quantização de \(k\);
- condições em \(r=0\) e na extremidade oposta;
- dado inicial em \(\tau\);
- escolha da orientação temporal de \(\gamma\);
- definição precisa de \(\mathcal R_B\).

Sem esses dados há uma família de backgrounds, não um background único.

---

## 2. Bloco II — coeficiente de Einstein--Hilbert e resíduo causal

Para uma métrica externa lentamente variável,

\[
\mathcal R_B[g]
=\eta_R e^{-2A}R[h]+\mathcal R_{B,\rm int}+\cdots,
\]

\[
dV_8=e^{4A}\sqrt{-h}\,R^3dr\,d\Omega_3\,d^4x.
\]

Logo,

\[
F_{EH}(\tau)=\int_{I_r\times S^3}
\eta_R e^{2A}\mathcal U R^3\,dr\,d\Omega_3,
\]

\[
\boxed{
C_R=\frac{\hbar}{\Lambda_C^2}\mathfrak C_\gamma[F_{EH}],
\qquad
G=\frac{c^4}{16\pi C_R}.
}
\]

### 2.1 Teorema de regularidade

Se \(A,R,\sigma\) forem holomorfos em \(\tau_*\), a fibra tiver volume
finito e a integral for uniformemente convergente, então \(F_{EH}\) é
holomorfa em \(\tau_*\). Portanto,

\[
\operatorname{Res}_{\tau_*}F_{EH}=0.
\]

Assim, um resíduo não nulo requer necessariamente quebra de pelo menos uma
dessas hipóteses: polo do warp, singularidade não integrável da medida,
degeneração do domínio ou contribuição explícita de contorno.

### 2.2 Condição de fechamento local

Suponha a expansão dominante

\[
A=-\frac p2\log w+A_0(r)+o(1),\quad
R=w^qR_0(r)+o(w^q),\quad
e^{-\sigma}=w^sU_0(r)+o(w^s),
\]

com \(w=\tau-\tau_*\). Então

\[
F_{EH}\sim w^{-p+3q+s}
\int\eta_R e^{2A_0}U_0R_0^3,dr,d\Omega_3.
\]

Existe polo simples precisamente se

\[
\boxed{-p+3q+s=-1.}
\]

e a integral do coeficiente for finita e não nula. Esta é a condição
assintótica que deve emergir das EDPs; ela não fixa separadamente \(p,q,s\).

### 2.3 Prescrição causal

Para

\[
F_{EH}=Q_{EH}/w+O(1),
\]

temos \(\oint F_{EH}d\tau=2\pi iQ_{EH}\). Portanto, uma ação real exige uma
prescrição explícita. Uma escolha matematicamente consistente seria

\[
\mathfrak C_\gamma[F]
:=\frac1{2\pi i}\oint_\gamma F(\tau)d\tau,
\]

que fornece \(\mathfrak C_\gamma[F_{EH}]=Q_{EH}\). Esta escolha é uma
normalização possível, não uma consequência automática da ação escrita. A
GDQ deve identificá-la com o princípio causal de Sudarshan para torná-la
oficial.

---

## 3. Bloco III — \(\alpha^4\), meio-instantão e planificação

### 3.1 O que a ação oficial contém

A ação contém a contração escalar \(\mathcal R_B\), mas não contém
explicitamente

\[
\operatorname{Tr}(\mathcal F_B\wedge\mathcal F_B).
\]

Esses objetos têm graus diferentes: o primeiro é uma densidade escalar
linear na curvatura contraída; o segundo é uma classe característica
quadrática. Portanto não existe, para uma conexão geral, identidade

\[
\int\mathcal R_B\mathcal U dV
=C\int\operatorname{Tr}(\mathcal F_B\wedge\mathcal F_B).
\]

Uma redução topológica só pode ocorrer após provar uma condição adicional,
por exemplo autodualidade mais uma identidade de Bogomolny/localização no
setor reduzido.

### 3.2 Resultado condicional rigoroso

Se a Hessiana/redução da própria ação produzir

\[
S_E^{\rm colar}/\hbar=\alpha^{-1}Q_B+\|\mathcal F_B-*\mathcal F_B\|^2,
\]

e se as condições relativas de bordo fornecerem \(Q_B=1/2\), então a sela
autodual implica

\[
\boxed{S_{\rm inst}/\hbar=1/(2\alpha)}.
\]

Logo, a consequência é provada, mas as duas premissas não são determinadas
pela ação oficial tal como atualmente especificada.

### 3.3 Potência \(\alpha^4\)

Uma forma de volume complexa em dimensão quatro é

\[
\frac1{4!}\Omega^4.
\]

Ela gera \(\alpha^4\) somente se cada fator normalizado de \(\Omega\) carregar
exatamente um fator independente de \(\alpha\). Essa associação não decorre
da dimensão por si só. É necessário definir

\[
\Omega=\alpha\,\widehat\Omega
\]

com \(\widehat\Omega\) geometricamente normalizada e provar que os demais
determinantes e jacobianos não alteram a potência. Assim, \(\alpha^4\) é
condicional a essa lei constitutiva.

### 3.4 Planificação

Para um modo zero \(\psi_0\), uma mudança estereográfica com jacobiano \(J\)
preserva a norma quando

\[
\psi_0^{\rm flat}=J^{-1/2}\psi_0^{\rm curved}.
\]

Então

\[
\int|\psi_0^{\rm flat}|^2Jd^4x
=\int|\psi_0^{\rm curved}|^2d^4x,
\]

e nenhum fator externo independente sobrevive:

\[
\boxed{J_{\rm flat}^{(0)}=1}
\]

para o modo normalizado. Esse resultado não vale automaticamente para modos
excitados ou determinantes completos.

---

## 4. Bloco IV — complemento de Schur e fator de Fano

A Hessiana de contorno possui a forma

\[
\mathbb K_\partial=
\begin{pmatrix}K_H&J\\J^\dagger&K_T\end{pmatrix}.
\]

Se \(K_T\) for invertível no complemento de seus modos zero, a integração
gaussiana do setor toroidal fornece exatamente

\[
\boxed{K_{\rm eff}=K_H-JK_T^{-1}J^\dagger.}
\]

Em bases espectrais \(K_Tt_a=\lambda_at_a\), o termo induzido é

\[
\langle h_i,JK_T^{-1}J^\dagger h_j\rangle
=\sum_{a:\lambda_a\ne0}
\frac{J_{ia}\overline{J_{ja}}}{\lambda_a}.
\]

Portanto, a admitância depende dos valores \(J_{ia}\) e \(\lambda_a\), não
apenas do número de canais. Mesmo para três modos Hopf e cinco modos
toroidais,

\[
\chi=\frac{\|J\|_{\rm HS}}{\|K_T\|_1}
=\frac{\left(\sum_{i=1}^3\sum_{a=1}^5|J_{ia}|^2\right)^{1/2}}
{\sum_{a=1}^5|\lambda_a|}
\]

não é universal.

O valor \(3\sqrt2/5\) segue somente sob as condições espectrais adicionais

\[
\sum_{i,a}|J_{ia}|^2=18,
\qquad
\sum_a|\lambda_a|=5.
\]

Essas condições equivalem a escolher a normalização que se pretendia
demonstrar. A ação oficial, sem operadores de contorno e condições de colagem
explicitados, não fixa tais números.

---

## 5. Síntese algébrica e veredito

Se

\[
p=\frac{\alpha^4(1+\alpha)}{\chi_{\rm Fano}}
e^{-1/(2\alpha)},
\qquad
\frac{GM_p^2}{\hbar c}=p,
\]

então

\[
\boxed{G=\frac{\hbar c}{M_p^2}p,}
\]

\[
\boxed{
C_R=\frac{c^3M_p^2}{16\pi\hbar}
\frac{\chi_{\rm Fano}}{\alpha^4(1+\alpha)}e^{1/(2\alpha)}.
}
\]

Os quatro blocos foram executados até onde a ação oficial determina os
resultados. Eles demonstram:

1. a redução geométrica e o sistema de fluxo, sujeito às convenções e dados
   de contorno;
2. a condição necessária e suficiente, no ansatz assintótico, para um polo
   simples;
3. a implicação topológica do meio-instantão, mas não sua emergência da ação;
4. o complemento de Schur exato e a não universalidade da contagem
   \(3\sqrt2/5\).

Consequentemente,

\[
\boxed{
\text{a ação oficial atualmente escrita não contém dados suficientes para
fixar numericamente }G.
}
\]

Para transformar a fórmula fenomenológica em teorema, devem ser acrescentados
como definições constitutivas da GDQ — ou derivados de partes já existentes do
manuscrito — exatamente três dados: as condições de contorno que selecionam o
background singular, a identidade de localização que gera o funcional
topológico e os operadores espectrais da colagem. Isso não é pós-ajuste se os
três forem definidos antes da avaliação de \(G\) e tiverem consequências
independentes testáveis.
