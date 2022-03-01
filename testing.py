import math

def square(number):
    result = number * number
    return result

def hypotenuse(b, c):
    hyp = (b**2 + c**2)**0.5
    return hyp

def areaCircle(radius):
    area = math.pi * (radius**2)
    return area

if __name__ == '__main__':
    print("I'm being run directly")
    print(__name__)
    answer = square(5)
    print(answer)
