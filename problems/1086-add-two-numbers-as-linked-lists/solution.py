def add_two_numbers(l1, l2):
    i = 0
    carry = 0
    result = []

    while i < len(l1) or i < len(l2):
        val1 = l1[i] if i < len(l1) else 0
        val2 = l2[i] if i < len(l2) else 0

        total = val1 + val2 + carry

        digit = total % 10
        carry = total // 10

        result.append(digit)

        i += 1

    if carry:
        result.append(carry)

    return result