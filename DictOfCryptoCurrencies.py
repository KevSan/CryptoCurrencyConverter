import requests


summary_api = "https://chainz.cryptoid.info/explorer/api.dws?q=summary#"
data_feed = requests.get(summary_api).json()

dict_of_crypto = {data_feed[key]['name'].lower() : key for key in data_feed}

def print_dict():
    for key in dict_of_crypto:
        print(key, ":", dict_of_crypto[key])

def key_in_dict_check(key):
    return(dict_of_crypto.__contains__(key))

def val_in_dict_check(val):
    return(val in dict_of_crypto.values())