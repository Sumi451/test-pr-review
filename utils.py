def process_data(data):
    '''Process the data'''
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result

def divide(a, b):
    # Missing error handling - potential issue
    return a / b

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def add(self, item):
        self.data.append(item)
    
    def process(self):
        # TODO: Implement processing logic
        pass
