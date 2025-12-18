# def print_stars(n):
#     if(n==1):
#         print("*")
#         return
#     print_stars(n-1)
#     current_stars=""
#     for i in range(n):
#         current_stars +="*"
#     print(current_stars)

def print_stars(n):
    if(n==1):
        print("*")
        return
    print_stars(n-1)
    print("*"*n)

    
print_stars(4)
