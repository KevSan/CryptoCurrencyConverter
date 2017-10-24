import requests
import DictOfCryptoCurrencies as dict_crypt_curr

def main_menu():
    print("Please enter one of the following options:")
    print("Enter 1 to convert one crypto currency to another")
    print("Enter 2 to see a list of all the crypto currency available to convert")
    print("Enter 3 to terminate program")

    action = input()
    return int(action)

def input_check(input):
    if (dict_crypt_curr.key_in_dict_check(input) == False):
        print("Error Message")
    else:
        if (dict_crypt_curr.val_in_dict_check(input) == False):
            print("Error Message")

def converter():
    print("Please enter first currency by it's name or it's ticker name")
    first_currency = input()
    input_check(first_currency)
    print("Enter how many", first_currency, "you want to convert")
    first_currency_qnty = int(input())
    #place a check to make sure input is number

    print("Pleas enter second currency by it's name or it's ticker name")
    second_currency = input()
    print(first_currency, "and", second_currency)

    API1 = "https://chainz.cryptoid.info/" + first_currency + "/api.dws?q=ticker.usd"
    API2 = "https://chainz.cryptoid.info/" + second_currency + "/api.dws?q=ticker.usd"

    currencyPriceOne = requests.get(API1).json()
    currencyPriceTwo = requests.get(API2).json()


    quantityDifference = currencyPriceOne / currencyPriceTwo
    result = quantityDifference * first_currency_qnty
    print(first_currency_qnty, first_currency, " = ", result, second_currency)


while(True):

    option = main_menu()
    if(option == 1):
        converter()

    elif(option == 2):
        dict_crypt_curr.print_dict()

    elif(option == 3):
        break

    else:
        print("I'm sorry, but that input is invalid. Please try again")
