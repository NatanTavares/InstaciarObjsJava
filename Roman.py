def data_roman_numbers():
    unit = 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'
    decimal = 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'
    hundreds = 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'
    thousands = 'M', 'MM', 'MMM'

    decimal_numbering = unit, decimal, hundreds, thousands
    return decimal_numbering


def convert_to_roman(p_number):
    final = ''

    if 0 < int(p_number) <= 3999:
        data = data_roman_numbers()
        reversed_numbers = p_number[::-1]
        result = []

        for i, alg in enumerate(reversed_numbers):
            if alg != '0':
                value_index = int(alg) - 1
                index = int(i)
                result.insert(0, data[index][value_index])

        for num_romam in result:
            final += num_romam

    return final


try:
    number_entered = input('Enter a value to be converted to Roman numerals: ')
    if convert_to_roman(number_entered):
        print(f'Result: {convert_to_roman(number_entered)}')
    else:
        print('>[Out range]: Try enter a value entry 1 at 3999')
except:
    print('>[Invalid value]: Try enter an integer value')

