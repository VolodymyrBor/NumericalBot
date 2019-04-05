class ErrorMethod:
    def __init__(self):
        f = open('data.txt', 'w')
        f.write('This method is not available')
        f.close()


class ErrorData:
    def __init__(self):
        f = open('data.txt', 'w')
        f.write('Error in  data')
        f.close()
