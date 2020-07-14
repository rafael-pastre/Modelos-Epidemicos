import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
S = [100]
I = [1]
R = [0]

N = S[0] + I[0] + R[0]

beta = 0.47
gamma = 0.25

for j in range(0, T-1):
    S.append(S[j] - beta*S[j]*I[j]/N)
    I.append(I[j] + beta*S[j]*I[j]/N - gamma*I[j])
    R.append(R[j] + gamma*I[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('SIR sem dinâmica demográfica')
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.scatter(t, R, marker='o', s=2)
plt.legend(['S', 'I', 'R'])
plt.savefig('FiguraSIR.png')
plt.show()