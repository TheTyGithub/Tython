import RosBasic

while True:
    text = input('RosBasic > ')
    result, error = RosBasic.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)