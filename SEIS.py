import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
S = [100]
E = [1]
I = [1]

N = [S[0] + E[0] + I[0]]

beta = 0.55
gamma = 0.27
mu = 0.002
Lambda = 0.57
alpha = 0.2

for j in range(0, T-1):
    S.append(S[j] + Lambda - mu*S[j] - beta*S[j]*I[j]/N[j] + gamma*I[j])
    E.append(E[j] + beta*S[j]*I[j]/N[j] - (mu+alpha)*E[j])
    I.append(I[j] + alpha*E[j] -(gamma+mu)*I[j])
    N.append(S[j] + E[j] + I[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('SEIS')
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, E, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.legend(['S', 'E', 'I'])
plt.savefig('FiguraSEIS.png')
plt.show()