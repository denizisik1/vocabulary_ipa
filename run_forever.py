from time import sleep

def run_forever():
    try:
        # Create infinite loop to simulate whatever is running
        # in your program
        while True:
            print("Hello!")
            sleep(10)

            # Simulate an exception which would crash your program
            # if you don't handle it!
            raise Exception("Error simulated!")
    except Exception:
        print("Something crashed your program. Let's restart it")
        run_forever() # Careful.. recursive behavior
        # Recommended to do this instead
        handle_exception()

def handle_exception():
    # code here
    pass

run_forever()
