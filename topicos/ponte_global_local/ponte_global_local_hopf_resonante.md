# Ponte global--local — superfície de Hopf resonante

## 1. Contração

Considere

$$
F_\lambda(z_1,z_2)
=\left(\alpha z_1+\lambda z_2^m,\beta z_2\right),
\qquad |\alpha|,|\beta|<1.
$$

Uma mudança holomorfa

$$
w_1=z_1+cz_2^m
$$

remove o termo não linear quando

$$
c=\frac{\lambda}{\beta^m-\alpha}.
$$

Logo a classe é nova somente na ressonância

$$
\boxed{\alpha=\beta^m.}
$$

Nesse caso a equação cohomológica possui denominador zero e o monômio não pode
ser eliminado por conjugação holomorfa.

Para $\lambda\neq0$, uma reescala de $z_1$ normalmente normaliza seu módulo;
assim, em muitas classificações, $\lambda=0$ e $\lambda\neq0$ são estratos,
e não uma linha de módulos métricos absolutos. Isso reforça que seu valor não
deve ser tratado como acoplamento livre.

## 2. Conjugação diferenciável

Escolha uma função suave $t$ no recobrimento tal que

$$
t(F_0z)=t(z)+1.
$$

Na ressonância, defina

$$
h_\lambda(z)
=\left(z_1+\frac\lambda\alpha t(z)z_2^m,z_2\right).
$$

Então

$$
\boxed{h_\lambda\circ F_0=F_\lambda\circ h_\lambda.}
$$

$h_\lambda$ não é holomorfa, mas fornece a identificação diferenciável dos
quocientes.

## 3. Representante de Beltrami

O campo infinitesimal é

$$
V^{1,0}
=\frac\lambda\alpha t(z)z_2^m\partial_{z_1},
$$

e o representante linear é

$$
\boxed{
\mu_{\rm res}^{(1)}
=\frac\lambda\alpha
z_2^m\bar\partial t\otimes\partial_{z_1}.
}
$$

Ele é localmente $\bar\partial$-exato, mas seu potencial não desce ao
quociente. A obstrução global é precisamente o monômio resonante.

## 4. Maurer--Cartan

Em primeira ordem,

$$
\bar\partial\mu_{\rm res}^{(1)}=0.
$$

Para amplitude finita, use o coeficiente de Beltrami da conjugação
$h_\lambda$:

$$
\mu_{\rm res}^{\rm exact}
=(\partial h_\lambda)^{-1}\bar\partial h_\lambda.
$$

Como ele é obtido pelo pullback de uma estrutura complexa integrável,

$$
\bar\partial\mu_{\rm exact}
+\frac12[\mu_{\rm exact},\mu_{\rm exact}]=0
$$

em todas as ordens. Truncar no termo linear não autoriza descartar a correção
quadrática.

## 5. Norma

Para qualquer métrica Hermitiana suave $g_H$ no quociente compacto,

$$
\boxed{
\|\mu_{\rm res}^{(1)}\|^2
=\frac{|\lambda|^2}{|\alpha|^2}
\int_{X_0}|z_2|^{2m}
|\bar\partial t|_{g_H}^2
|\partial_{z_1}|_{g_H}^2,dV_{g_H}<\infty.
}
$$

Não existe valor absoluto canônico sem derivar a métrica compatível para o
quociente diagonal resonante. Usar o métrico cilíndrico escalar de $qI$ quando
$|\alpha|\neq|\beta|$ seria inconsistente. Portanto a finitude é derivada,
mas um número não é fabricado.

## 6. Simetria

O monômio $z_2^m\partial_{z_1}$ possui carga

$$
m\theta_2-\theta_1
$$

sob $U(1)_1\times U(1)_2$. Para $\lambda\neq0$, preserva apenas o subgrupo

$$
\theta_1=m\theta_2.
$$

Assim a deformação quebra a simetria do background linear. No ponto
$\lambda=0$, ela é não-singlet e não acopla linearmente aos resíduos
homogêneos:

$$
\boxed{B_{\mu_{\rm res}}=0.}
$$

## 7. Naturalidade da ação oficial

Para manter a compatibilidade hermitiana, a família sem hipótese métrica nova
é

$$
X_\lambda
=(g_\lambda,J_\lambda,f_\lambda)
=h_\lambda^*(g_0,J_0,f_0).
$$

Então

$$
H_\lambda=h_\lambda^*H_0,
\quad
\mathcal R_{B,\lambda}=h_\lambda^*\mathcal R_{B,0},
\quad
\mathcal U_\lambda dV_\lambda
=h_\lambda^*(\mathcal U_0dV_0).
$$

Além disso,

$$
\det DF_\lambda=\alpha\beta
$$

é independente de $\lambda$. A identificação do domínio fundamental é
transportada por $h_\lambda$. Portanto, com os dados globais escalares já
fixados,

$$
\boxed{
\mathcal S_{\rm GDQ}[X_\lambda]
=\mathcal S_{\rm GDQ}[X_0].
}
$$

A não equivalência biholomorfa da classe resonante é real em geometria
complexa marcada, mas não gera energia quando todos os campos são apenas
transportados por uma identificação diferenciável e nenhuma marcação
holomorfa externa foi prescrita.

## 8. Hessiana física

Ao longo da família compatível,

$$
\boxed{
D^k\mathcal S_{\rm GDQ}/D\lambda^k=0
\quad(k\ge1).
}
$$

Logo ela é novamente um zero modular da ação atual. O estrato $\lambda\neq0$
pode mudar a álgebra de simetria, mas não fornece massa ou estabilização sem
um funcional que selecione uma métrica não-pullback. Introduzir tal métrica à
mão violaria o escopo.

## 9. Mapa para o colar

Ao cortar o quociente, o modo satisfaz a identificação torcida por
$F_\lambda$. Os termos das duas faces cancelam. Sua restrição local pode ser
usada como vetor de auditoria do kernel, mas não como novo parâmetro físico de
Galerkin.

## 10. Veredito

1. o termo resonante é globalmente não removível por biholomorfismo;
2. produz um Beltrami integrável explícito;
3. possui norma finita, dependente da métrica compatível;
4. quebra a simetria para um $U(1)$ resonante;
5. não acopla linearmente no background simétrico;
6. com a única métrica derivada sem hipótese adicional — o pullback — a ação é
   exatamente plana;
7. portanto não resolve o residual nem produz Hessiana física não nula.

