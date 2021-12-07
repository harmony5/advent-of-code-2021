data = open("input.txt").readlines()

def solve(rows, f, col_idx=0):
    if len(rows) == 1:
        return rows[0]
    else:
        icol = [r[col_idx] for r in rows]
        return solve([r for r in rows if f(r[col_idx], icol)], f, col_idx+1)
        
def filter(criteria):
    def f(bit, col):
        if col.count("1") == col.count("0"):
            return bit == str(criteria)
        if criteria == 0:
            return (col.count("1") < col.count("0")) == int(bit)
        if criteria == 1:
            return (col.count("1") > col.count("0")) == int(bit)
    return f

ox = solve(data,  filter(1))
co2 = solve(data, filter(0))

ox = int(ox, 2)
co = int(co2, 2)
print(ox*co)