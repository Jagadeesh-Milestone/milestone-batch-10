#function as an argument value:
def d1(text):
    return text.upper()

def d2(text):
    return text.lower()

def d3(func):
    result=func('Hello World')
    print(result)

d3(d1)
d3(d2)