import ddg3

def buscar(dadoBuscado):
    busca = ddg3.query(dadoBuscado)
    dict_ = list()
    for dado in range(len(busca.related)):
        resultado = dict()
        resultado["Título"] = busca.related[dado].text
        resultado["URL"] = busca.related[dado].url
        dict_.append(resultado)
    return dict_
