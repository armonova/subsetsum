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
Digite o número da opção do teste que você deseja realizar:
1. Executar todos os testes de sucesso do arquivo 'cases-success.json'
2. Executar todos os testes de erro do arquivo 'cases-error.json'
3. Inserir um novo problema manualmente
4. Finalizar o programa

```
Você pode escolher qualquer uma das opções acima para testar o programa.
1. A opção 1 irá rodar todos os códigos que estão listados no arquivo ```cases-success.json``` Obs.: todos os exemplos listados nesse arquivo **possuem** solução ótima.
2. A opção 2 irá rodar todos os códigos que estão listados no arquivo ```cases-error.json``` - Obs.: todos os exemplos listados nesse arquivo **não possuem** solução ótima.
3. Um novo menu será aberto para que o usuário possa inserir um problema manualmente
4. O programa ficará em loop até que o usuário digite o número 4

Obs. 1.: Para o teste de número ```2``` ainda não foi estipulado o tempo necessário para resolver todos os problemas do arquivo ```cases-error.json```. O último teste realizado executou por 21 horas e não obtever o resultado do últim teste do arquivo. 
Obs. 2: É possível alterar os arquivos ```cases-success.json``` e ```cases-error.json``` para inserção ou remoção de novos testes.

#### Para inserção de novos testes
Abra o arquivo ```cases-success.json``` e/ou ```cases-error.json```, para criar outros casos, basta adicionar o teste no arquivo - ou remover algum.
O teste a ser inserido deve seguir a seguinte estrutura:
```sh
{
    "weights": [
        30, 40, 10, 15, 10, 60, 54
    ],
    "target": 55,
    "expected": "True"
}
```
Explicação da estrutura:
* ```weights```: vetor de pesos a serem avaliados;
* ```target```: valor alvor que se deseja alcançar com a combinação dos pesos;
* ```expected```: para validação da resposta, o ```expected``` é a resposta esperada para o problema descrito.

### 3. Resultado
Se a opção ```1``` ou ```2``` forem selecionadas, os resultados serão salvos nos arquivos de texto ```result_success.txt``` e ```result_error.txt```, respectivamente. 
A solução de cada problema terá o formato da estrutrua abaixo:
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
Caso a opção escolhida no menu principal for a ```3. Inserir um novo problema manualmente```, o resultado aparecerá no console conforme a mesma estrutura mostrada acima.
