pos = 0
def search(list, n):


    l = 0
    u = len(list)-1

    for i in range(u):
        if list[i] == n:
            if list[l] == n:
                globals()['pos'] = l
                return True
            if list[u] == n:
                globals()['pos'] = u
                return True
            else:
                while l <= u:
                    mid = (l+u) // 2 # // means int division

                    if list[mid] == n:
                        globals()['pos'] = mid
                        return True
                    else:
                        if list[mid] < n:
                            l = mid
                        else:
                            u = mid
    else:
        return False





list = [1, 3, 7, 9, 20, 30, 45, 57, 89, 99, 103, 123, 167, 190, 239, 274, 448, 564, 567, 999]

n = 7

if search(list, n):
    print(" found on index number ", pos )

else:
    print(' not found ')