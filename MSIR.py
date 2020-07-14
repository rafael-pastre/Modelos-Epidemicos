import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
M = [0]
S = [100]
I = [1]
R = [0]

N = [M[0] + S[0] + I[0] + R[0]]

beta = 0.55
gamma = 0.27
mu = 0.002
Lambda = 0.27
delta = 0.04

for j in range(0, T-1):
    M.append(M[j] + Lambda -delta*M[j] -mu*M[j])
    S.append(S[j] + delta*M[j] - beta*S[j]*I[j]/N[j] -mu*S[j])
    I.append(I[j] + beta*S[j]*I[j]/N[j] - gamma*I[j] -mu*I[j])
    R.append(R[j] + gamma*I[j] -mu*R[j])
    N.append(M[j] + S[j] + I[j] + R[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('MSIR')
plt.scatter(t, M, marker='o', s=2)
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.scatter(t, R, marker='o', s=2)
plt.legend(['M', 'S', 'I', 'R'])
plt.savefig('FiguraMSIR.png')
plt.show()