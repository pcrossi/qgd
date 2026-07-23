# Q30 — Cálculo de $\sigma$ e do gap a partir da ação GDQ

## 1. Enunciado exato

Pretende-se calcular, sem importar uma ação fundamental de Yang--Mills ou uma
ação de plaqueta,

$$
\sigma_{\rm GDQ}
=\inf\frac{E_{\rm tubo}}{L_z}
$$

e o primeiro autovalor positivo da Hessiana física no tubo minimizante,

$$
\lambda_1^+
=\inf\operatorname{spec}
\left(operatorname{Hess}\mathcal S_{\rm GDQ}\big|_{\rm phys}\right)
\setminus\{0\}.
$$

O domínio local oficial é $\mathbb R^4\times T^4$. A estrutura $SU(3)$ da Q28
é uma decomposição efetiva do fibrado interno; ela rotula o setor de
holonomia, mas não substitui as variáveis fundamentais $(g,f,\bar f)$ da ação.

## 2. Entrada fundamental

A única ação usada como ponto de partida é

$$
\mathcal S_{\rm GDQ}
=\int_\gamma\left[\int_{\mathcal M_{\mathbb C}}
\frac{\hbar}{\Lambda_C^2}
\left[
\tau\left(\mathcal R+g^{\mu\bar\nu}
\partial_\mu f\partial_{\bar\nu}\bar f\right)
+\frac{f+\bar f}{2}-n
\right]
\mathcal U\sqrt{\det g}\,d^{2n}z\right]\frac{d\tau}{\tau}.
$$

Não se acrescenta $\operatorname{tr}F^2$, $H^2$, Bohm ou potencial confinante
como termos fundamentais independentes. Se aparecerem, seus coeficientes
devem resultar da redução da curvatura de Bismut, da medida $\mathcal U$ e da
decomposição de $f$.

## 3. Ansatz tubular mínimo

Use coordenadas $(z,x^a,y^i)$, onde $z$ é o eixo do tubo, $x^a$ são as duas
direções transversais físicas e $y^i$ coordenam o $T^4$. O ansatz deve ter a
forma

$$
ds^2
=e^{2A(r)}dz^2+e^{2B(r)}(dr^2+r^2d\theta^2)
+G_{ij}(r)\bigl(dy^i+K^i_A A^A\bigr)
\bigl(dy^j+K^j_B A^B\bigr),
$$

$$
f=f_R(r)+if_I(r,\theta),
\qquad
\oint d f_I=2\pi n_C.
$$

Aqui $n_C$ é a classe de circulação/holonomia. Os campos $A^A$ são componentes
da métrica/fibração na redução, não novos campos fundamentais.

Condições mínimas:

1. regularidade em $r=0$;
2. energia transversal finita;
3. aproximação ao background admissível quando $r\to\infty$;
4. classe $n_C$ fixada;
5. gauge geométrico fixado antes da Hessiana.

## 4. Redução que deve ser executada

Inserindo o ansatz na ação e integrando $T^4$ e o contorno de fluxo, deve-se
obter sem pós-ajuste

$$
E_\perp[q]
=2\pi\int_0^\infty r\,dr\,
\mathcal L_\perp
\left(q,q';n_C\right),
$$

com

$$
q=(A,B,G_{ij},f_R,f_I).
$$

A tensão será então

$$
\boxed{
\sigma_{\rm GDQ}
=E_\perp[q_*]-E_\perp[q_{\rm vac}],
}
$$

onde $q_*$ resolve as equações de Euler--Lagrange na classe $n_C\ne0$. A
subtração do vácuo é necessária para não confundir energia de fundo com
tensão do tubo.

## 5. Hessiana e gap

Somente depois de obter $q_*$ define-se

$$
\mathcal H_{\rm GDQ}^{\rm tubo}
=P_{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}[q_*]
P_{\rm phys}.
$$

Devem ser removidos:

1. difeomorfismos;
2. transformações de frame interno;
3. translações do centro do tubo;
4. outros modos zero coletivos.

O gap físico condicional é

$$
\boxed{
\Delta_{\rm GDQ}
=\frac{\hbar c}{\ell_C}\sqrt{\lambda_1^+},
\qquad
\lambda_1^+>0,
}
$$

com $\ell_C=\hbar c/\Lambda_C$ e autovalores escritos em unidades de Cartan.

## 6. Auditoria do código histórico

`numerico/q30_confinamento/solve_confinement_q30.py` não executa essa cadeia.
Ele escolhe externamente:

1. $\mathcal R=6$ em $S^3$ normalizado;
2. um perfil $|\nabla f|^2=4\sin^2\chi$;
3. $|H|^2=24$;
4. condições de Dirichlet e um operador escalar 1D;
5. em outra saída, ação de plaqueta com $\beta=6$, $a=0{,}1$ fm e uma escala
   de $110$ MeV.

Seus autovalores são testes de um operador escolhido. Não são derivação de
$\sigma$ ou do gap da GDQ e permanecem como exploração histórica.

## 7. Primeiro diagnóstico

O obstáculo atual não é numérico. Falta calcular explicitamente
$\mathcal L_\perp$ pela substituição do ansatz tubular na ação oficial. Sem
essa redução, escolher um perfil e diagonalizá-lo seria engenharia inversa.

O próximo passo é calcular separadamente:

1. ~~$\sqrt{\det g}$, $\mathcal U$ e o setor cinético de $f$~~ — executado
   em `questoes/q30/associados/reducao_medida_cinetica_tubo.md`;
2. a parcela torsional de Bismut foi reduzida no subansatz diagonal em
   `questoes/q30/associados/reducao_torcao_bismut_tubo.md`; o resultado é um no-go para torção
   strong-KT não trivial regular nesse subansatz, exigindo conexão KK fora da
   diagonal ou fluxo topológico;
3. ~~$g^{M\bar N}\partial_Mf\partial_{\bar N}\bar f$~~ — executado no mesmo
   adendo;
4. os termos de bordo exigidos pela variação radial;
5. as equações de Euler--Lagrange transversais.

A hipótese arquitetural vigente do autor foi formalizada em
`questoes/q30/associados/ansatz_torcao_sem_elongacao.md`: congelar as deformações Hermitianas
simétricas e permitir apenas a conexão $\mathfrak{su}(3)$ antissimétrica. Ela
evita o no-go diagonal, mas ainda deve passar pelo teste
$\delta\mathcal S_{\rm GDQ}/\delta S|_{S=0}=0$.

## 8. Status

$$
\boxed{
\text{Q30 iniciada no nível quantitativo GDQ; redução transversal oficial
ainda pendente.}
}
$$

Este documento substitui como roteiro quantitativo qualquer leitura do solver
histórico como prova numérica. Ele não substitui
`questoes/q30/associados/conexao_su3_wilson_gap.md`, que permanece como fechamento estrutural
condicional.
