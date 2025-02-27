

class Restaurante:

    restaurantes = []


    def __init__(self, nome, categoria):
        self._nome = nome.title()

        self.categoria = categoria.upper()

        self._ativo = False

        Restaurante.restaurantes.append(self)
    

    def __str__(self):

        return f'{self._nome} | {self.categoria}'
    

    def listar_restaurantes():

        for restaurante in Restaurante.restaurantes:

            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante._ativo}')



def listar_restaurantes():
    

    print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}')

    for restaurante in Restaurante.restaurantes:

        print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')

    @property

    def ativo(self):

        return '⌧' if self._ativo else '☐'


restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')


Restaurante.listar_restaurantes()

''' 

    #Exibindo metodos da classe
    
    print(dir(restaurante_praca)


print(vars(restaurante_praca))

#Exibindo Valor inserido

print(vars(restaurante_praca))
'''

#

'''

class Musica:

    def __init__(self, nome, artista, duracao= int):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao


musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)

musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)

musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)
'''