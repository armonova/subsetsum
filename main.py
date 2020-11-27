import json
import os
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


def tests_cases(test_cases, result_name):
    file_result = open(result_name, 'w')
    for index, test_case in enumerate(test_cases):
        w, i, t = test_case["weights"], len(test_case["weights"]) - 1, test_case["target"]
        file_result.write("T E S T E   N Ú M E R O :  " + str(index + 1))
        file_result.write("\nO problema tem as seguintes caracterísicticas:")
        file_result.write("\nVetor de pesos: " + str(w))
        file_result.write("\nTamanho do vetor: " + str(i + 1))
        file_result.write("\nValor alvo: " + str(t))
        file_result.write("\nResultado esperado: " + test_case["expected"])
        stat_pd = timer()
        return_prg_din = str(subset_sum_prog_din(w, i, t))
        end_pd = timer()
        total_time_pd = end_pd - stat_pd
        file_result.write("\n\nAlgorítmo de programação DINÂMICA\nResultado: " + str(return_prg_din))
        file_result.write("\nTempo de execução: " + str(round(total_time_pd, 2)) + "seg")

        stat_sb = timer()
        return_sb = str(subset_sum_recursive(w, i, t))
        end_sb = timer()
        total_time_sb = end_sb - stat_sb
        file_result.write("\n\nAlgorítmo RECURSIVO\nResultado: " + str(return_sb))
        file_result.write("\nTempo de execução: " + str(round(total_time_sb, 2)) + "seg")
        file_result.write("\n\n===========================\n")

    file_result.close()
    print("\n\nFim da execução. Aperte enter para voltar ao menu inicial")
    print("Os resultados foram salvos no arquivo " + result_name)
    input()


def test_manual(result_name):
    print("Digite cada elemento que deseja inserir no vetor de pesos")
    print(
        "Digite o número e aperte enter para adicionar, se deseja parar de adicionar, digite qualquer letra a aperte enter")
    w = []
    num = "0"
    while num.isnumeric():
        w.append(int(num))
        num = input()
    w.pop(0)
    i = len(w) - 1
    t = int(input("Digite o valor alvo: "))
    expected = input("Digite o resultado esperado: ")

    print("\n===========================")
    print("R E S O L U Ç Ã O")
    print("O problema tem as seguintes caracterísicticas:")
    print("Vetor de pesos: " + str(w))
    print("Tamanho do vetor: " + str(i + 1))
    print("Valor alvo: " + str(t))
    print("Resultado esperado: " + expected)
    stat_pd = timer()
    return_prg_din = str(subset_sum_prog_din(w, i, t))
    end_pd = timer()
    total_time_pd = end_pd - stat_pd
    print("\n\nAlgorítmo de programação DINÂMICA\nResultado: " + str(return_prg_din))
    print("Tempo de execução: " + str(round(total_time_pd, 2)) + "seg")

    stat_sb = timer()
    return_sb = str(subset_sum_recursive(w, i, t))
    end_sb = timer()
    total_time_sb = end_sb - stat_sb
    print("\nAlgorítmo RECURSIVO\nResultado: " + str(return_sb))
    print("Tempo de execução: " + str(round(total_time_sb, 2)) + "seg")
    print("===========================\n")

    print("Fim da execução. Aperte enter para voltar ao menu inicial")
    input()


loop = True

while loop:
    os.system('clear')
    print("Digite o número da opção do teste que você deseja realizar:")
    print("1. Executar todos os testes de sucesso do arquivo 'cases-success.json'")
    print("2. Executar todos os testes de erro do arquivo 'cases-error.json'")
    print("3. Inserir um novo problema manualmente")
    print("4. Finalizar o programa")
    choice = input()
    if int(choice) == 1:
        print("Processando...")
        result_name = "result_success.txt"
        json_file = open("cases-success.json")
        data = json.load(json_file)
        test_cases = data["test_cases"]
        json_file.close()
        tests_cases(test_cases, result_name)
    elif int(choice) == 2:
        print("Processando...")
        result_name = "result_error.txt"
        json_file = open("cases-error.json")
        data = json.load(json_file)
        test_cases = data["test_cases"]
        json_file.close()
        tests_cases(test_cases, result_name)
    elif int(choice) == 3:
        result_name = "result_manual.txt"
        test_manual(result_name)
    elif int(choice) == 4:
        loop = False
    else:
        pass
