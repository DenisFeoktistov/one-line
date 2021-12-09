(lambda dp: ([dp.append(dp[-1] + dp[-2]) for _ in range(15)], print(dp)))([1, 1])
