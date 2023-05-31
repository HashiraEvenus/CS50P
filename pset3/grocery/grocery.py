
groceries={}
while True:
    try:
        item = input().upper()
    except EOFError:
        for thing in sorted(groceries):
            print(groceries[thing],thing)
        break
    except KeyError:
        pass
    if item in groceries:
        groceries[item] += 1
    else:
        groceries[item] = 1

