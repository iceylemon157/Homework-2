liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

token_names = ["tokenA", "tokenB", "tokenC", "tokenD", "tokenE"]
# current_token = 'tokenB'
# current_amount = 5.0

def bfs():
    que = []
    que.append(('tokenB', 5.0, ['tokenB'], liquidity.copy()))
    # dic = dict([(x, 0.0) for x in token_names])
    # dic['tokenB'] = 5.0

    state_set = set()

    ans_path, ans_amount = None, None

    value = 0

    while que:
        name, amount, path, liq = que.pop(0)

        # print(path, liq.items())

        state = (name, amount, tuple(sorted(liq.items())))
        if state in state_set:
            continue

        state_set.add(state)

        if name == 'tokenB' and value < amount:
            value = amount
            # print(value)

        #     continue
        if name == 'tokenB' and amount > 20.0:
            for x, y in liq.items():
                print(x, y)
            ans_path, ans_amount = path, amount
            return ans_path, ans_amount
            # return path, amount

        amount *= 0.997

        for (a, b), (liq_a, liq_b) in liq.items():
            k = liq_a * liq_b
            if a == name:
                new_amount = k / (liq_a + amount)
                # if new_amount > dic[b]:
                #     dic[b] = new_amount
                new_liq = liq.copy()
                new_liq[(a, b)] = (liq_a + amount, new_amount)
                que.append((b, liq_b - new_amount, path + [b], new_liq))

            elif b == name:
                new_amount = k / (liq_b + amount)
                # if new_amount > dic[a]:
                #     dic[a] = new_amount
                new_liq = liq.copy()

                new_liq[(a, b)] = (new_amount, liq_b + amount)
                que.append((a, liq_a - new_amount, path + [a], new_liq))

    return ans_path, ans_amount

    # print(dic)
    # return dic

def dfs(path, token_amount, current_liquidity, prev=None):
    print('path', path, 'token_amount', token_amount, 'current_liquidity', current_liquidity)

    if path[-1] == 'tokenB' and token_amount > 25.0:
        print('-' * 100)
        print(path, token_amount)
        print('-' * 100)
        return

    for (a, b), (liq_a, liq_b) in current_liquidity.items():
        print('a', a, 'b', b, 'liq_a', liq_a, 'liq_b', liq_b)
        k = liq_a * liq_b
        if a == path[-1]:
            if token_amount > liq_a or b == prev:
                continue
            new_liq_b = k / (liq_a + token_amount)
            current_liquidity[(a, b)] = (liq_a + token_amount, new_liq_b)
            dfs(path + [b], liq_b - new_liq_b, current_liquidity, a)
            current_liquidity[(a, b)] = (liq_a, liq_b)
            
        elif b == path[-1]:
            if token_amount > liq_b or a == prev:
                continue
            new_liq_a = k / (liq_b + token_amount)
            current_liquidity[(a, b)] = (new_liq_a, liq_b + token_amount)
            dfs(path + [a], liq_a - new_liq_a, current_liquidity, b)
            current_liquidity[(a, b)] = (liq_a, liq_b)


    pass

def main():
    path, amount = bfs()

    path_str = '->'.join(path)
    print(f'path: {path_str}, tokenB balance={amount}')

main()
