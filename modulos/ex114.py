# Crie um código em Python que teste se o site determinado está acessível pelo computador usado.

import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.python.org')
except urllib.error.URLError:
    print('O site não está acessível no momento')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read())
