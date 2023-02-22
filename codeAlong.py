# print("Hello world")

# age = 19

# if age >= 21:
#     print("youre good to go")
# elif age < 21:
#     print("are you a super model? NO! GET OUT OF HERE")

# num = 0

# while num <= 100:
#     if(num) == 50:
#         break
#     print(num)
#     num = num +10

# print("ALL DONE")

target = 37
guess = None

while guess != target:
    guess = input('Please enter a guess: ')
    guess = int(guess)

print("all done")


for snack in [1,2,3,4,5]:
    print(f"i ate a {snack}")