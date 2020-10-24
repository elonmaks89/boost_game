# 3 seconds time count for one answer. Counts time from 1 to 3.
def count(self):
    self.counter += 1
    if self.counter == 4:
        self.counter = 1
    self.lab4.config(text=f'Время: {str(self.counter)}')
