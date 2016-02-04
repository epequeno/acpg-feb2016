def say_hello(name, count):
    data = ''
    for i in range(count):
        data += 'Hello {}\n'.format(name.upper())
    return data
