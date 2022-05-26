import re

#url = "https://www.moeda.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
#url = Url("https://www.moeda.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
#resultado = url.get_resultado()

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
    def sanitiza_url(self, url):
        if (type(url) == str):
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if(not self.url):
            raise ValueError("A URL ESTÁ VAZIA")
        
        padrao_url = re.compile('(http(s)?://)?(www.)?moeda.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if(not match):
            raise ValueError("A URL NÃO É VÁLIDA.")
        else:
            print("A URL é válida")

    
    def get_url_base(self):
        indice_interrocao = self.url.find('?')
        url_base = self.url[:indice_interrocao]
        return url_base    
                 
    def get_texto_url(self):
        indice_interrocao = self.url.find('?')
        texto_url = self.url[indice_interrocao + 1:]
        return texto_url
    
    def get_palavra(self, palavra):
        inidice_palavra = self.get_texto_url().find(palavra)
        indice_resultado = inidice_palavra + len(palavra) + 1
        indice_e_comercial = self.get_texto_url().find('&', indice_resultado)
        
        resultado_sem_tratamento = self.get_texto_url()[indice_resultado:]
        resultado_com_tratamento = self.get_texto_url()[indice_resultado: indice_e_comercial]
        
        if(indice_e_comercial == -1):
            return resultado_sem_tratamento
        else:
            return resultado_com_tratamento 
            
extrator_url =ExtratorUrl("https://www.moeda.com.br/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
resultado = extrator_url.get_palavra("quantidade")
print(resultado) 
        

            

    
    
    
         