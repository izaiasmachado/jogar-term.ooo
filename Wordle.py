import unicodedata
import unidecode

import string
from random import randint

class Wordle:
    def norm(self, word):
        if word:       
            norm_word = unicodedata.normalize('NFKD', word).lower()
            unaccented_string = unidecode.unidecode(norm_word)
            return unaccented_string           

    def load_words(self):
        file = open('palavras.txt', mode='r')

        all_text = file.read()
        file.close()

        self.words = all_text.split(',')
        self.normalize_words()

    def normalize_words(self):
        self.norm_words = []
        for word in self.words:  
            norm_word = self.norm(word)

            if norm_word:
                self.norm_words.append(norm_word)

    def define_answer(self):
        lexic_length = len(self.norm_words)
        random_index = randint(0, lexic_length)
        
        self.answer = self.norm_words[random_index]

    def __init__(self, total_tries=6):
        self.load_words()
        self.define_answer()

        self.total_tries = total_tries
        self.won = False
        self.finished = False

        self.tries = []
        self.guesses_accuracy = []
        
        self.available_caracters = list(string.ascii_lowercase)
        self.removed_caracters = []
        
    def get_available_caracters(self):
        return self.available_caracters

    def remove_caracter_from_list(self, caracter):
        if caracter in self.available_caracters:
            index = self.available_caracters.index(caracter)

            removed_caracter = self.available_caracters[index]
            self.removed_caracters.append(removed_caracter)

            del self.available_caracters[index]

    def validate_caracters(self, word):
        for c in word:
            if not(c in self.available_caracters):
                raise Exception('A palavra possui caracteres já eliminados')

    def guess(self, word):
        if self.finished:
            raise Exception('O jogo já acabou!')

        guess_accuracy = []

        if len(word) != 5:
            raise Exception('A palavra tem que ter 5 letras ;)')

        self.validate_caracters(word)

        if not(word in self.norm_words):
            raise Exception('Palavra não existe')

        word_index = self.norm_words.index(word)
        tried_word = self.words[word_index]

        self.tries.append(tried_word)

        for index in range(5):
            right_caracter = self.answer[index]
            guessed_caracter = word[index]

            if right_caracter == guessed_caracter:
                guess_accuracy.append(0)

            elif self.answer.find(guessed_caracter) != -1:
                guess_accuracy.append(1)

            else:
                guess_accuracy.append(2)
                self.remove_caracter_from_list(guessed_caracter)

        self.guesses_accuracy.append(guess_accuracy)
        self.update_game_status()

        return { 'tried_word': tried_word, 'guess_accuracy': guess_accuracy }        

    def update_game_status(self):
        number_of_tries = len(self.tries)
        run_out_of_tries = number_of_tries == self.total_tries

        if len(self.guesses_accuracy) >= 1:
            self.won = self.guesses_accuracy[-1] == [0, 0, 0, 0, 0]
        
        self.finished = self.won or run_out_of_tries

    def get_game_status(self):
        self.status = {
            'won': self.won,
            'finished': self.finished,
            'tries': self.tries,
            'number_of_tries': len(self.tries),
            'available_caracters': self.available_caracters,
            'removed_caracters': self.removed_caracters,
        } 

        if (self.finished): 
            self.status['answer'] = self.answer

        return self.status