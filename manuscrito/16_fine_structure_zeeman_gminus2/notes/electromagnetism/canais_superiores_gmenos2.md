---
title: "Canais superiores de g-2"
---

# Canais superiores de $g-2$

## 1. Enunciado

Esta nota registra o que foi realmente fechado sobre os termos superiores de
$g-2$ na GDQ.

O termo líder está fechado:

$$
a^{(1)}=\frac{\alpha}{2\pi}.
$$

O problema metrológico completo é calcular, para cada lépton:

$$
a_\ell
=
\frac{1}{\gamma_{0,\ell}}
\frac{
\langle c_\ell,H_{C,\ell}^{+}m_{\perp,\ell}\rangle
}{
\langle c_\ell,H_{C,\ell}^{+}c_\ell\rangle
}.
$$

O objeto que substitui diagramas na GDQ é, portanto:

$$
H_{C,\ell}^{+}m_{\perp,\ell}.
$$

## 2. Expansão formal da Hessiana

Escreva:

$$
H_C
=
H_0+\alpha H_1+\alpha^2H_2+\cdots,
$$

$$
m_\perp
=
\alpha m_1+\alpha^2m_2+\cdots.
$$

A pseudoinversa física deve ser expandida no complemento dos modos nulos e dos
vínculos:

$$
H_C^+
=
H_0^+
-\alpha H_0^+H_1H_0^+
+O(\alpha^2).
$$

Logo:

$$
a_\ell
=
\alpha
\frac{
\langle c,H_0^+m_1\rangle
}{
\gamma_0\langle c,H_0^+c\rangle
}
+O(\alpha^2).
$$

A condição líder da GDQ é:

$$
\frac{
\langle c,H_0^+m_1\rangle
}{
\gamma_0\langle c,H_0^+c\rangle
}
=
\frac{1}{2\pi}.
$$

## 3. Bloco líder computável

O bloco reduzido que realiza essa contração é:

$$
H_{\rm lead}
=
\begin{pmatrix}
1 & -1\\
-1 & 2\pi/\alpha
\end{pmatrix},
\qquad
c=
\begin{pmatrix}
1\\0
\end{pmatrix},
\qquad
m_\perp=
\begin{pmatrix}
0\\1
\end{pmatrix}.
$$

Ele satisfaz exatamente:

$$
\frac{\langle c,H_{\rm lead}^{-1}m_\perp\rangle}
{\langle c,H_{\rm lead}^{-1}c\rangle}
=
\frac{\alpha}{2\pi}.
$$

Com $\alpha^{-1}=137.035999177$:

$$
a^{(1)}
=
1.161409732097664\times10^{-3}.
$$

## 4. Resíduos metrológicos observados

Comparando apenas depois da derivação do termo líder:

| caso | $a_{\rm obs}-a^{(1)}$ | coeficiente agregado em $(\alpha/\pi)^2$ |
|---|---:|---:|
| elétron | $-1.7575515076\times10^{-6}$ | $-0.325744542535$ |
| múon | $4.5108579023\times10^{-6}$ | $0.836042265346$ |

Esses coeficientes não são derivados. Eles medem o tamanho que a Hessiana
física superior precisará produzir.

## 5. Diagnóstico inverso e não-unicidade

É possível construir blocos artificiais com um canal superior:

$$
H=
\begin{pmatrix}
1 & -1 & -J_2\\
-1 & K_1 & 0\\
-J_2 & 0 & K_2
\end{pmatrix},
\qquad
m_\perp=(0,1,\mu_2).
$$

Escolhendo $\mu_2$ pelo alvo experimental, recupera-se o valor observado. Mas
isso é diagnóstico inverso, não previsão.

Para o elétron e múon, uma escolha particular dá:

| caso | $\mu_2^{\rm required}$ | classificação |
|---|---:|---|
| elétron | $-1.5132915275\times10^{-3}$ | diagnóstico inverso |
| múon | $8.0307898069\times10^{-1}$ | diagnóstico inverso |

A auditoria de não-unicidade mostra que o mesmo valor observado é reconstruído
por muitas triplas $(J_2,K_2,\mu_2)$. Portanto $\mu_2^{\rm required}$ não é
observável derivado.

## 6. Extração de canais quando a Hessiana é dada

Dado um arquivo ou operador físico contendo $H$, $c$ e $m_\perp$, o algoritmo
é:

1. normalizar o eixo protegido:

$$
e_0=\frac{c}{\lVert c\rVert};
$$

2. projetar o complemento:

$$
P_\perp=I-e_0e_0^\dagger;
$$

3. diagonalizar:

$$
P_\perp HP_\perp e_i=K_i e_i;
$$

4. calcular:

$$
J_i=-\langle e_0,He_i\rangle,
\qquad
\mu_i=\langle e_i,m_\perp\rangle.
$$

Se a entrada é uma Hessiana oficial projetada, esses coeficientes são
derivados. Se a entrada é um bloco `required`, eles apenas recuperam a
engenharia inversa embutida no bloco.

## 7. Galerkin oficial reduzido

Foi testada uma truncagem Galerkin reduzida diretamente inspirada na ação
oficial, com:

$$
f=F+iP,
\qquad
\mathcal U=e^{-F}.
$$

As coordenadas foram:

| índice | modo |
|---:|---|
| 0 | circulação/fase linear no ciclo |
| 1 | harmônico líder $\sin\theta$ |
| 2 | harmônico superior $\sin2\theta$ |
| 3 | densidade $\operatorname{Re}f\cos\theta$ |
| 4 | métrica conformal $\cos\theta$ |

Resultado:

1. a ação nua fornece $H$ e $c$;
2. sem fonte magnética externa, $m_\perp^{\rm naked}=0$ e $a=0$;
3. a fonte magnética precisa vir do mapa físico $M[\Phi;B]$;
4. a truncagem simples possui modos negativos e não é a sela leptônica física.

Este resultado é importante: ele impede chamar uma truncagem instável de
previsão metrológica.

## 8. Background leptônico efetivo e fonte magnética

O mapa magnético fraco é:

$$
M[\Phi;B]
=
B\left(\gamma_0\mathcal C[\Phi]+M_\perp[\Phi]\right).
$$

A parte mínima é protegida:

$$
M_{\rm min}=B\gamma_0\mathcal C.
$$

A parte transversal líder é a componente harmônica:

$$
M_\perp^{(1)}=B A_h[\Phi],
\qquad
\langle h,h\rangle=\frac{1}{2\pi}.
$$

Os backgrounds efetivos mínimos preservam:

| lépton | $M_\ell/M_e$ | $K_2$ efetivo | $a$ obtido |
|---|---:|---:|---:|
| elétron | $1$ | $8.6102257658\times10^2$ | $\alpha/(2\pi)$ |
| múon | $206.7685934706$ | $1.7803242711\times10^5$ | $\alpha/(2\pi)$ |
| tau | $3477.4464050984$ | $2.9941598636\times10^6$ | $\alpha/(2\pi)$ |

Eles mostram que a hierarquia fornece rigidez de fundo, mas não cria por si só
o resíduo superior.

## 9. Regra de seleção de Hodge

Para campo magnético uniforme no ciclo de Noether:

$$
h=\frac{d\vartheta}{2\pi}.
$$

Modos superiores exatos têm a forma:

$$
e_k\propto d\sin(k\vartheta),
\qquad
k\ge1.
$$

Como $h$ é harmônico e $e_k$ é exato:

$$
\langle h,e_k\rangle=0.
$$

Numericamente, o teste preservado fornece:

$$
\langle h,e_1\rangle\simeq -4.36\times10^{-17},
\qquad
\langle h,e_2\rangle\simeq -2.72\times10^{-17}.
$$

Portanto:

$$
\mu_{2,\ell}^{\rm direto}=0.
$$

Consequência: a correção universal não pode ser uma nova fonte linear direta
em campo magnético uniforme.

## 10. Mistura Hessiana e canal de densidade

O primeiro mecanismo universal permitido é uma correção da Hessiana:

$$
H_C=H_0+\alpha H_1+\cdots.
$$

A seleção harmônica fornece:

$$
\cos^2\theta
=
\frac12(1+\cos2\theta).
$$

Removendo o modo constante:

$$
\beta_{12}
=
\langle u_2,u_1^2-\langle u_1^2\rangle\rangle
=
\frac{1}{2\sqrt\pi}
\simeq
0.282094791773878.
$$

O teste reduzido com:

$$
(H_1)_{12}=(H_1)_{21}
=
\beta_{12}\sqrt{K_1K_2}
$$

é estável, mas altera $a$ apenas nas últimas casas registradas:

$$
a\simeq1.1614146537\times10^{-3}.
$$

O teste local de variações superiores mostra que o acoplamento cúbico robusto
na ação reduzida não é líder ao quadrado diretamente para o superior, mas sim
mediado pela densidade:

$$
T_{123}
\simeq
-6.2831748693
\simeq
-2\pi.
$$

Assim, a correção relevante tem a forma:

$$
\Delta H_{12}
=
\eta_\ell T_{123},
$$

onde $\eta_\ell$ deve ser calculado a partir da sela leptônica física.

## 11. Sela angular reduzida

A sela angular reduzida normalizada varia:

$$
y=(a_1,a_2,\eta,\sigma),
$$

com circulação fixa:

$$
P'
=
\frac{1}{2\pi}
+a_1\cos\theta
+2a_2\cos2\theta.
$$

O vínculo de medida é:

$$
\frac{1}{2\pi}
\int_0^{2\pi}\rho\sqrt g\,d\theta
=1.
$$

A única raiz estacionária normalizada encontrada no modelo reduzido é:

$$
a_1=a_2=\eta_\ell=\sigma=0.
$$

O valor numérico final foi:

$$
\eta_\ell\simeq -1.34\times10^{-9},
$$

com autovalor negativo da Hessiana:

$$
\lambda_{\min}\simeq -6.247\times10^{-2}.
$$

Portanto, a sela angular homogênea reduzida não é a sela leptônica física 8D
e não pode produzir a correção metrológica.

## 12. Status

Fechado estruturalmente:

- Zeeman por Noether e isotropia;
- $g_0=2$;
- $a^{(1)}=\alpha/(2\pi)$;
- o operador Hessiano que define a anomalia;
- a não unicidade dos canais superiores inversos;
- a regra de seleção $\mu_2^{\rm direto}=0$ para campo uniforme;
- a rota mediada pela densidade para correções superiores.

Permanece metrológico/futuro:

- resolver a sela leptônica 8D estável $\Phi_\ell$;
- calcular $H_{C,\ell}$, $T_{ijk}$, $Q_{ijkl}$ e $M[\Phi;B]$ nessa sela;
- obter $\eta_\ell$ ou o perfil não homogêneo completo da densidade;
- reexecutar o mesmo extrator sem usar $g-2$ experimental como alvo.
