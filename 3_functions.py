#funtions definition
"""def hello(x="World"):
    print(f"Hello {x}")

hello()
hello(input("Enter your name:").strip().title().split()[1])"""
#functions in order
"""""
def main():
    hello()
    hello(input("enter your name: ").strip().title().split()[0])

def hello(x="World"):
    print(f"Hello {x}")

main()
"""
#functions with return values
def main():
    x=input("Enter a number: ")
    print(f"The square of {x} is", square(x))
#square = lambda x: int(x)**2
def square(x):
#    return(int(x)**2)
#    return(int(x)*int(x))
    return (pow(int(x), 2))
main()