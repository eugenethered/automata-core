class BigFloat:

    def __init__(self, *args):
        self.number = 0
        self.fraction = 0
        self.parse_args(args)

    def set(self, number, fraction):
        self.number = number
        self.fraction = fraction

    def parse_args(self, args):
        if len(args) > 1:
            self.set(args[0], args[1])
        elif isinstance(args[0], str):
            number_values = args[0].split('.')
            self.set(int(number_values[0]), int(number_values[1]))

    def stringify(self, delimiter):
        return f'{self.number}{delimiter}{self.fraction}'

    def __repr__(self):
        return f'{self.number}.{self.fraction}'

    def __eq__(self, other):
        return str(self) == str(other)
