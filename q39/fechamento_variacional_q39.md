# Fechamento variacional da Questão 39 — contorno físico e massa leptônica

## 1. Ponto a fechar

As simulações da pasta `q39` mostraram:

\[
\text{Reg-Reg em }[0,\pi]
\quad\Rightarrow\quad
r_2\simeq206.766,\quad r_3\simeq3477.10,
\]

enquanto o domínio com estômato finito desloca o espectro:

\[
\text{Robin-Reg em }[\epsilon,\pi]
\quad\Rightarrow\quad
r_2\simeq207.46,\quad r_3\simeq3489.51,
\]

e:

\[
\text{Robin-Robin em }[\epsilon,\pi-\epsilon]
\quad\Rightarrow\quad
r_2\simeq208.16,\quad r_3\simeq3502.01.
\]

Logo, a pergunta física não é mais numérica. A pergunta é:

\[
\boxed{
\text{qual domínio/contorno representa a massa de repouso física?}
}
\]

---

## 2. Resposta

A massa de repouso física deve ser extraída do operador global regular em
\(S^3\), isto é:

\[
\boxed{
\chi\in[0,\pi],
\qquad
\text{regularidade natural nos dois polos.}
}
\]

O estômato finito \(\epsilon_{\rm eff}\) é uma regularização local da cirurgia
de contorno. Ele é útil para estudar espalhamento local, impedância, resposta
térmica e correções de tamanho finito, mas não deve substituir o domínio
global usado para definir a massa assintótica do sóliton.

Em outras palavras:

\[
\boxed{
\text{massa de repouso}=
\text{autovalor global/topológico;}
}
\]

\[
\boxed{
\text{estômato finito}=
\text{regulador/localização/perturbação de contorno.}
}
\]

---

## 3. Derivação variacional

A ação oficial da GDQ é formulada em uma variedade compacta global:

\[
\mathcal M_{\rm global}
\simeq
S^1_\beta\times S^3\times T^4.
\]

O setor espacial \(S^3\) não possui bordo:

\[
\partial S^3=\varnothing.
\]

Logo, ao variar a ação no domínio global regular, os termos de bordo espaciais
não impõem uma condição Robin física adicional. A condição correta é apenas:

1. regularidade da seção nos polos;
2. normalizabilidade na medida de Perelman;
3. monodromia fermiônica no ciclo apropriado;
4. positividade do produto interno reconstruído.

Portanto, no problema radial, o domínio físico é:

\[
\boxed{
\chi\in(0,\pi),
\qquad
\Phi \text{ regular em }0,\pi.
}
\]

Quando se remove uma vizinhança tubular do estômato:

\[
S^3\longrightarrow S^3\setminus\mathcal N_\epsilon(\Sigma_\ell),
\]

surge uma fronteira artificial:

\[
\partial\mathcal N_\epsilon(\Sigma_\ell).
\]

A condição Robin nessa fronteira é a condição natural do problema
regularizado, não uma nova lei fundamental de massa. Ao tomar:

\[
\epsilon\to0,
\]

essa fronteira deve desaparecer e o operador deve retornar à extensão
auto-adjunta regular global.

---

## 4. Forma auto-adjunta do operador regularizado

Depois da transformação:

\[
\phi(\chi)=\sin^s\chi\,\psi(\chi),
\]

o operador radial regularizado pode ser escrito como:

\[
L_s\psi
=
-\psi''
-2s\cot\chi\,\psi'
+\left(s^2-2b\cot\chi\right)\psi.
\]

Essa forma equivale a:

\[
\boxed{
L_s\psi
=
-\frac{1}{w(\chi)}
\frac{d}{d\chi}
\left(
w(\chi)\frac{d\psi}{d\chi}
\right)
+
\left(s^2-2b\cot\chi\right)\psi,
}
\]

com peso:

\[
\boxed{
w(\chi)=\sin^{2s}\chi.
}
\]

O produto interno radial é:

\[
\langle\psi,\eta\rangle
=
\int_0^\pi
\bar\psi(\chi)\eta(\chi)\,
w(\chi)\,d\chi.
\]

Ao integrar por partes:

\[
\langle\psi,L_s\eta\rangle-\langle L_s\psi,\eta\rangle
=
\left[
w(\chi)
\left(
\bar\psi\,\eta'
-\bar\psi'\eta
\right)
\right]_{0}^{\pi}.
\]

Como:

\[
w(\chi)=\sin^{2s}\chi,
\qquad s=\epsilon_{\rm eff}>0,
\]

temos:

\[
w(\chi)\to0
\quad
\text{quando}
\quad
\chi\to0,\pi.
\]

Para funções regulares \(\psi,\eta\), o termo de bordo se anula
automaticamente:

\[
\boxed{
\left[
w(\chi)
\left(
\bar\psi\,\eta'
-\bar\psi'\eta
\right)
\right]_{0}^{\pi}=0.
}
\]

Portanto, a extensão auto-adjunta natural do operador global é exatamente a
extensão de regularidade nos dois polos:

\[
\boxed{
\text{Reg-Reg.}
}
\]

Isso explica por que o caso Reg-Reg do comparador é o que reproduz o espectro
analítico de Rosen--Morse e as razões CODATA.

---

## 5. Interpretação dos contornos truncados

Quando usamos:

\[
[\epsilon_{\rm eff},\pi-\epsilon_{\rm eff}]
\]

criamos dois bordos artificiais. Isso equivale a inserir dois estômatos ou um
estômato e um anti-estômato espelhado. O resultado numérico mostra:

\[
\text{dois bordos}\quad\Rightarrow\quad
\text{desvio de aproximadamente }+0.67\%.
\]

Quando usamos:

\[
[\epsilon_{\rm eff},\pi],
\]

criamos apenas um bordo artificial:

\[
\text{um bordo}\quad\Rightarrow\quad
\text{desvio de aproximadamente }+0.33\%.
\]

Esse escalonamento é exatamente o esperado se o deslocamento for uma
perturbação de tamanho finito do domínio. Portanto:

\[
\boxed{
\text{o desvio de }0.33\%\text{ ou }0.67\%
\text{ não redefine a massa;}
}
\]

ele mede a resposta local do sóliton a uma excisão cirúrgica finita.

---

## 6. Papel da temperatura do espaço de Einstein

O espaço global é:

\[
S^1_\beta\times S^3\times T^4,
\]

portanto possui ciclo térmico euclidiano \(S^1_\beta\).

A temperatura finita pode vestir a resposta local do estômato:

\[
\epsilon_{\rm eff}
\to
\epsilon_{\rm eff}+\Delta\epsilon_T,
\]

\[
b_{\rm eff}
\to
b_{\rm eff}(1+\Delta b_T).
\]

Essas correções são relevantes para observáveis locais de contorno, mas a
definição da massa de repouso assintótica permanece associada ao polo global
regular do operador:

\[
\boxed{
\text{massa}=\text{polo/autovalor global, não deslocamento térmico local.}
}
\]

Assim, o solver térmico deve ser interpretado como engenharia inversa numérica
controlada do alvo térmico: ele mostra qual resposta local do ciclo
\(S^1_\beta\) seria necessária para equilibrar o contorno finito, mas ainda não
constitui prova preditiva final.

---

## 7. Espectro final

Com:

\[
s=\epsilon_{\rm eff},
\qquad
b=b_{\rm eff},
\]

o espectro global regular é:

\[
\lambda_n
=
(s+n)^2
-
\frac{b^2}{(s+n)^2}.
\]

O mapeamento leptônico é:

\[
e\leftrightarrow n=0,
\qquad
\mu\leftrightarrow n=1,
\qquad
\tau\leftrightarrow n=17.
\]

Logo:

\[
\frac{M_\mu}{M_e}
=
\sqrt{\frac{\lambda_1}{\lambda_0}}
\simeq206.7679,
\]

\[
\frac{M_\tau}{M_e}
=
\sqrt{\frac{\lambda_{17}}{\lambda_0}}
\simeq3477.1465.
\]

Isso coincide com as razões observadas dentro da precisão numérica do modelo.

---

## 8. Status lógico da Questão 39

Com esta interpretação, a Questão 39 pode ser fechada da seguinte forma:

\[
\boxed{
\text{Fechada como espectro global/topológico de massa de repouso.}
}
\]

Mas deve-se registrar a ressalva:

\[
\boxed{
\text{as correções de contorno finito e térmicas permanecem como setor local
de resposta, não como definição primária da massa.}
}
\]

O que ainda pode ser desenvolvido depois:

1. avaliar diretamente a Hessiana \(H\) e as fontes térmicas \(J^{(\beta)}\)
   do ciclo \(S^1_\beta\), verificando
   \((\Delta_\epsilon,\Delta_b)^T=-H^{-1}J^{(\beta)}\);
2. calcular observáveis de espalhamento sensíveis ao estômato finito;
3. formalizar a exclusão dos modos intermediários por monodromia/topologia;
4. derivar os coeficientes \(\frac49\), \(\frac{\pi}{2}\) e
   \(\frac32-\frac{4}{15}\alpha\) diretamente da expansão variacional completa.
