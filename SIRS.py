import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
S = [100]
I = [1]
R = [0]

N = [S[0] + I[0] + R[0]]

beta = 0.52
gamma = 0.25
mu = 0.002
Lambda = 0.27
f = 0.05

for j in range(0, T-1):
    S.append(S[j] + Lambda - beta*S[j]*I[j]/N[j] -mu*S[j] +f*R[j])
    I.append(I[j] + beta*S[j]*I[j]/N[j] - gamma*I[j] -mu*I[j])
    R.append(R[j] + gamma*I[j] - mu*R[j] - f*R[j])
    N.append(S[j] + I[j] + R[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('SIRS')
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.scatter(t, R, marker='o', s=2)
plt.legend(['S', 'I', 'R'])
plt.savefig('FiguraSIRS.png')
plt.show()