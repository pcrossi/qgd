---
title: "Nota — Redução radial do buraco negro regular"
---

# Nota — Redução radial do buraco negro regular

Esta nota registra a construção que transforma a ideia de core regular em uma
redução variacional testável. Ela não substitui a sela covariante 8D completa
da ação oficial; ela é a menor redução radial que preserva densidade,
rigidez de Bohm e torção de Bismut.

## 1. Variável física

A densidade constitutiva da GDQ é:

$$
\rho=e^{-f_R}.
$$

No setor radial usa-se:

$$
u(r)=\sqrt\rho.
$$

A escolha por $u$ não é convenção de mecânica quântica externa. Ela apenas
torna explícita a rigidez de amplitude que já aparece quando a ação oficial é
escrita em variáveis de densidade.

## 2. Funcional reduzido

O funcional radial mínimo testado foi:

$$
E[u,\phi]
=
\frac12\int|\nabla u|^2\,dV
+
\frac{\lambda_T}{2}\int u^4\,dV
+
\frac12\int\phi u^2\,dV.
$$

Os três termos representam, respectivamente:

1. rigidez de amplitude/Bohm;
2. repulsão torsional efetiva;
3. retroação geométrica gravitacional reduzida.

A variável $\phi$ satisfaz:

$$
\Delta\phi=u^2.
$$

Com normalização:

$$
\int u^2\,dV=1,
$$

introduz-se o multiplicador $\mu$ e obtém-se:

$$
-\frac12\Delta u
+
(\phi+\lambda_Tu^2)u
=
\mu u.
$$

Na simetria esférica:

$$
u'=v,
$$

$$
v'
=
2(\phi+\lambda_Tu^2-\mu)u
-\frac{2}{r}v,
$$

$$
\phi'=\frac{M(r)}{r^2},
\qquad
M'=r^2u^2.
$$

As condições usadas foram:

$$
u'(0)=0,
\qquad
M(0)=0,
\qquad
u(R)=0,
\qquad
M(R)=1,
\qquad
\phi(R)=-\frac1R.
$$

## 3. Core regular

A solução reduzida retorna:

$$
\mu=-1.067957044153\times10^{-1}.
$$

No centro:

$$
M(r)\sim r^{2.99999076}.
$$

Esse resultado é a checagem essencial. Se:

$$
M(r)=m_3r^3+O(r^5),
$$

então:

$$
A(r)=1-\frac{2\eta M(r)}{r}
=
1-2\eta m_3r^2+O(r^4).
$$

Logo o centro é regular, de tipo de Sitter efetivo, e não Schwarzschild
singular.

## 4. Compactação e horizontes

O parâmetro:

$$
\eta=\frac{GM_{\rm ADM}}{c^2R_0}
$$

é dado de contorno ADM/compactação da solução. Ele não é constante livre da
ação.

A condição de horizonte é:

$$
A(r_H)=0.
$$

Como:

$$
A(r)=1-\frac{2\eta M_{\rm red}(r)}{r},
$$

o limiar é:

$$
\eta_{\rm crit}
=
\min_r\frac{r}{2M_{\rm red}(r)}.
$$

Numericamente:

$$
\eta_{\rm crit}=5.188522012681.
$$

Para $\eta=8$, aparecem:

$$
r_{H,1}=4.222352820613,
\qquad
r_{H,2}=15.95712272799.
$$

## 5. Reconstrução efetiva por conservação

Escreve-se:

$$
g_{tt}=-A(r)e^{2\Phi(r)}.
$$

Definindo:

$$
\nu'
=
\partial_r\log\sqrt{-g_{tt}}
=
\Phi'+\frac{A'}{2A},
$$

a conservação radial efetiva fornece:

$$
\nu'
=
\frac{m+4\pi r^3p_r}{r^2A}.
$$

Portanto:

$$
\Phi'
=
\frac{m+4\pi r^3p_r}{r^2A}
-
\frac{A'}{2A}.
$$

Na redução testada:

$$
p_r
=
-\epsilon+\frac{(u')^2}{8\pi}.
$$

O componente tangencial é reconstruído por:

$$
p_t
=
p_r
+
\frac r2
\left[
p_r'
+
(\epsilon+p_r)
\left(
\Phi'+\frac{A'}{2A}
\right)
\right].
$$

Com $\eta=8$ e $\lambda_T=3$, obteve-se:

$$
\epsilon_{\rm core}
=
9.934478711421\times10^{-3},
$$

$$
p_{r,\rm core}
=
-9.934477941512\times10^{-3},
$$

$$
p_{t,\rm core}
=
-9.934158191133\times10^{-3}.
$$

A comparação entre $p_r$ métrico e $p_r$ de entrada deu:

$$
\max_{\rm core}|p_r^{\rm metric}-p_r^{\rm input}|
=
2.506468990693\times10^{-12}.
$$

O resíduo de conservação foi:

$$
{\rm RMS}_{\rm core}
=
2.104757829586\times10^{-16},
$$

e nos patches estáticos:

$$
{\rm RMS}_{|A|>5\times10^{-2}}
=
9.997320016076\times10^{-18}.
$$

## 6. Condições de energia

No core:

$$
\epsilon+p_r
\simeq
0,
$$

$$
\epsilon+p_t
\simeq
3.205202875438\times10^{-7},
$$

e:

$$
\epsilon+p_r+2p_t
=
-1.986831561236\times10^{-2}.
$$

Assim, NEC/WEC são saturadas e SEC é violada. Essa violação é necessária para
escapar dos teoremas clássicos de singularidade; na GDQ ela vem da pressão
geométrica de densidade, Bohm e torção, não de matéria exótica externa.

