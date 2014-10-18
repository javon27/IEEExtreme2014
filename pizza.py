"""
pdf-source: resist-our-pizza-English.pdf
"""
ingredients = {}
ingredients['Anchovies'] = 50
ingredients['Artichoke'] = 60
ingredients['Bacon'] = 92
ingredients['Broccoli'] = 24
ingredients['Cheese'] = 80
ingredients['Chicken'] = 30
ingredients['Feta'] = 99
ingredients['Garlic'] = 8
ingredients['Ham'] = 46
ingredients['Jalapeno'] = 5
ingredients['Meatballs'] = 120
ingredients['Mushrooms'] = 11
ingredients['Olives'] = 25
ingredients['Onions'] = 11
ingredients['Pepperoni'] = 80
ingredients['Peppers'] = 6
ingredients['Pineapple'] = 21
ingredients['Ricotta'] = 108
ingredients['Sausage'] = 115
ingredients['Spinach'] = 18
ingredients['Tomatoes'] = 14

inpewt = input()


def dequeue():
    global inpewt
    n = inpewt[0]
    inpewt = inpewt[1:]
    return n

inpewt = inpewt.split()
boxes = int(dequeue())
calories = 0
for i in range(boxes):
    slices = int(dequeue())
    calories += slices * 270
    if not inpewt[0].isdigit():
        toppings = dequeue().split(',')
        for topping in toppings:
            calories += slices*ingredients[topping]
print('The total calorie intake is '+str(calories))
