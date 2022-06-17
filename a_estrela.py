CidH = {
    "A"          : 240,
    "B"     : 186,
    "C"       : 182,
    "D"       : 163,
    "E"        : 170,
    "F"       : 150,
    "G"       : 165,
    "H"       : 139,
    "I"          : 120,
    "J"         : 130,
    "K"       : 122,
    "L"         : 104,
    "M"        : 100,
    "N"       : 77,
    "O": 72,
    "P"         : 65,
    "Q"     : 65,
    "R"      : 0,
}

mapaCid = {
    "A"          : {"B": 73, "C": 64, "D": 89, "E" : 104},
    "B"     : {"A": 73, "K": 83},
    "C"       : {"A": 64, "I": 64},
    "D"       : {"A": 89 , "N": 89  },
    "E"        : {"A": 104,"J":40 },
    "F"       : {"I": 31, "N": 84 },
    "G"       : {"J": 35, "Q":113 },
    "H"       : {"K": 35, "L": 36 },
    "I"          : {"C": 64, "F": 31, "M":20,"L":28 },
    "J"         : {"E": 40, "N": 53,"G":35,"Q":80 },
    "K"       : {"B": 83, "H": 35 },
    "L"         : {"H": 36,"P":63,"I":28 },
    "M"        : {"I": 20, "O": 50 },
    "N"       : {"F": 84, "D": 89, "J": 53 },
    "O": {"P": 41, "M": 50, "R": 72 },
    "P"         : {"L": 63, "O": 41, "R": 65},
    "Q"     : {"J": 80, "G": 113, "R":65 },
    "R"      : {"P": 65, "Q": 65,"O": 72},

}

def sortFunc(item):
    return item["prioridade"]

def algA():
    inicio = "A"
    destino = "R"
    borda = [{"nome": inicio, "prioridade": 0}] #fila ordenada pela variavel prioridade de acordo com o custo de caminho
    vim_de = {} 
    menor_custo = {}
    vim_de[inicio] = None # Nó iniciado com o menor custo

    menor_custo[inicio] = 0
    
   # Condição de percorrer enquanto houver nós abertos com vizinhos não visitados 
    while len(borda)>0:
        borda.sort(key=sortFunc) #ordena a fila "borda" de acordo com a prioridade
        atual = borda.pop(0)['nome']  # Atribui cidade atual ao topo da fila de prioridade
    
        if atual == destino:  # Verifica se chegou a cidade destino 
          break
      # Calcula menor f(n)
        for prox in mapaCid[atual]:
            novo_custo = menor_custo[atual] + mapaCid[atual][prox] 
            if prox not in menor_custo or novo_custo < menor_custo[prox]: #se o nodo aberto(prox) nao tem menor custo ou novo custo tem menor custo que o menor custo do nodo aberto, o novo menor_custo sera atribuido ao novo_custo
                menor_custo[prox] = novo_custo
                prioridade = novo_custo + CidH[prox] #atribui a prioridade o novo custo somado a heuristica
                borda.append({"nome" : prox, "prioridade": prioridade}) # Adiciona no array todos os nós que foram abertos e verificados
                vim_de[prox] = atual #atribui ao nodo aberto(prox) o conteudo de atual 
    caminho = [destino]
    prox = vim_de[destino]
    while prox is not None: #Quando prox(nodo aberto) nao estiver vazio
        caminho.append(prox) #adiciona o nó ao array
        prox= vim_de[prox] #atribui-se o nodo aberto ao array de localização
    caminho.reverse() # Inverte completamente o array para imprimir o caminho em ordem
   
    
    print ("A rota pelo alg A* é: ")
    print (' -> '.join(caminho))
    print ("Distancia: " + str(menor_custo[destino]) + "km")

if __name__ == '__main__':
    algA()
