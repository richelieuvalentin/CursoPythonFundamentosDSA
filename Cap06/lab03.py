
musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.
# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.


# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.

# importa o pacote "re" para trabalhar com expressões regulares
import re 

# Retorna o comprimento da lista criar utlizando a função "findall" para buscar as ocorrências do caracter "a"
quanti_a = len(re.findall("a", musica))

print('O caracter "a" aparece', quanti_a, 'vezes na música.')

# 2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.

# Utilizando a função "findall"
tempo = re.findall("tempo", musica)
quant_tempo = len(tempo)

print('A palavra "tempo" aparece', quant_tempo, "vezes na música.")

# 3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.

# Utiizando a função e "\w" para buscar o padrão
palavra_excl = re.findall(r"\w+!", musica)
print("As palavras seguidas por exclamação são:", palavra_excl)

# 4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.

# Utilizando para "\b" e "\s" para filtrar a correspondência
esse_amargo = re.findall(r"\besse\s(\w+)\samargo\b", musica)
print(esse_amargo)

# 5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.

caracter_acent = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", caracter_acent)


