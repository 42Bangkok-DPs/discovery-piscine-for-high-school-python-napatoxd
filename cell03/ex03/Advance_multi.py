def multiplication_tables():
    i = 0
    j = 0
    while i <= 10:
        table = []
        while j <= 10:
            table.append(i * j)
            j += 1
        print(f"Table de {i}: {' '.join(map(str, table))}")
        i += 1

multiplication_tables()

