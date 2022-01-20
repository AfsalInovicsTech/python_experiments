


def double_previos_result(number):
    def inner_func():
        nonlocal number
        number *= 2
        return number
    return inner_func
