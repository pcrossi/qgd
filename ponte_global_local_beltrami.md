# Ponte global--local — auditoria das deformações de Beltrami

## 1. Enunciado

Procura-se a menor deformação integrável de $J$ depois que o cálculo de
Nijenhuis excluiu o modo homogêneo $\chi(s)$. Uma deformação é representada
por

$$
\mu\in\Omega^{0,1}(T^{1,0}M)
$$

e deve satisfazer

$$
\bar\partial\mu+\frac12[\mu,\mu]=0.
$$

O domínio reduzido é

$$
M_{\rm col}=T^4\times I\times S^3.
$$

Ele possui bordo. Portanto a expressão

$$
H^{0,1}(T^{1,0}M_{\rm col})
$$

não define sozinha o espaço espectral físico: é necessário especificar o
domínio de $\bar\partial$, a condição elíptica no bordo e se os módulos globais
do toro estão fixos pelos dados cosmológicos.

## 2. Setor calculável sem hipótese adicional

No produto plano, o fator $T^4$ é um toro complexo de dimensão dois. Seu
fibrado holomorfo tangente é trivial. Logo

$$
H^{0,1}(T^{1,0}T^4)
\simeq H^{0,1}(\mathcal O_{T^4})\otimes\mathbb C^2
\simeq\mathbb C^2\otimes\mathbb C^2,
$$

e

$$
\boxed{\dim_{\mathbb C}H^{0,1}(T^{1,0}T^4)=4.}
$$

Em coordenadas holomorfas $(z^1,z^2)$, um primeiro representante pode ser

$$
\boxed{
\mu_0=d\bar z^1\otimes\partial_{z^2}.
}
$$

Ele não é $\bar\partial$-exato por uma função vetorial periódica global. Como
seus coeficientes são constantes e os campos $\partial_{z^i}$ comutam,

$$
\bar\partial\mu_0=0,
\qquad
[\mu_0,\mu_0]=0.
$$

Portanto Maurer--Cartan é satisfeita exatamente, não apenas em primeira ordem.

## 3. Contribuição à ação oficial

No background produto, $\mu_0$ é constante no toro e no colar. A variação da
forma fundamental toroidal também é paralela:

$$
d(\delta\omega_{\mu_0})=0.
$$

Consequentemente,

$$
\delta H
=D(d_J^c\omega)[0,\delta J_{\mu_0}]=0.
$$

Se a métrica é variada simultaneamente para permanecer hermitiana, essa
variação é precisamente uma deformação do módulo complexo plano. A curvatura
do toro continua nula e não aparecem derivadas radiais. Assim, no setor
produto homogêneo,

$$
\boxed{
D^2\mathcal S_{\rm GDQ}[\mu_0,\mu_0]=0
}
$$

antes dos vínculos cosmológicos. O representante é um módulo zero global, não
uma rigidez positiva ou negativa do estômato.

Se a estrutura complexa do $T^4$ faz parte do dado cosmológico fixado, então
$\mu_0$ não pertence ao espaço de variações admissíveis. Se ela puder variar,
o modo deve ser removido ou fixado como módulo; não pode ser contado como gap.

## 4. Interface e matching

Para o representante constante,

$$
\mu_0|_{Y_-}=\mu_0|_{Y_+},
\qquad
\nabla_\nu\mu_0=0.
$$

Seu par de dados de interface é, portanto,

$$
(q_{\mu_0},\Pi_{\mu_0})=(\mu_0,0).
$$

Ele não altera $a,c,u$ nem seus momentos normais na ordem linear. Logo a
derivada do tripleto residual original na direção desse modo é

$$
\boxed{
D_{\mu_0}(r_a,r_c,r_u)=0.
}
$$

Assim, o primeiro Beltrami não-gauge que pode ser calculado rigorosamente não
resolve a deficiência de posto da Porta B.

## 5. Por que um perfil radial não pode ser inserido

Tomar

$$
\mu=b(s)\mu_0
$$

produz em geral

$$
\bar\partial\mu=(\bar\partial b)\wedge\mu_0\neq0.
$$

Portanto $b(s)$ não é um parâmetro de tiro integrável isolado. Seria necessário
acrescentar componentes compensadoras e resolver o sistema Maurer--Cartan com
uma condição elíptica de bordo. Escolher $b(s)$ livre repetiria o erro do modo
$\chi(s)$.

## 6. Setor interno não homogêneo

Para procurar um Beltrami que realmente acople a $(a,c,u)$, deve-se definir o
complexo de bordo

$$
\bar\partial_{\mathsf B}:
\operatorname{Dom}_{\mathsf B}\Omega^{0,1}(T^{1,0})
\longrightarrow\Omega^{0,2}(T^{1,0}),
$$

com uma condição $\mathsf B$ derivada da colagem variacional. O candidato
físico é então um autovetor do laplaciano de Kodaira--Spencer

$$
\Box_{\bar\partial,\mathsf B}
=\bar\partial_{\mathsf B}^*\bar\partial_{\mathsf B}
+\bar\partial_{\mathsf B}\bar\partial_{\mathsf B}^*
$$

que satisfaça:

$$
\Box_{\bar\partial,\mathsf B}\mu=0,
\qquad
\bar\partial_{\mathsf B}^*\mu=0,
$$

e seja ortogonal a $\bar\partial V^{1,0}$.

A condição de interface natural, quando a forma quadrática for derivada, tem
a estrutura de continuidade de traço e balanço de fluxo:

$$
[\mu]_Y=0,
\qquad
[\Pi_\mu]_Y=0.
$$

Mas o coeficiente de $\Pi_\mu$ deve vir da segunda variação de
$-|d_J^c\omega|^2/12$; ele não pode ser substituído por Robin escolhida.

## 7. Contribuição quadrática geral implementável

Para qualquer modo integrável admissível, defina

$$
\mathscr D_J\mu
=D_J(d_J^c\omega)[\mu].
$$

A parcela torsional da Hessiana contém

$$
\boxed{
q_{H,J}[\mu]
=-\frac{\hbar}{12\Lambda_C^2}
\int_\gamma\!\int_M
\tau\mathcal U
\left(
2|\mathscr D_J\mu|^2
+2\langle H,D_J^2(d_J^c\omega)[\mu,\mu]\rangle
\right)dV\,\frac{d\tau}{\tau},
}
$$

acrescida dos termos de medida e das variações métricas exigidas pela
compatibilidade hermitiana. Essa é uma fórmula de montagem, não um sinal de
estabilidade: o sinal global e os termos cruzados só são conhecidos depois de
avaliar o modo e o background.

O acoplamento ao residual é a coluna

$$
B_\mu=D_\mu(r_a,r_c,r_u).
$$

Somente se $B_\mu\neq0$ o modo aumenta o posto do matching. Para $\mu_0$,
$B_{\mu_0}=0$ exatamente.

## 8. Veredito

O cálculo fornece um resultado negativo útil:

1. existem quatro módulos complexos toroidais não-gauge;
2. o primeiro satisfaz Maurer--Cartan exatamente;
3. ele é um modo zero produto;
4. não acopla ao tripleto residual;
5. um perfil radial isolado não é integrável.

O setor interno não homogêneo não pode ser calculado univocamente antes de
derivar a condição de bordo para o complexo de Kodaira--Spencer. Portanto não
há autorização para acrescentar um parâmetro Beltrami ao solver atual.

## 9. Código

`ponte_global_local_beltrami.py` e
`teste_ponte_global_local_beltrami.py` verificam dimensão, Maurer--Cartan,
momento normal e desacoplamento do representante toroidal constante.

