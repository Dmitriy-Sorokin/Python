print('Таблица умножения')
for i in range(1, 10):
    for j in range(2, 10):
        print(f'{i} * {j} = {i * j}\t', end=' ')
    print(' ')
else:
    print('Well done')
