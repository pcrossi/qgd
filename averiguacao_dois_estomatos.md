# Averiguação independente — configuração de dois estômatos

## 1. Pergunta

Uma configuração com dois estômatos pode satisfazer a conservação do fluxo e
ser estável?

Esta nota é deliberadamente independente das questões consolidadas. Seu
resultado não deve ser transferido automaticamente para a contagem de
gerações, para bárions ou para qualquer interpretação de partícula.

## 2. Equilíbrio vetorial

Para dois fluxos de igual módulo,

$$
\mathbf T_a
=T(\cos\theta_a,\sin\theta_a),
$$

o vínculo é

$$
\mathbf T_1+\mathbf T_2=0.
$$

Logo,

$$
\theta_2-\theta_1=\pi\pmod{2\pi}.
$$

A solução existe e é antipodal.

## 3. Estabilidade angular

O funcional reduzido é

$$
\mathcal E_2
=\frac{\kappa T^2}{2}
\left|
\widehat{\mathbf T}_1+widehat{\mathbf T}_2
\right|^2
=\kappa T^2\left[1+\cos(\theta_1-\theta_2)\right].
$$

Escrevendo

$$
\theta_2-\theta_1=\pi+\delta,
$$

obtém-se

$$
\mathcal E_2
=\frac{\kappa T^2}{2}\delta^2+O(\delta^4).
$$

A Hessiana nas duas coordenadas angulares possui espectro

$$
\boxed{
\operatorname{spec}H_2
=\kappa T^2\{0,2\}.
}
$$

O zero é a rotação comum. Depois de removê-la, resta um autovalor positivo.
Portanto,

$$
\boxed{
N=2\text{ é angularmente estável no modelo de fechamento.}
}
$$

## 4. O que essa estabilidade não demonstra

A estabilidade angular não prova que exista uma solução estacionária completa
da ação GDQ com dois estômatos. Ainda seria necessário verificar:

1. o modo que altera a distância entre os dois centros;
2. os modos radiais de cada garganta;
3. atração, repulsão ou aniquilação entre fluxos opostos;
4. a Hessiana métrico--dilatônica do background bicêntrico;
5. a possibilidade de separação contínua em dois defeitos independentes.

O cálculo angular testa somente a orientação dos fluxos.

## 5. Geometria da configuração

Dois vetores opostos ocupam uma única reta na distribuição horizontal. A
configuração é, portanto, colinear. Geometricamente ela é compatível com:

1. um tubo com duas extremidades;
2. uma garganta ligando duas regiões;
3. um dipolo;
4. um par estômato--antiestômato, dependendo da orientação escalar.

Ela não constitui um junction ramificado no plano horizontal.

Três estômatos, por outro lado, formam o primeiro equilíbrio que ocupa as duas
dimensões horizontais:

$$
\mathbf T_1+\mathbf T_2+\mathbf T_3=0,
\qquad
\theta_{ab}=120^\circ.
$$

Assim, a diferença entre dois e três não é simplesmente estabilidade versus
instabilidade. É

$$
\boxed{
\text{configuração colinear de ligação}
\quad\text{versus}\quad
\text{junction não colinear}.
}
$$

## 6. Carga orientada

O fechamento mecânico não determina sozinho as cargas escalares $q_a$.
Direções espaciais opostas podem carregar:

$$
(q_1,q_2)=(1,-1)
$$

ou

$$
(q_1,q_2)=(1,1),
$$

desde que o balanço global inclua o bulk e a carga total. Portanto, não é
correto excluir dois estômatos apenas alegando neutralidade: isso depende da
relação ainda não demonstrada entre orientação mecânica e circulação escalar.

## 7. Conclusões

1. Dois estômatos são estáveis contra perturbações angulares relativas no
   funcional universal de fechamento.
2. O cálculo disponível não determina sua estabilidade radial ou sua
   estabilidade contra separação e aniquilação.
3. Dois estômatos descrevem naturalmente uma estrutura colinear de ligação,
   não um junction horizontal.
4. Estabilidade isoladamente não permite selecionar três em vez de dois.
5. A distinção física exige um critério independente: ramificação,
   indecomponibilidade topológica, carga, condição de colagem ou estabilidade
   do modo de distância.
6. Até esse critério ser calculado, a existência de um setor bicêntrico
   estável deve permanecer uma possibilidade legítima da GDQ.

## 8. Próximo teste decisivo

O teste mínimo é introduzir a separação $d$ entre os dois centros e calcular a
ação on-shell

$$
\mathcal S_2^{\rm on-shell}(d).
$$

Uma molécula bicêntrica estável exigiria

$$
\frac{d\mathcal S_2^{\rm on-shell}}{dd}=0,
\qquad
\frac{d^2\mathcal S_2^{\rm on-shell}}{dd^2}>0
$$

em algum $d=d_* >0$. Se a ação for monotônica, o par se separa ou colapsa e a
estabilidade angular não corresponde a um objeto bicêntrico estável.

## 9. Avaliação do modo de separação no setor mínimo

O termo da ação oficial que controla a fase é positivo:

$$
\mathcal S_v
=\frac{\hbar\tau}{\Lambda_C^2}
\int\mathcal U\,|\nabla v|^2dV.
$$

Para duas fontes localizadas, escreva

$$
v=q_1G_1+q_2G_2,
$$

onde $G_a$ é a função de Green centrada no estômato $a$. A parte dependente da
distância é o termo cruzado

$$
\mathcal S_{\rm int}(d)
=2\frac{\hbar\tau}{\Lambda_C^2}
q_1q_2
\int\mathcal U\,\nabla G_1\cdot\nabla G_2,dV.
$$

No regime local em quatro dimensões reais, a função de Green tem a forma

$$
G(d)=\frac1{4\pi^2d^2}.
$$

Absorvendo o prefator positivo em $C>0$,

$$
\boxed{
\mathcal S_{\rm int}(d)=C\frac{q_1q_2}{d^2}.
}
$$

Então

$$
\mathcal S_{\rm int}'(d)
=-2C\frac{q_1q_2}{d^3}.
$$

Para qualquer $d>0$ e $q_1q_2\ne0$,

$$
\mathcal S_{\rm int}'(d)\ne0.
$$

Logo, não existe ponto estacionário em distância finita nesse setor.

### Fluxos de mesmo sinal

Se $q_1q_2>0$, a energia diminui quando $d$ aumenta. O par se repele e tende a
separar-se.

### Fluxos de sinais opostos

Se $q_1q_2<0$, a energia diminui quando $d$ diminui. O par se atrai e tende a
colapsar, aniquilar ou atingir o contato regulado pelo raio do estômato.

## 10. Veredito de estabilidade

Há duas respostas distintas:

$$
\boxed{
\text{estável angularmente: sim.}
}
$$

$$
\boxed{
\text{estável como objeto bicêntrico separado: não, no setor mínimo da ação.}
}
$$

O modo de separação não possui mínimo em $d>0$. Portanto, a configuração de
dois estômatos não é um sóliton bicêntrico ligado no background local mínimo:
ela se separa ou colapsa conforme a orientação escalar.

Uma estabilidade a distância finita só poderia aparecer se outro termo da
ação completa produzisse uma contribuição concorrente, por exemplo

$$
\mathcal S_{\rm extra}(d)
$$

com derivada de sinal oposto. Nenhum termo desse tipo foi demonstrado nesta
averiguação. Assim, não se deve afirmar estabilidade bicêntrica completa com
os dados atuais.
