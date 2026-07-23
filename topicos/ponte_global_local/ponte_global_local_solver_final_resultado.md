# Resultado auditado do solver final causal

## 1. Montagem executada

O script `ponte_global_local_solver_final.py` reuniu:

1. dois colares internos independentes;
2. exterior causal com warps $A_0$ e $A_s$;
3. colagem canônica de $(a,c,u)$ e seus momentos;
4. restrição do lapse;
5. vínculo de raio

$$
\mathcal C_R
=\frac{2y+z}{3}-\log(\pi^2\sqrt\alpha);
$$

6. vínculo energético normalizado;
7. onze parâmetros e onze resíduos.

## 2. Resultado da execução

A execução não produziu uma sela. O integrador causal abandonou a trajetória
antes do extremo exterior e o candidato foi corretamente rejeitado:

$$
\boxed{
\texttt{accepted\_as\_reduced\_saddle=False}.
}
$$

Não existe, portanto, posto físico ou gap a declarar nessa execução.

## 3. Diagnóstico da primeira normalização

Tratar o momento bruto do sistema reduzido como se já fosse a energia
adimensional, impondo $p_0e^{-x_0}=1$, gerou velocidades iniciais fora da
escala natural e explosão da integração.

Esse teste exclui a identificação direta

$$
p_0^{\rm red}=\widehat E_H.
$$

## 4. Diagnóstico da normalização por $\Pi_G$

Foi testada também a identificação

$$
p_0^{\rm red}=\Pi_G\widehat E_H,
$$

com

$$
\Pi_G
=\frac{\alpha^4(1+\alpha)}{3\sqrt2/5}e^{-1/(2\alpha)}
=5{,}890655556\times10^{-39}.
$$

Durante a evolução, $p_0$ recebe a contribuição

$$
\dot p_0=\mathscr V F.
$$

Na semente histórica essa contribuição é de ordem macroscópica nas unidades
reduzidas. Dividir o resíduo por $\Pi_G$ produz condicionamento de ordem
$10^{38}$--$10^{44}$ e a trajetória novamente não alcança o extremo.

Esse teste não refuta a normalização global por $\alpha$. Ele demonstra apenas
que

$$
\boxed{
\Pi_G\text{ não é, sem um jacobiano adicional, a unidade canônica de }p_0.
}
$$

## 5. Correção pela normalização constitucional

Seja

$$
Z_0=\int ds\,\mathscr V.
$$

O zero mode da normalização impõe

$$
e^{-\lambda_N}=\frac{Z_{\rm cos}}{Z_0}
$$

e transforma o momento pela mesma razão. Logo a quantidade geométrica
normalizada é

$$
\frac{p_0^{\rm red}e^{-x_0}}{Z_0}.
$$

Os volumes coordenados compactos cancelam entre o momento e a normalização de
$\mathcal U$; não são fatores físicos independentes.

## 6. O elo único realmente faltante

É necessário calcular uma vez o mapa

$$
K_\gamma(\alpha)
=\frac{\hbar}{\Lambda_C^2\beta_EE_H}
\operatorname{Re}\!\int_\gamma\frac{d\tau}{\tau},
$$

a partir dos fatores que permanecem depois da normalização:

$$
\frac{\hbar}{\Lambda_C^2},
\qquad
\int_\gamma\frac{d\tau}{\tau},
$$

e da normalização global de Einstein já assumida. O vínculo correto será

$$
\boxed{
\mathcal C_E
=K_\gamma(\alpha)
\frac{p_0^{\rm red}e^{-x_0}}{Z_0}-1=0.
}
$$

O valor de $K_\gamma$ não deve ser escolhido pelo condicionamento do solver.

## 7. Validações que permanecem positivas

Foram reexecutados independentemente:

1. redução isotrópica causal: resíduo simbólico zero;
2. momento do relógio: resíduo simbólico zero;
3. determinante cinético: $\det M_C=32$;
4. conservação da restrição causal: erro máximo
   $2{,}665\times10^{-15}$;
5. vínculo de raio: posto do sistema anterior elevado de oito para nove.

Portanto, a falha está isolada no transporte da normalização energética para
o momento reduzido, e não nas equações causais ou em $\mathcal C_R$.

## 8. Veredito

$$
\boxed{
\text{solver montado e executado; sela não validada na execução histórica.}
}
$$

Atualização: `topicos/ponte_global_local/ponte_global_local_tau_causal_resultado.md` mostrou, usando o
projetor causal normalizado já estabelecido em Q4, Q9 e Q29, que
$K_\gamma=1$ no setor estacionário. O teste anterior com esse valor deixa de
ser uma escolha arbitrária, mas continua não sendo uma sela porque a busca
histórica não convergiu. A pendência passa a ser exclusivamente resolver e
validar o sistema não linear com método numérico robusto.

Somente após essa avaliação deve-se repetir a busca, calcular o posto e então
substituir a sela na Hessiana física já formulada.

## 9. Execução com normalização acumulada

O solver foi ampliado com

$$
\dot Z=\mathscr V
$$

e passou a avaliar a razão $p_0e^{-x_0}/Z_0$. O integrador explícito foi
substituído por um método rígido implícito na validação; isso eliminou a falsa
interrupção da trajetória. No teste com $K_\gamma=1$, o resíduo inicial ficou
finito e a busca reduziu o custo de $1{,}3222$ para $0{,}99865$, mas entrou em
região numericamente rígida antes de obter uma raiz. A execução foi
interrompida e nenhum candidato foi aceito.

Esse teste é exploratório porque $K_\gamma=1$ ainda não foi derivado. Ele
confirma que a normalização acumulada remove o condicionamento artificial de
$10^{38}$, mas não demonstra a sela.
