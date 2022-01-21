try: 
    fo = open('nari.txt')
    print(fo.read())
    fo.close()
# Exception outputs the Runtime error that occurs when the the try section fails
except Exception as e:
    print(e)
finally:
    print("This executes after the try and except sections")