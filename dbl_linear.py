def dbl_linear(n):
    u = [1]  # Initialize the sequence with the first element

    # Index for the next elements in the sequence
    idx_y = 0
    idx_z = 0

    while len(u) <= n:
        next_y = 2 * u[idx_y] + 1
        next_z = 3 * u[idx_z] + 1

        # Add the smaller of the next elements to the sequence
        if next_y <= next_z:
            u.append(next_y)
            idx_y += 1
            if next_y == next_z:
                idx_z += 1
        else:
            u.append(next_z)
            idx_z += 1

    return u[n]

dbl_linear(10)