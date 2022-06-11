n = int(input("How many names you want to enter? "))
# next line seems better but has issues
# phone_book = dict(input().split() for _ in range(n))
name_numbers = [input("Enter name and number: ").split() for _ in range(n)]
phone_book = {k:v for k,v in name_numbers}

while True:
    try:
        name = input("Enter name to search: ")
        if name in phone_book:
            print('%s = %s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break