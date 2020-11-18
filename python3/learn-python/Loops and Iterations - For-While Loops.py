############### for ###################
nums = [1, 2, 3, 4, 5]

# simple loop
for num in nums:
    print(num)

# break keyword
for num in nums:
    if num == 3:
        print("found")
        break
    print(num)

# continue keyword
for num in nums:
    if num == 3:
        print("found")
        continue
    print(num)

# nested loop
for num in nums:
    for letter in 'abc':
        print(num, letter)

# range()
for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

############## while #################
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x = x + 1

### infinity loop ###
# while True:
#     print(x)
#     x = x + 1
