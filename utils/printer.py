GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def print_header(title="", length=50):
      title = title.center(length, "=")
      return print("\n",GREEN, title,RESET)

