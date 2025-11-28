
def recuperar_senha(N, M, K, senha, listas, P):
    # Identificar posições borradas
    posicoes = [i for i, c in enumerate(senha) if c == '#']
    senha = list(senha)
    
    # Ordenar listas lexicograficamente
    listas = [sorted(lista) for lista in listas]
    
    # Pré-calcular potências para saber quantas senhas cada escolha gera
    potencias = [1] * M
    for i in range(M - 2, -1, -1):
        potencias[i] = potencias[i + 1] * len(listas[i + 1])
    
    # Construir a senha letra por letra
    P -= 1  # Tornar zero-indexado
    for i in range(M):
        for j, letra in enumerate(listas[i]):
            qtd = potencias[i]
            if P < qtd:
                senha[posicoes[i]] = letra
                break
            P -= qtd
    
    return ''.join(senha)

# Exemplo de uso
N = 6
M = 2
K = 2
senha = "x#yy#z"
listas = ["ab", "cd"]
P = 3

print(recuperar_senha(N, M, K, senha, listas, P))  # Saída esperada: xbyycz