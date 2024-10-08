def multiplication_tables():
    i = 0
    while i <= 10:
        table = []
        j = 0
        while j <= 10:
            table.append(i * j)
            j += 1
        print(f"Table de {i}: {' '.join(map(str, table))}")
        i += 1

def main():
    user_input = input("ป้อนข้อมูล (กด Enter เพื่อดูตารางการคูณทั้งหมด): ").strip()
    
    if user_input:  
        print("none")
    else:
        multiplication_tables()

if __name__ == "__main__":
    main()
