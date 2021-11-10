
################SETS#############################
A = {2, 4, 6, 8}
B = {4, 10}
sym_diff = A.symmetric_difference(B)
print(f'Symmetric difference: {sym_diff}')


ad1_id = {'001', '002', '003'}
ad2_id = {'002', '003', '007'}
result = ad1_id.symmetric_difference(ad2_id)
print(f'Selected ID: {result}')

is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}
result = is_clicked.intersection(is_bought)
print(f'Customer ID: {result}')
###########################Tuple################################################
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = dji1 + dji2
print(result)

dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
result = (dji1, dji2)
print(result)

members = (('Kate', 23), ('Tom', 19))
members = (members[0], ('John', 26), members[1])
print(members)

default = ('YES', 'NO', 'NO', 'YES', 'NO')
print(f"Number of occurrences: {default.count('YES')}")

names = ('Monica', 'Tom', 'John', 'Michael')
sorted_names = tuple(sorted(names))
print(sorted_names)
print(type(sorted_names))

info = (('Monica', 19), ('Tom', 21), ('John', 18))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Ascending: {asc}')
print(f'Descending: {desc}')

stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
print(stocks[0][1][1])

#############################################List###########################################
cities = ['Los Angeles', 'New York', 'Chicago']
cities.append('Houston')
print(cities)

idx = ['001', '002', '001', '003', '001']
print(f"Number of occurrences: {idx.count('001')}")

text = 'Python programming'
text = text.lower()
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters)

filenames = ['view.jpg', 'bear.jpg', 'ball.png']
filenames.insert(0, 'phone.jpg')
filenames.remove('ball.png')
print(filenames)

day1 = ['3984', '9042', '4829', '2380']
day2 = ['4231', '5234', '1345', '2455']
day1.extend(day2)
print(day1)

hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))

#######################################Dictionary#############################

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals)

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.keys())


capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.values())

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
    }
print(capitals.items())

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}
print(capitals.get('Austria'))


stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks['AAPL.US'])

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
print(stocks['MSFT.US']['Microsoft Corp'])


stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks['MSFT.US']['Microsoft Corp'] = 190
print(stocks['MSFT.US'])

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}
stocks['V.US'] = {'Visa Inc': 185}
print(stocks.values())

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]
print(list(enumerate(tickers)))

project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

result = list(set(project_ids.values()))
result.sort()
print(result)

stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
del stats['traffic']
print(stats)

users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
print(users.get('004', 'indefinite'))

############################For########################
result = []
for i in range(10, 100):
    if i % 11 == 0:
        result.append(str(i))
print(','.join(result))

result = []
for i in range(10, 100):
    if i % 11 == 0 and i % 3 != 0:
        result.append(str(i))
print(','.join(result))

items = [1, 3, 4, 5, 6, 9, 10, 17, 23, 24]
result = []
for item in items:
    if not item % 2 != 0:
        result.append(item)
print(result)

items = [1, 5, 3, 2, 2, 4, 2, 4]
result = []

for item in items:
    if not item in result:
        result.append(item)

print(result)

text = 'Python is a very popular programming language'

words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []

for prob in probabilities:
    if prob > 0.5:
        result.append(prob)

print(result)

probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = []

for prob in probabilities:
    if prob > 0.5:
        result.append(1)
    else:
        result.append(0)

print(result)

items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1

print(freq)

text = """Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else"""

words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 6]
print(words)

indexes = [
    'BOVESPA', 'DOW JONES COMP', 'DOW JONES INDU',
    'DOW JONES TRANS', 'DOW JONES UTIL', 'IPC',
    'IPSA', 'MERVAL', 'NASDAQ COMP', 'NASDAQ100',
    'S&P500', 'S&P/TSX COMP'
]

for index in indexes:
    if 'DOW' in index or 'S&P' in index:
        print(index)

gaming = {
    '11B': 362.5,
    'CDR': 297.0,
    'CIG': 0.85,
    'PLW': 318.0,
    'TEN': 300.0
}

for ticker, close in gaming.items():
    if close > 100.0:
        print(ticker)

names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')

names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']
for name in names:
    if name.isalnum():
        print(f'Hello {name}')


def maximum(x, y):
    if x >= y:
        return x
    else:
        return y

def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z

def multi(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)

def filter_ge_6(words):
    result = []
    for word in words:
        if len(word) >= 6:
            result.append(word)
    return result

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            total += 1
    return total

def count_str(items):
    total = 0
    for item in items:
        if isinstance(item, str):
            if len(item) > 2:
                total += 1
    return total

def remove_duplicates(items):
    return list(set(items))

def is_distinct(items):
    return len(items) == len(set(items))


def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)


function(3)
function(5, ['a', 'b', 'c'])
function(6)

def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False

filename = 'view.jpg'
print(filename[-3:])

filename = 'view.jpg'
print(filename[5:])

string = 'PKV-89415-PLN'
code = string[:3] + string[-3:]
print(code)


def search(search_str, item_str):
    found = False
    for i in range(0, len(search_str)):
        location_counter = 0
        location = 0
        for j in range(0, len(item_str)):
            print(f"i,j:{i}{j}")
            print(f"BOOL{found}")
            print(f"location_counter{location_counter}")

            if item_str[j] == search_str[i]:
                location_counter += 1
                if location_counter == len(search_str):
                    found = True
            else:
                found = False
                location_counter = 0
        if found == True:
            break
    return found


print(search("hay stack needle hay stack", "needle"))