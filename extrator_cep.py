import re #REGULAR EXPRESSION -- RegEx

endereco = "Rua das Flores 72, apartamento 1002, Laranjerias, Rio de Janeiro, RJ, 23440-120"

#Cep --> 5 dígitos + hífen (opcional) + 3 dígitos 

#INICIANDO PADRÃO (PADRÃO NORMAL)
#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")  #Cadada dígito dentre de [] é uma possibilidade daquele dígito, '?' No padrão quer dizer queoder ser encontrado la ou não 

#PADRÃO COM QUANTTIFICADORES
#[0-9] --> números de 0 à 9; [-]{0,1} --> Pode aparecer de 0 à 1 vez
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}") #{} recebe um número, e esse número indica quantas vezes aquele padrão tem que aparecer (Ex: Dígitos de 0 à 9 aparecem 5 vezes no início do CEP e 3 vezes após o hífem)
busca = padrao.search(endereco) #Match (retorna Match ou None)                                                                   
if(busca):
    cep = busca.group()
    print(cep)
    
