pos = 0
def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1

    return False




list = [5, 8, 4, 6, 9, 2]

n = 9

if search(list, n):
    print(" found on index number ", pos )

else:
    print(' not found ')