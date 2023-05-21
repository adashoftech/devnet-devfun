import requests

#use variables in code instead of full URL
base_url = 'https://deckofcardsapi.com/api/'
response = requests.get(f"{base_url}new/")

#response = requests.get('https://deckofcardsapi.com/api/deck/new/')

#code using variables
if response.status_code == 200:
    deck_id = response.json()['deck_id']
    requests.get(f"{base_url}{deck_id}/shuffle/")
else:
    print(f"Request unsuccessful. Status code: {response.status_code}")
    exit()

draw_response = requests.get(f"{base_url}/deck/{deck_id}/draw/?count=5")
draw = draw_response.json()

i = 1

for card in draw['cards']:
    print(f"Card {i} is {card['value']} of {card['suit']}")
    i += 1

#code using full URL
# if response.status_code == 200:
#     deck_id = response.json()['deck_id']
#     requests.get(f"https://deckofcardsapi.com/api/{deck_id}/shuffle/")
# else:
#     print(f"Request unsuccessful. Status code: {response.status_code}")
#     exit()

# draw_response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5")
# draw = draw_response.json()

# i = 1

# for card in draw['cards']:
#     print(f"Card {i} is {card['value']} of {card['suit']}")
#     i += 1