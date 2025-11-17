str_list=list("abcdefgh")
print(str_list)
first_str=str_list[0:len(str_list)//2:1]
reversed_first=first_str[::-1]
print(first_str)
print(reversed_first)
print("".join(first_str)+"|" + "".join(reversed_first))