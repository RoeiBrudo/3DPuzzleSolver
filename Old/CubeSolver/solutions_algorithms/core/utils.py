def get_perm(a, b):
    a = a.upper()
    b = b.upper()
    true_ind = []
    for i in range(len(a)):
        if a[i] not in b:
            return False, None
        else:
            true_ind.append(b.index(a[i]))
    return True, true_ind


