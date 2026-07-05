### Complexificação do Momentum e a 1-Forma de Kähler

No formalismo geométrico adotado, definimos o espaço-tempo como uma variedade de Kähler equipada com uma métrica hermitiana complexa $\tilde{g}_{\mu\nu} = g_{\mu\nu} + iB_{\mu\nu}$ e uma conexão afim de Cartan contendo uma torção topológica irredutível $T^\lambda_{\mu\nu}$. Sob essa estrutura, o campo da matéria (solíton hidrodinâmico) deixa de ser modelado por amplitudes abstratas em um espaço de Hilbert e passa a ser descrito em sua representação polar clássica pelo fluido:
$$\Psi(z) = \sqrt{\rho(z)} e^{\frac{i}{\hbar} S_R(z)},$$
onde $\rho(z)$ representa a densidade volumétrica de probabilidade do fluido do vácuo e $S_R(z)$ denota a Ação Real, identificada fisicamente como a Função Principal de Hamilton.

Para unificar a dinâmica estatística difusiva e a inércia direcional do campo em um único objeto geométrico contínuo, mapeamos de forma isomórfica essa função de onda na Ação Complexa Unificada $S_C$ por meio de uma relação exponencial pura:
$$\Psi(z) = e^{\frac{i}{\hbar} S_C(z)}.$$
Igualando ambas as representações com o objetivo de isolar o funcional de ação complexificado, estabelece-se o vínculo:
$$e^{\frac{i}{\hbar} S_C} = \sqrt{\rho} e^{\frac{i}{\hbar} S_R}.$$
Aplicando a continuação analítica do logaritmo complexo em ambos os membros da equação, obtemos a separação de componentes:
$$\frac{i}{\hbar} S_C = \ln\left(\rho^{1/2}\right) + \frac{i}{\hbar} S_R.$$
Multiplicando toda a expressão por $-i\hbar$ para purificar o termo linear de translação, a álgebra opera a extração direta de $S_C$:
$$S_C = S_R - i\hbar \ln\left(\rho^{1/2}\right) = S_R - i \frac{\hbar}{2} \ln\rho.$$
Ao definirmos a componente imaginária da ação — associada diretamente ao potencial osmótico e aos termos de difusão estocástica do vácuo — como $S_I = -\frac{\hbar}{2} \ln\rho$, a estrutura se consolida de forma limpa na decomposição linear canônica:
$$S_C = S_R + i S_I.$$
A extensão das variáveis de momentum para a 1-forma complexa $\omega$ emerge naturalmente ao aplicarmos o operador de derivada exterior covariante $\nabla_\mu$ sobre a ação unificada $S_C$. Este operador atua acoplado de forma compulsória à conexão afim assimétrica com torção de Cartan, blindando a integrabilidade do campo ao longo das geodésicas complexas da variedade:
$$\omega = p_\mu dx^\mu = \nabla_\mu S_C \, dx^\mu = \nabla_\mu \left( S_R - i \frac{\hbar}{2} \ln\rho \right) dx^\mu.$$
Distribuindo o operador de diferenciação linear pelas parcelas real e imaginária do funcional, temos:
$$\omega = \left( \nabla_\mu S_R \right) dx^\mu - i \frac{\hbar}{2} \left( \nabla_\mu \ln\rho \right) dx^\mu.$$
Aplicando a regra da cadeia ao gradiente logarítmico que dita o perfil cinético da densidade ($\nabla_\mu \ln\rho = \frac{1}{\rho} \nabla_\mu \rho$), a forma expandida final da 1-forma estabelece-se rigorosamente por:
$$\omega = \nabla_\mu S_R \, dx^\mu - i \frac{\hbar}{2\rho} \nabla_\mu \rho \, dx^\mu.$$
Substituindo as variáveis dinâmicas fundamentais do fluido — onde identificamos o momentum mecânico clássico de corrente (responsável pelo transporte balístico regular) como $p_\mu^{\text{c}} = \nabla_\mu S_R$ e o momentum osmótico de flutuação em direção ao equilíbrio como $u_\mu = -\frac{\hbar}{2\rho} \nabla_\mu \rho$ —, a 1-forma assume sua assinatura canônica complexa unificada:
$$\omega = (p^{\text{c}}_\mu + i u_\mu) dx^\mu.$$
O termo osmótico $i u_\mu$ não constitui uma parcela adicionada exteriormente à 1-forma, mas sim a componente imaginária intrínseca do próprio vetor de momentum complexificado $p_\mu = p_\mu^{\text{c}} + i u_\mu$. Esta dedução demonstra que a oscilação quântica e a densidade estatística não operam de maneira disjunta; o momentum do fluido encontra-se intrinsicamente acoplado à torção geométrica do espaço-tempo local, provando que o "giro" abstrato da fase quântica mapeia-se como um micro-torcimento estrutural contínuo do próprio tecido métrico ao longo do trajeto do solíton.
