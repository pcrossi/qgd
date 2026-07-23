# Q48 — Como obter as correções hiperfinas por $\mathsf R_p$

## 1. Resposta curta

Os termos finais da hiperfina são obtidos substituindo o próton pontual da
fórmula de Fermi por uma interface dinâmica. A interface é codificada pela
impedância:

$$
\mathsf R_p
=
K_{YY}
-
K_{YI}K_{II}^{-1}K_{IY},
$$

calculada da Hessiana física da ação GDQ no background protônico.

O deslocamento hiperfino adicional é:

$$
\Delta\nu_{\rm hfs}^{p}
=
\frac1h
\langle 1s,F|
P_{\rm hfs}^\dagger
\left(
\mathsf R_p-\mathsf R_{\rm point}
\right)
P_{\rm hfs}
|1s,F\rangle_{\Delta F=1}.
$$

---

## 2. Decomposição dos termos

Escrevemos:

$$
\nu_{\rm hfs}
=
\nu_F
+
\Delta\nu_{\rm recoil}
+
\Delta\nu_{\rm surf}
+
\Delta\nu_{\rm geom}.
$$

Onde:

$$
\Delta\nu_{\rm recoil}
=
\frac1h
\langle 1s|
P_{\rm recoil}^\dagger
\Delta\mathsf R_p
P_{\rm recoil}
|1s\rangle,
$$

$$
\Delta\nu_{\rm surf}
=
\frac1h
\langle 1s|
P_{\rm surf}^\dagger
\Delta\mathsf R_p
P_{\rm surf}
|1s\rangle,
$$

$$
\Delta\nu_{\rm geom}
=
\frac1h
\langle 1s|
P_{\rm mag}^\dagger
\Delta\mathsf R_p
P_{\rm mag}
|1s\rangle.
$$

com:

$$
\Delta\mathsf R_p
=
\mathsf R_p-\mathsf R_{\rm point}.
$$

---

## 3. Significado físico

- $\nu_F$ é o termo de Fermi: próton como dipolo magnético pontual.
- $\Delta\nu_{\rm recoil}$ corrige o fato de elétron e próton formarem sistema
  ligado com centro de massa finito.
- $\Delta\nu_{\rm surf}$ mede que a magnetização do próton é distribuída numa
  superfície, não numa delta pontual.
- $\Delta\nu_{\rm geom}$ mede a deformação interna do canal magnético da
  superfície protônica pela Hessiana GDQ.

Todos vêm do mesmo objeto:

$$
\mathsf R_p^{\rm phys}.
$$

---

## 4. O que precisa ser calculado

Para transformar isso em número:

1. escolher o background protônico final $\Phi_{p,*}$ da Q40;
2. montar a Hessiana de superfície;
3. projetar modos físicos;
4. calcular o complemento de Schur;
5. subtrair o limite pontual;
6. contrair com os projetores hiperfinos do estado $1s$.

Nenhum desses passos exige inserir o Hamiltoniano hiperfino padrão como
axioma. O Hamiltoniano hiperfino aparece como forma efetiva de baixa energia
da impedância de superfície.

Status:

$$
\boxed{
\text{rota derivada e fechada formalmente; resta avaliação numérica de }K_p.
}
$$

---

## 5. Avaliação reduzida já adicionada

O script:

$$
\texttt{calcular\_hiperfina\_tamanho\_finito\_q48.py}
$$

foi atualizado para incluir:

1. o canal magnético líder da Q43,

   $$
   a_e^{(1)}=\frac{\alpha}{2\pi};
   $$

2. a impedância coletiva reduzida da Q40,

   $$
   \mathcal I_\Sigma(x)
   =
   -
   \left[
   j_0^2\frac{x^2}{1+x}
   +
   j_1^2\frac{x^2}{(1+x)^2}
   +
   j_2^2\frac{x^3}{(1+x)^2}
   \right].
   $$

Na escala atômica:

$$
q\sim\frac1{a_B^*},
$$

o parâmetro reduzido é:

$$
x=2.101391825244532\times10^{-11}.
$$

Como $\mathcal I_\Sigma=O(x^2)$, o efeito dessa impedância coletiva é:

$$
\mathcal I_\Sigma(x)
=
-2.089031019060285\times10^{-21}.
$$

Conclusão:

$$
\boxed{
\text{a superfície coletiva }q^4\text{ de Q40 é irrelevante para a hiperfina atômica.}
}
$$

Ela é importante para espalhamento/fatores de forma em $q$ intermediário, mas
não para fechar o resíduo de $1s$ hiperfino. O resíduo remanescente deve ser
calculado pelos canais:

1. recuo relativístico;
2. Zemach/magnetização distribuída;
3. termos superiores da Hessiana magnética local.

---

## 6. Efeito Zemach de casca superficial

O canal de magnetização distribuída pode ser avaliado, no primeiro modelo
reduzido de superfície, tratando as densidades elétrica e magnética como duas
cascas finas coincidentes no raio $r_p$.

O raio de Zemach é:

$$
r_Z
=
\int d^3r\,d^3r'\,
\rho_E(\mathbf r)\rho_M(\mathbf r')
|\mathbf r-\mathbf r'|.
$$

Para duas cascas esféricas finas idênticas, esse valor é a corda média entre
dois pontos da esfera:

$$
r_Z^{\rm shell}
=
\frac43r_p.
$$

Com:

$$
r_p=0.84077876545\,{\rm fm},
$$

obtemos:

$$
r_Z^{\rm shell}
=
1.121038353933\,{\rm fm}.
$$

A correção fracionária líder de Zemach é:

$$
\delta_Z
=
-2\alpha\frac{\mu c}{\hbar}r_Z.
$$

Numericamente:

$$
\delta_Z
=
-4.234604693327742\times10^{-5}.
$$

Aplicada depois do canal magnético líder:

$$
\nu_F(1+a_e^{(1)})(1+\delta_Z)
=
1.420427793305934\times10^9\,{\rm Hz}.
$$

Comparação com a linha de 21 cm:

$$
\Delta\nu=22041.537935\,{\rm Hz},
$$

e:

$$
\frac{\Delta\nu}{\nu_{\rm obs}}
=
1.551778\times10^{-5}.
$$

Classificação:

$$
\boxed{
\text{avaliação reduzida geométrica de superfície; não é ajuste ao alvo.}
}
$$

O resíduo restante é:

$$
-1.551753495565578\times10^{-5}
$$

como fração multiplicativa a ser atribuída aos canais de recuo e Hessiana
magnética superior.

---

## 7. Recuo cinemático e Hessiana magnética residual

O recuo cinemático fino reduzido foi avaliado como:

$$
\delta_{\rm rec}^{\rm kin}
=
-\frac12\alpha^2\frac{\mu}{m_p}.
$$

Numericamente:

$$
\delta_{\rm rec}^{\rm kin}
=
-1.449290394263207\times10^{-8}.
$$

Esse termo é pequeno na hiperfina de hidrogênio. Depois de aplicar
$a_e^{(1)}$, Zemach de casca e esse recuo, obtém-se:

$$
\nu_{\rm red}
=
1.420427772719811\times10^9\,{\rm Hz}.
$$

O resíduo requerido da Hessiana magnética superior é:

$$
\Delta\nu_{\rm Hess}^{\rm mag,req}
=
-22020.951811\,{\rm Hz}.
$$

ou, como fração:

$$
-1.550304227659893\times10^{-5}.
$$

Esse número não é declarado previsão. Ele é o alvo operacional que o elemento
de matriz:

$$
\frac1h
\langle 1s|
P_{\rm mag}^{\dagger}
\Delta\mathsf R_{p}^{\rm mag,sup}
P_{\rm mag}
|1s\rangle
$$

deve produzir quando a Hessiana magnética superior for calculada diretamente.
