import requests
import pandas as pd #so far not needed

# pip install requests
# pip install wheel
# pip install pandas




print("Enter first currency ticker name")
currency1 = input()
print("Enter how many", currency1, "you want to convert")
currency1quantity = int(input())
print("Enter second currency ticker name")
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