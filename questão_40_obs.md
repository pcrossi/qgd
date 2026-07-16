# Questão 40 — Como próton e nêutron são derivados?

## 1. Veredito

A Questão 40 está **bem encaminhada estruturalmente**, mas ainda **não está
fechada como derivação completa de próton e nêutron**.

O manuscrito já contém uma rota coerente para:

1. interpretar o próton e o nêutron como sólitons bariônicos trimodais;
2. associar massa bariônica a volume/topologia do setor interno;
3. obter carga por resíduos holomorfos;
4. interpretar spin por circulação/torção de Cartan;
5. explicar a diferença $M_n-M_p$ por cisalhamento torsional;
6. descrever estabilidade do próton por conservação topológica;
7. descrever instabilidade do nêutron livre por transição quiral.

Mas ainda faltam peças obrigatórias para declarar a resposta completa:

1. solução bariônica explícita da ação oficial;
2. operador Hessiano/estabilidade do bárion;
3. paridade definida por operador geométrico;
4. raio derivado sem inserir escala experimental;
5. momentos magnéticos de próton e nêutron derivados pelo mesmo formalismo;
6. fatores de forma $G_E(q^2)$, $G_M(q^2)$;
7. matriz de espalhamento bariônica;
8. espectro excitado;
9. prova de estabilidade global contra todos os canais de decaimento permitidos.

Portanto:

$$
\boxed{
\text{Q40: rota estrutural forte, mas ainda não fechada como teoria bariônica completa.}
}
$$

---

## 2. O que o texto original já fornece

O material principal está no capítulo:

$$
\texttt{pt-br/26 - Próton - O Solíton de Ricci Composto.md}.
$$

Há apoio adicional em:

1. `pt-br/Apêndice 1 - A Dedução Espectral do Índice de Compressão Torsional.md`;
2. `pt-br/notas/4/nota_4.9_carga_quantizada.md`;
3. `pt-br/notas/27/nota_27.4_raio_do_proton.md`;
4. `pt-br/notas/27/nota_27.9_spin_proton.md`;
5. `questão_30.md`, para confinamento;
6. `questão_36.md`, para calibração metrológica de massas;
7. `questão_38.md`, para evitar circularidade quando $M_p$ entra em $G$.

---

## 3. Estrutura bariônica proposta

Na GDQ, o próton e o nêutron não são partículas pontuais fundamentais. Eles são
tratados como sólitons compostos de gênero/topologia bariônica:

$$
n_B=3.
$$

A imagem geométrica é:

$$
\boxed{
\text{bárion}
=
\text{sóliton de Ricci--Bismut com três estômatos confinados.}
}
$$

Os três estômatos não devem ser tomados como quarks pontuais no sentido do
Modelo Padrão. Eles são subestruturas geométricas internas: polos, gargantas ou
defeitos de vorticidade que, quando sondados localmente, podem reproduzir
frações de carga e canais de espalhamento parecidos com partons.

O critério estacionário deve ser:

$$
\delta \mathcal S_{\rm GDQ}=0
$$

restrito à classe topológica com três estômatos:

$$
\mathcal C_B
=
\{
(g,f,B):\; N_{\rm estoma}=3,\;
\rho=e^{-f}\to0\text{ nos núcleos},\;
\rho>0\text{ fora deles}
\}.
$$

O texto atual descreve essa configuração fisicamente, mas ainda não apresenta a
solução explícita:

$$
(g_B,f_B,B_B)
$$

como ponto crítico da ação oficial.

Essa é a primeira lacuna técnica.

---

## 4. Massa do próton

O manuscrito propõe:

$$
\left(\frac{M_p}{M_e}\right)_0
=
6\pi^5
\approx
1836.11810871.
$$

Depois acrescenta uma correção de fronteira:

$$
\frac{M_p}{M_e}
=
6\pi^5
+
\frac{
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
}{\alpha^{-1}}.
$$

Equivalentemente:

$$
\boxed{
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
$$

Numericamente:

$$
6\pi^5
\approx
1836.11810871,
$$

$$
\gamma_B
=
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\approx
4.73657763,
$$

e:

$$
\frac{M_p}{M_e}
\approx
1836.15267319.
$$

Essa expressão é numericamente muito próxima da razão experimental
próton/elétron. Porém, para a Q40, a pergunta obrigatória é mais forte:

$$
\boxed{
\text{por que }6\pi^5\text{ é razão de massas, e não apenas coincidência numérica?}
}
$$

Essa pergunta ainda não está completamente respondida no manuscrito.

---

## 5. Condição necessária para $6\pi^5$ ser razão de massas

Para $6\pi^5$ ter estatuto físico, é preciso provar um teorema do tipo:

$$
\boxed{
\frac{M_B}{M_e}
=
\frac{\mathcal E_B}{\mathcal E_e}
=
\frac{\mathcal I_B}{\mathcal I_e}.
}
$$

Aqui:

- $\mathcal E_B$ é a energia do sóliton bariônico;
- $\mathcal E_e$ é a energia do sóliton eletrônico;
- $\mathcal I_B$ e $\mathcal I_e$ são integrais geométricas
  adimensionais extraídas da mesma ação, com a mesma medida, a mesma
  normalização e a mesma calibração metrológica.

A rota correta é:

$$
\mathcal E_{\mathcal C}
=
E_0
\mathcal I_{\mathcal C},
$$

onde $E_0$ é a escala calibrada, por exemplo:

$$
E_0=M_ec^2.
$$

Então:

$$
\frac{M_B}{M_e}
=
\mathcal I_B
\quad
\text{se}
\quad
\mathcal I_e=1.
$$

Portanto, $6\pi^5$ representa uma razão de massas somente se for demonstrado
que:

$$
\boxed{
\mathcal I_p^{(0)}
=
\int_{K_B}
\mathcal U_*
\sqrt{\det g_*}\,d\mu_B
=
6\pi^5
}
$$

e simultaneamente:

$$
\boxed{
\mathcal I_e=1
}
$$

na normalização eletrônica usada como unidade de massa.

Sem essa ponte variacional, $6\pi^5$ permanece apenas um volume geométrico
numericamente próximo de $M_p/M_e$.

### 5.1 Decomposição volume--superfície

O primeiro passo dessa ponte foi documentado em:

$$
\texttt{q40/adendo\_volume\_superficie.md}.
$$

A ideia central é que a energia estática do bárion deve decompor-se como:

$$
\boxed{
\mathcal I_B
=
\mathcal I_B^{\rm bulk}
+
\mathcal I_B^{\partial}.
}
$$

Para o próton:

$$
\boxed{
\mathcal I_p^{\rm bulk}
=
6\pi^5
}
$$

e:

$$
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
$$

Essa estrutura é análoga à decomposição de Gamow no modelo de gota nuclear:

$$
\text{energia}
=
\text{termo de volume}
+
\text{termo de superfície}
+\cdots
$$

mas, na GDQ, a interpretação é geométrica:

1. $6\pi^5$ é o termo de bulk/volume do domínio bariônico compacto;
2. $\frac{3\pi}{2}$ é a contribuição de holonomia/Chern--Simons dos três
   estômatos;
3. $\frac{3}{4\pi^3}$ é a correção espectral mínima das gargantas;
4. $\alpha$ é a admitância eletro-geométrica que converte a holonomia de
   fronteira em energia inercial observável.

A torção aparece como termo de superfície porque densidades topológicas de
torção podem ser escritas como transgressões:

$$
\int_{\Sigma_B^\circ} d\mathcal T_{\rm top}
=
\int_{\partial\Sigma_B^\circ}\mathcal T_{\rm top}.
$$

Assim:

$$
\boxed{
\text{volume = massa de bulk;}
\qquad
\text{torção = correção de superfície por Stokes/transgressão.}
}
$$

Esse passo resolve a interpretação conceitual da fórmula. Ainda falta executar
a derivação variacional explícita:

$$
\mathcal S_{\rm GDQ}
\longrightarrow
\mathcal H_{\rm bulk}
\quad\text{e}\quad
\mathcal H_{\partial}.
$$

### 5.2 Estrutura do termo $6\pi^5$

O passo seguinte foi documentado em:

$$
\texttt{q40/adendo\_bulk\_6pi5.md}.
$$

Nesse adendo, o fator $6\pi^5$ foi organizado como volume de energia do
domínio bariônico trimodal:

$$
\boxed{
6\pi^5
=
3\times 2\pi^5.
}
$$

A interpretação é:

1. o fator $3$ vem dos três estômatos/folhas do bárion;
2. o fator $2\pi^5$ é o volume da câmara fundamental pentadimensional:

   $$
   \operatorname{Vol}(\mathcal F)
   =
   \int_0^{2\pi}d\phi_1
   \prod_{j=2}^{5}\int_0^\pi d\phi_j
   =
   2\pi^5.
   $$

Assim:

$$
T^5_{\rm trançado}
=
\bigsqcup_{a=1}^{3}\mathcal F_a,
$$

e:

$$
\boxed{
\operatorname{Vol}(T^5_{\rm trançado})
=
3\operatorname{Vol}(\mathcal F)
=
6\pi^5.
}
$$

Isso evita esconder o fator $3$ dentro de um determinante métrico efetivo e
deixa clara sua origem bariônica.

Em termos de massa:

$$
\boxed{
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
6\pi^5.
}
$$

A prova completa ainda exige mostrar, a partir da ação oficial, que:

$$
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}
\longrightarrow
d\mu_{T^5_{\rm trançado}}.
$$

### 5.3 Redução variacional do bulk

Esse passo foi avançado em:

$$
\texttt{q40/adendo\_reducao\_variacional\_bulk.md}.
$$

A redução usa a ação oficial sem modificá-la. No setor estacionário:

$$
\partial_\tau g=0,
\qquad
\partial_\tau f=0,
\qquad
\partial_\tau B=0.
$$

No bulk, após separar os termos de fronteira/torsão, a equação estacionária
tem a forma de solíton:

$$
\mathcal R_{\mu\bar\nu}
+\nabla_\mu\nabla_{\bar\nu}f
=
\lambda_B g_{\mu\bar\nu}.
$$

Essa condição torna constante a densidade reduzida:

$$
\Theta_B
=
\frac{1}{E_0}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau(\mathcal R_B+|\nabla f_B|^2)+\Phi_B-n
\right].
$$

Com a calibração eletrônica:

$$
E_0=M_ec^2,
\qquad
\mathcal I_e=1,
$$

a unidade local de bulk fica normalizada como:

$$
\Theta_B=1.
$$

Logo:

$$
\boxed{
\mathcal H_{\rm bulk}^{(p)}
\mathcal U_p\sqrt{\det g_p}\,d^5\phi
=
d\mu_{T^5_{\rm trançado}}
}
$$

no ponto estacionário normalizado.

Assim:

$$
\boxed{
\mathcal I_p^{\rm bulk}
=
\int_{T^5_{\rm trançado}}d\mu
=
6\pi^5.
}
$$

O status passa a ser: a ponte variacional reduzida está formulada; falta
escrever a solução explícita $(g_p,f_p)$ e verificar diretamente a equação de
solíton em cada câmara fundamental.

### 5.4 Ansatz explícita para o bulk

A solução-modelo de bulk foi documentada em:

$$
\texttt{q40/adendo\_ansatz\_gp\_fp.md}.
$$

Em cada câmara fundamental $\mathcal F_a$, toma-se:

$$
\boxed{
g_p^{(a)}
=
\sum_{A=1}^{5}d\phi_A^2,
\qquad
f_p^{(a)}=f_0,
\qquad
B^{(a)}=0
\quad\text{no interior}.
}
$$

Então:

$$
\mathcal R_{AB}=0,
\qquad
\nabla_A\nabla_Bf=0.
$$

Logo, a equação de solíton no bulk:

$$
\mathcal R_{AB}
+\nabla_A\nabla_Bf
=
\lambda_Bg_{AB}
$$

é satisfeita com:

$$
\boxed{
\lambda_B=0.
}
$$

Com a medida reduzida normalizada:

$$
\Theta_p=1,
\qquad
\mathcal U_p=1,
\qquad
\sqrt{\det g_p}=1,
$$

temos:

$$
\mathcal I_p^{\rm bulk}
=
\sum_{a=1}^{3}
\int_{\mathcal F_a}d^5\phi
=
3(2\pi^5)
=
\boxed{6\pi^5}.
$$

Portanto, a parte de bulk/volume fica fechada no nível de ansatz estacionária
por câmara. A parte ainda aberta passa a ser a cola global: identificações
entre câmaras, conexão de Bismut/Cartan nas fronteiras e transgressão
torsional.

### 5.5 Cola global e superfície torsional

A cola global e o termo de superfície foram documentados em:

$$
\texttt{q40/adendo\_cola\_torcao\_superficie.md}.
$$

As três câmaras são coladas por mapas de transição:

$$
\Psi_{ab}:\partial\mathcal F_a\to\partial\mathcal F_b.
$$

Esses mapas carregam a conexão de Bismut/Cartan de fronteira:

$$
\mathfrak G_p
=
\{\,\mathcal F_a,\Psi_{ab},\mathcal A_{ab},B_{ab}\,\}_{a,b=1}^{3}.
$$

No interior:

$$
B^{(a)}=0.
$$

Na cola:

$$
B_{ab}\neq0.
$$

O termo de fronteira é escrito como transgressão:

$$
\mathcal I_p^{\partial}
=
\alpha
\int_{\partial\Sigma_p^\circ}
\mathcal T_{\rm eff}.
$$

A contribuição de holonomia/Chern--Simons dos três estômatos é:

$$
S_{\rm CS}^{(3)}
=
3\frac{\pi}{2}
=
\frac{3\pi}{2}.
$$

A contribuição espectral mínima das três gargantas é:

$$
\lambda_{\rm throat}^{(3)}
=
\frac{3}{\operatorname{Vol}(S^3)\operatorname{Vol}(S^1)}
=
\frac{3}{(2\pi^2)(2\pi)}
=
\frac{3}{4\pi^3}.
$$

Portanto:

$$
\boxed{
\mathcal I_p^{\partial}
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
$$

Com a parte de bulk:

$$
\mathcal I_p^{\rm bulk}=6\pi^5,
$$

obtemos:

$$
\boxed{
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
$$

Assim, a massa do próton fica fechada estruturalmente como:

$$
\boxed{
\text{massa do próton}
=
\text{volume de bulk}
+
\text{superfície torsional}.
}
$$

---

## 6. Como essa ponte deve ser feita

A prova deve ter quatro passos.

### 6.1 Reduzir a ação oficial para uma energia estática

Partir da ação GDQ oficial e restringir ao setor estacionário:

$$
\partial_\tau g=0,
\qquad
\partial_\tau f=0,
\qquad
\partial_\tau B=0.
$$

A energia do sóliton deve aparecer como funcional:

$$
E[g,f,B]
=
E_0
\int_{\Sigma}
\mathcal H_{\rm GDQ}(g,f,B)
\mathcal U\sqrt{\det g}\,d\Sigma.
$$

### 6.2 Normalizar o elétron

O elétron deve definir a unidade:

$$
\mathcal I_e
=
\int_{\Sigma_e}
\mathcal H_{\rm GDQ}(g_e,f_e,B_e)
\mathcal U_e\sqrt{\det g_e}\,d\Sigma_e
=1.
$$

Isso é compatível com a conclusão da Questão 36: a teoria prevê razões
adimensionais; a unidade MeV é metrológica.

### 6.3 Calcular o setor bariônico

Para o bárion trimodal:

$$
\mathcal I_p^{(0)}
=
\int_{\Sigma_B}
\mathcal H_{\rm GDQ}(g_B,f_B,B_B)
\mathcal U_B\sqrt{\det g_B}\,d\Sigma_B.
$$

O capítulo 26 afirma que a integral volumétrica reduzida é:

$$
\mathcal I_p^{(0)}=6\pi^5.
$$

Mas a auditoria exige explicitar:

1. qual é exatamente $\Sigma_B$;
2. qual é a métrica reduzida $g_B$;
3. por que o domínio é pentadimensional;
4. por que os limites de integração são os indicados;
5. por que $\sqrt{\det g_{5D}}$ produz exatamente o fator 6;
6. por que essa integral entra no funcional de energia, e não apenas no volume
   cinemático.

### 6.4 Mostrar que a correção de fronteira é prevista antes do CODATA

A correção:

$$
\Delta_B
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
$$

deve ser derivada como termo de contorno da ação:

$$
\Delta_B
=
\frac{1}{E_0}
\int_{\partial\Sigma_B}
\mathcal B_{\rm CS/Fredholm}(g,f,B)\,dS.
$$

O texto já fornece interpretação:

- $\frac{3\pi}{2}$: termo Chern--Simons/topológico de contorno;
- $\frac{3}{4\pi^3}$: menor contribuição espectral/garganta;
- $\alpha$: admitância eletro-geométrica.

Mas ainda falta demonstrar essa expressão diretamente da ação oficial ou de uma
ação efetiva derivada dela.

---

## 7. Massa do nêutron

O nêutron é descrito como a mesma classe bariônica trimodal:

$$
n_B=3,
$$

mas com orientação quiral antiparalela.

O próton é a configuração de menor energia com carga assintótica:

$$
Q_p=+1.
$$

O nêutron é a configuração neutra:

$$
Q_n=0.
$$

A diferença de massa vem do cisalhamento torsional:

$$
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}
+
\delta_B.
$$

No texto aparecem duas rotas numéricas próximas para $\delta_B$:

1. no capítulo 26, por índice de compressão quiral:

$$
\delta_B
\approx
2.530988;
$$

2. no Apêndice 1, por inércia efetiva:

$$
\delta_{\rm efetivo}
=
\ln(2\pi^2)\frac{3\sqrt2}{5}
\approx
2.530827.
$$

Essa diferença é pequena, mas deve ser eliminada antes de declarar a Q40
fechada. A teoria deve escolher uma única definição:

$$
\boxed{
\delta_B
=
\frac{1}{E_0}
\int_{\Sigma_n-\Sigma_p}
\rho\,
\frac14 B_{\mu\nu\lambda}B^{\mu\nu\lambda}
\sqrt{\det g}\,d\Sigma.
}
$$

Depois disso, a relação correta fica:

$$
\boxed{
\frac{M_n-M_p}{M_e}
=
\delta_B.
}
$$

Essa é a forma estruturalmente correta. O valor numérico deve ser consequência
da integral, não entrada posterior.

---

## 8. Carga

A parte da carga está bem estruturada.

O documento `nota_4.9_carga_quantizada.md` usa a integral de resíduos:

$$
Q
=
\frac{1}{2\pi i}
\oint_\gamma
\frac{\phi'(z)}{\phi(z)}\,dz
=
\sum_k \operatorname{Res}
\left(
\frac{\phi'}{\phi},z_k
\right)
=N\in\mathbb Z.
$$

Para o próton:

$$
\boxed{Q_p=+1.}
$$

Para o nêutron:

$$
\boxed{Q_n=0.}
$$

A interpretação correta é:

$$
\boxed{
\text{as cargas fracionárias locais são partições de um resíduo global inteiro.}
}
$$

Assim, a GDQ não precisa transformar-se no Modelo Padrão. Ela pode reproduzir
o comportamento efetivo de subcanais fracionários sem assumir quarks pontuais
como ontologia fundamental.

Status:

$$
\boxed{\text{carga estruturalmente resolvida.}}
$$

Falta apenas formalizar essa regra na mesma solução bariônica usada para a
massa.

---

## 9. Spin

O spin do bárion é tratado como circulação/holonomia de Bismut--Cartan.

A nota `nota_27.9_spin_proton.md` propõe:

$$
J_{\rm total}
=
J_{\rm estomas}
+
J_{\rm vorticidade}.
$$

O spin total do próton deve ser:

$$
\boxed{
J_p=\frac12\hbar.
}
$$

O nêutron também deve satisfazer:

$$
\boxed{
J_n=\frac12\hbar.
}
$$

O ponto conceitual é compatível com a discussão anterior da teoria: spin é
circulação geométrica, não seta interna pontual.

Status:

$$
\boxed{\text{spin estruturalmente encaminhado.}}
$$

Falta escrever a integral de holonomia para próton e nêutron dentro da mesma
classe de soluções $(g_B,f_B,B_B)$, e demonstrar que o resultado é exatamente
$\hbar/2$.

---

## 10. Paridade

A paridade ainda está pouco explicitada.

Para o estado fundamental bariônico esperado, a resposta deve ser:

$$
\boxed{
J_p^P=J_n^P=\frac12^+.
}
$$

Na linguagem GDQ, isso significa:

1. a densidade de Perelman $\rho=e^{-f}$ é par sob inversão espacial;
2. a configuração fundamental não possui nó radial excitado;
3. a torção $B$ entra como objeto axial/pseudotensorial compatível com
   paridade positiva do estado global;
4. a orientação quiral distingue próton e nêutron internamente, mas não muda a
   paridade espacial do estado fundamental.

Falta definir explicitamente o operador de paridade:

$$
\mathsf P:\; x^i\mapsto -x^i
$$

atuando sobre:

$$
(g,f,B,\rho,S_R).
$$

Status:

$$
\boxed{\text{paridade ainda não fechada.}}
$$

---

## 11. Raio

O manuscrito possui uma rota para o raio de carga do próton:

$$
r_p^2
\equiv
\frac{1}{M_p}
\int_{\Omega_{\rm estoma}}
r^2 R(g,\mathcal T_P)e^{-f}\,dV.
$$

Também há uma explicação para a diferença entre raio eletrônico e raio muônico:

$$
\Delta r_p
\sim
-
\frac{\alpha}{2\pi}
\left(
\frac{M_\mu}{M_p}
\right)^2
\delta_{\rm corte}.
$$

Isso é fisicamente interessante, mas para a Q40 ainda não basta.

Falta mostrar:

1. como $r_{p(e)}$ é obtido sem inserir $0.8775\,{\rm fm}$;
2. como $\delta_{\rm corte}$ é derivado da ação;
3. como o raio se relaciona com os fatores de forma;
4. qual raio é intrínseco e qual é dependente do probe.

Status:

$$
\boxed{\text{raio: rota proposta, ainda não fechado.}}
$$

---

## 12. Momentos magnéticos

O nêutron possui uma rota explícita no capítulo 26:

$$
\mu_n
\approx
-
(\delta_{\rm efetivo}\chi_{\rm Fano,n})
\frac{\pi}{2}
\mu_N.
$$

O texto também menciona que uma integração numérica do sistema de três
estômatos converge para:

$$
\mu_n\to -1.913042\,\mu_N.
$$

Isso é promissor, mas ainda há duas lacunas:

1. falta apresentar o mesmo cálculo para o próton:

$$
\mu_p\approx +2.792847\,\mu_N;
$$

2. falta derivar ambos por uma única fórmula:

$$
\boxed{
\vec\mu_B
=
\frac12
\int_{\Sigma_B}
\vec r\times \vec J_B\,dV,
}
$$

com:

$$
\vec J_B
=
\rho_B\,\vec v_B
\quad
\text{e}
\quad
\vec v_B
=
\frac{1}{m_B}\nabla S_R
$$

ou a versão geométrica equivalente sem introduzir massa como parâmetro
primitivo.

Status:

$$
\boxed{\text{momento magnético do nêutron encaminhado; próton incompleto.}}
$$

---

## 13. Fatores de forma

Para completar a derivação bariônica, é obrigatório obter os fatores de forma:

$$
G_E^p(q^2),\quad
G_M^p(q^2),\quad
G_E^n(q^2),\quad
G_M^n(q^2).
$$

Na GDQ, eles deveriam ser transformadas de Fourier das distribuições
geométricas de carga e corrente:

$$
G_E(q^2)
=
\int_{\Sigma_B}
e^{i\vec q\cdot\vec x}
\rho_Q(\vec x)\,d^3x,
$$

$$
G_M(q^2)
=
\int_{\Sigma_B}
e^{i\vec q\cdot\vec x}
\rho_M(\vec x)\,d^3x.
$$

Com:

$$
\rho_Q
\sim
\operatorname{Res}_\gamma(\partial\log\phi),
$$

e:

$$
\rho_M
\sim
\vec r\times \rho \vec v.
$$

Essas funções ainda não estão derivadas.

Status:

$$
\boxed{\text{fatores de forma ausentes.}}
$$

---

## 14. Espectro excitado

A Q40 exige o espectro excitado.

Para um bárion geométrico, isso significa linearizar a ação ao redor da solução:

$$
g=g_B+h,
\qquad
f=f_B+\varphi,
\qquad
B=B_B+\beta.
$$

O operador quadrático deve ser:

$$
\mathcal H_B^{(2)}
=
\delta^2\mathcal S_{\rm GDQ}
\big|_{(g_B,f_B,B_B)}.
$$

O espectro excitado é:

$$
\mathcal H_B^{(2)}\Psi_k
=
\lambda_k\Psi_k.
$$

Fisicamente, esses modos deveriam corresponder a ressonâncias bariônicas:

$$
N^\*,\quad \Delta,\quad \text{modos radiais},\quad \text{modos torsionais}.
$$

O manuscrito ainda não fornece esse espectro.

Status:

$$
\boxed{\text{espectro excitado ausente.}}
$$

---

## 15. Espalhamento

O espalhamento bariônico deve vir de uma matriz:

$$
\mathcal S_{B}
:
\mathcal H_{\rm in}
\to
\mathcal H_{\rm out}.
$$

Na linguagem GDQ, a matriz deve ser construída por:

1. perturbações incidentes do fluido;
2. interação com o núcleo de três estômatos;
3. imposição de causalidade de Sudarshan;
4. extração de fases de espalhamento;
5. cálculo de seções de choque.

O texto possui ideias de Fredholm/Fano e menções a DIS, mas ainda não fornece:

$$
\frac{d\sigma}{d\Omega},
\qquad
\sigma_{\rm tot},
\qquad
\mathcal A(s,t),
\qquad
\text{fases parciais}.
$$

Status:

$$
\boxed{\text{espalhamento bariônico ainda não fechado.}}
$$

---

## 16. Estabilidade

Há duas estabilidades diferentes.

### 16.1 Estabilidade do próton

A estabilidade do próton é associada à conservação do resíduo global:

$$
Q_p
=
\frac{1}{2\pi i}
\oint_{\gamma_{\rm global}}
\frac{\phi'}{\phi}\,dz
=1.
$$

Enquanto esse número de polo for conservado, não há decaimento contínuo para o
vácuo:

$$
\boxed{
Q_p=1\;\text{é invariante topológico.}
}
$$

Essa é uma boa rota estrutural.

Falta, porém, demonstrar que todos os canais de decaimento compatíveis com
energia, carga, spin e paridade são topologicamente proibidos.

### 16.2 Instabilidade do nêutron livre

O nêutron possui carga global nula, mas tensão torsional interna:

$$
\Delta E_{\rm torsion}
=
\int
\rho\,
\frac14 B_{\mu\nu\lambda}B^{\mu\nu\lambda}\,dV.
$$

Por isso, pode relaxar para:

$$
n\to p+e^-+\bar\nu_e.
$$

O capítulo 26 propõe:

$$
\tau_n
=
\frac{32}{15}\alpha^{-11}\tau_e.
$$

Correção posterior: a relação foi transportada para a taxa de transição pela
combinação contraída dos terceiros jatos,

$$
2|C_S|^2+6|C_T|^2
=\frac{15\pi^3}{16}\frac{\alpha^{11}m_ec^2}{I_\beta}.
$$

A separação individual dos canais permanece para observáveis polarizados:

$$
\Gamma_n
=
\frac{1}{\tau_n}
$$

a partir da matriz de transição geométrica.

Status:

$$
\boxed{\text{estabilidade estrutural proposta; prova completa ainda falta.}}
$$

---

## 17. Resposta direta à pergunta obrigatória sobre $6\pi^5$

O número:

$$
6\pi^5
$$

não pode ser aceito apenas porque:

$$
6\pi^5\approx 1836.118
$$

é próximo de:

$$
\frac{M_p}{M_e}\approx1836.153.
$$

Para não ser numerologia, ele precisa ser identificado como o autovalor ou a
integral de energia adimensional do sóliton bariônico na mesma normalização
que fixa o elétron:

$$
\boxed{
6\pi^5
=
\frac{
E_{\rm próton}^{(0)}
}{
E_{\rm elétron}
}.
}
$$

Mais precisamente:

$$
\boxed{
6\pi^5
=
\frac{
\int_{\Sigma_p}
\mathcal H_{\rm GDQ}^{(0)}
\mathcal U_p\sqrt{\det g_p}\,d\Sigma_p
}{
\int_{\Sigma_e}
\mathcal H_{\rm GDQ}^{(0)}
\mathcal U_e\sqrt{\det g_e}\,d\Sigma_e
}.
}
$$

Se o denominador for normalizado como unidade:

$$
\int_{\Sigma_e}
\mathcal H_{\rm GDQ}^{(0)}
\mathcal U_e\sqrt{\det g_e}\,d\Sigma_e
=1,
$$

então:

$$
\boxed{
\frac{M_p^{(0)}}{M_e}=6\pi^5.
}
$$

Essa é a resposta conceitual correta.

Mas o manuscrito ainda precisa executar a demonstração integral completa.

---

## 18. O que falta para fechar a Q40

Para fechar a Q40, devemos produzir um documento técnico adicional com estes
blocos.

### Bloco A — Solução bariônica

Definir:

$$
\mathcal C_B,\qquad
(g_B,f_B,B_B),
\qquad
N_{\rm estoma}=3.
$$

Mostrar:

$$
\delta\mathcal S_{\rm GDQ}[g_B,f_B,B_B]=0.
$$

### Bloco B — Energia e $6\pi^5$

Derivar:

$$
E_B=E_0\mathcal I_B,
$$

$$
\mathcal I_e=1,
\qquad
\mathcal I_p^{(0)}=6\pi^5.
$$

Esse é o bloco mais importante.

### Bloco C — Correção de fronteira do próton

Derivar:

$$
\Delta_p
=
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
$$

### Bloco D — Diferença nêutron-próton

Unificar:

$$
\delta_B
$$

em uma única fórmula, removendo a pequena divergência entre o capítulo 26 e o
Apêndice 1.

### Bloco E — Observáveis

Derivar:

1. $Q_p,Q_n$;
2. $J_p,J_n$;
3. $P_p,P_n$;
4. $r_p,r_n$;
5. $\mu_p,\mu_n$;
6. $G_E,G_M$;
7. espectro excitado;
8. matriz de espalhamento;
9. estabilidade e decaimento.

---

## 19. Conclusão

A resposta atual é:

$$
\boxed{
\text{o próton e o nêutron são modelados como sólitons trimodais de Ricci--Bismut.}
}
$$

O próton é a configuração carregada estável:

$$
\boxed{
Q_p=+1,\qquad J_p^P=\frac12^+.
}
$$

O nêutron é a configuração neutra com cisalhamento torsional:

$$
\boxed{
Q_n=0,\qquad J_n^P=\frac12^+,
\qquad
M_n-M_p>0.
}
$$

A massa do próton é proposta como:

$$
\boxed{
\frac{M_p}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right).
}
$$

Após os adendos da pasta `q40/`, essa fórmula deixa de ser apenas uma proposta
numérica e passa a ter a seguinte decomposição estrutural:

$$
\boxed{
\frac{M_p}{M_e}
=
\underbrace{6\pi^5}_{\rm bulk}
+
\underbrace{
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
}_{\rm superfície/torsão}.
}
$$

O termo $6\pi^5$ foi associado à soma dos volumes das três câmaras
fundamentais:

$$
6\pi^5=3(2\pi^5),
$$

e o termo de superfície foi associado à transgressão torsional de fronteira.

A massa do nêutron é proposta como:

$$
\boxed{
\frac{M_n}{M_e}
=
\frac{M_p}{M_e}
+
\delta_B.
}
$$

O fechamento de $\delta_B$ foi documentado em:

$$
\texttt{q40/adendo\_neutron\_deltaB.md}.
$$

A definição única adotada é:

$$
\boxed{
\delta_B
=
\frac{M_n-M_p}{M_e}
=
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
$$

Essa expressão representa a energia de cisalhamento torsional antiparalelo da
cola do nêutron em relação à cola do próton.

Assim:

$$
\boxed{
\frac{M_n}{M_e}
=
6\pi^5
+
\alpha
\left(
\frac{3\pi}{2}
+
\frac{3}{4\pi^3}
\right)
+
\ln(2\pi^2)\frac{3\sqrt2}{5}.
}
$$

Assim, o status refinado é:

$$
\boxed{
\text{massas de próton e nêutron fechadas estruturalmente; observáveis bariônicos ainda abertos.}
}
$$

O que ainda falta para fechar toda a Q40 não é mais a origem das massas
bariônicas, mas:

1. derivar paridade;
2. derivar raio;
3. derivar momentos magnéticos;
4. calcular fatores de forma;
5. calcular espectro excitado;
6. construir espalhamento;
7. provar estabilidade global.

Portanto, a Q40 fica parcialmente fechada: o setor de massas $p,n$ está
estruturado; os demais observáveis bariônicos ainda precisam de fechamento
próprio.
