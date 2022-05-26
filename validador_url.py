# Exemplos de URLs válidas:

# moeda.com/cambio
# moeda.com.br/cambio
# www.moeda.com/cambio
# www.moeda.com.br/cambio
# http://www.moeda.com/cambio
# http://www.moeda.com.br/cambio
# https://www.moeda.com/cambio
# https://www.moeda.com.br/cambio

# Exemplos de URLs inválidas:

# https://moeda/cambio
# https://moeda.naoexiste/cambio
# ht://moeda.naoexiste/cambio

# https://www.moeda.com.br/cambio
import re

url = 'https://www.moeda.com.br/cambio'
#Ao usar () quer dizer que tem q ser exatamente o que ta dentro deles, e colchetes [abc] quer dizer qualquer caracter dentro das colchetes
padrao_url = re.compile('(http(s)?://)?(www.)?moeda.com(.br)?/cambio')
match = padrao_url.match(url) #match para verificar se é exatamente o que queremos 

if(not match):
    raise ValueError("A URL NÃO É VÁLIDA.")
else:
    print("A URL é válida")































