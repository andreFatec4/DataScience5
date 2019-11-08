
# 1 Adicione o atributo intenção de voto à base de dados referente à rede social de 
# cientistas de dados. Sorteie uma intenção de voto para cada usuário da rede. Aumente 
# o tamanho da base de modo que ela tenha 100 usuários.

import random
import math
from collections import Counter

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"},
]

def add_voto(lista):
    for n in lista:
        n['voto'] = random.choice(['Haddad', "Bolsonaro"])
    return print(lista)

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            # Com a Base de Dados Original, não encontrei qualquer possibilidade de relação #
                        # Então criei outra que segue abaixo #
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class DataCientist:
    def __init__ (self, idade, salario, assuntos_interesse, qtde_amigos, intencao_de_voto=None):
        self.idade = idade
        self.salario = salario
        self.assuntos_interesse = assuntos_interesse
        self.qtde_amigos = qtde_amigos
        self.intencao_de_voto = intencao_de_voto
    def __str__ (self):
        return f'Cientista(idade: {self.idade}, salario: {self.salario}, assuntos_interesse: {self.assuntos_interesse}, qtde_amigos: {self.temas_em_comum}, intencao_de_voto: {self.intencao_de_voto})'
    def __eq__ (self, other):
        return self.intencao_de_voto == other.intencao_de_voto
    def __hash__(self):
        return 1

def gera_base (n):
    lista = []
    for _ in range (n):
        idade = random.randint(22, 60)
        salario = 7000 + random.random() * 4000
        assuntos_interesse = random.randint(5, 15)
        qtde_amigos = random.randint(1, 30)
        intencao_de_voto = random.choice(['Haddad', "Bolsonaro"])
        c = DataCientist (idade, salario, assuntos_interesse, qtde_amigos, intencao_de_voto)
        lista.append(c)
    return lista

def test_gera_base ():
    lista = gera_base(5)
    for elemento in lista:
        print (elemento)

def rotulo_de_maior_frequencia_sem_empate (pessoas):
    frequencias = Counter (pessoas)
    rotulo, frequencia = frequencias.most_common(1)[0]
    qtde_de_mais_frequentes = len([count for count in frequencias.values() if count == frequencia])
    if qtde_de_mais_frequentes == 1:
        #print ("K: ", len(pessoas))
        #print ("Frequência: ", frequencia)
        #print ("Rótulo: ", rotulo)
        return rotulo
    return rotulo_de_maior_frequencia_sem_empate (pessoas[:-1])

def distance (p1, p2):
    d_idade = math.pow((p1.idade - p2.idade), 2)
    d_salario = math.pow((p1.salario - p2.salario), 2)
    d_assuntos_interesse = math.pow((p1.assuntos_interesse - p2.assuntos_interesse), 2)
    d_qtde_amigos = math.pow((p1.qtde_amigos - p2.qtde_amigos), 2)
    return math.sqrt(d_idade + d_salario+d_assuntos_interesse + d_qtde_amigos)

def knn (k, observacoes_rotuladas, nova_observacao):
    ordenados_por_distancia = sorted (observacoes_rotuladas, key= lambda obs: distance (obs,nova_observacao))
    k_mais_proximos = ordenados_por_distancia[:k]
    resultado = rotulo_de_maior_frequencia_sem_empate(k_mais_proximos)
    return resultado.intencao_de_voto

def validacao ():
    lista = gera_base(100)
    acertos = 0
    erros = 0
    for tupla in enumerate(lista):
        instancia_a_rotular = tupla[1]
        base_a_ser_usada = lista[0:tupla[0]] + lista[tupla[0] + 1:]
        resultado = knn(5, base_a_ser_usada, instancia_a_rotular)
        if resultado == instancia_a_rotular.intencao_de_voto:
            acertos += 1
        else:
            erros += 1
    
    print (f'Acertos: {acertos}, Erros: {erros}')

def main():
    #add_voto(users)
    #test_gera_base ()
    validacao ()
main()