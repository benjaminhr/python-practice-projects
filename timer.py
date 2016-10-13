import threading

def bang():
    threading.Timer(0.5, bang).start()
    print("Nigger")
    threading.Timer(0.5, bang).start()
    print("Neekeri")

def main():
    bang()
    return 0

if __name__ == '__main__':
    main()
