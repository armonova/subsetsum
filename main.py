import json
from timeit import default_timer as timer


# https://www.youtube.com/watch?v=ehrJjRHCBvY
# https://www.ime.usp.br/~pf/analise_de_algoritmos/aulas/mochila-subsetsum.html
# https://www.youtube.com/watch?v=ZprpEfLCIfk


def subset_sum_recursive(weights, iteration, target):
    if iteration == 0:
        if target == 0:
            return True
        return False
    b = subset_sum_recursive(weights, iteration - 1, target)
    if b is False and weights[iteration] <= target:
        b = subset_sum_recursive(weights, iteration - 1, target - weights[iteration])
    return b


def subset_sum_prog_din(weights, iteration, target):
    t = [[0 for x in range(target + 1)] for y in range(iteration + 1)]
    for i in range(iteration + 1):
        t[i][0] = True
    for j in range(1, target + 1):
        t[0][j] = False
        for i in range(1, iteration + 1):
            b = t[i - 1][j]
            if b == 0 and weights[i] <= j:
                b = t[i - 1][j - weights[i]]
            t[i][j] = b
    return t[iteration][target]


json_file = open("cases.json")
data = json.load(json_file)
test_cases = data["test_cases"]
json_file.close()
num = int(input("Digite o número do problema que você quer resovler: "))
w, i, t = test_cases[num]["weights"], len(test_cases[num]["weights"]) - 1, test_cases[num]["target"]

print("\nO problema selecionado tem as seguintes caracterísicticas:")
print("Vetor de pesos: " + str(w))
print("Tamanho do vetor: " + str(i))
print("Valor alvo: " + str(t))
print("Resposta esperada: " + test_cases[num]["expected"])
stat_pd = timer()
return_prg_din = str(subset_sum_prog_din(w, i, t))
end_pd = timer()
total_time_pd = end_pd - stat_pd
print("\nAlgorítmo de programação dinâmica: " + str(return_prg_din))
print("Tempo de execução: " + str(round(total_time_pd, 2)) + "seg")

stat_sb = timer()
return_sb = str(subset_sum_recursive(w, i, t))
end_sb = timer()
total_time_sb = end_sb - stat_sb
print("\nAlgorítmo recursivo: " + str(return_sb))
print("Tempo de execução: " + str(round(total_time_sb, 2)) + "seg")
