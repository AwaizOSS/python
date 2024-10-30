import math

x = 99


def circle(pi, r=2):
    global x
    x = 12
    # global shouldnt be used normally as it ruins the dev experience by overwriting global variables that'll be unexpected for other devs
    # 2 acts as default value and it should be after argument with no default value
    return round(pi * r**2, 2), round(2 * pi * r, 2)


a, c = circle(r=3, pi=math.pi)

# lambda or anonymous function
cube = lambda x: x**3


def multiple_parameters(*args):
    # we can have anything in place of args but args is industry std and it actually is a tuple(print it to see) which means we can loop through it
    # sum is an in-built method
    return sum(args)


def multiple_key_value_parameters(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


# multiple_key_value_parameters(a="a", b="b")


# factory functions aka closures
def fun1():
    x = 10

    def fun2(y):
        return x * y

    return fun2


result = fun1()
print(result)
# here we are getting a function definition returned, but its not just definitioin. it also brings the variable from the scope it was called in, which in our case is the value of x. this is called backpacking
print(result(2))


# 9 write a generator function that yeilds even numbers up to a specified limit
def even_till(n):
    for x in range(2, n + 1, 2):
        # skips i number during iteration because of last argument, as the last parameter is never inclusive in python
        yield x


for i in even_till(11):
    print(i)
# the way we have defined the function, lets the function remember what last result it produced and continue from there for this particular loop
# print(i)
