# Questão 33 — Qual é a escala de corte?

## 1. Pergunta

O arquivo `33-0.md` pergunta:

\[
\boxed{
\text{qual é a escala de corte da GDQ?}
}
\]

A inconsistência apontada é:

\[
\boxed{
\text{o texto usa aproximadamente }0{,}511\,{\rm MeV}
\text{ e }1\,{\rm GeV}.
}
\]

As perguntas obrigatórias são:

1. existe uma única escala?
2. ela é física ou regulador?
3. por que experimentos muito acima dessa escala continuam descritos pelo
   Modelo Padrão?
4. como o corte depende da partícula?

---

## 2. Resposta curta

A teoria não deve usar uma única escala numérica para todos os contextos.

Na GDQ há três objetos diferentes que precisam ser separados:

\[
\boxed{
\Lambda_C
\neq
\Lambda(\tau)
\neq
m_i.
}
\]

Onde:

1. \(\Lambda_C\) é a escala geométrica de Cartan que aparece na ação como
   escala dimensional da teoria efetiva;
2. \(\Lambda(\tau)=\tau^{-1/2}\) é a escala de resolução do fluxo/núcleo de
   calor;
3. \(m_i\) é massa, autovalor ou energia de repouso de uma excitação física.

Portanto:

\[
\boxed{
0{,}511\,{\rm MeV}
\text{ não pode ser o corte UV universal da teoria.}
}
\]

E:

\[
\boxed{
1\,{\rm GeV}
\text{ também não pode ser declarado corte universal sem qualificação.}
}
\]

O valor \(0{,}511\,{\rm MeV}\) é a massa do elétron. Ele pode definir a escala
inercial/Compton do setor eletrônico:

\[
\Lambda_e:=m_ec^2,
\]

mas não o limite de validade de loops do Modelo Padrão.

O valor \(\sim1\,{\rm GeV}\) pode ser interpretado como escala efetiva
hadrônica/solitônica, próxima de \(\Lambda_{\rm QCD}\) ou da rigidez de um
setor bariônico. Mas não deve ser identificado automaticamente com o corte
universal de toda a GDQ.

---

## 3. O que a Q32 já estabeleceu

Na Questão 32, o fator de amortecimento foi derivado estruturalmente como
semigrupo de calor:

\[
\boxed{
G_\tau
=
e^{-\tau L_{\rm GDQ}^{(2)}}
\left(L_{\rm GDQ}^{(2)}\right)^{-1}.
}
\]

Em limite plano:

\[
\boxed{
G_\Lambda(p_E)
=
\frac{e^{-p_E^2/\Lambda^2}}{p_E^2+m^2}.
}
\]

Com:

\[
\boxed{
\Lambda(\tau)=\tau^{-1/2}.
}
\]

Isso mostra que \(\Lambda\) do fator gaussiano é primariamente uma escala de
resolução associada ao parâmetro de fluxo:

\[
\boxed{
\tau
\longleftrightarrow
\text{escala de coarse-graining geométrico}.
}
\]

Logo:

\[
\boxed{
\Lambda(\tau)
\text{ não é necessariamente uma massa de partícula.}
}
\]

---

## 4. O papel de \(\Lambda_C\) na ação oficial

A ação oficial contém:

\[
\boxed{
\frac{\hbar}{\Lambda_C^2}.
}
\]

Esse fator fixa a escala dimensional da ação:

\[
\boxed{
\Lambda_C
=
\text{escala geométrica de Cartan da teoria efetiva.}
}
\]

Ele não deve ser confundido com:

1. massa do elétron;
2. massa do próton;
3. escala eletrofraca;
4. escala de Planck;
5. escala cosmológica.

A leitura correta é:

\[
\boxed{
\ell_C:=\Lambda_C^{-1}
\text{ é comprimento/rigidez característico da camada efetiva de Cartan.}
}
\]

Mas o valor numérico de \(\Lambda_C\) ainda precisa ser derivado por uma
condição espectral ou geométrica.

---

## 5. Por que \(0{,}511\,{\rm MeV}\) não pode ser corte universal?

Se:

\[
\Lambda_{\rm UV}=m_e\simeq0{,}511\,{\rm MeV},
\]

então amplitudes com momento:

\[
p\gg0{,}511\,{\rm MeV}
\]

seriam fortemente amortecidas por:

\[
e^{-p^2/m_e^2}.
\]

Isso contradiz imediatamente:

1. espalhamento de elétrons em MeV, GeV e TeV;
2. QED perturbativa de alta precisão;
3. processos eletrofracos acima de \(M_W,M_Z\);
4. física de colisores;
5. produção de jatos hadrônicos;
6. dados do LEP, Tevatron e LHC.

Portanto:

\[
\boxed{
m_e
\text{ pode ser escala inercial do elétron, mas não corte UV universal.}
}
\]

No máximo:

\[
\boxed{
\Lambda_e=m_ec^2
}
\]

é uma escala de resposta do modo eletrônico ou de seu comprimento de Compton:

\[
\lambda_e=\frac{\hbar}{m_ec}.
\]

Ela não é o limite de integração de loops fundamentais.

---

## 6. Por que \(1\,{\rm GeV}\) também precisa de cuidado?

Uma escala:

\[
\Lambda_{\rm had}\sim1\,{\rm GeV}
\]

é fisicamente plausível para o setor hadrônico, pois está próxima de:

1. massa do próton;
2. escala de confinamento;
3. escala de quebra de descrição perturbativa de QCD;
4. rigidez solitônica bariônica.

Mas se ela for usada como corte universal duro:

\[
e^{-p^2/(1\,{\rm GeV})^2},
\]

então processos com:

\[
p\gg1\,{\rm GeV}
\]

também seriam indevidamente suprimidos.

Isso conflita com a existência de física bem descrita em:

\[
10\,{\rm GeV},\quad
100\,{\rm GeV},\quad
1\,{\rm TeV},\quad
13\,{\rm TeV}.
\]

Logo:

\[
\boxed{
1\,{\rm GeV}
\text{ pode ser escala efetiva hadrônica/Cartan setorial, não corte universal
duro.}
}
\]

---

## 7. Como experimentos acima da escala continuam descritos pelo Modelo Padrão?

A resposta correta é que o corte GDQ não deve ser interpretado como um teto
rígido de energia externa.

Ele é um amortecimento de modos virtuais de alta curvatura/eigenvalor no
operador geométrico:

\[
\boxed{
e^{-\tau L_{\rm GDQ}^{(2)}}.
}
\]

O que é amortecido não é simplesmente:

\[
\boxed{
\text{qualquer partícula com energia }E>\Lambda.
}
\]

Mas sim:

\[
\boxed{
\text{modos virtuais que sondam eigenvalores geométricos acima da resolução
do setor efetivo.}
}
\]

Assim, partículas externas podem ter energia alta, desde que o setor efetivo
reconstruído continue válido e os observáveis sejam descritos por amplitudes
renormalizadas.

Em linguagem de EFT:

\[
\boxed{
\Lambda_C
\text{ marca a escala onde novas estruturas geométricas aparecem, não uma
parede cinemática universal.}
}
\]

Se a teoria quer preservar o sucesso do Modelo Padrão acima de \(1\,{\rm GeV}\),
então deve assumir:

\[
\boxed{
\Lambda_C^{\rm universal}
\gg
\text{escalas já testadas}
}
\]

ou então:

\[
\boxed{
\Lambda_C
\text{ é setorial, e }1\,{\rm GeV}\text{ vale apenas no setor hadrônico.}
}
\]

---

## 8. Como o corte depende da partícula?

A dependência por partícula não deve ser escrita como:

\[
\boxed{
\Lambda_i=m_i.
}
\]

Isso é incorreto como corte UV.

A forma correta é espectral:

\[
\boxed{
L_i^{(2)}\psi_{i,n}
=
\lambda_{i,n}\psi_{i,n}.
}
\]

O amortecimento é:

\[
\boxed{
e^{-\tau\lambda_{i,n}}.
}
\]

Então a escala efetiva de cada setor é:

\[
\boxed{
\Lambda_i(\tau)
\sim
\tau^{-1/2}
}
\]

medida em relação aos autovalores do operador daquele setor.

Se o setor possui massa efetiva:

\[
\lambda_{i,p}\simeq p_E^2+m_i^2,
\]

então:

\[
\boxed{
e^{-\tau\lambda_{i,p}}
=
e^{-\tau p_E^2}
e^{-\tau m_i^2}.
}
\]

Aqui \(m_i\) desloca o espectro; ele não substitui automaticamente
\(\Lambda(\tau)\).

Logo:

\[
\boxed{
\text{a partícula altera o espectro }L_i^{(2)},\text{ não o princípio universal
do corte.}
}
\]

---

## 9. O problema no capítulo 33 original

O capítulo `pt-br/33 - A Barreira Ultravioleta e a Estabilidade
Eletrofraca.md` contém três problemas que precisam ser corrigidos futuramente no
manuscrito.

### 9.1 Erro na escala eletrofraca

O texto usa:

\[
v_K
=
\frac{M_e}{\alpha}
\left(
1-\frac{3}{4\pi^2}
\right)^{-1/2}
\approx246\,{\rm GeV}.
\]

Mas essa fórmula não produz \(246\,{\rm GeV}\). Como já registrado na Questão
29:

\[
\boxed{
v_K\simeq72{,}85\,{\rm MeV}.
}
\]

Portanto, essa expressão não pode sustentar a escala eletrofraca.

### 9.2 Uso indevido de \(\Lambda_e=m_e\) como corte de loops do Higgs

O capítulo estima:

\[
\Delta M_H^2
\propto
\lambda^2(0{,}511\,{\rm MeV})^2.
\]

Isso só funciona porque usa a massa do elétron como corte de loop. Mas esse
procedimento não é compatível com física de altas energias.

O correto é escrever:

\[
\boxed{
\Delta M_H^2
\sim
\lambda^2\Lambda_H^2,
}
\]

onde \(\Lambda_H\) deve ser a escala geométrica efetiva do setor conformal/Higgs,
derivada do operador:

\[
L_H^{(2)}.
\]

Não se pode simplesmente impor:

\[
\Lambda_H=m_e.
\]

### 9.3 Notação dimensional incorreta

O texto deve evitar escrever:

\[
125\,{\rm GeV}^2.
\]

O correto para massa é:

\[
\boxed{
M_H\simeq125\,{\rm GeV}.
}
\]

Para massa ao quadrado:

\[
\boxed{
M_H^2\simeq(125\,{\rm GeV})^2.
}
\]

---

## 10. Respostas diretas

### 1. Existe uma única escala?

Não, não como número único aplicado a tudo.

Há:

\[
\boxed{
\Lambda_C,\quad \Lambda(\tau),\quad \Lambda_{\rm setor},\quad m_i.
}
\]

Mas apenas \(\Lambda_C\) é candidata a escala geométrica fundamental da camada
efetiva de Cartan.

### 2. É física ou regulador?

É física se for derivada da geometria:

\[
\boxed{
\Lambda_C=\ell_C^{-1}.
}
\]

Mas \(\Lambda(\tau)\) também atua como regulador operacional do semigrupo:

\[
\boxed{
\Lambda(\tau)=\tau^{-1/2}.
}
\]

Portanto:

\[
\boxed{
\text{é escala física de resolução geométrica, não regulador artificial.}
}
\]

### 3. Por que experimentos muito acima continuam descritos pelo Modelo Padrão?

Porque o corte não pode ser uma parede rígida em energia externa. Ele amortece
modos virtuais/eigenmodos geométricos no operador efetivo:

\[
\boxed{
e^{-\tau L_{\rm GDQ}^{(2)}}.
}
\]

Se \(\Lambda_C\) fosse universal e próximo de \(1\,{\rm GeV}\), a teoria
entraria em conflito com experimentos acima dessa escala. Logo, \(1\,{\rm GeV}\)
deve ser setorial/hadrônico, ou \(\Lambda_C^{\rm universal}\) deve ser muito
maior.

### 4. Como o corte depende da partícula?

Por meio do espectro do operador quadrático de cada setor:

\[
\boxed{
L_i^{(2)}\psi_{i,n}=\lambda_{i,n}\psi_{i,n}.
}
\]

Não por:

\[
\boxed{
\Lambda_i=m_i.
}
\]

---

## 11. Fechamento

A Questão 33 não pode ser fechada aceitando simultaneamente:

\[
\Lambda_{\rm UV}=0{,}511\,{\rm MeV}
\]

e:

\[
\Lambda_C\sim1\,{\rm GeV}
\]

como se fossem a mesma escala universal.

A resposta correta é:

\[
\boxed{
\Lambda_C
\text{ é a escala geométrica da camada efetiva;}
\qquad
\Lambda(\tau)=\tau^{-1/2}
\text{ é a escala de resolução do fluxo;}
\qquad
m_i
\text{ são massas/autovalores de setores físicos.}
}
\]

Portanto:

\[
\boxed{
\text{Questão 33 fica estruturalmente respondida, mas exige correção futura do
capítulo 33 original.}
}
\]

