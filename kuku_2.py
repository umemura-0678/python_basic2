i = int(input("行数を入力してください:")) 
j = int(input("列数を入力してください:"))

for i in range(1, i + 1):
    for j in range(1, j + 1):
        print(i * j, end=" ")
    print()


