# Questão 16 — Qual é o coeficiente de difusão?

## 1. Pergunta

A Questão 16 pergunta:

\[
\boxed{
\text{qual coeficiente de difusão a GDQ usa: }
\nu=\frac{\hbar}{2m}
\text{ ou um }\nu_0\text{ universal?}
}
\]

As perguntas obrigatórias de `16-0.md` são:

1. é \(\nu=\hbar/(2m)\) ou \(\nu_0\) universal?
2. como uma difusão universal produz massas distintas?
3. o fator \(\Omega=m/m_0\) é derivado ou definido?
4. como termos envolvendo gradientes de \(\Omega\) são tratados na
   Fokker--Planck?

O critério de resolução é:

\[
\boxed{
\text{derivar a equação estocástica com difusão variável, incluindo os
termos de Itô.}
}
\]

---

## 2. Resposta curta

A GDQ deve distinguir dois níveis.

No nível fundamental do vácuo geométrico, o coeficiente universal é:

\[
\boxed{
\nu_0=\frac{\hbar}{2m_0}.
}
\]

No setor efetivo de uma excitação com massa inercial \(m\), o coeficiente
observado é:

\[
\boxed{
\nu_{\rm eff}
=
\frac{\hbar}{2m}.
}
\]

A ligação entre os dois é feita pelo fator de compressão geométrica:

\[
\boxed{
\Omega(x,t):=\frac{m(x,t)}{m_0}.
}
\]

Então:

\[
\boxed{
\nu(x,t)
=
\nu_0\Omega^{-1}(x,t)
=
\frac{\hbar}{2m_0}\frac{m_0}{m(x,t)}
=
\frac{\hbar}{2m(x,t)}.
}
\]

Portanto:

\[
\boxed{
\nu_0\text{ é universal no bulk;}
\qquad
\nu_{\rm eff}=\nu_0\Omega^{-1}\text{ é o coeficiente observado na excitação.}
}
\]

Se \(\Omega\) é constante dentro de um setor de partícula, recupera-se
exatamente a difusão de Nelson:

\[
\boxed{
\nu_{\rm eff}=\frac{\hbar}{2m}.
}
\]

Se \(\Omega=\Omega(x,t)\) varia, a equação de Fokker--Planck deve conter os
termos de Itô gerados por \(\nabla\Omega\).

---

## 3. Processo estocástico correto

No espaço físico efetivo, considere a difusão de Itô:

\[
\boxed{
dX_t^i
=
b^i(X_t,t)\,dt
+
\sqrt{2\nu_0\Omega^{-1}(X_t,t)}\,dW_t^i.
}
\]

Em forma tensorial plana:

\[
\boxed{
dX_t^i=b^i\,dt+\sigma^i{}_a\,dW_t^a,
\qquad
\sigma^i{}_a\sigma^j{}_a=2D^{ij},
}
\]

com:

\[
\boxed{
D^{ij}=\nu_0\Omega^{-1}\delta^{ij}.
}
\]

Em geometria riemanniana efetiva, a forma covariante é:

\[
\boxed{
D^{ij}=\nu_0\Omega^{-1}h^{ij}.
}
\]

onde \(h^{ij}\) é a métrica espacial induzida na fatia física.

---

## 4. Fokker--Planck com difusão variável

Para uma difusão de Itô:

\[
dX_t^i=b^i\,dt+\sigma^i{}_a\,dW_t^a,
\]

a equação de Fokker--Planck é:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nabla_i\nabla_j(D^{ij}\rho).
}
\]

No caso isotrópico:

\[
D^{ij}=\nu(x,t)h^{ij},
\qquad
\nu(x,t)=\nu_0\Omega^{-1}(x,t),
\]

temos:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\Delta_h(\nu\rho).
}
\]

Substituindo \(\nu=\nu_0\Omega^{-1}\):

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nu_0\Delta_h(\Omega^{-1}\rho).
}
\]

Expandindo:

\[
\boxed{
\Delta_h(\Omega^{-1}\rho)
=
\Omega^{-1}\Delta_h\rho
+2\nabla^i\Omega^{-1}\nabla_i\rho
+\rho\,\Delta_h\Omega^{-1}.
}
\]

Portanto:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nu_0\left[
\Omega^{-1}\Delta_h\rho
+2\nabla^i\Omega^{-1}\nabla_i\rho
+\rho\,\Delta_h\Omega^{-1}
\right].
}
\]

Essa é a correção que faltava: se \(\Omega\) não é constante, há termos
obrigatórios de Itô contendo \(\nabla\Omega\) e \(\Delta\Omega\).

---

## 5. Forma conservativa

A mesma equação pode ser escrita como conservação de fluxo:

\[
\boxed{
\partial_t\rho+\nabla_iJ^i=0,
}
\]

com:

\[
\boxed{
J^i
=
b^i\rho-\nabla^i(\nu\rho).
}
\]

Ou:

\[
\boxed{
J^i
=
b^i\rho
-
\nu\nabla^i\rho
-
\rho\nabla^i\nu.
}
\]

Como:

\[
\nabla^i\nu
=
\nabla^i(\nu_0\Omega^{-1})
=
-\nu_0\Omega^{-1}\nabla^i\ln\Omega
=
-\nu\nabla^i\ln\Omega,
\]

temos:

\[
\boxed{
J^i
=
b^i\rho
-
\nu\nabla^i\rho
+
\rho\nu\nabla^i\ln\Omega.
}
\]

Logo, gradientes de massa efetiva geram um termo de deriva adicional no fluxo
probabilístico.

---

## 6. Relação com Nelson: velocidades forward, backward e osmótica

Na formulação de Nelson com difusão variável, escrevemos:

\[
\boxed{
dX_t^i=b_+^i\,dt+\sqrt{2\nu}\,dW_t^i
}
\]

para a evolução forward, e uma evolução backward compatível.

As Fokker--Planck forward/backward são:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b_+^i\rho)
+
\Delta_h(\nu\rho),
}
\]

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b_-^i\rho)
-
\Delta_h(\nu\rho).
}
\]

Definindo:

\[
\boxed{
v^i:=\frac{b_+^i+b_-^i}{2},
\qquad
u^i:=\frac{b_+^i-b_-^i}{2},
}
\]

a soma das duas equações dá a continuidade:

\[
\boxed{
\partial_t\rho+\nabla_i(\rho v^i)=0.
}
\]

A diferença das duas equações dá:

\[
\boxed{
\nabla_i(\rho u^i)=\Delta_h(\nu\rho).
}
\]

No setor sem corrente solenoidal osmótica adicional, isto implica:

\[
\boxed{
\rho u^i=\nabla^i(\nu\rho).
}
\]

Assim:

\[
\boxed{
u^i
=
\frac{1}{\rho}\nabla^i(\nu\rho)
=
\nu\nabla^i\ln\rho+\nabla^i\nu.
}
\]

Como \(\nu=\nu_0\Omega^{-1}\), segue:

\[
\boxed{
u^i
=
\nu_0\Omega^{-1}\nabla^i\ln\rho
+
\nabla^i(\nu_0\Omega^{-1}).
}
\]

Ou:

\[
\boxed{
u^i
=
\nu\left(
\nabla^i\ln\rho-\nabla^i\ln\Omega
\right).
}
\]

Portanto, a fórmula antiga:

\[
u^i=\nu_0\Omega^{-1}\nabla^i\ln\rho
\]

só é válida se:

\[
\boxed{
\nabla_i\Omega=0.
}
\]

No caso geral, o termo \(-\nu\nabla^i\ln\Omega\) é obrigatório.

---

## 7. Como uma difusão universal produz massas distintas?

A massa distinta não aparece porque o vácuo tenha vários \(\nu_0\). Ela aparece
porque cada excitação solitônica deforma localmente a geometria e altera o
fator \(\Omega\).

O postulado cinemático universal é:

\[
\boxed{
\nu_0=\frac{\hbar}{2m_0}.
}
\]

A excitação com massa efetiva \(m\) possui:

\[
\boxed{
\Omega=\frac{m}{m_0}.
}
\]

Logo:

\[
\boxed{
\nu_{\rm eff}
=
\nu_0\Omega^{-1}
=
\frac{\hbar}{2m}.
}
\]

Assim, massas maiores correspondem a regiões geometricamente mais comprimidas,
com menor amplitude difusiva efetiva. Massas menores correspondem a regiões
menos comprimidas, com maior amplitude difusiva efetiva.

Essa leitura é consistente com a ideia central da GDQ:

\[
\boxed{
\text{massa é resposta geométrica/local do solíton, não parâmetro
primitivo do vácuo.}
}
\]

---

## 8. \(\Omega=m/m_0\) é derivado ou definido?

Há duas camadas.

### 8.1 Definição operacional

Na equação estocástica local:

\[
\boxed{
\Omega(x,t):=\frac{m(x,t)}{m_0}
}
\]

é uma definição operacional do fator de compressão/inércia efetiva.

Essa definição é necessária para escrever:

\[
\boxed{
\nu(x,t)=\nu_0\Omega^{-1}(x,t).
}
\]

### 8.2 Origem geométrica

Na teoria completa, \(\Omega\) deve ser derivado da geometria da excitação:

\[
\boxed{
\Omega=\Omega[g,f,\bar f,\text{dados topológicos}].
}
\]

Isto significa que a massa \(m\) deve emergir como funcional geométrico do
solíton, por exemplo a partir de energia integrada, curvatura localizada,
volume comprimido, condições de contorno e dados topológicos.

Portanto, a posição correta é:

\[
\boxed{
\Omega\text{ é definido operacionalmente no setor estocástico,}
}
\]

mas:

\[
\boxed{
\Omega\text{ deve ser derivado geometricamente para cada espécie física.}
}
\]

Não há inconsistência nisso. A definição local permite fechar a Fokker--
Planck; a derivação global pertence ao problema espectral/solitônico da massa.

---

## 9. Caso de massa constante

Para uma partícula de massa fixa \(m\), temos:

\[
\Omega=\frac{m}{m_0}=\text{constante}.
}
\]

Então:

\[
\nabla_i\Omega=0,
\qquad
\Delta_h\Omega=0.
\]

A Fokker--Planck reduz-se a:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nu_{\rm eff}\Delta_h\rho.
}
\]

com:

\[
\boxed{
\nu_{\rm eff}=\frac{\hbar}{2m}.
}
\]

E a velocidade osmótica reduz-se a:

\[
\boxed{
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho.
}
\]

Esse é o limite usual de Nelson/Madelung.

---

## 10. Caso de massa variável ou meio geométrico não homogêneo

Se:

\[
\Omega=\Omega(x,t),
\]

então:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nu_0\Delta_h(\Omega^{-1}\rho).
}
\]

Na forma expandida:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b^i\rho)
+
\nu_0\Omega^{-1}\Delta_h\rho
+2\nu_0\nabla^i\Omega^{-1}\nabla_i\rho
+\nu_0\rho\,\Delta_h\Omega^{-1}.
}
\]

E:

\[
\boxed{
u^i
=
\nu\left(\nabla^i\ln\rho-\nabla^i\ln\Omega\right).
}
\]

Esses termos não são opcionais. Eles são a contribuição de Itô da difusão
multiplicativa.

Se forem negligenciados sem declarar \(\nabla\Omega=0\), a derivação fica
incompleta.

---

## 11. Relação com a ação oficial

A ação fundamental da GDQ permanece inalterada:

\[
\boxed{
\mathcal{S}_{\rm GDQ}
=
\int_{\gamma}
\left[
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n
\right]
\mathcal U
\sqrt{\det g}\,
d^{2n}z
\right]
\frac{d\tau}{\tau}.
}
\]

com:

\[
\boxed{
\mathcal U=\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n}
=\frac{\rho}{(4\pi z_\tau)^n}.
}
\]

A discussão sobre \(\nu_0\), \(\Omega\) e \(\nu_{\rm eff}\) pertence à redução
estocástica/Madelung da teoria, não substitui a ação oficial.

---

## 12. Correção recomendada ao texto original

O texto pode manter a tese:

\[
\boxed{
\text{o vácuo possui difusão universal }\nu_0,
\text{ e massas distintas surgem por compressão geométrica.}
}
\]

Mas deve corrigir a passagem:

\[
dx^i=b_\pm^i\,dt+\sqrt{2\nu_0\Omega^{-1}}\,dW^i
\quad\Longrightarrow\quad
u^i=\nu_0\Omega^{-1}\nabla^i\ln\rho.
\]

A forma correta é:

\[
\boxed{
dx^i=b_\pm^i\,dt+\sqrt{2\nu_0\Omega^{-1}}\,dW^i
}
\]

com Fokker--Planck:

\[
\boxed{
\partial_t\rho
=
-\nabla_i(b_\pm^i\rho)
\pm
\Delta_h(\nu_0\Omega^{-1}\rho),
}
\]

e velocidade osmótica:

\[
\boxed{
u^i
=
\nu_0\Omega^{-1}
\left(
\nabla^i\ln\rho-\nabla^i\ln\Omega
\right).
}
\]

No setor \(\Omega=\text{constante}\), isso reduz-se a:

\[
\boxed{
u^i=\frac{\hbar}{2m}\nabla^i\ln\rho.
}
\]

---

## 13. Veredito

\[
\boxed{
\text{Questão 16 fechada estruturalmente na redução estocástica.}
}
\]

A resposta resolve as quatro exigências de `16-0.md`:

1. \(\nu_0=\hbar/(2m_0)\) é universal no bulk;
2. \(\nu_{\rm eff}=\nu_0\Omega^{-1}=\hbar/(2m)\) é observado no setor de massa
   \(m\);
3. \(\Omega=m/m_0\) é definição operacional local, mas deve ser derivado da
   geometria solitônica na teoria completa;
4. os gradientes de \(\Omega\) entram obrigatoriamente pela Fokker--Planck de
   Itô:
   \[
   \partial_t\rho
   =
   -\nabla_i(b^i\rho)
   +
   \nu_0\Delta_h(\Omega^{-1}\rho).
   \]
