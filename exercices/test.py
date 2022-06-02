import operator

"""
def get_truth(inp, relate, cut):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '==': operator.eq}
    return ops[relate](inp, cut)


print(get_truth(1.0, '>', 0.0)) # prints True
print(get_truth(1.0, '<', 0.0)) # prints False
print(get_truth(1.0, '>=', 0.0)) # prints True
print(get_truth(1.0, '<=', 0.0)) # prints False
print(get_truth(1.0, '==', 0.0)) # prints False
"""
print(operator.gt(2,2))