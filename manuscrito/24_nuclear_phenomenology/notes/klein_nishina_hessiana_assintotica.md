---
title: "Nota — Klein--Nishina como redução assintótica"
---

# Nota — Klein--Nishina como redução assintótica

Esta nota registra a construção completa usada no texto principal. Ela é uma
redução assintótica da GDQ, não uma substituição da ação oficial por QED.

## 1. Dados do problema

O processo é:

$$
\gamma(k,\epsilon)+e(p,s)
\longrightarrow
\gamma(k',\epsilon')+e(p',s').
$$

No domínio de laboratório assintoticamente plano:

$$
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
\qquad
p+k=p'+k'.
$$

No repouso inicial do sóliton eletrônico:

$$
p=(m_ec,\mathbf 0),
\qquad
x=\frac{E}{m_ec^2}.
$$

Da conservação de Noether:

$$
(p+k-k')^2=p'^2=m_e^2c^2.
$$

Cancelando $p^2=m_e^2c^2$ e usando $k^2=k'^2=0$, fica:

$$
2p\cdot(k-k')-2k\cdot k'=0.
$$

No referencial de repouso:

$$
p\cdot k=m_ecE,
\qquad
p\cdot k'=m_ecE',
\qquad
k\cdot k'=\frac{EE'}{c^2}(1-\cos\theta).
$$

Logo:

$$
m_ec(E-E')
=
\frac{EE'}{c^2}(1-\cos\theta).
$$

Dividindo por $EE'$:

$$
\frac{1}{E'}-\frac{1}{E}
=
\frac{1-\cos\theta}{m_ec^2}.
$$

Portanto:

$$
\frac{E'}{E}
=
\frac{1}{1+x(1-\cos\theta)}.
$$

## 2. Expansão da ação oficial

No setor assintótico do elétron, a expansão da ação oficial fornece:

$$
\mathcal S_{\rm GDQ}[\Phi_e^*+\delta\Phi]
=
\mathcal S_*
+
\frac12
\langle\delta\Phi,K_e^{\rm phys}\delta\Phi\rangle
+
\frac{1}{3!}\mathcal V_e^{(3)}[\delta\Phi^3]
+
\frac{1}{4!}\mathcal V_e^{(4)}[\delta\Phi^4]
+
\cdots.
$$

Aqui $\Phi_e^*$ é o background eletrônico estacionário:

$$
\Phi_e^*
=
(g_e^*,J_e^*,H_e^*,f_e^*,\mathcal U_e^*).
$$

O operador físico é obtido removendo modos de calibre, longitudinais e de
contorno redundantes:

$$
K_e^{\rm phys}
=
P_{\rm phys}
\operatorname{Hess}_{\Phi_e^*}\mathcal S_{\rm GDQ}
P_{\rm phys}.
$$

O canal fotônico é o subespaço transversal sem massa:

$$
P_\gamma K_e^{\rm phys}P_\gamma
=
0
\quad
\text{no limite assintótico}.
$$

Como operador espectral:

$$
P_\gamma
=
\frac{1}{2\pi i}
\oint_{\mathcal C_\gamma}
(z-K_e^{\rm phys})^{-1}\,dz.
$$

O vértice efetivo Compton é:

$$
\mathcal V_{\gamma e\gamma}^{\rm eff}
=
P_\gamma
\mathcal V_e^{(3)}
G_e^{\rm phys}
\mathcal V_e^{(3)}
P_\gamma
+
P_\gamma\mathcal V_e^{(4)}P_\gamma.
$$

Com:

$$
\mathcal V_e^{(3)}
=
\left.
\frac{\delta^3\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*},
\qquad
\mathcal V_e^{(4)}
=
\left.
\frac{\delta^4\mathcal S_{\rm GDQ}}
{\delta\Phi\,\delta\Phi\,\delta\Phi\,\delta\Phi}
\right|_{\Phi_e^*}.
$$

Os dois termos com o propagador físico geram os dois ramos causais:

$$
G_e^{\rm phys}(p+k)
\sim
\frac{1}{(p+k)^2-m_e^2c^2}
=
\frac{1}{2p\cdot k},
$$

$$
G_e^{\rm phys}(p-k')
\sim
\frac{1}{(p-k')^2-m_e^2c^2}
=
\frac{1}{-2p\cdot k'}.
$$

Esses são os canais $s$ e $u$ da redução operacional.

## 3. Projetor fotônico e transversalidade

A identidade de Noether do canal $U(1)_Q$ implica transversalidade:

$$
k_\mu\mathcal M^{\mu\nu}=0,
\qquad
k'_\nu\mathcal M^{\mu\nu}=0.
$$

No limite plano, para vetor auxiliar $n^\mu$ com $k\cdot n\ne0$, o projetor
transversal é:

$$
\Pi_{\mu\nu}^{\perp}(k;n)
=
-\eta_{\mu\nu}
+
\frac{k_\mu n_\nu+n_\mu k_\nu}{k\cdot n}
-
\frac{n^2k_\mu k_\nu}{(k\cdot n)^2}.
$$

Como os termos proporcionais a $k_\mu$ ou $k'_\nu$ são anulados por Noether,
observáveis físicos podem ser calculados usando apenas a classe transversal:

$$
\sum_{\lambda=1}^{2}
\epsilon_\mu^{(\lambda)}(k)
\epsilon_\nu^{(\lambda)}(k)^*
=
\Pi_{\mu\nu}^{\perp}(k;n).
$$

## 4. Projetor de circulação/spin

O spin eletrônico na GDQ é a circulação/Hopf estável do estômato. No limite
Dirac--Bismut assintótico, o projetor de uma orientação é:

$$
P_s(p)
=
\frac12
(\slashed p+m_ec)
(1+\gamma^5\slashed S_s),
$$

com:

$$
S_s\cdot p=0,
\qquad
S_s^2=-1.
$$

Para feixe não polarizado, a média dos dois estados de circulação cancela a
parte axial:

$$
\frac12\sum_{s=\pm}P_s(p)
=
\frac12(\slashed p+m_ec).
$$

Isso é a completude assintótica dos modos Hopf; não é postulado adicional.

## 5. Contração não polarizada

A amplitude assintótica reduzida tem a forma:

$$
\mathcal M
=
-e^2
\bar u(p')
\left[
\slashed\epsilon'^{\,*}
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\slashed\epsilon
+
\slashed\epsilon
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\slashed\epsilon'^{\,*}
\right]
u(p).
$$

A quantidade observável é:

$$
\overline{|\mathcal M|^2}
=
\frac12
\sum_{s,s'}
\frac12
\sum_{\lambda,\lambda'}
|\mathcal M|^2.
$$

Com os projetores, isso vira a contração:

$$
\overline{|\mathcal M|^2}
=
\frac{e^4}{4}
\operatorname{Tr}
\left[
(\slashed p'+m_ec)
\mathcal A_{\mu\nu}
(\slashed p+m_ec)
\overline{\mathcal A}_{\rho\sigma}
\right]
\Pi_\perp^{\mu\rho}(k')
\Pi_\perp^{\nu\sigma}(k),
$$

onde:

$$
\mathcal A_{\mu\nu}
=
\gamma_\mu
\frac{\slashed p+\slashed k+m_ec}{2p\cdot k}
\gamma_\nu
+
\gamma_\nu
\frac{\slashed p-\slashed k'+m_ec}{-2p\cdot k'}
\gamma_\mu.
$$

Usando:

$$
p+k=p'+k',
\qquad
p^2=p'^2=m_e^2c^2,
\qquad
k^2=k'^2=0,
$$

e removendo as componentes longitudinais pelos projetores físicos, a parte
angular reduzida é:

$$
T_{\rm KN}
=
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta.
$$

## 6. Normalização por fluxo

A seção de choque é a razão entre fluxo espalhado por ângulo sólido e fluxo
incidente:

$$
\frac{d\sigma}{d\Omega}
=
\frac{d\Phi_{\rm out}/d\Omega}{\Phi_{\rm in}}.
$$

Na GDQ, o fluxo é a corrente reconstruída:

$$
J^\mu_{\rm GDQ}
=
\rho v^\mu.
$$

A integração da conservação de Noether produz o Jacobiano cinemático:

$$
\left(\frac{E'}{E}\right)^2.
$$

O prefator assintótico é:

$$
r_e^2
=
\alpha^2
\left(\frac{\hbar}{m_ec}\right)^2.
$$

Nesta redução, $\alpha$ e $m_e$ entram como quantidades já herdadas da
geometria em capítulos anteriores. O fechamento metrológico mais forte é
recalcular o mesmo prefator diretamente de
$\mathcal V_{\gamma e\gamma}^{\rm eff}$ e dos fluxos do background 8D.

Assim:

$$
\frac{d\sigma}{d\Omega}
=
\frac{r_e^2}{2}
\left(\frac{E'}{E}\right)^2
\left(
\frac{E'}{E}
+
\frac{E}{E'}
-
\sin^2\theta
\right).
$$

## 7. Seção total

Integrando sobre o ângulo sólido, obtém-se a fórmula total:

$$
\sigma_{\rm KN}(x)
=
2\pi r_e^2
\left[
\frac{1+x}{x^3}
\left(
\frac{2x(1+x)}{1+2x}
-
\ln(1+2x)
\right)
+
\frac{\ln(1+2x)}{2x}
-
\frac{1+3x}{(1+2x)^2}
\right].
$$

No limite $x\to0$:

$$
\sigma_{\rm KN}
\longrightarrow
\sigma_T
=
\frac{8\pi}{3}r_e^2.
$$

Para a avaliação numérica em energia muito baixa, usa-se a expansão estável da
mesma expressão total:

$$
\frac{\sigma_{\rm KN}}{\sigma_T}
=
1-2x+\frac{26}{5}x^2+O(x^3).
$$

O script [[../scripts/klein_nishina_total_e_fluxo.py]] verifica a igualdade
entre integração numérica angular e expressão total analítica.

## 8. Status

O que está fechado nesta nota:

1. cinemática Compton por Noether;
2. canais $s/u$ como ramos do propagador físico;
3. soma spin/polarização como completude de projetores na redução
   assintótica;
4. normalização por fluxo e limite Thomson;
5. comparação numérica angular e total.

O que permanece condicional:

1. construir $P_\gamma$ diretamente no background eletrônico 8D;
2. construir $P_s$ diretamente do operador Hopf/circulação da Hessiana;
3. avaliar $\mathcal V_{\gamma e\gamma}^{\rm eff}$ pela ação oficial sem
   passar pela forma assintótica;
4. extrair $r_e^2$ por fluxo GDQ completo, não apenas pela forma reduzida.
