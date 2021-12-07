print(*filter(lambda p: p[1] > 1_000_000, ((x, (lambda x, f: f(x, f))(x, lambda x, self: x + 1 if x <= 1 else x + 1 + 2 * x + self(x - 1, self) + self(x - 3, self))) for x in range(35))))
