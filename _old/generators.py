def naturalNumberGen(n):
    num = 1
    while num <= n:
        yield num
        num += 1

""" for i in naturalNumberGen(10):
    print(i)

print(sum(naturalNumberGen(1000))) """


def csvSplitter(text: str):
    i = 0
    buffer = ''
    while i < len(text):
        if (text[i] == ','):
            result = buffer
            buffer = ''
            yield result
        else:
            buffer += text[i]
        i += 1


for word in csvSplitter('hello,world,monty,python'):
    print(word)