# sent = input("enter something: ")
# # print(len(set(sent)))
# temp = []
# for ch in sent:
#     if ch not in temp:
#         temp.append(ch)
# print(len(temp))
        



from functools import partial, reduce
 
 
# def power(a, b):
#     return a**b
 
 
# # partial functions
# pow2 = partial(power, b=2)
# pow4 = partial(power, b=4)
# power_of_5 = partial(power, 5)
 
# print(power(2, 3))
# print(pow2(5))
# print(pow4(3))
# print(power_of_5(2))
 
# print('Function used in partial function pow2 :', pow2.func)
# print('Default keywords for pow2 :', pow2.keywords)
# print('Default arguments for power_of_5 :', power_of_5.args)


# x = [1,2,3]
# res = reduce(lambda x1,x2:x1+x2, x)
# print(res)
# import json
# from tkinter import *
# window = Tk()

# employee = {}

# def register():
#     employee.update(
#         {
#             'name':user_name_value.get(),
#             'age':age_value.get(),
#             'department':department_value.get(),
#         }
#     )
    
#     employee_json = json.dumps(employee)
#     with open("employees", "a") as f:
#         f.write(employee_json)



# user_name_value = StringVar()
# frame1 = Frame(window)
# frame1.pack()

# Label(frame1, text="username", width=15, anchor="w").pack(side="left")
# user_name_entry = Entry(frame1, textvariable=user_name_value)
# user_name_entry.pack(side="right")

# age_value = StringVar()
# frame2 = Frame(window)
# frame2.pack()

# Label(frame2, text="age", width=15, anchor="w").pack(side="left")
# age_entry = Entry(frame2, textvariable=age_value)
# age_entry.pack(side="right")

# department_value = StringVar()
# frame2 = Frame(window)
# frame2.pack()

# Label(frame2, text="department", width=15, anchor="w").pack(side="left")
# department_entry = Entry(frame2, textvariable=department_value)
# department_entry.pack(side="right")

# Button(window, text="Register", command=register).pack()

# window.mainloop()


# s = ['Dave', 'Cynthia', 'Alice', "am", "a", "amir", "sara"]

# s.sort()
# print(s)
# s.sort(key= lambda e:len(e))
# print(s)

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar"))

def is_palidrome(s):
    for i in range(len(s)//2):

        if s[i] != s[len(s)-1-i]:
            return False
    return True
print(is_palindrome("racecar"))

def is_palindrome(s):
    
    rev = ''.join(reversed("racecar"))
    if s == rev:
        return True
    return False
print(is_palindrome("racecar"))



def is_palindrome(d1):
    d2 = ""
    for s in d1:
        d2 = s + d2

    if d1 == d2:
        return True
    return False

print(is_palindrome("racecar"))


def is_palindrome(s):
    l = len(s)
    if l < 2:
        return True
    elif s[0] == s[l -1]:
        return is_palindrome(s[1:l-1])
    else:return False
    
print(is_palindrome("racecar"))

