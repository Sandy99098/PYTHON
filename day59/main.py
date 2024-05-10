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
