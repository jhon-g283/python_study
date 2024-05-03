# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

a = 100
tax = 0.1
b , c= (10,20)
print(a,tax)
print(b,c)
string = "unko!"
print(string.upper())
print(string.capitalize())
print(string.replace("!","?"))
print(type(a))
print(type(string))

num_1 = 100
num_2 = 200
num_3 = num_1+ num_2
num_4= 1/1

float_1 = 1.5
float_2 = 2.5
float_3 = float_1 + float_2
num_float = num_3/float_1
print(num_3,type(num_3))
print(float_3,type(float_3))
print(num_float,type(num_float))
print(num_4,type(num_4))

hundred = 10*10
hundred_2 = 10**2 #2乗
hundred_3 = 10 // 3 #商が返ってくる


print(hundred,hundred_2)
print(hundred_3)
print("py" * 2) #文字列を繰り返す
print("-" * 20) #文字列を繰り返す
jojo = "空条" + "丈太郎"
ora = "オラ" * 20

print(jojo + " " + ora)
print(f"{jojo}  スタープラチナ！ {ora}") #フォーマット文字列

p = "python"
result1 = "thon" in p #thon is contained
result2 = "son" in p #son is not contained
print(result1,result2)

print (5 in [1,2,3,4,5])
print (0 in [1,2,3,4,5])
print (6 not in [1,2,3,4,5])

in_5 =  5 in [1,2,3,4,5]
in_0 = 0 in [1,2,3,4,5]
not_in_6 = 6 not in [1,2,3,4,5]

print(in_5 and not_in_6)
print(in_5 or in_0)

my_list = [1,2,3,4,5,"a","b","c","d","e"]
print(my_list[0],my_list[6],type(my_list))
print("last item is : " + my_list[-1])
print( my_list[0:5])
print( my_list[:10]) # 0省略
print( my_list[5:]) # 以降のものすべて出す
print( my_list[5::2]) #　２つとばしでだす
print( my_list[::2]) # 2つずつ出す

s= "Python"
print(s[1])
s= "T1-2345-6789"
print(s[1:].replace("-","")) # 1文字以降のものでハイフンを消す

my_list.append("f")
print(my_list)
my_list2 = [1,2,3,4,5,6,7,8,9,10]
print(my_list2.sort())

has_10 = "10" in my_list2
print(has_10)
has_10 = 10 in my_list2
print(has_10)

my_list_nest = [[1,2,3],[4,5,6],[7,8,9]]

print(my_list_nest[0])
print(my_list_nest[0][1])
print(my_list_nest[0][1:])
my_list_nest.append(1)
my_list_nest.append([10,11,12])
print(my_list_nest)

my_list_nest.append([[13,14,15],[16,17,18]])
print(my_list_nest[-1][0][-1])
prompt = {"role":"user","content":"Hello"}
print(prompt["role"])
print(prompt["content"])
#print(prompt[-1]) # ひょうじしない
prompt["role"] = "AI"
print(prompt)
has_content = "content" in prompt
print(has_content)
print(prompt.values())
print(prompt.keys())
print(prompt.items())

my_dict = {"name":"Jhon","age":"36","copuontry":"Norway"}
age = my_dict["age"]
print(age)
# city = my_dict["city"]
# print(city)
city = my_dict.get("city")
print(city) #None
city = my_dict.get("city","-からの時には代わりに出す文字を設定可能-") #
print(city) #None

a,b=10,100
print(a,b)
c = 10,100 #tuple Type
print(c,type(c))

my_tuple = (1,2,3,4,5)
print(my_tuple)
not_tuple = (1)
its_tuple = 1,

print(not_tuple,type(not_tuple))
print(its_tuple,type(its_tuple))

langs = ["Python","Java","C++","C#","Javascript","PHP","Swift"]

for num, lang in enumerate(langs,start=1):print(num,lang)

def foo(Money):
    return  Money*2,"coment:This is Function"

resutlMoney = foo(100)
print(resutlMoney)


age = 18
age = age-1
if age >= 18 :
    print(age,":can drink")
else:
    print(age,"dont drink!")

    money = 1000

money=500
if money >= 1000:
    print("マグロ")
elif money >= 800:
    print("エビ")
else:
    print("食べられない")

moji ="Python"
if moji !="":
        print("Not Empty")
else:
        print("Empty")


list = [1,2]
if list[0] =="":
     print("Not Empty")
else:
     print("Empty")

like_baseball = False
like_football = True

if like_football and like_baseball:
    print("soccer and baseball")

elif like_baseball or like_football:
    print("soccer or baseball")
    if like_baseball:
        print("baseball")
    else:
        print("soccer")
else:
    print("nothing")

string = "Python"
for s in string:
    print(s)

day = ["M","Tu","W","Th","F","St","Su"]

for d in day:
    print(d)

dayList = {"M":"1","Tu":"2","W":"3","Th":"4","F":"5","St":"6","Su":"7"}

for d in dayList:
    print(f"曜日：{d},は{dayList[d]}日目")

for d in dayList.values():
    print(f"valuesでとりだすことがかのう:{d}")

for key,val in dayList.items():
    print(f"itemsではキーとValueとしてとりだすことがかのう　key:{key}  val:{val}")

contries = ["India","USA","UK","Canada","Australia"]


for num,country in enumerate(contries):
    print(num,country)

contries2 = {"India": "New Delhi","USA": "Washington DC","UK": "London","Canada": "Otawa","Australia": "Canbera"}

for num,ctiy2 in enumerate(contries2.items()):
    print(num,ctiy2)

for num,(cnt2,ctiy2) in enumerate(contries2.items(),start=3):
    print(num,cnt2,ctiy2)

import random

# Press the green button in the gutter to run the script.
print("-*-"*30)
if __name__ == '__main__':
    print_hi('PyCharm')

#---------------------------------
print("-+-" * 30)

"""
    import random
    
    money = int(input("plaese input money"))
    
    while money >= 100:
        money -= 100
        gacha = random.randint(1,100)
    
        if gacha == 1:
            print("SSR")
        elif gacha <= 5:
            print("SR")
    
        else:
            print("R")

"""

for _ in range(99):

    if _== 10:
        break
    print(_)

    print("break loop ")

for _ in range(100):

    if _%2 == 0:
        continue
    print(_,":continueで偶数スキップ")

def greet(name = "Default name",age="??"):
    """


    :param name:なまえ
    :param age: ねんれい
    :return:
    """
    print("Hello,World")
    print(f"I am {name} and {age} years old")
    print("Nice to meet you",end="\n\n")

    greet_message = ["My name is",f"{name} . and ",f"I am {age} years old","Thank you!"]


    return "\n".join(greet_message)


aliceInfo= greet("Alice",15)
DefaultInfo= greet()
IkumaInfo = greet(name = "Ikuma")

print(aliceInfo)

def goodMorning():
    # 何もしないときはPassを書くこと
    pass

"""
    num= input("input number")
    
    try:
        num = int(num)
        num = num/0
    except ValueError as e:
    
        print(f"{e} is Validation Exception please input number")
    
    except ZeroDivisionError as e:
    
        print(f"{e} is ZeroDivisionError Exception please input number")
    
    else:
        print(num + 10)
    
    finally:
        print("exit Execution")
"""

def ask_age():
    while True:
        try:
            age = int(input("input your Age"))

            if age >= 120:
                raise ValueError("Over 120 !!!!")

        except ValueError as ValuOf_Error:
            print(f"Error is -- {ValuOf_Error}")

        else:
            return age

user_age = ask_age()
print(f"your age is {user_age}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
