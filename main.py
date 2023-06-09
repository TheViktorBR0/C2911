responce = requests.get('https://coinmarketcap.com/')

responce_text = responce.text

responce_parse = responce_text.split('<span>')

for parse_elem1 in responce_parse:
    if parse_elem1.startswith('$'):
        for parse_elem2 in parse_elem1.split("</span>"):
            if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
                print(parse_elem2)