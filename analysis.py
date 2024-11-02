def print_hello():
    """print 'my fist function' """
    print("my first function")


def input_int_number():
    """input an int from thr user until it is valid """
    x: int = 0
    while True:
        try:
            x = int(input("enter a number"))
            break
        except:
            print("must be int")


print("analysis:", __name__)
