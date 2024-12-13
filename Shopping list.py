shopping_list = []
total_cost = 0.0

while True:
    product = input("Welk product wil je toevoegen? ")
    quantity = input(f"Hoeveel {product} wil je? ")
    cost = float(input(f"Hoeveel kost {product}? "))

    shopping_item = f"{product} ({quantity})"
    shopping_list.append(shopping_item)

    total_cost += cost

    continue_choice = input("Wil je nog een product toevoegen? (ja/nee) ")
    if continue_choice.lower() != 'ja':
        break
print ("=========================")

print("\nJe boodschappenlijst:")
print ("=========================")
for item in shopping_list:
    print(item)

print ("=========================")

print(f"Totaal kosten: €{total_cost:.2f}")