# Q53 — Refinamento metrológico pela Hessiana neutra oficial

## 1. Status

A Q53 fica encerrada no nível estrutural:

$$
\boxed{
\text{neutrino = modo neutro torsional/fase; massas neutras = candidato reduzido forte.}
}
$$

Este documento registra apenas o refinamento necessário para transformar a
redução quantitativa atual em previsão metrológica máxima.

Classificação:

$$
\boxed{
\text{programa de refinamento; não reabre a Q53 estrutural.}
}
$$

---

## 2. Resultado reduzido atual

A execução reduzida usa:

$$
S_\nu=\alpha^7Q_\beta^2,
$$

$$
\lambda
=
\left(
0,
\frac{\chi_\nu^2}{2},
\frac{6\pi}{5}
\right),
\qquad
\chi_\nu=\frac{12}{25}e^{-\alpha/4}.
$$

Com isso:

$$
\Delta m_{21}^2
=
7.741214557111\times10^{-5}\ {\rm eV}^2,
$$

$$
\Delta m_{31}^2
=
2.542566638608\times10^{-3}\ {\rm eV}^2.
$$

Comparando com NuFIT 6.0 NO:

| quantidade | GDQ reduzido | referência | erro relativo |
|---|---:|---:|---:|
| $\Delta m_{21}^2$ | $7.741214557111\times10^{-5}\ {\rm eV}^2$ | $7.49\times10^{-5}\ {\rm eV}^2$ | $+3.353999\%$ |
| $\Delta m_{31}^2$ | $2.542566638608\times10^{-3}\ {\rm eV}^2$ | $2.534\times10^{-3}\ {\rm eV}^2$ | $+0.338068\%$ |

Leitura:

- o modo superior está quase fixado pela circulação global $3/5$;
- o gargalo quantitativo é o bloco bicanal de interface que fixa
  $\lambda_2$.

---

## 3. O que deve ser derivado diretamente

O refinamento deve substituir a leitura reduzida por uma avaliação direta do
bloco neutro físico:

$$
K^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm folha},
K_{\rm neutro}^{\rm phys}
\Psi_\beta^{\rm folha}
\right\rangle_{\mathcal U},
$$

com matriz de Gram:

$$
G^\nu_{\alpha\beta}
=
\left\langle
\Psi_\alpha^{\rm folha},
\Psi_\beta^{\rm folha}
\right\rangle_{\mathcal U}.
$$

O problema físico é:

$$
K^\nu c_i=\lambda_iG^\nu c_i.
$$

O fechamento metrológico exige obter, sem usar dados de oscilação:

$$
\lambda_2=\frac{\chi_\nu^2}{2},
\qquad
\lambda_3=\frac{6\pi}{5},
\qquad
Z_\nu,
\qquad
\delta_{\rm CP},
\qquad
V_{\rm GDQ}(n_e).
$$

---

## 4. Cadeia correta de refinamento

1. Construir o background neutro admissível:

$$
\Phi_*^\nu=(g,J,H,f,\mathcal U)_\nu.
$$

2. Projetar a Hessiana oficial no setor neutro:

$$
K_{\rm neutro}^{\rm phys}
=
P_{\rm neutro}^{\rm phys}
\operatorname{Hess}\mathcal S_{\rm GDQ}
P_{\rm neutro}^{\rm phys}.
$$

3. Transportar o canal beta neutro para as três folhas leptônicas:

$$
\Psi_\alpha^{\rm folha}
=
\mathcal P_{\alpha e}\psi_{\bar\nu}.
$$

4. Calcular $G^\nu$ e $K^\nu$ por integrais ponderadas com $\mathcal U$.

5. Diagonalizar o problema generalizado:

$$
K^\nu c_i=\lambda_iG^\nu c_i.
$$

6. Obter a normalização global--local:

$$
m_i^2c^4=Z_\nu E_C^2\lambda_i.
$$

7. Calcular a fase CP como holonomia orientada neutra:

$$
\delta_{\rm CP}^{\rm GDQ}
=
\arg\operatorname{Hol}_{\Gamma_{\rm folhas}}
(\nabla^B_{\rm neutro}).
$$

8. Calcular a refração em meio como perturbação de impedância:

$$
J_{\rm meio}^{\rm clássico}
\to
\delta\Phi_{\rm meio}
\to
\Delta K_\nu^{\rm meio}
\to
V_{\rm GDQ}(n_e).
$$

---

## 5. Critério de sucesso

O refinamento será preditivo se:

1. $S_\nu$, $\lambda_2$, $\lambda_3$ e $Z_\nu$ forem calculados antes da
   comparação experimental;
2. a matriz $K^\nu$ for Hermitiana no produto $G^\nu$;
3. o espectro tiver três modos neutros estáveis;
4. as diferenças $\Delta m^2$ saírem sem ajuste posterior;
5. a fase CP e o potencial de meio forem obtidos por holonomia e impedância,
   não por importação de PMNS/MSW como axiomas.

---

## 6. Conclusão operacional

O refinamento não muda a conclusão da Q53. Ele apenas define o próximo nível de
precisão:

$$
\boxed{
\text{Q53 estruturalmente fechada; refinamento metrológico = Hessiana neutra 8D.}
}
$$

