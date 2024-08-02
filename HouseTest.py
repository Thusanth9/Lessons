 

test = [1,2,3,4,5]
count = 0


print("---------------")

for x in range(len(test)):
    print(x)
    #testMethod()


for item in test:
    print(item)

print("--------------")


print("--------------")
while count < 10:
    print("Hello")
    count += 1
print("--------------")



def testMethod(a):
    print(a)
    return 5, 6, 7

a,b,c = testMethod(7)
print(a)
print(b)
