url = "https://www.moeda.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"


#Sanitização da URL
url = url.strip()

if (url ==""): #raise usado para mostrar que deu algo errado 
    raise ValueError("A URL ESTÁ VAZIA")


#SEPARA TEXTO DO SITE 
indice_interrocao = url.find('?')
url_base = url[:indice_interrocao]
texto_url = url[indice_interrocao + 1:]
print(texto_url)


#BUSCA INDICES E RESULTADO DA PALAVRA(PARÂMETRO)
palavra = "moedaOrigem"
inidice_palavra = texto_url.find(palavra)
indice_resultado = inidice_palavra + len(palavra) + 1
indice_e_comercial = texto_url.find('&', indice_resultado)

resultado_sem_tratamento = texto_url[indice_resultado:]
resultado_com_tratamento = texto_url[indice_resultado: indice_e_comercial]

#CONDIÇÃO DE FUNCIONAMENTO
if(indice_e_comercial == -1):
    print(resultado_sem_tratamento, '- Não teve tratamento')
else:
    print(resultado_com_tratamento, '- Teve tratamento')    

 
 