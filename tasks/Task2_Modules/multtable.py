def print_mult_table(num):
    for i in range(1, num + 1):
        for j in range(1, i+1):
            print(f'{i}x{j}={i * j}')
        print('=' * 10)
        
def get_mult_table(n):
    tables = []
    for i in range(1, n+1):
        mult_table = []
        for j in range(1, i+1):
            mult_table.append(j * i)
        tables.append(mult_table)
    
    return tables