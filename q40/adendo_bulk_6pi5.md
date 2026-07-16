# Adendo Q40 — Derivação do termo de bulk \(6\pi^5\)

## 1. Objetivo

Este adendo ataca a pendência central da Questão 40:

\[
\boxed{
\text{por que }6\pi^5\text{ deve ser lido como razão de massa?}
}
\]

O adendo anterior mostrou a decomposição:

\[
\mathcal I_p
=
\mathcal I_p^{\rm bulk}
+
\mathcal I_p^{\partial}.
\]

Agora precisamos justificar:

\[
\boxed{
\mathcal I_p^{\rm bulk}=6\pi^5.
}
\]

A resposta não pode ser “porque o número bate”. A resposta deve ser:

\[
\boxed{
6\pi^5
\text{ é a integral de energia de bulk do domínio bariônico,}
}
\]

normalizada pela unidade eletrônica:

\[
\mathcal I_e=1.
\]

---

## 2. Calibração metrológica

Pela conclusão da Questão 36, massas absolutas em MeV não são geradas sem uma
unidade. A teoria deve prever razões adimensionais.

Fixamos:

\[
E_0=M_ec^2.
\]

Para qualquer classe solitônica \(\mathcal C\):

\[
M_{\mathcal C}c^2
=
E_0\mathcal I_{\mathcal C}.
\]

Logo:

\[
\boxed{
\frac{M_{\mathcal C}}{M_e}
=
\mathcal I_{\mathcal C}.
}
\]

Assim, no setor bariônico:

\[
\boxed{
\frac{M_p^{(0)}}{M_e}
=
\mathcal I_p^{\rm bulk}.
}
\]

Portanto, demonstrar:

\[
\mathcal I_p^{\rm bulk}=6\pi^5
\]

é equivalente a demonstrar:

\[
\frac{M_p^{(0)}}{M_e}=6\pi^5.
\]

---

## 3. Normalização eletrônica

O elétron é o sóliton elementar de referência. Sua integral adimensional deve
ser:

\[
\boxed{
\mathcal I_e=1.
}
\]

Isso não significa que a teoria “postula” a massa do elétron como estrutura
interna. Significa apenas que a escala de energia é calibrada por \(M_e\),
exatamente como já foi estabelecido na Questão 36.

Formalmente:

\[
\mathcal I_e
=
\int_{\Sigma_e}
\mathcal H_{\rm bulk}^{(e)}
\mathcal U_e
\sqrt{\det g_e}\,d\Sigma_e
=1.
\]

A massa bariônica então é a razão entre duas integrais:

\[
\frac{M_p^{(0)}}{M_e}
=
\frac{
\int_{\Sigma_p}
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p
\sqrt{\det g_p}\,d\Sigma_p
}{
\int_{\Sigma_e}
\mathcal H_{\rm bulk}^{(e)}
\mathcal U_e
\sqrt{\det g_e}\,d\Sigma_e
}.
\]

Com \(\mathcal I_e=1\):

\[
\frac{M_p^{(0)}}{M_e}
=
\mathcal I_p^{\rm bulk}.
\]

---

## 4. Domínio bariônico de bulk

O bárion trimodal possui três estômatos confinados. O domínio interno de
calibração não é um toro plano livre; é um toro de Clifford trançado por três
folhas de estômato:

\[
\boxed{
K_p=T^5_{\rm trançado}.
}
\]

A estrutura mínima usada no capítulo 26 pode ser escrita como:

\[
T^5_{\rm trançado}
\simeq
\bigsqcup_{a=1}^{3}\mathcal F_a,
\]

onde cada folha \(\mathcal F_a\) é uma câmara fundamental associada a um dos
três estômatos.

Cada câmara possui coordenadas:

\[
(\phi_1,\phi_2,\phi_3,\phi_4,\phi_5),
\]

com domínio:

\[
\phi_1\in[0,2\pi],
\qquad
\phi_2,\phi_3,\phi_4,\phi_5\in[0,\pi].
\]

Assim, o volume de uma câmara fundamental, na métrica normalizada de bulk, é:

\[
\operatorname{Vol}(\mathcal F)
=
\int_0^{2\pi}d\phi_1
\prod_{j=2}^{5}
\int_0^\pi d\phi_j
=
2\pi^5.
\]

Como há três folhas/estômatos:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=
3\,\operatorname{Vol}(\mathcal F)
=
3(2\pi^5)
=
\boxed{6\pi^5}.
\]

Essa é a forma mais limpa de entender o fator \(6\):

\[
\boxed{
6\pi^5
=
3\times 2\pi^5.
}
\]

O \(3\) vem da trimodalidade bariônica; \(2\pi^5\) vem da câmara fundamental
pentadimensional.

---

## 5. Relação com a integral do capítulo 26

O capítulo 26 escreve:

\[
\operatorname{Vol}(T^5_{\rm trançado})
=
\int_{0}^{2\pi}d\phi_1
\int_{0}^{\pi}d\phi_2
\int_{0}^{\pi}d\phi_3
\int_{0}^{\pi}d\phi_4
\int_{0}^{\pi}
\sqrt{\det g_{5D}}\,d\phi_5
=
6\pi^5.
\]

Essa expressão pode ser interpretada de duas formas equivalentes:

### Forma A — três folhas explícitas

Tomamos:

\[
\sqrt{\det g_{5D}}=1
\]

em cada câmara fundamental e somamos as três folhas:

\[
\sum_{a=1}^{3}
\int_{\mathcal F_a}d^5\phi
=
3(2\pi^5)
=
6\pi^5.
\]

### Forma B — degenerescência absorvida na métrica efetiva

Trabalhamos em uma única câmara, mas a métrica efetiva carrega a degenerescência
trimodal:

\[
\sqrt{\det g_{5D}^{\rm eff}}=3.
\]

Então:

\[
\int_{\mathcal F}
3\,d^5\phi
=
3(2\pi^5)
=
6\pi^5.
\]

As duas leituras são matematicamente equivalentes. A forma A é conceitualmente
mais segura, porque não esconde o fator \(3\) dentro de um determinante
métrico.

Portanto, a forma recomendada para a Q40 é:

\[
\boxed{
T^5_{\rm trançado}
\text{ é uma cobertura trimodal da câmara fundamental.}
}
\]

---

## 6. Por que é pentadimensional?

A dimensão \(5\) do domínio de bulk bariônico não deve ser tratada como ajuste.
Ela aparece porque o bárion exige:

1. três canais internos de estômato;
2. um ciclo global de fase;
3. um ciclo de fechamento/confinamento.

Assim:

\[
3+1+1=5.
\]

Em linguagem geométrica:

\[
T^5_{\rm trançado}
\]

é o domínio interno mínimo capaz de acomodar:

1. os três polos/gargantas do bárion;
2. a holonomia global de carga;
3. o fechamento elástico do tubo de fluxo.

Isso é compatível com a interpretação já usada na Q39: a compactificação global
serve para calibração de massas, enquanto o limite plano local é apenas uma
aproximação laboratorial.

---

## 7. Por que o volume vira energia de bulk?

No ponto estacionário, a densidade de energia de bulk deve ser constante na
câmara fundamental normalizada.

Essa é a hipótese de homogeneidade solitônica:

\[
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p
\sqrt{\det g_p}
=
1
\quad
\text{em unidades eletrônicas.}
\]

Então:

\[
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
1\,d\mu
=
\operatorname{Vol}(T^5_{\rm trançado})
=
6\pi^5.
\]

Mais explicitamente:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
6\pi^5.
}
\]

Essa é a ponte massa-volume.

A prova completa exigirá demonstrar a condição:

\[
\boxed{
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p
\sqrt{\det g_p}
\longrightarrow
d\mu_{T^5_{\rm trançado}}
}
\]

a partir da ação oficial. Mas a estrutura lógica da derivação fica fixada.

---

## 8. Teorema de bulk

Podemos registrar o resultado como teorema condicional.

**Teorema de bulk bariônico.** Considere o setor estacionário da GDQ na classe
bariônica trimodal. Suponha que:

1. a escala metrológica seja fixada por \(E_0=M_ec^2\);
2. a integral eletrônica normalizada satisfaça \(\mathcal I_e=1\);
3. o domínio interno do próton seja a cobertura trimodal:

   \[
   T^5_{\rm trançado}
   =
   \bigsqcup_{a=1}^{3}\mathcal F_a;
   \]

4. cada câmara fundamental tenha volume:

   \[
   \operatorname{Vol}(\mathcal F)=2\pi^5;
   \]

5. a densidade estacionária de bulk reduza-se à medida invariante normalizada.

Então:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
6\pi^5.
}
\]

Consequentemente:

\[
\boxed{
\frac{M_p^{(0)}}{M_e}=6\pi^5.
}
\]

---

## 9. O que foi resolvido

Este adendo resolve três pontos que estavam soltos:

1. o fator \(6\) não é arbitrário:

   \[
   6=3\times2,
   \]

   onde \(3\) é a trimodalidade bariônica e \(2\pi^5\) é o volume da câmara
   pentadimensional;

2. \(6\pi^5\) só entra como massa porque a integral eletrônica foi normalizada:

   \[
   \mathcal I_e=1;
   \]

3. o volume é volume de energia, não apenas volume geométrico:

   \[
   \mathcal I_p^{\rm bulk}
   =
   \int
   \mathcal H_{\rm bulk}
   \mathcal U\sqrt{\det g}\,d^5\phi.
   \]

---

## 10. O que ainda falta

Ainda falta a prova variacional forte:

\[
\mathcal S_{\rm GDQ}
\longrightarrow
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}
=
d\mu_{T^5_{\rm trançado}}.
\]

Em termos práticos, falta escrever:

1. a métrica \(g_p\) do domínio trançado;
2. a densidade \(\mathcal U_p\);
3. o perfil estacionário \(f_p\);
4. a Hamiltoniana reduzida \(\mathcal H_{\rm bulk}^{(p)}\);
5. a demonstração de que o produto reduz à medida invariante.

Esse é o próximo nível de fechamento.

---

## 11. Conclusão

A derivação organizada fica:

\[
\frac{M_p}{M_e}
=
\underbrace{
\mathcal I_p^{\rm bulk}
}_{6\pi^5}
+
\underbrace{
\mathcal I_p^{\partial}
}_{\alpha(\frac{3\pi}{2}+\frac{3}{4\pi^3})}.
\]

Com:

\[
\boxed{
\mathcal I_p^{\rm bulk}
=
3
\left(
\int_0^{2\pi}d\phi_1
\prod_{j=2}^{5}\int_0^\pi d\phi_j
\right)
=
6\pi^5.
}
\]

Portanto, a leitura correta é:

\[
\boxed{
6\pi^5
\text{ é a energia de bulk normalizada do próton,}
}
\]

desde que a redução estacionária da ação GDQ para o setor bariônico produza a
medida invariante do toro trançado.
