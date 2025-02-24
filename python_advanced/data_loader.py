def generate_data(
        path_file: str, 
        number_start: int = 0, 
        number_end: int = 10, 
        count: int = 100, 
        sign_operation: list[str] = None
        ):
    """
    Create file 'path_file'.csv data set math example
    param path_file: set file path *.csv
    param number_start: start position for random.randint(start, end)
    param number_end: end position for random.randint(start, end)
    param count: amount line in data set
    param sign_operation: list of basic math operation: +, -, *, /, **, %, //
    """

    import random
    import operator

    sign_operation = sign_operation if sign_operation and type(sign_operation) == list else ['+', '-', '*', '/']

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '//': operator.floordiv,
        '%': operator.mod
    }

    with open(path_file, 'w', encoding='utf8') as file:
        file.write(f'number_1,number_2,answer,operand\n')
        i = 0
        while i < count:
            number_1 = random.randint(number_start, number_end)
            number_2 = random.randint(number_start, number_end)
            operand = random.choice(sign_operation)
            if operand not in '//%' or number_2 != 0:
                answer = operators[operand](number_1, number_2)
            else:
                continue
            line = f'{number_1},{number_2},{answer},{operand}\n'
            file.write(line)
            i += 1


def show_gistogram(path_file: str):
    import pandas as pd
    df = pd.read_csv(path_file)
    # df['species'] = pd.Categorical.from_codes(y, target_names)

    print(df.head())
    # Визуализация при помощи matplotlib
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Построение парных графиков при помощи sns
    sns.pairplot(df, hue='operand')
    plt.show()


if __name__ == '__main__':
    generate_data('examples.csv')
    show_gistogramm('examples.csv')
