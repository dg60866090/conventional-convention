fruits = ['Apple', 'Banana', 'Pineapple', 3]

animals = [
    'Lions',
    'Tiger',
    'Rabbit',
    3
]

Clubs = [
    'ManU',
    'ManC',
    3,
]

for i in range(1,16+1):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    elif i%15==0:
        print('fizzbuzz')
    else:
        print(i)
