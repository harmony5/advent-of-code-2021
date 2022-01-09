def minmax(seq, key=lambda x: x):
    min_el = max_el = None
    for el in set(seq):
        if min_el is None or key(el) < key(min_el):
            min_el = el
        if max_el is None or key(el) > key(max_el):
            max_el = el

    return min_el, max_el


def reduce_rating(ratings, col_index, bit, use_most_common):
    current_col = [row[col_index] for row in ratings]
    least_common, most_common = minmax(current_col, key=current_col.count)

    # '0' and '1' are equally common
    if least_common == most_common:
        criteria = bit
    else:
        criteria = most_common if use_most_common else least_common

    return [row for row in ratings if row[col_index] == criteria]


if __name__ == "__main__":
    with open("input.txt") as f:
        data = [line.strip() for line in f.readlines()]

    oxy_ratings = reduce_rating(data, 0, "1", use_most_common=True)
    co2_ratings = reduce_rating(data, 0, "0", use_most_common=False)

    bit_size = len(data[0])
    for i in range(1, bit_size):

        if len(oxy_ratings) > 1:
            oxy_ratings = reduce_rating(oxy_ratings, i, "1", use_most_common=True)

        if len(co2_ratings) > 1:
            co2_ratings = reduce_rating(co2_ratings, i, "0", use_most_common=False)

    oxy = int(oxy_ratings[0], 2)
    co2 = int(co2_ratings[0], 2)
    print(f"{oxy_ratings=};\n{co2_ratings=}")
    print(f"{oxy=};{co2=}; {oxy * co2=}")
