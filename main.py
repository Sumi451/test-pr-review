def calculate_sum(a, b):
    '''Calculate sum of two numbers'''
    result = a + b  # Fixed spacing
    return result

def calculate_product(a, b):
    '''Calculate product of two numbers'''
    return a * b

def process_list(items):
    # New function with potential issues
    total = 0
    for i in items:
        total = total + i
    return total