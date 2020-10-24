def answer_handler_yes(self):
    # Defining methods, taking argument as event of pressing buttons.
    if self.current_answer == 'ДА':
        # If condition returns True it changes properties of Label widget,
        # adds 20 scores and prints to user.
        self.lab8.config(text='Верно!', bg='green')
        self.game_scores
        self.game_scores += 20
        if self.game_scores > 500:
            # If condition returns True it changes properties of Label widget.
            self.lab8.config(text='Поздравляем! Вы выиграли!', bg='yellow', width=40)
        self.lab2.config(text=f'Очки: {self.game_scores}')
    else:
        # If condition returns False it changes properties of Label widget,
        # subtracts 30 scores and prints to the user.
        self.lab8.config(text='Неверно!', bg='red')
        self.game_scores
        self.game_scores -= 30
        if self.game_scores < 0:
            # If condition returns True it setting value to zero to avoid "-" sign.
            self.game_scores = 0
        self.lab2.config(text=f'Очки: {self.game_scores}')


def answer_handler_no(self):
    # Same result as above in answer_handler_yes() method.
    if self.current_answer == 'НЕТ':
        self.lab8.config(text='Верно!', bg='green')
        self.game_scores
        self.game_scores += 20
        if self.game_scores > 500:
            self.lab8.config(text='Поздравляем! Вы выиграли!', bg='yellow', width=40)
        self.lab2.config(text=f'Очки: {self.game_scores}')
    else:
        self.lab8.config(text='Неверно!', bg='red')
        self.game_scores
        self.game_scores -= 30
        if self.game_scores < 0:
            self.game_scores = 0
        self.lab2.config(text=f'Очки: {self.game_scores}')
