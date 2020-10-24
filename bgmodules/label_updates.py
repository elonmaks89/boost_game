from random import *

# Setting dictionary with meaning words.
dct = {
    1:'красный',
    2:'оранжевый',
    3:'желтый',
    4:'зеленый',
    5:'голубой',
    6:'синий',
    7:'фиолетовый'
    }

# Setting dictionary with colors of meaning words.
dct_2 = {
    1:'#ff0000',
    2:'#ff7d00',
    3:'#ffff00',
    4:'#00ff00',
    5:'#007dff',
    6:'#0000ff',
    7:'#7d00ff'
    }

# Updating First Main Label for the random text of meaning word.
def update_label_1(self):
    # Setting random values to variable from 1 to 7.
    self.rand_num_1 = randint(1,7)
    # Iterates through every item keys in dct dictionary.
    for i in dct.keys():
        # Stops iterating if score value reaches 500 (You win) and if time count is equals 3.
        if self.game_scores > 500 and self.counter == 3:
            break
        # Getting value of dct item keys and changing label properties if it matches
        # at least to one random number. Checking it every 3 seconds.
        if i == self.rand_num_1:
            self.lab5.config(text=dct.get(i))
            self.lab8.config(text='?', bg='white')
            # If random number of the First Main Label is equals to random number of the Fourth Main Label
            # then it is the right answer and we save it to current_answer variable.
            if self.rand_num_1 == self.rand_num_4:
                self.current_answer = 'ДА'
            else:
                self.current_answer = 'НЕТ'
                
# Updating First Main Label for the random color of the text of meaning word.
def update_label_2(self):
    self.rand_num_2 = randint(1,7)
    for i in dct_2.keys():
        if self.game_scores > 500 and self.counter == 3:
            break
        if i == self.rand_num_2:
            self.lab5.config(fg=dct_2.get(i))
            self.lab8.config(text='?', bg='white')
        
# Updating Second Main Label for the random text of meaning word.
def update_label_3(self):
    self.rand_num_3 = randint(1,7)
    for i in dct.keys():
        if self.game_scores > 500 and self.counter == 3:
            break
        if i == self.rand_num_3:
            self.lab6.config(text=dct.get(i))
            self.lab8.config(text='?', bg='white')

# Updating Second Main Label for the random color of the text of meaning word.
def update_label_4(self):
    # Setting random values to variable from 1 to 7.
    self.rand_num_4 = randint(1,7)
    # Iterates through every item keys in dct dictionary.
    for i in dct_2.keys():
        # Stops iterating if score value reaches 500 (You win) and if time count is equals 3.
        if self.game_scores > 500 and self.counter == 3:
            break
        # Getting value of dct item keys and changing label properties if it matches
        # at least to one random number. Checking it every 3 seconds.
        if i == self.rand_num_4:
            self.lab6.config(fg=dct_2.get(i))
            self.lab8.config(text='?', bg='white')
            # If random number of the First Main Label is equals to random number of the Fourth Main Label
            # then it is the right answer and we save it to current_answer variable.
            if self.rand_num_1 == self.rand_num_4:
                self.current_answer = 'ДА'
            else:
                self.current_answer = 'НЕТ'
