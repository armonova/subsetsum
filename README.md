# Problema da Soma dos Subconjuntos: Solução Baseada em Programação Dinâmica e Recursividade
##### Arthur Novaes, Vinícius França e Gustavo Zille

Este repositório possui os códigos para o trabalho final da disciplina de Otmização 

Neste projeto contem os seguintes arquivos:
* ```main.py```: arquivo com o programa em Python;
* ```cases.json```: arquivo com os problemas testados (é possível a inserção de novos testes no arquivo);
* ```results.txt```: arquivo com os resultados apresentados no trabalho.



# Para executação do código é necessário seguir os seguintes passos:
### 1. Rodar o código
Obs.: É necessário ter o python3 instalado
```sh
$ python3 main.py
```

### 2. Aparecerá uma mensagem do tipo
```sh
Digite o número do problema que você quer resovler:
```
Consulte o arquivo ```cases.json``` para escolher o problema que se deseja resolver. É possível criar outros casos, basta adiciona-lo no arquivo.
Como resposta da pergunta acima, deve ser inserido um número que coorresponde à posição do vetor em que o problema se encontra no arquivo ```cases.json``` dentro do objeto ```test_cases```, ou seja, a o primeiro teste, descrito abaixo, está na posição ```0``` do vetor ```test_cases```
```sh
{
    "weights": [
        30, 40, 10, 15, 10, 60, 54
    ],
    "target": 55,
    "expected": "True"
}
```
A estrutura do teste é a sguinte:
* ```weights```: vetor de pesos a serem avaliados;
* ```target```: valor alvor que se deseja alcançar com a combinação dos pesos;
* ```expected```: para validação da resposta, o ```expected``` é a resposta esperada para o problema descrito.

### 3. Resultado
Após a inserção do número do teste a ser validado, será exibido o resultado das consultas para o algorítimo recursivo e da programação dinâmica como o exemplo abaixo:
```sh
O problema selecionado tem as seguintes caracterísicticas:
Vetor de pesos: [30, 40, 10, 15, 10, 60, 54]
Tamanho do vetor: 6
Valor alvo: 55
Resposta esperada: True

Algorítmo de programação dinâmica: True
Tempo de execução: 0.0seg

Algorítmo recursivo: True
Tempo de execução: 0.0seg
```

