if __name__ == '__main__':
    N = int(input())
    lista = []

    for _ in range(N):
        entrada = input().split()
        comando = entrada[0]

        if comando == "insert":
            index = int(entrada[1])
            value = int(entrada[2])
            lista.insert(index, value)
        elif comando == "print":
            print(lista)
        elif comando == "remove":
            value = int(entrada[1])
            lista.remove(value)
        elif comando == "append":
            value = int(entrada[1])
            lista.append(value)
        elif comando == "sort":
            lista.sort()
        elif comando == "pop":
            lista.pop()
        elif comando == "reverse":
            lista.reverse()
