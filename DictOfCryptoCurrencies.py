from requests.structures import CaseInsensitiveDict

cid_of_crypto = CaseInsensitiveDict({"LiteCoin" : "ltc",
                             "Dash" : "dash",
                             "BitConnect Coin": "bcc",
                             "Koruna" : "koruna",
                             "Wexcoin" : "wex",
                             "e-Coin" : "ecn",
                             "Blocknet Old Chain" : "block-old",
                             "Stratis" : "strat",
                             "PIVX" : "pivx",
                             "BitCore" : "btx",
                             "Blocknet" : "block",
                             "SysCoin 2.1" : "sys",
                             "Capricoin" : "cpc",
                             "DigiByte" : "dgb",
                             "PURA" : "pura",
                             "Particl" : "part",
                             "NavCoin" : "nav",
                             "Sprouts" : "sprts",
                             "I/O Coin" : "ioc",
                             "Grantcoin" : "grt",
                             "ZCoin" : "xzc",
                             "PeerCoin" : "ppc",
                             "ViaCoin" : "via",
                             "Rubycoin" : "rby",
                             "Ion" : "ion",
                             "CROWN" : "crw",
                             "BitBay" : "bay",
                             "AsiaCoin" : "ac",
                             "MonetaryUnit" : "mue",
                             "EnergyCoin" : "enrg",
                             "Diamond" : "dmd",
                             "PotCoin" : "pot",
                             "Mooncoin" : "moon",
                             "Einsteinium" : "emc2",
                             "Experience Points" : "xp",
                             "BlackCoin" : "blk",
                             "Unobtanium" : "uno",
                             "OKCash" : "ok",
                             "Transfercoin" : "tx",
                             "Radium" : "rads",
                             "iXcoin" : "ixc",
                             "VeriCoin" : "vrc",
                             "BitCloud" : "btdx",
                             "BitSend" : "bsd",
                             "Gambit" : "gam",
                             "Groestlcoin" : "grs",
                             "SolarCoin" : "slr",
                             "Neoscoin" : "neos",
                             "Spectrecoin" : "xspec",
                             "B3Coin" : "b3",
                             "XCurrency" : "xc",
                             "PinkCoin" : "pink",
                             "EquiTrader" : "eqt",
                             "GoldCoin" : "gld",
                             "CureCoin" : "cure",
                             "Karma" : "karm",
                             "Global Currency Reserve" : "gcr",
                             "ECCoin" : "ecc",
                             "BitBean" : "bitb",
                             "Dnotes" : "note",
                             })

def print_dict():
    for key in cid_of_crypto:
        print(key, ":", cid_of_crypto[key])

def key_in_dict_check(key):
    return(cid_of_crypto.__contains__(key))

def val_in_dict_check(val):
    return(val in cid_of_crypto.values())
    #must be lower case letter

