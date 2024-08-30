def kevin_sort(arr, bit_index=None):
    if len(arr) <= 1:
        return arr

    if bit_index is None:

        max_bits = max(arr).bit_length()
        bit_index = max_bits - 1

    if bit_index < 0:
        return arr

    zero= []
    one = []

    for num in arr:

        if (num >> bit_index) & 1 == 1:
            one.append(num)
        else:
            zero.append(num)

    sorted_zero = kevin_sort(zero, bit_index - 1)
    sorted_one = kevin_sort(one, bit_index - 1)


    return sorted_zero + sorted_one


arr = [84,65,96,54,24,88,14,34,1472,1,36445]
ordenado = kevin_sort(arr)
print("Arreglo ordenado:", ordenado)