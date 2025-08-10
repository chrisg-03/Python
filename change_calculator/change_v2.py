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

quarter, dime, nickel, penny = 25, 10, 5, 1
coins = [quarter, dime, nickel, penny]
ref = {}

def calculate_coins(cents, coin):
    global i
    while cents >= coin:
        i += 1
        cents -= coin
    return cents

while True:
    try:   
        cents = int(input("Enter change owed: "))
        if cents > 0:
            break
        else:
            print("Please use a positive value.")        
    except ValueError:
        print("Use an integer")

for name in coins:
    i = 0
    cents = calculate_coins(cents, name)
    ref[name] = i
    print(ref)

print(sum(ref.values()))
