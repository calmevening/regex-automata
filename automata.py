import requests
import re
import sys
from bs4 import BeautifulSoup

url = sys.argv[1]
key = sys.argv[2]
num = int(sys.argv[3])
num2 = int(sys.argv[4])
regstr = sys.argv[5]

while num != num2:
    data = { #edit the request body for your needs
        'file': f'{num:04}',
        'dlkey': f'{key}',
    }
    x = requests.post(url, data=data)
    print('Searching link ' + f'{num}' + '.')
    soup = BeautifulSoup(x.text, "html.parser")
    for link in soup.findAll('a'):
        for match in re.finditer(regstr, str(x.text)):
            print('Doing regex.')
            with open("output.txt", "a") as myfile:
                myfile.write(match.group(0) + '\n')
    num += 1
    print('Done.')
