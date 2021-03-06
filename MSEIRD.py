import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
M = [0]
S = [100]
E = [1]
I = [1]
R = [0]
D = [0]

N = [M[0] + S[0] + E[0] + I[0] + R[0] + D[0]]

beta = 1.15
gamma = 0.5
mu = 0.002
Lambda = 0.27
delta = 0.05
alpha = 0.25
epsilon = 0.017

for j in range(0, T-1):
    M.append(M[j] + Lambda -delta*M[j] -mu*M[j])
    S.append(S[j] + delta*M[j] - beta*S[j]*I[j]/N[j] -mu*S[j])
    E.append(E[j] + beta*S[j]*I[j]/N[j] - (mu+alpha+epsilon)*E[j])
    I.append(I[j] + alpha*E[j] -(gamma+mu)*I[j])
    R.append(R[j] + gamma*I[j] -mu*R[j])
    D.append(D[j] + epsilon*I[j])
    N.append(M[j] + S[j] + E[j] + I[j] + R[j] + D[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('MSEIRD')
plt.scatter(t, M, marker='o', s=2)
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, E, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.scatter(t, R, marker='o', s=2)
plt.scatter(t, D, marker='o', s=2)
plt.legend(['M', 'S', 'E', 'I', 'R', 'D'])
plt.savefig('FiguraMSEIRD.png')
plt.show()