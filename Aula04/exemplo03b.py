pontos = int(input('informe os pontos: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'excelente! você tem {pontos} agora! ')

if pontos >= 50:
    pontos = pontos + 5
    print(f'Bom desempenho! você tem {pontos} agora! ')

else:
    print(f'você tem {pontos}! Não desanime, você está começando')