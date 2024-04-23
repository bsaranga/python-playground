class MyIterator:
    def __init__(self, start, end) -> None:
        self.current = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.end:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration
        

my_iterator = MyIterator(1,6)

for i in my_iterator:
    print(i)