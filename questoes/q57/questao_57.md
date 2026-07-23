# Questão 57 — MOND e \(a_0\)

## 1. Enunciado

A questão pede corrigir a inconsistência numérica do capítulo legado e
responder:

1. qual é a derivação única de \(a_0\);
2. como surgem curvas de rotação planas;
3. como tratar lentes gravitacionais;
4. como tratar dinâmica de aglomerados;
5. como tratar CMB;
6. como comparar a GDQ com MOND e matéria escura.

O erro aritmético explícito é:

$$
\frac{5{,}46\times10^{-10}}{2\pi}
\approx
8{,}69\times10^{-11},
$$

não \(1{,}21\times10^{-10}\).

---

## 2. Veredito

$$
\boxed{
\text{Q57 fechada estruturalmente; cosmologia perturbativa completa fica como extensão metrológica.}
}
$$

O fechamento consiste em separar três coisas que estavam misturadas no texto
legado:

1. a escala de horizonte \(cH_0\);
2. a escala de de Sitter \(cH_0\sqrt{\Omega_\Lambda}\);
3. a projeção circular \(1/(2\pi)\).

A rota coerente com a Q56 usa o mesmo contorno global, o raio de Hubble
\(R_H=c/H_0\). Portanto,

$$
\boxed{
a_0^{\rm GDQ}
=
\frac{c^2}{2\pi R_H}
=
\frac{cH_0}{2\pi}.
}
$$

Essa é a derivação única adotada nesta questão. A rota
\(cH_0\sqrt{\Omega_\Lambda}/(2\pi)\) é uma escala de horizonte de de Sitter,
mas não reproduz o valor MOND e não deve ser confundida com a fórmula
principal.

---

## 3. Cadeia dedutiva GDQ

A cadeia estrutural é:

$$
\mathcal S_{\rm GDQ}
\to
\text{sela cosmológica global}
\to
\text{contorno }R_H
\to
\text{circulação/projeção }2\pi
\to
a_0^{\rm GDQ}
\to
\text{resposta galáctica de baixa aceleração}.
$$

O \(2\pi\) não é um ajuste ao valor de MOND. Ele é a normalização circular da
resposta radial de fluxo quando uma escala global de horizonte é projetada no
canal local de circulação.

Assim:

$$
a_H=cH_0=\frac{c^2}{R_H},
$$

e a aceleração efetiva por ciclo de circulação é:

$$
a_0^{\rm GDQ}=\frac{a_H}{2\pi}.
$$

---

## 4. Avaliação numérica

Foi criado o script:

```text
questoes/q57/associados/calcular_a0_q57.py
```

A saída foi salva em:

```text
questoes/q57/associados/saida_calculo_a0_q57.md
```

Com \(H_0=67{,}4\,{\rm km\,s^{-1}\,Mpc^{-1}}\):

$$
a_0^{\rm GDQ}
=
1{,}042197881145\times10^{-10}\ {\rm m/s^2}.
$$

Com \(H_0=73\,{\rm km\,s^{-1}\,Mpc^{-1}}\):

$$
a_0^{\rm local}
=
1{,}128789989964\times10^{-10}\ {\rm m/s^2}.
$$

Comparação fenomenológica com a escala MOND típica
\(a_0^{\rm MOND}\sim1{,}2\times10^{-10}\,{\rm m/s^2}\):

| Fórmula | Valor \({\rm m/s^2}\) | Comentário |
| --- | ---: | --- |
| \(cH_0/(2\pi)\), \(H_0=67{,}4\) | \(1{,}0422\times10^{-10}\) | rota GDQ global coerente com Q56 |
| \(cH_0/(2\pi)\), \(H_0=73\) | \(1{,}1288\times10^{-10}\) | escala local |
| \(cH_0\sqrt{\Omega_\Lambda}/(2\pi)\) | \(8{,}6238\times10^{-11}\) | escala de de Sitter; não é a rota principal |

Classificação numérica:

$$
\boxed{
\text{avaliação direta e comparação fenomenológica, não previsão cega completa.}
}
$$

---

## 5. Curvas de rotação

Em galáxias isoladas e no regime de baixa aceleração, a GDQ deve reduzir a
resposta radial efetiva para a lei de transição:

$$
g_{\rm obs}\simeq \sqrt{g_N a_0^{\rm GDQ}},
\qquad
g_N=\frac{GM_b(r)}{r^2}.
$$

Então:

$$
\frac{v^2}{r}\simeq \sqrt{\frac{GM_b}{r^2}a_0^{\rm GDQ}},
$$

e:

$$
\boxed{
v^4\simeq GM_b a_0^{\rm GDQ}.
}
$$

Isto recupera a estrutura da relação bariônica de Tully--Fisher.

Na GDQ, essa relação não é tomada como axioma MOND. Ela é uma redução
galáctica do acoplamento entre:

1. contorno cosmológico \(R_H\);
2. circulação local \(2\pi\);
3. resposta radial da Hessiana gravitacional efetiva;
4. massa bariônica como fonte geométrica estabilizada.

---

## 6. Lentes gravitacionais

Uma MOND puramente escalar frequentemente enfrenta dificuldade em lentes,
porque alterar apenas a aceleração dinâmica de estrelas não garante alterar do
mesmo modo a métrica óptica que desvia fótons.

Na GDQ, a rota correta é diferente. Lentes devem vir da métrica efetiva
reconstruída:

$$
K_{\rm grav}^{\rm phys}\,\delta\Phi
=
J_{\rm bar}+J_{\rm tor},
$$

onde:

- \(J_{\rm bar}\) é a fonte bariônica;
- \(J_{\rm tor}\) é a fonte geométrica de torção/elasticidade residual;
- \(K_{\rm grav}^{\rm phys}\) é a Hessiana física projetada da ação oficial.

A deflexão é calculada pela geometria óptica do campo resultante, não por uma
lei MOND inserida manualmente:

$$
\hat\alpha
=
\int_{\gamma_{\rm luz}}
\nabla_\perp
\left(
\Phi+\Psi
\right)
\frac{2\,dl}{c^2}.
$$

Status:

$$
\boxed{
\text{lentes fechadas estruturalmente; mapas metrológicos exigem resolver }K_{\rm grav}^{\rm phys}.
}
$$

---

## 7. Aglomerados e Bullet Cluster

Aglomerados não devem ser tratados como simples galáxias MOND maiores. Eles
são sistemas de muitos corpos, com história dinâmica, colisões, gás
dissipativo e componente geométrica residual.

Na GDQ, o análogo fenomenológico da matéria escura em aglomerados é:

$$
\Theta_{\mu\nu}^{(H)}
\sim
H_{\mu\alpha\beta}H_\nu{}^{\alpha\beta}
-
\frac12 g_{\mu\nu}|H|^2,
$$

isto é, tensão elástica/torsional do background Hermitiano--Bismut sem estômato
material carregado.

Isso permite separar:

1. gás bariônico: sofre choque e dissipação;
2. galáxias: seguem quase balisticamente;
3. tensão geométrica residual: pode permanecer alinhada ao potencial de lentes.

Portanto a GDQ não é apenas MOND local. Ela contém uma componente geométrica
real que pode mimetizar matéria escura fria em aglomerados.

Status:

$$
\boxed{
\text{mecanismo estrutural presente; simulação de aglomerados fica como extensão metrológica.}
}
$$

---

## 8. CMB

O CMB exige mais do que curvas de rotação. É necessário um componente que:

1. gravite;
2. seja pouco acoplado ao plasma fóton--bárion antes da recombinação;
3. tenha baixa pressão efetiva;
4. sustente potenciais gravitacionais que modulam os picos acústicos.

Na GDQ, esse papel é atribuído ao setor geométrico residual:

$$
\rho_{\rm geo},\quad
\delta_{\rm geo},\quad
\Theta_{\mu\nu}^{(H)}.
$$

No limite linear, a forma esperada é:

$$
\ddot\delta_{\rm geo}
 +
\mathcal H\dot\delta_{\rm geo}
 -
4\pi G\rho_{\rm eff}\delta_{\rm geo}
=
O(c_s^2k^2)+O(\sigma_H).
$$

Quando \(c_s^2\approx0\) e o acoplamento eletromagnético é nulo, esse setor
se comporta como componente escura fria efetiva.

Status:

$$
\boxed{
\text{a estrutura de CMB é consistente; o espectro }C_\ell\text{ completo exige solver cosmológico GDQ.}
}
$$

---

## 9. Comparação com MOND e matéria escura

| Item | MOND | Matéria escura fria | GDQ |
| --- | --- | --- | --- |
| Curvas de rotação | boa em galáxias | boa com halos | boa estruturalmente via \(a_0^{\rm GDQ}\) |
| \(a_0\) | parâmetro fenomenológico | não fundamental | ligado a \(cH_0/(2\pi)\) |
| Tully--Fisher | natural | emerge por halos/feedback | natural no limite profundo |
| Lentes | exige extensão relativística | natural | vem da métrica/Hessiana, não só de aceleração escalar |
| Aglomerados | problemáticos em MOND pura | fortes | exigem tensão geométrica residual |
| CMB | problemático em MOND pura | forte | exige setor geométrico desacoplado |

Conclusão comparativa:

$$
\boxed{
\text{A GDQ não é MOND; ela contém um limite MOND galáctico e um setor geométrico escuro para cosmologia.}
}
$$

---

## 10. O que falta e o que não falta

Não falta mais:

1. corrigir a aritmética de \(a_0\);
2. escolher uma fórmula única;
3. explicar curvas de rotação;
4. indicar por que MOND escalar pura não basta;
5. indicar o setor GDQ que substitui matéria escura em lentes, aglomerados e
   CMB.

Falta apenas para metrologia completa:

1. construir \(K_{\rm grav}^{\rm phys}\) cosmológico;
2. resolver perturbações lineares com \(\rho_{\rm geo}\) e
   \(\Theta_{\mu\nu}^{(H)}\);
3. comparar com SPARC/RAR, lentes de aglomerados e \(C_\ell\) do CMB;
4. definir o contorno cosmológico usado em cada comparação:
   \(R_H\), horizonte de partículas ou horizonte de de Sitter.

Esses itens são programa de extensão, não reabrem a resposta estrutural da
Q57.

---

## 11. Fechamento

A Q57 fica fechada como:

$$
\boxed{
a_0^{\rm GDQ}=\frac{cH_0}{2\pi}
}
$$

com interpretação:

$$
\boxed{
\text{a aceleração MOND é o limite galáctico da ponte horizonte--circulação da GDQ.}
}
$$

O valor numérico global é:

$$
\boxed{
a_0^{\rm GDQ}
=
1{,}04\times10^{-10}\ {\rm m/s^2}
\quad
(H_0=67{,}4).
}
$$

O valor local é:

$$
\boxed{
a_0^{\rm local}
=
1{,}13\times10^{-10}\ {\rm m/s^2}
\quad
(H_0=73).
}
$$

O texto legado deve ser corrigido removendo a frase que associa
\(5{,}46\times10^{-10}/2\pi\) a \(1{,}21\times10^{-10}\).
