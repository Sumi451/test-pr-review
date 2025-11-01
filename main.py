def calculate_sum(a, b):
    '''Calculate sum of two numbers'''
    result = a + b
    return result

def calculate_product(a, b):
    '''Calculate product of two numbers'''
    return a * b

def process_list(items):
    # Missing type hints - style issue
    total = 0
    for i in items:
        total = total + i
    return total
