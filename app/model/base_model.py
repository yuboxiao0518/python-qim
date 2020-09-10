
class Data(object):
    def __init__(self, code, data):
        # 成功为20000
        self.code = code
        self.data = data


class Items(object):
    def __init__(self, total, items):
        self.total = total
        self.items = items
