import requests

responce = requests.get('https://finance.i.ua/')

responce_text = responce.text

responce_parse = responce_text.split('<span>')

print('Print a price with hryvnias(₴): ')
price = input()

for parse_elem1 in responce_parse:
    for parse_elem2 in parse_elem1.split("</span>"):
        if parse_elem2[1].isdigit():
            cours = float(price) / float(parse_elem2)
            print("Rounded price in dollars($) is: ")
            print(round(cours, 2), '$')
            quit()