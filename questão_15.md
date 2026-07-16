# Questão 15 — Como \(f\), \(S_I\) e \(\rho\) se relacionam?

## 1. Pergunta

A Questão 15 pergunta:

\[
\boxed{
\text{como o campo complexo }f,\text{ a ação osmótica }S_I
\text{ e a densidade }\rho\text{ se relacionam?}
}
\]

As perguntas obrigatórias de `15-0.md` são:

1. \(f\) é real ou complexo?
2. Se \(f\) é complexo, a medida de Perelman permanece positiva?
3. A relação correta é \(\rho=e^{-f}\), \(\rho=e^{S_I/\hbar}\) ou inclui
   \((4\pi\tau)^{-n/2}\)?
4. Como a normalização é preservada?
5. Como \(S_I=\hbar\mathcal W\) poderia relacionar um campo local a um
   funcional global?

A correção principal é:

\[
\boxed{
S_I=\hbar\mathcal W
\text{ não deve ser usado como identidade local.}
}
\]

O campo \(S_I(x)\) é local. O funcional \(\mathcal W[g,f,\tau]\) é global.
Eles pertencem a níveis matemáticos distintos.

---

## 2. Resposta curta

Na GDQ, \(f\) é um campo escalar complexo:

\[
\boxed{
f
=
-\frac{S_I-iS_R}{\hbar}
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar}.
}
\]

Logo:

\[
\boxed{
\operatorname{Re}f=-\frac{S_I}{\hbar},
\qquad
\operatorname{Im}f=\frac{S_R}{\hbar}.
}
\]

A densidade de Madelung é a parte real positiva extraída de \(f\):

\[
\boxed{
\rho
=
e^{S_I/\hbar}
=
e^{-(f+\bar f)/2}.
}
\]

Portanto:

\[
\boxed{
S_I=\hbar\ln\rho,
\qquad
f=-\ln\rho+i\frac{S_R}{\hbar}.
}
\]

A medida oficial da ação não é simplesmente \(\rho\). Ela é:

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

com:

\[
\boxed{
z_\tau=\tau+i\nu_0t,
\qquad
\nu_0=\frac{\hbar}{2m_0},
\qquad
n=4.
}
\]

Assim, a igualdade precisa é:

\[
\boxed{
(4\pi z_\tau)^n\mathcal U=\rho.
}
\]

---

## 3. \(f\) é real ou complexo?

\[
\boxed{
f\text{ é complexo.}
}
\]

Ele contém duas informações físicas diferentes:

\[
\boxed{
f=f_R+if_I,
}
\]

com:

\[
\boxed{
f_R=-\frac{S_I}{\hbar},
\qquad
f_I=\frac{S_R}{\hbar}.
}
\]

Aqui:

- \(S_I\) é a ação osmótica, entrópica ou log-amplitude;
- \(S_R\) é a ação mecânica real, isto é, a fase de Madelung;
- \(\rho=e^{S_I/\hbar}\) é a densidade positiva;
- \(\Psi=\sqrt\rho\,e^{iS_R/\hbar}\) é a função de onda efetiva.

Portanto, o mapa completo é:

\[
\boxed{
f
\longleftrightarrow
(\rho,S_R)
}
\]

no setor regular \(\rho>0\).

---

## 4. A medida permanece positiva se \(f\) é complexo?

Sim, no sentido físico relevante.

A positividade não vem de \(e^{-f}\), pois \(e^{-f}\) seria complexo quando
\(\operatorname{Im}f\neq0\). A medida real positiva vem da combinação
hermitiana:

\[
\boxed{
e^{-(f+\bar f)/2}
=
e^{-\operatorname{Re}f}
=
e^{S_I/\hbar}
=
\rho>0.
}
\]

Portanto, a fase \(S_R\) não entra no peso real da medida. Ela entra na parte
oscilatória da função de onda:

\[
\boxed{
\Psi=\sqrt\rho\,e^{iS_R/\hbar}.
}
\]

Essa separação é essencial:

\[
\boxed{
\text{amplitude } \rho
\text{ vem de } \operatorname{Re}f;
\qquad
\text{fase } S_R
\text{ vem de } \operatorname{Im}f.
}
\]

Logo, a medida é positiva porque depende de \(f+\bar f\), não de \(f\)
isoladamente.

---

## 5. Qual é a relação correta: \(\rho=e^{-f}\), \(\rho=e^{S_I/\hbar}\) ou
com fator de kernel?

Há três objetos distintos.

### 5.1 Densidade hidrodinâmica

\[
\boxed{
\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2}.
}
\]

Essa é a densidade de Madelung.

### 5.2 Medida da ação oficial

\[
\boxed{
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

Essa é a medida que aparece na ação GDQ.

### 5.3 Caso puramente real auxiliar

Se, apenas como caso auxiliar, \(S_R=0\), então \(f=\bar f\) é real e:

\[
\rho=e^{-f}.
\]

Mas essa não é a forma geral da teoria, porque a GDQ precisa da fase
\(S_R\). A forma geral é:

\[
\boxed{
\rho\neq e^{-f}
\quad\text{em geral;}
\qquad
\rho=e^{-(f+\bar f)/2}.
}
\]

Portanto, a resposta correta para a Questão 15 é:

\[
\boxed{
\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2},
\qquad
\mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

---

## 6. Como a normalização é preservada?

A normalização física é:

\[
\boxed{
\int_{\Sigma_t}\rho\,d\mu_h=1,
}
\]

na hipersuperfície física \(\Sigma_t\) da redução lorentziana \(N^4\), com
medida induzida \(d\mu_h\).

No setor Madelung regular, a equação de continuidade obtida da ação efetiva é:

\[
\boxed{
\partial_t\rho+\nabla_i(\rho v^i)=0,
\qquad
v^i=\frac{1}{m}h^{ij}\nabla_jS_R.
}
\]

Integrando em \(\Sigma_t\):

\[
\frac{d}{dt}\int_{\Sigma_t}\rho\,d\mu_h
=
-\int_{\Sigma_t}\nabla_i(\rho v^i)\,d\mu_h.
\]

Pelo teorema da divergência:

\[
\boxed{
\frac{d}{dt}\int_{\Sigma_t}\rho\,d\mu_h
=
-\int_{\partial\Sigma_t}\rho v^i n_i\,dA.
}
\]

Assim, a normalização é preservada se:

\[
\boxed{
\int_{\partial\Sigma_t}\rho v^i n_i\,dA=0.
}
\]

Isso ocorre, por exemplo, para:

- decaimento suficientemente rápido no infinito;
- condições periódicas no toro;
- condições de contorno sem fluxo;
- setores compactos sem bordo.

Então:

\[
\boxed{
\frac{d}{dt}\int_{\Sigma_t}\rho\,d\mu_h=0.
}
\]

Na ação geométrica completa, o fator de kernel \((4\pi z_\tau)^{-n}\) pertence
à medida \(\mathcal U\), não altera a definição local de \(\rho\). Ele organiza
a evolução em escala/contorno causal:

\[
\boxed{
\mathcal U\,d\mu_g
=
\frac{\rho}{(4\pi z_\tau)^n}\,d\mu_g.
}
\]

Se a integral geométrica total de \(\mathcal U\) for usada como normalização de
kernel, a preservação depende da equação conjugada de transporte/heat kernel e
das condições de bordo. Já a normalização probabilística física é preservada
pela continuidade de \(\rho\).

---

## 7. Por que \(S_I=\hbar\mathcal W\) não é correto como identidade local?

A identidade:

\[
\boxed{
S_I=\hbar\mathcal W
}
\]

é problemática se lida literalmente.

O motivo é simples:

\[
\boxed{
S_I=S_I(x,\tau)
\text{ é campo local;}
\qquad
\mathcal W[g,f,\tau]\text{ é funcional global.}
}
\]

O funcional de Perelman tem a forma esquemática:

\[
\boxed{
\mathcal W[g,f,\tau]
=
\int_M
\left[
\tau(\mathcal R+|\nabla f|^2)+f-n
\right]
(4\pi\tau)^{-n/2}e^{-f}\,dV_g.
}
\]

Na GDQ complexa oficial, sua versão física aparece hermitianizada e com
\(z_\tau\), mas a distinção estrutural permanece: \(\mathcal W\) é uma integral
sobre a variedade, não um campo ponto a ponto.

Portanto, a expressão correta não é:

\[
S_I(x)=\hbar\mathcal W[g,f,\tau].
\]

A forma aceitável é uma destas:

### 7.1 Relação local correta

\[
\boxed{
S_I(x,\tau)=\hbar\ln\rho(x,\tau)
=-\hbar\,\operatorname{Re}f(x,\tau).
}
\]

Essa é a relação fundamental usada na teoria.

### 7.2 Relação global correta

A integral de \(S_I\) ou de \(f\) pode contribuir para um funcional global:

\[
\boxed{
\mathcal W
=
\mathcal W[g,f,\tau]
=
\mathcal W[g,S_I,S_R,\tau].
}
\]

Isto é:

\[
\boxed{
\mathcal W\text{ é funcional de }S_I,
\text{ não é igual a }S_I.
}
\]

### 7.3 Se quiser ligar global a local, é preciso um operador

Para obter um campo local a partir de um funcional global, seria necessário
definir explicitamente uma derivada funcional, densidade variacional ou
potencial conjugado, por exemplo:

\[
\boxed{
\Pi_I(x)
:=
\frac{\delta\mathcal W}{\delta S_I(x)}.
}
\]

ou uma densidade local \(\mathfrak w(x)\) tal que:

\[
\boxed{
\mathcal W=\int_M\mathfrak w(x)\,d\mu_g.
}
\]

Mesmo nesse caso, a relação seria com \(\Pi_I(x)\) ou \(\mathfrak w(x)\), não
com \(\mathcal W\) inteiro.

Logo, a correção oficial é:

\[
\boxed{
\text{retirar }S_I=\hbar\mathcal W
\text{ como identidade local.}
}
\]

---

## 8. Relação com a objeção de Wallstrom

O capítulo original `15 - A Objeção de Wallstrom.md` discute a quantização da
circulação da fase:

\[
\boxed{
\oint_\gamma\nabla S_R\cdot dx=nh.
}
\]

Esse tema depende da parte imaginária de \(f\):

\[
\boxed{
S_R=\hbar\,\operatorname{Im}f.
}
\]

Já a Questão 15 de auditoria pergunta principalmente sobre a parte real:

\[
\boxed{
S_I=-\hbar\,\operatorname{Re}f,
\qquad
\rho=e^{S_I/\hbar}.
}
\]

Portanto, Wallstrom não substitui esta resposta. Ele é uma consequência
topológica posterior da fase \(S_R\), enquanto esta questão fixa a ontologia
local de \(f,S_I,\rho,\mathcal U\).

O capítulo original pode ser mantido, mas deve evitar qualquer frase que
confunda:

\[
\boxed{
\rho=e^{-f}
}
\]

com a relação geral correta:

\[
\boxed{
\rho=e^{-(f+\bar f)/2}.
}
\]

---

## 9. Formulação final para inserir no texto principal

Uma redação limpa para o texto principal é:

> O campo fundamental \(f\) da GDQ é complexo. Sua parte real codifica a
> ação osmótica \(S_I\), enquanto sua parte imaginária codifica a ação de fase
> \(S_R\):
> \[
> f=-\frac{S_I-iS_R}{\hbar}.
> \]
> Assim,
> \[
> \rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2},
> \qquad
> \Psi=\sqrt\rho\,e^{iS_R/\hbar}.
> \]
> A medida que entra na ação GDQ não é \(\rho\) isoladamente, mas
> \[
> \mathcal U=\frac{\rho}{(4\pi z_\tau)^n}.
> \]
> O funcional de Perelman \(\mathcal W\) é um funcional global de
> \(g,f,\tau\); portanto, não deve ser identificado ponto a ponto com
> \(S_I/\hbar\). A relação local correta é
> \[
> S_I=\hbar\ln\rho=-\hbar\,\operatorname{Re}f.
> \]

---

## 10. Veredito

\[
\boxed{
\text{Questão 15 fechada oficialmente.}
}
\]

A resposta resolve as cinco exigências de `15-0.md`:

1. \(f\) é complexo;
2. a medida positiva usa \(f+\bar f\), não \(f\) sozinho;
3. \(\rho=e^{S_I/\hbar}=e^{-(f+\bar f)/2}\);
4. \(\mathcal U=\rho/(4\pi z_\tau)^n\);
5. \(S_I=\hbar\mathcal W\) é removido como identidade local.

