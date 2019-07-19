balance = { 
    'user1': 100,
    'user2': 500 
}

transactions = [ 
    {'user1': -10},
    {'user2': -20}, 
    {'user1': 50}, 
    {'user2': -20},
    {'user2': -100},
]

def calculateNewBalance(balance, transactions):
    for transaction in transactions:
        for key,val in transaction.items():
            user = key
            value = val
        balance[user] += value 
    return balance


newBalance = calculateNewBalance(balance, transactions)
print(newBalance)
