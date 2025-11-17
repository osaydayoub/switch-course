INPUT_LENGTH = 15
GREEN = "\033[92m"
RED = "\033[91m"
BLUE ="\033[94m"
RESET = "\033[0m"

# def is_palindrome(text):
#     left = 0
#     right = len(text)-1
#     while left < right:
#         if(text[left] != text[right]):
#             return False
#         left+=1
#         right-=1
#     return True

def is_palindrome(text):
    return text == text[::-1]

# def is_all_lowercase(text):
#     for i in range(len(text)) :
#         if not (text[i]>="a" and text[i]<='z'):
#             return False
#     return True

def is_all_lowercase(text):
    for char in text:
        if not ("a" <= char <= "z"):
            return False
    return True

def is_all_digits(text):
    for char in text:
        if not("0"<=char<="9"):
            return False
    return True


def is_longer_than(text, threshold=INPUT_LENGTH):
    return len(text)>threshold

def is_empty(text):
    return len(text) == 0
def exit_app():
    print("Exit successfully")

operations = {
    "1": ("Palindrome", "Check if the input is palindrome", is_palindrome),
    "2": ("Lower", "Check if all characters in the input are lowercase", is_all_lowercase),
    "3": ("Digit", "Check if all characters in the input are digits", is_all_digits),
    "4": ("Long", "Check if the input length is longer than "+RED+str(INPUT_LENGTH), is_longer_than),
    "5": ("Empty", "Check if the input is empty", is_empty),
    "6": ("Exit", "Exit successfully from the application", exit_app)
}

running = True
while running:
    print(f"{RED}The available operations are:{RESET}")
    for key,op in operations.items():
        print(f"{RED}{key} - {op[0]}: {GREEN}{op[1]}")
    print()
    op_number = input(f"{RED}Please enter the number of the operation you choose: ")
    op = operations.get(op_number)
    if(op!=None):
        text_input = input(f"Enter an input: {GREEN}")
        if(op_number != "6"):
            result = op[2](text_input)
            print(f"{RED}The answer is: {BLUE}{result}{RESET}")
        else:
            op[2]()
            running = False
    else:
        print(f"{RED}Invalid option. Please try again.{RESET}")
    print(f"{RESET}")
    