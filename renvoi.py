import requests

epreuve = 'https://www.newbiecontest.org/epreuves/prog/prog1.php'
url = 'https://www.newbiecontest.org/epreuves/prog/verifpr1.php?solution='
cookie = {'SMFCookie89':'a%3A4%3A%7Bi%3A0%3Bs%3A3%3A%22896%22%3Bi%3A1%3Bs%3A40%3A%2227788be99485cfa481b3ec74603678025ec6a5cf%22%3Bi%3A2%3Bi%3A1837613304%3Bi%3A3%3Bi%3A0%3B%7D'}

r = requests.get(epreuve, cookies = cookie)
solution = r.text[64:]
url = url + solution
requests.post(url, cookies = cookie)
e = requests.get(url, cookies = cookie)
e = e.text

print (e)
