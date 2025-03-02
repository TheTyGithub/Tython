import Tython

while True:
    text = input('Tython > ')
    result, error = Tython.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)