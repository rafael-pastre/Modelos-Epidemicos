import matplotlib.pyplot as plt

T = 100             # total time

t = range(0, T)
S = [100]
I = [1]

N = S[0] + I[0]

beta = 0.52
gamma = 0.25

for j in range(0, T-1):
    S.append(S[j] - beta*S[j]*I[j]/N + gamma*I[j])
    I.append(I[j] + beta*S[j]*I[j]/N - gamma*I[j])

plt.xlabel('Tempo')
plt.ylabel('Número de indivíduos')
plt.title('SIS')
plt.scatter(t, S, marker='o', s=2)
plt.scatter(t, I, marker='o', s=2)
plt.legend(['S', 'I', 'S'])
plt.savefig('FiguraSIS.png')
plt.show()