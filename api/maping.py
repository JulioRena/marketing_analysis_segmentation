
def encontrar_valor_intervalo(valor, mapeamento):
    intervalos = sorted(mapeamento.keys(), key=lambda x: float(x.split(',')[0][1:]))
    
    for intervalo in intervalos:
        lim_inf, lim_sup = intervalo[1:-1].split(', ')
        lim_inf, lim_sup = float(lim_inf), float(lim_sup)
        if lim_inf < valor <= lim_sup:
            return mapeamento[intervalo]

    menor_intervalo = intervalos[0]
    maior_intervalo = intervalos[-1]
    
    lim_inf_menor, lim_sup_menor = menor_intervalo[1:-1].split(', ')
    lim_inf_menor = float(lim_inf_menor)
    
    lim_inf_maior, lim_sup_maior = maior_intervalo[1:-1].split(', ')
    lim_sup_maior = float(lim_sup_maior)
    
    if valor <= lim_inf_menor:
        return mapeamento[menor_intervalo]
    else:
        return mapeamento[maior_intervalo]