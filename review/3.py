# f = open("test", "w")
# print("hello", "friends", sep="-", end=" ", file=f)
# print("How Are You Today?", file=f)

# import time
# message = "hello friends. How Are You Today?"
# for c in message:
#     print(c, end="", flush=True)
#     time.sleep(0.2)

# t = (1,)
# t += (2,3)
# print(t)
# لیست = [2,4,6,-3,0,100]
# لیست.sort(reverse=True)
# print(لیست)

# heights = []
# for i in range(3):
#     heights.append(float(input("enter your height: ")))
    
# c = 0
# for i in range(len(heights)):
#     if 170 <= heights[i] < 180:
#         c += 1
        
# print(c)

# names = []
# c = 0
# for i in range(5):
#     names.append(input("enter a name: "))
#     if names[-1][0].lower() == "a":
#         c += 1
        
# print(c)


scores = [12,13,14,15]
for i in range(len(scores)):
    scores[i] += 2
print(scores)