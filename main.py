import urllib.request
import requests

#-------------------------------------------------------------

# opener = urllib.request.build_opener()
# responce = opener.open('https://httpbin.org/get')
#
# print(responce.read())

#-------------------------------------------------------------

# responce = requests.get('https://httpbin.org/get')
# print(responce.text)
# print(f"Datatype - {type(responce.text)}")

#-------------------------------------------------------------

# responce = requests.post('https://httpbin.org/post', data="Test data", headers={'h1': 'Test Title'})
# print(responce.text)

#-------------------------------------------------------------

# responce = requests.get('https://coinmarketcap.com/')
#
# responce_text = responce.text
#
# responce_parse = responce_text.split('<span>')
#
# for parse_elem1 in responce_parse:
#     if parse_elem1.startswith('$'):
#         for parse_elem2 in parse_elem1.split("</span>"):
#             if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
#                 print(parse_elem2)

#-------------------------------------------------------------

# res_parse_list = []
#
# responce = requests.get('https://coinmarketcap.com/')
#
# responce_text = responce.text
#
# responce_parse = responce_text.split('<span>')
#
# for parse_elem1 in responce_parse:
#     if parse_elem1.startswith('$'):
#         for parse_elem2 in parse_elem1.split("</span>"):
#             if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
#                 res_parse_list.append(parse_elem2)
#
# bitcoin_exchange_rate = res_parse_list[0]
# print('BTC =', bitcoin_exchange_rate)

#-------------------------------------------------------------