# Jogar Term.ooo

Script autônomo para jogar [term.ooo](term.ooo).

## Como funciona?
O jogo foi programado no arquivo [Wordle](Wordle.py) na classe Wordle, as [palavras](palavras.txt) são utilizadas tanto no jogo quanto na [função principal](main.py). 

Para o jogo autônomo, são basicamente eliminadas as palavras conforme o retorno dado pela função `guess` do jogo.

Devido aos acentos do Português, as palavras são normalizadas e os acentos são retirados. O dataset das palavras foi retirado do código do site já mencionado.

## Árvore de arquivos
```
.
├── LICENSE
├── main.py
├── palavras-wordle.txt
├── README.md
└── Wordle.py
```

## Exemplo de funcionamento
Diferente do jogo online, a cada execução é escolhida uma palavra aleatória do banco de palavras.

Quando o chute tem a letra na mesma posição da resposta, a saída é 0. 
Quando o chute tem a letra na mesma posição, mas em local diferente a saída é 1. 
Se o chute não possui a letra, a saída é 2.

```
1/6 - Chute: caubi
Você tentou: caubi
[2, 2, 2, 0, 2]
Removidas 10554 palavras de 10588

2/6 - Chute: jembe
Você tentou: jembê
[2, 2, 2, 0, 2]
Removidas 28 palavras de 34

3/6 - Chute: lobby
Você tentou: lobby
[2, 0, 0, 0, 0]
Removidas 5 palavras de 6

4/6 - Chute: hobby
Você tentou: hobby
[0, 0, 0, 0, 0]
Você ganhou em 4 de 6 tentativas!
```