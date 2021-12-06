print((lambda x, fac: fac(x, fac))(6, lambda x, self: 1 if x == 1 else x * self(x - 1, self)))
