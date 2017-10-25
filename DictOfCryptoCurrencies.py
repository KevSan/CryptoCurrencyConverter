from requests.structures import CaseInsensitiveDict
import requests


summary_api = "https://chainz.cryptoid.info/explorer/api.dws?q=summary#"
data_feed = requests.get(summary_api).json()

cid_of_crypto = CaseInsensitiveDict({data_feed[key]['name'] : key for key in data_feed})

def print_dict():
    for key in cid_of_crypto:
        print(key, ":", cid_of_crypto[key])

def key_in_dict_check(key):
    return(cid_of_crypto.__contains__(key))

def val_in_dict_check(val):
    return(val in cid_of_crypto.values())