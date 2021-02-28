class myIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    # creaing iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            number = self.current
            self.current += 1
            return number
        raise StopIteration


new_iterator = myIterator(10, 20)
print(type(new_iterator))
for number in new_iterator:
    print(number)
