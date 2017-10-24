import requests
import DictOfCryptoCurrencies as dict_crypt_curr

def main_menu():
    print("Please enter one of the following options:")
    print("Enter 1 to convert one crypto currency to another")
    print("Enter 2 to see a list of all the crypto currency available to convert")
    print("Enter 3 to terminate program")

    action = input()
    return int(action)

while(True):

    option = main_menu()
    if(option == 1):
        #print(dict_crypt_curr.key_in_dict_check("LiteCoin"))
        #print(dict_crypt_curr.key_in_dict_check("litecoin"))

        print("Please enter first currency by it's name or it's ticker name")
        currency1 = input()
        print("Enter how many", currency1, "you want to convert")
        currency1quantity = int(input())
        print("Pleas enter second currency by it's name or it's ticker name")
        currency2 = input()
        print(currency1, "and", currency2)

        API1 = "https://chainz.cryptoid.info/" + currency1 + "/api.dws?q=ticker.usd"
        API2 = "https://chainz.cryptoid.info/" + currency2 + "/api.dws?q=ticker.usd"

        currencyPriceOne = requests.get(API1).json()
        currencyPriceTwo = requests.get(API2).json()

        #print(currencyPriceOne, type(currencyPriceOne))


        quantityDifference = currencyPriceOne / currencyPriceTwo
        #print(quantityDifference)
        result = quantityDifference * currency1quantity

        print(currency1quantity, currency1, " = ", result, currency2)
        #print(currencyPriceOne, "and", currencyPriceTwo)

    elif(option == 2):
        dict_crypt_curr.print_dict()

    elif(option == 3):
        break

    else:
        print("I'm sorry, but that input is invalid. Please try again")
