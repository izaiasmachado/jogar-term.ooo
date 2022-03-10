from Wordle import Wordle
from random import randint

def filter_words(words, guess, accuracy):
    filtered_words = []
    
    for word in words:    
        usable = True

        for i in range(5):
            c = guess[i]

            if accuracy[i] == 0:
                if c != word[i]:
                    usable = False

            if accuracy[i] == 1:
                if c == word[i] or not(c in word):
                    usable = False

            if accuracy[i] == 2:
                if c in word:
                    usable = False
        
        if usable:
            filtered_words.append(word)

    return filtered_words

def play():
    game = Wordle(6)
    finished = False
    tries = 1
    total_tries = game.total_tries
    words = game.norm_words

    while not(finished):
        random_index = randint(0, len(words) - 1)
        guess = words[random_index]
        print('{}/{} - Chute: {}'.format(tries, total_tries, guess))

        try: 
            response = game.guess(guess)
            print('Você tentou: {}'.format(response['tried_word']))
            print('{}'.format(response['guess_accuracy']))
            
            status = game.get_game_status()
            finished = status['finished']
            tries = status['number_of_tries'] + 1

            # print('Caracteres removidos: {}'.format(status['removed_caracters']).join(', '))

            if not(finished):
                filtered = filter_words(words, guess, response['guess_accuracy'])
                print('Removidas {} palavras de {}'.format(len(words) - len(filtered), len(words)))
                words = filtered
                print('')


        except Exception as e:
            print('Erro: {}'.format(e))
            print('Tente novamente ;)')

    status = game.get_game_status()

    if status['won']:
        print('Você ganhou em {} de {} tentativas!'.format(status['number_of_tries'], total_tries))
    else:
        print('Você perdeu ;/')
        print('A palavra era {}!'.format(status['answer']))

play()