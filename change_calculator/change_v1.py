'''
Change calculator using greedy algorithm method; an approach for solving a problem by selecting the best option available at the moment.
- Quick to implement
- Optimal solution with minimal resources or knowledge

Application
- Scheduling start and end times to get best efficiency (activity selection problem)
- weighted importance by frequent used items for efficiency (huffman coding)
- coin change problem (portfolio optimization)

1. Prompt for user input where change is > 0
2. Using a top down approach deduct change according to highest to lowest value
3. Return amount of coins 
'''
quarter = 25
dime = 10
nickel = 5
penny = 1
i = 0
res = {}

def calculate_quarter(cents, coin):
    global i
    while cents >= coin:
        i += 1
        cents -= coin
    res[coin] = i
    return cents

while True:
    try:
        cents = int(input("Enter amount of change in cents: "))
        if cents < 0:
            print("Please return a valid number")
        else:
            break
    except ValueError:
        print("Please provide an integer")

i = 0
cents = calculate_quarter(cents, quarter)
print(res)

i = 0
cents = calculate_quarter(cents, dime)
print(res)

i = 0
cents = calculate_quarter(cents, nickel)
print(res)

i = 0
cents = calculate_quarter(cents, penny)
print(res)
print("Total coins:", sum(res.values()))






