# global scope
x = 500

drive_key = "ABCD PQRS 1234"

def do_something():
    # print strings
    # I want to increment this x value to 600
    # and use the latest 600 value throughout the script
    global x
    print("value before intro", x)
    x = x + 100
    print("latest value", x)


do_something()
# here after the value of x is 600

print(x)


# example 1
def find_tax(tax_percent):
    # add tax_percent to the x value and return it
    # for e.g. if 18
    # 600 * 18/100
    global x
    print("base price is ", x)
    answer = x * tax_percent / 100
    print(answer)


find_tax(18)


def read_data_from_pendrive(passcode):
    global drive_key

    if passcode == drive_key:
        # allow access
        pass
    else:
        return "Prohibited"
