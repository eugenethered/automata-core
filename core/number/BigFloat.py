class BigFloat:

    def __init__(self, *args):
        self.number = 0
        self.fraction = 0
        self.fraction_leading_zeros = 0
        self.parse_args(args)

    def set(self, number, fraction, fraction_leading_zeros=0):
        self.number = number
        self.fraction = fraction
        self.fraction_leading_zeros = fraction_leading_zeros

    def parse_args(self, args):
        if len(args) > 2:
            self.set(args[0], args[1], args[2])
        elif len(args) > 1:
            self.set(args[0], args[1])
        elif isinstance(args[0], str):
            if args[0].find('.') == -1:
                self.set(int(args[0]), 0, 0)
            else:
                number_values = args[0].split('.')
                (fraction, leading_zeros) = self.fraction_data(number_values[1])
                self.set(int(number_values[0]), fraction, leading_zeros)

    def fraction_data(self, value):
        return int(value), self.leading_zeros_count(value)

    @staticmethod
    def leading_zeros_count(value):
        leading_zero_count = 0
        numbers = list(value)
        for n in numbers:
            if n != '0':
                break
            if n == '0':
                leading_zero_count += 1
        return leading_zero_count

    def stringify(self, delimiter):
        return f'{self.number}{delimiter}{self.fraction}'

    def is_zero(self):
        return self.number == 0 and self.fraction == 0

    def add(self, other):
        number = self.number + other.number
        fraction = self.__add_fractions(other)
        fraction_leading_zeros = self.calculate_different_leading_zeros(other)
        return BigFloat(number, fraction, fraction_leading_zeros)

    def __add_fractions(self, other):
        if other.fraction_leading_zeros > self.fraction_leading_zeros:
            leading_zeros = other.fraction_leading_zeros - self.fraction_leading_zeros
            fraction = self.fraction * (10 ** leading_zeros)
            return fraction + other.fraction
        elif other.fraction_leading_zeros < self.fraction_leading_zeros:
            leading_zeros = self.fraction_leading_zeros - other.fraction_leading_zeros
            fraction = other.fraction * (10 ** leading_zeros)
            return fraction + self.fraction
        else:
            return self.fraction + other.fraction

    def calculate_different_leading_zeros(self, other):
        if self.fraction_leading_zeros > other.fraction_leading_zeros:
            return other.fraction_leading_zeros
        elif self.fraction_leading_zeros < other.fraction_leading_zeros:
            return self.fraction_leading_zeros
        return self.fraction_leading_zeros

    def __repr__(self):
        if self.fraction_leading_zeros > 0:
            fraction_value = f'{self.fraction}'.zfill(len(str(self.fraction)) + self.fraction_leading_zeros)
            return f'{self.number}.{fraction_value}'
        else:
            return f'{self.number}.{self.fraction}'

    def __eq__(self, other):
        return str(self) == str(other)
