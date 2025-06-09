def is_correct(expr):
    a = int(expr[0:2])
    b = int(expr[5:7])
    c = int(expr[10:12])
    if a < 10 or b < 10 or c < 10:
        return False
    op = expr[3]
    if op == '+':
        return a + b == c
    elif op == '-':
        return a - b == c
    else:
        return False

def try_fill(expr, i):
    global found
    if found:
        return None
    if i == len(expr):
        if is_correct(expr):
            found = True
            return expr
        return None

    if expr[i] == '?':
        if i == 3:
            for op in ['+', '-']:
                new_expr = expr[:i] + op + expr[i+1:]
                result = try_fill(new_expr, i+1)
                if result:
                    return result
        else:
            for digit in '0123456789':
                new_expr = expr[:i] + digit + expr[i+1:]
                result = try_fill(new_expr, i+1)
                if result:
                    return result
    else:
        return try_fill(expr, i+1)
    return None

T = int(input())
for _ in range(T):
    s = input().strip()
    found = False
    if s[3] in ['*', '/']:
        print("WRONG PROBLEM!")
    else:
        result = try_fill(s, 0)
        if result:
            print(result)
        else:
            print("WRONG PROBLEM!")
