# Questão 4 — Ação funcional e consistência quântica

## 1. Resposta direta

A Questão 4 pergunta se a ação funcional da GDQ é matematicamente consistente
e se ela sustenta a passagem para loops quânticos.

A resposta final é:

\[
\boxed{
\text{A ação oficial é preservada.}
}
\]

\[
\boxed{
\text{A consistência variacional fica fechada após explicitar o papel de }
\gamma,\ z_\tau,\ \mathcal U
\text{ e o princípio de Laurent.}
}
\]

\[
\boxed{
\text{A consistência de loops fica fechada em nível perturbativo condicional,
via camada auxiliar BRST e form factor causal de Cartan.}
}
\]

Não se afirma que a ação oficial sozinha, sem camada de quantização, já contém
todos os propagadores, gauge fixing, fantasmas e provas não perturbativas.

---

## 2. Ação oficial

A ação oficial do capítulo 04 permanece:

\[
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
\]

Defina:

\[
\mathcal L_0
=
\tau
\left(
\mathcal R
+g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
+\frac{f+\bar f}{2}
-n.
\]

Então:

\[
\mathcal{S}_{\rm GDQ}
=
\int_\gamma
\int_{\mathcal M_\mathbb C}
\frac{\hbar}{\Lambda_C^2}
\mathcal U
\mathcal L_0
\sqrt g\,
d^{2n}z
\frac{d\tau}{\tau}.
\]

Essa ação não é substituída pela ação efetiva da Questão 2. A Questão 2
fornece uma forma reduzida/controlada útil para checar consistência
variacional, mas a ação acima permanece o funcional oficial.

---

## 3. Compatibilidade com as Questões 2 e 3

A Questão 3 fixou:

\[
n=\dim_{\mathbb C}M=4.
\]

A Questão 2 fixou:

\[
M=\mathbb R^4\times T^4,
\qquad
\dim_{\mathbb R}M=8.
\]

Assim, na Questão 4:

\[
\boxed{
n=4,
\qquad
d=2n=8.
}
\]

A notação \(\mathcal M_\mathbb C\) deve ser lida como a estrutura complexa
usada para escrever o funcional geométrico da GDQ sobre o bulk
\(M=\mathbb R^4\times T^4\), ou como sua parametrização complexa local.

---

## 4. Variável causal complexa

O tempo de fluxo \(\tau\) tem dimensão de área.

O tempo físico \(t\) tem dimensão de tempo.

Portanto, a variável complexa correta não é \(\tau+it\), mas:

\[
\boxed{
z_\tau=\tau+i\nu_0t.
}
\]

Com:

\[
\nu_0=\frac{\hbar}{2m_0}.
\]

Então:

\[
[\tau]=[\nu_0t]=L^2.
\]

Essa variável implementa a união entre:

1. fluxo difusivo/reológico de Perelman;
2. tempo físico hiperbólico;
3. prescrição causal de Sudarshan.

---

## 5. Prescrição causal de Sudarshan

O contorno \(\gamma\) não é artifício ad hoc.

Na GDQ:

\[
\boxed{
\gamma \text{ codifica a prescrição causal de Sudarshan.}
}
\]

Ele representa a combinação de setores retardado e avançado:

\[
G_{\rm sym}
=
\frac12
\left(
G_{\rm ret}
+G_{\rm adv}
\right).
\]

Termos exatos satisfazem:

\[
\oint_\gamma dF=0,
\]

desde que:

1. \(F\) seja monovalorada;
2. \(\gamma\) não cruze cortes de ramo;
3. as singularidades internas sejam controladas;
4. os campos sejam regulares ao longo do contorno.

Assim, \(\gamma\) pode cancelar contribuições de borda exatas sem exigir que
todos os campos se anulem artificialmente no infinito.

---

## 6. Medida \(\mathcal U\)

A ambiguidade original era tratar \(\mathcal U\) ora como multiplicador
independente, ora como densidade física.

A resolução é definir \(\mathcal U\) constitucionalmente como funcional de
\(f,\bar f,z_\tau\):

\[
\boxed{
\mathcal U[f,\bar f,z_\tau]
=
\frac{
e^{-(f+\bar f)/2}
}{
(4\pi z_\tau)^n
}.
}
\]

Para \(n=4\):

\[
\boxed{
\mathcal U
=
\frac{
e^{-(f+\bar f)/2}
}{
(4\pi z_\tau)^4
}.
}
\]

Como:

\[
f=-\frac{S_I-iS_R}{\hbar},
\]

tem-se:

\[
\frac{f+\bar f}{2}
=
-\frac{S_I}{\hbar}.
\]

Logo:

\[
e^{-(f+\bar f)/2}
=
e^{S_I/\hbar}
=
\rho.
\]

Portanto:

\[
\mathcal U
=
\frac{\rho}{(4\pi z_\tau)^n}.
\]

Essa definição remove a variação independente de \(\mathcal U\). Assim:

\[
\delta\mathcal U
=
-\frac12
\mathcal U
\left(
\delta f+\delta\bar f
\right),
\]

com \(z_\tau\) mantido fixo na variação dos campos.

---

## 7. Kernel de calor

Como:

\[
d=\dim_{\mathbb R}M=2n,
\]

o kernel real escala como:

\[
K(\tau)
\sim
(4\pi\tau)^{-d/2}
=(4\pi\tau)^{-n}.
\]

Para:

\[
n=4,
\]

segue:

\[
\boxed{
K(\tau)\sim(4\pi\tau)^{-4}.
}
\]

Logo, a antiga escala \(\tau^{-2}\) só valeria se \(n\) fosse interpretado
como dimensão real quatro, o que não é a definição atual da GDQ.

---

## 8. Decomposição de \(f\)

Com:

\[
f
=
-\frac{S_I}{\hbar}
+i\frac{S_R}{\hbar},
\]

a parte real codifica a densidade:

\[
\rho=e^{S_I/\hbar}.
\]

A parte imaginária codifica a fase:

\[
\operatorname{Im}f=\frac{S_R}{\hbar}.
\]

Para o termo:

\[
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\]

ser escrito como soma limpa dos termos de \(S_I\) e \(S_R\), deve-se tomar a
parte real hermitiana/simetrizada:

\[
\operatorname{Re}
\left(
g^{\mu\bar\nu}
\partial_\mu f
\partial_{\bar\nu}\bar f
\right)
=
\frac1{\hbar^2}
g^{\mu\bar\nu}
\left(
\partial_\mu S_I\partial_{\bar\nu}S_I
+\partial_\mu S_R\partial_{\bar\nu}S_R
\right).
\]

Essa leitura elimina a ambiguidade dos termos mistos imaginários.

---

## 9. Contorno e equações locais

A variação da ação no contorno tem a forma:

\[
\delta S
=
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}
=0.
\]

Expandindo:

\[
E(z_\tau)
=
\sum_{k=-\infty}^{\infty}
E_kz_\tau^k,
\]

obtém-se:

\[
\oint_\gamma
E(z_\tau)
\frac{dz_\tau}{z_\tau}
=
2\pi iE_0.
\]

Logo:

\[
\delta S=0
\Longrightarrow
E_0=0.
\]

Para obter equações locais modo a modo, adota-se o princípio suplementar:

\[
\boxed{
\text{Princípio de estacionariedade dos coeficientes de Laurent.}
}
\]

Isto é:

\[
\boxed{
E_k=0
\quad
\forall k.
}
\]

Com esse princípio, a prescrição de contorno gera equações diferenciais locais
na expansão física do funcional.

---

## 10. Relação com a ação efetiva da Questão 2

A ação efetiva da Questão 2:

\[
S_{\rm eff}
=
S_{\rm EH}+S_\Psi+S_B
\]

não substitui a ação oficial.

Ela funciona como redução controlada sobre \(N^4\), onde:

1. a métrica física é \(h\);
2. \(\Psi=\sqrt\rho e^{iS/\hbar}\);
3. a parte imaginária da equação de \(\Psi\) fornece continuidade;
4. a parte real fornece Hamilton--Jacobi com Bohm;
5. a torção é descrita por \(B\).

Essa redução mostra que a interpretação Madelung/Perelman da ação oficial é
compatível com uma EFT causal sobre \(N^4\).

---

## 11. Setor perturbativo auxiliar

Na leitura própria da GDQ, a prescrição causal de Sudarshan deve projetar os
modos físicos sem tornar fantasmas campos fundamentais. Porém, se quisermos
auditar a teoria com a linguagem perturbativa covariante padrão, entram
campos auxiliares que não aparecem explicitamente na ação oficial isolada.

Portanto, para comparação com a quantização perturbativa covariante,
introduz-se uma camada auxiliar opcional:

\[
S_{\rm pert}
=
S_{\rm gauge}
+S_{\rm spin}
+S_{\rm gf+gh}.
\]

Essa camada não substitui a ação oficial e não define a ontologia da GDQ. Ela
serve como ferramenta de auditoria para escrever regras de flutuação quântica
em torno de um background da ação oficial.

O setor gauge mínimo é:

\[
U(1)^4.
\]

A ação gauge auxiliar é:

\[
S_{\rm gauge}
=
-\frac14
\int_N
G_{ab}
F^a_{\mu\nu}F^{b\mu\nu}
\sqrt{-h}\,d^4x.
\]

O setor espinorial usa:

\[
\slashed D_{B,A}
=
\gamma^\mu
\left(
\nabla_\mu^{\rm LC}
+\frac18B_{\mu\nu\lambda}\gamma^{\nu\lambda}
-iq_aA^a_\mu
\right).
\]

E:

\[
S_{\rm spin}
=
\int_N
\bar\psi
\left(
i\hbar\slashed D_{B,A}
-mc
\right)
\psi
\sqrt{-h}\,d^4x.
\]

---

## 12. Gauge fixing e BRST

Para quantização covariante, introduzem-se:

\[
c^a,
\qquad
\bar c^a,
\qquad
b^a.
\]

Com:

\[
\mathcal G^a=\nabla^\mu A^a_\mu.
\]

O setor de gauge fixing e fantasmas é:

\[
S_{\rm gf+gh}
=
s
\int_N
\sqrt{-h}\,
\bar c_a
\left(
\mathcal G^a
+\frac{\xi}{2}b^a
\right)
d^4x.
\]

As transformações BRST mínimas são:

\[
sA^a_\mu=\nabla_\mu c^a,
\]

\[
sc^a=0,
\]

\[
s\bar c^a=b^a,
\]

\[
sb^a=0.
\]

Para espinores:

\[
s\psi=iq_ac^a\psi,
\qquad
s\bar\psi=-iq_ac^a\bar\psi.
\]

No setor \(U(1)^4\):

\[
\boxed{
s^2=0.
}
\]

Logo:

\[
\boxed{
Q_B^2=0.
}
\]

O espaço físico é:

\[
\boxed{
\mathcal H_{\rm phys}
=
\frac{\ker Q_B}{\operatorname{Im}Q_B}.
}
\]

Assim, modos exatos BRST são removidos do espectro físico.

---

## 13. Papel de \(\gamma\) na unitariedade

\(\gamma\) é o princípio causal próprio da GDQ. O BRST, quando usado, é uma
ferramenta auxiliar de auditoria covariante.

A divisão correta é:

1. \(\gamma\) seleciona a prescrição causal dos propagadores e os polos físicos;
2. BRST, se introduzido, remove graus de liberdade de gauge não físicos na
   linguagem covariante padrão;
3. a positividade é avaliada em \(\mathcal H_{\rm phys}\);
4. a evolução preserva o espaço físico se:

\[
[Q_B,H]=0.
\]

No setor \(U(1)^4\) com acoplamento vetorial e sem anomalia BRST:

\[
\boxed{
[Q_B,H]=0.
}
\]

Assim:

\[
\boxed{
\gamma \text{ é a prescrição causal fundamental; BRST é uma checagem auxiliar
compatível, não um campo fundamental da GDQ.}
}
\]

---

## 14. Form factor de Cartan

Para implementar a escala UV de Cartan na camada perturbativa, usa-se:

\[
\mathcal K
\longrightarrow
\mathcal K_C
=
e^{-\Box_h/\Lambda_C^2}
\mathcal K.
\]

No espaço euclidiano:

\[
\Box_h\to-k_E^2.
\]

Então:

\[
\mathcal K_C(k_E)
=
e^{k_E^2/\Lambda_C^2}
\mathcal K(k_E).
\]

Logo:

\[
\boxed{
G_C(k_E)
=
e^{-k_E^2/\Lambda_C^2}
G_0(k_E).
}
\]

Isso fornece a origem controlada do fator de supressão:

\[
\boxed{
e^{-k_E^2/\Lambda_C^2}.
}
\]

Esse form factor pertence à prescrição de quantização Sudarshan--Cartan, não
à substituição da ação oficial.

---

## 15. Finitude superficial de loops

Com o form factor de Cartan em cada propagador interno, um loop euclidiano
tem integrando limitado por:

\[
P(k_E)
\exp\left(
-c\frac{k_E^2}{\Lambda_C^2}
\right),
\qquad
c>0.
\]

Então:

\[
\int_{\mathbb R^4}
d^4k_E\,
P(k_E)
e^{-ck_E^2/\Lambda_C^2}
<\infty.
\]

Portanto:

\[
\boxed{
\text{os loops euclidianos são superficialmente UV finitos sob a prescrição
Sudarshan--Cartan.}
}
\]

Esse resultado é condicional a:

1. form factor aplicado de modo covariante;
2. preservação BRST;
3. ausência de polos físicos extras;
4. continuação causal controlada por \(\gamma\);
5. background regular.

---

## 16. Ausência de novos polos fantasmas

O form factor:

\[
e^{-\Box_h/\Lambda_C^2}
\]

é uma função inteira sem zeros.

Multiplicar o operador cinético por função inteira sem zeros não cria novas
raízes:

\[
e^{F(k)}\mathcal K(k)=0
\quad
\Longleftrightarrow
\quad
\mathcal K(k)=0.
\]

Logo:

\[
\boxed{
\text{o form factor de Cartan não cria novos polos fantasmas no nível
quadrático.}
}
\]

Ainda é necessário verificar interações e backgrounds específicos, mas a
objeção principal de fantasmas do regulador exponencial fica controlada.

---

## 17. O que está demonstrado

Ficam demonstrados no nível necessário para a Questão 4:

1. a ação oficial é preservada;
2. \(\gamma\) é prescrição causal estrutural;
3. \(z_\tau=\tau+i\nu_0t\) corrige a dimensão da variável complexa;
4. o kernel correto usa expoente \((4\pi z_\tau)^{-n}\);
5. \(\mathcal U\) é definida como funcional de \(f,\bar f,z_\tau\);
6. a passagem do contorno para equações locais exige o princípio de Laurent;
7. a camada perturbativa mínima usa \(U(1)^4\);
8. as transformações BRST são nilpotentes;
9. \(Q_B^2=0\);
10. o espaço físico é \(\ker Q_B/\operatorname{Im}Q_B\);
11. \(\gamma\) é compatível com unitariedade BRST;
12. o form factor de Cartan produz o corte \(e^{-k_E^2/\Lambda_C^2}\);
13. os loops euclidianos são superficialmente finitos sob essa prescrição;
14. o form factor inteiro não cria novos polos fantasmas no nível quadrático.

---

## 18. O que permanece condicional

Não se deve superafirmar:

1. prova não perturbativa de unitariedade;
2. renormalização completa a todas as ordens em qualquer background;
3. ausência de todas as anomalias possíveis;
4. derivação de massas, cargas ou \(\alpha\);
5. equivalência completa com o Modelo Padrão;
6. prova de finitude em backgrounds singulares;
7. quantização completa do setor gravitacional/difeomórfico.

Esses pontos ficam para etapas futuras.

---

## 19. Veredito

\[
\boxed{
\text{A Questão 4 está concluída no nível de consistência variacional
semiclássica e quantização perturbativa condicional.}
}
\]

Mais precisamente:

\[
\boxed{
\text{a ação oficial é preservada;}
}
\]

\[
\boxed{
\gamma \text{ é a prescrição causal de Sudarshan;}
}
\]

\[
\boxed{
\mathcal U
=
\frac{e^{-(f+\bar f)/2}}{(4\pi z_\tau)^n};
}
\]

\[
\boxed{
\text{o setor de loops pode ser auditado por uma camada auxiliar BRST;}
}
\]

\[
\boxed{
\text{com o form factor de Cartan, os loops são superficialmente UV finitos
sem novos polos fantasmas no nível quadrático.}
}
\]

Portanto, a Questão 4 pode ser considerada fechada, desde que seu status seja
mantido corretamente:

\[
\boxed{
\text{fechada como EFT/quantização perturbativa condicional, não como prova
não perturbativa absoluta.}
}
\]
