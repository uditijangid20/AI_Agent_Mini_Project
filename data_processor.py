# data_processor.py — missing comments, poor naming
def p(d):
    r = []
    for x in d:
        if x > 0:
            r.append(x * 2)
    return r

raw = [1, -2, 3, -4, 5]
print(p(raw))
print("thanks")
