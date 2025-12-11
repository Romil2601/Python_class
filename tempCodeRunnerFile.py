class MyIterator:
    def __init__(self, data):
        self.data = data
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.data):
            value = self.data[self.i]
            self.i += 1
            return value
        else:
            raise StopIteration


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in MyIterator(nums):
    print(n)