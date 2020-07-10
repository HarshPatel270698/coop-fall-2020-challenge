class EventSourcer():
    # Do not change the signature of any functions
    def __init__(self):
        self.value = 0
        self.change_history = [self.value]
        self.change_counter = 0

    def add(self, num: int):
        self.value = self.value + num
        self.change_counter+=1
        self.change_history.append(self.value)
        return self.value

    def subtract(self, num: int):
        self.value = self.value - num
        self.change_counter+=1
        self.change_history.append(self.value)
        return self.value

    def undo(self):
        temp_counter = self.change_counter
        temp_counter-=1
        if temp_counter > self.change_counter:
            self.value = self.change_history[self.change_counter]
            return self.value
        else:
            print("No more acceptable undos")
            return self.value

    def redo(self):
        temp_counter = self.change_counter
        temp_counter+=1
        if temp_counter < self.change_counter:
            self.value = self.change_history[self.change_counter]
            return self.value
        else:
            print("No more acceptable redos")
            return self.value

    def bulk_undo(self, steps: int):
        temp_counter = self.change_counter
        temp_counter-=steps
        if temp_counter < self.change_counter:
            self.value = self.change_history[self.change_counter]
            return self.value
        else:
            print("Can't do undo for these many steps")
            return self.value

    def bulk_redo(self, steps: int):
        temp_counter = self.change_counter
        temp_counter+=steps
        if temp_counter < self.change_counter:
            self.value = self.change_history[self.change_counter]
            return self.value
        else:
            print("Can't do redo for these many steps")
            return self.value
