#  decoraters in python
# dec function return function  and it takes functon as an arguments

def my_dec( func):
    def fm(*args,**kwargs):  # used when we wanna  pass the arguments in the function used . * args in tuple and ** kwargs for dictionary. other wisw donot use it 
        print("Hello good morning ")
        func( *args,**kwargs)
        print(" I am now outside the function")
    return fm

@my_dec
def hello():
    print("Hello world")
    
def add(a,b):
    print(a+b)
    
hello()
my_dec(add)(2,4)



#  Example
print("using decorators , example ")


def myfn(fun):
    def fn(*args,**kwargs):
        print("Good morning ")
        fun(*args,**kwargs)
        print("I am outside the function ")
        print(type(args))  # args is tuple
        print(type(kwargs))  # kwargs is dictionary
        
    return fn
@myfn
def name():
    print("Harry")
    
def sum(a,b):
    print(a+b)

name()
myfn (sum)(2,3)
