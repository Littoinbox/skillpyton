# -*- coding: utf-8 -*-

def echo(value=None):
    print(f"Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                print(f'Before yield {value}')
                value = yield value
                print(f'After yield {value}')
            except Exception as e:
                print(f'Exception as {e}')
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")


def update_gen(gen):
    gen.send(5)
    # gen.send(6)


generator = echo(1)
print(next(generator))
generator.send(34)
print(next(generator))
# update_gen(gen=generator)
# print(next(generator))
# print(generator.close())
# print(next(generator))
# print(generator.send(2))
# print(next(generator))
# print(generator.send(3))
# print(next(generator))
