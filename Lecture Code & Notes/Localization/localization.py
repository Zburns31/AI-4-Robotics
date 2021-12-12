# p = [0.2, 0.2, 0.2, 0.2, 0.2]

n = 5
p = [1 / n for i in range(n)]

pHit = 0.6
pMiss = 0.2

prior = ["miss", "hit", "hit", "miss", "miss"]

posterior = [0, 0, 0, 0, 0]
for idx, val in enumerate(prior):
    print(idx, val)

    if val == "miss":
        posterior[idx] = p[idx] * pMiss
    else:
        posterior[idx] = p[idx] * pHit

total = sum(posterior)
for i in range(len(posterior)):
    posterior[i] = posterior[i] / total
