def amplify(n):
    store = []
    for i in range(1,n+1):
        if i % 4 == 0:
            store.append(i * 10)
        else:
            store.append(i)
    return store

simplify = amplify(4)
print(simplify)
        
