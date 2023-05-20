#print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    print('start')
    print(error)
    print('No errors')
except:
    print('We have an error')

print('Next code')