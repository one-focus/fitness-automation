import requests

for i in range(10):
    # Making a get request
    response = requests.post('https://gym-face.ru/my/cart/login/?ref=&fb=&product_id=4974&form_id=winf&email=asdfsadf%40fasdfsdf.df&external=Y')

    # print elapsed time
    print(response.elapsed)

print("----")
for i in range(10):
    response = requests.get('https://gym-face.ru/my/cart/B31ZG5Z2M2020/')

    print(response.elapsed)
