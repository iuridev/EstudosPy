'''
DESAFIO
Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.



Entrada
A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

Saída
Imprima o nome do animal correspondente à entrada fornecida.
'''

''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
a = input() 
b = input() 
c = input() 

if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        elif c == 'onivoro':
            print('pomba')          
    elif b == 'mamifero':
        if c == 'herbivoro':
            print('vaca')
        elif c == 'onivoro':
            print('homem')    
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        elif c == 'herbivoro':
            print('lagarta')          
    elif b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        elif c == 'onivoro':
            print('minhoca')   