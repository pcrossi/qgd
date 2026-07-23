# Saída — recuo, Hessiana magnética e Lamb Q48

## 1. Hiperfina: recuo cinemático fino

Classificação: avaliação direta reduzida. Este termo não é o recoil
completo de QED ligada; é a correção cinemática conservadora do contato
por curvatura finita de dois corpos.

- delta_rec^kin = -1.449290394263207e-08
- nu após a_e + Zemach = 1420427793.305935 Hz
- nu após a_e + Zemach + recuo cinemático = 1420427772.719811 Hz
- erro relativo após recuo cinemático = 1.550328262456269e-05

## 2. Hessiana magnética superior requerida

Classificação: diagnóstico de resíduo, não previsão. O número abaixo diz
qual elemento de matriz da Hessiana magnética superior deve ser produzido
quando os blocos K_YY, K_YI e K_II forem avaliados diretamente.

- fração requerida = -1.550304227659893e-05
- deslocamento requerido = -22020.951811 Hz
- delta_Z total requerido depois de a_e+recuo = -5.784843271738893e-05
- r_Z requerido = 1.531437205775 fm
- r_M efetivo requerido no mapa de casca = 1.456530981267 fm
- deslocamento r_M-r_p = +0.615752215817 fm

Forma GDQ:

$$
\Delta\nu_{\rm Hess}^{\rm mag}
=
\frac1h
\langle 1s|
P_{\rm mag}^{\dagger}
\Delta\mathsf R_{p}^{\rm mag,sup}
P_{\rm mag}
|1s\rangle.
$$

## 3. Lamb shift por deltaD_near

Classificação: diagnóstico de escala do operador de campo próximo.
Enquanto Delta R_p não for calculado diretamente, este valor não é
previsão GDQ.

- Lamb de referência usado para escala = 1057844000.000000 Hz
- Lamb de referência = 4.374891259184723e-06 eV
- tamanho finito H 2s já avaliado = 5.715065938836622e-10 eV
- deltaD_near requerido após tamanho finito = 4.374319752590839e-06 eV
- equivalente = 1057705810.320421 Hz

Forma GDQ:

$$
\Delta E_{\rm Lamb}
=
\langle 2s_{1/2}|\delta H_{\rm near}|2s_{1/2}\rangle
-
\langle 2p_{1/2}|\delta H_{\rm near}|2p_{1/2}\rangle.
$$

com

$$
\delta\mathcal D_{\rm near}
=
\Pi_{\rm spin}
(\mathsf R_p-\mathsf R_{\rm point})
\Pi_{\rm spin}.
$$
