dados = list()
grupoDePessoas = list()
pp = list()
pl = list()
pessoasC = pessoaP = pessoaL = 0

for c in range(0,4):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pessoasC += 1
    grupoDePessoas.append(dados[:])
    dados.clear()

print(grupoDePessoas)

for p in grupoDePessoas:
    if p[1] >= 100:
        pp.append(p[0])
    else:
        pl.append(p[0])
        
print('\n')
print(f'Cadastros: {pessoasC}')
print(f'Pessoas Pessadas: {pp}')
print(f'Pessoas Leves: {pl}')

