fruits = ['apple','strawberry','watermelon','banana']
# for fruit in fruits:
#     print(fruit)
    
iterator = iter(fruits)
while True:
    try:
        item = next(iterator)
        print(item)
    except StopIteration:
        break