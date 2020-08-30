# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hi, {0}, {1}".format(name,"test"))

def url_pw_Creat(url):
    Start_index = url.find("/",url.find("/")+1) +1
    End_index = url.find(".")
    Re_url = url[Start_index:End_index]
    pw = Re_url[:3] + str(len(Re_url)) + str(Re_url.count("e")) + "!"
    print(pw)
# Press the green button in the gutter to run the script.

def list_study():
    subway = ["유재석","조세호","박명수"]
    print(subway)

    print(subway.index("조세호"))

    subway.append("하하")
    print(subway)

    subway.insert(1,"정형돈")
    print(subway)

    subway.pop()
    print(subway)

    # subway.pop()
    # print(subway)
    #
    # subway.pop()
    # print(subway)

    subway.append("유재석")
    print(subway)
    print(subway.count("유재석"))

    num_list = [5,2,3,4,1]
    num_list.sort()
    print(num_list)

    num_list.reverse()
    print(num_list)

    num_list.clear()
    print(num_list)

    mix_list = ["조세호", 20, True]
    print(mix_list)

    num_list.extend(mix_list)
    print(num_list)

def dictionary_sutdy():
    print("시작")
    cabinet = {3:"유재석",100:"김태호"}
    print(cabinet[3])
    print(cabinet[100])

    print(cabinet.get(3))

    #print(cabinet[5])
    print(cabinet.get(5))
    print(cabinet.get(5,"사용가능"))
    print("hi")

    print(3 in cabinet)
    print(5 in cabinet)

    cabinet2 = {"A-3":"유재석", "B-100":"김태호"}
    print(cabinet2["A-3"])
    print(cabinet2["B-100"])

    print(cabinet2)
    cabinet2["A-3"] = "김종국"
    cabinet2["c-20"] = "조세호"
    print(cabinet2)

    del cabinet2["A-3"]
    print(cabinet2)

    print(cabinet2.keys())
    print(cabinet2.values())

    print(cabinet2.items())

    cabinet2.clear()
    print(cabinet2 )

def tuple_study():
    print("튜플시작")
    menu = ("돈까스", "치즈까스")
    print(menu[0])
    print(menu[1])

    # name = "김종국"
    # age = 20
    # hobby = "운동"
    # print(name,age, hobby)

    (name, age, hobby) = ("김종국", 20, "운동")
    print(name, age, hobby)

def set_study():
    print("집합시작")
    my_set = {1,2,3,3,5}
    print(my_set)

    java = {"유재석", "김태호","양세형" }
    python = set(["유재석", "박명수"])

    #교집합
    print(java & python)
    print(java.intersection((python)))
    #합집합
    print(java | python)
    print(java.union(python))

    print(java-python)
    print(java.difference((python)))

    python.add("김태호")
    print(python )

    java.remove("김태호")
    print(java)
def struct_cast():
    print("자료구조의 변경")
    menu = {"커피", "우유", "주스"}
    print(menu)
    print(menu, type(menu))

    menu = list(menu)
    print(menu, type(menu))

    menu = tuple(menu)
    print(menu, type(menu))

    menu = set(menu)
    print(menu, type(menu))

def exam_1():
    print("예제문제1 시작")

    people = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    people2 = list(range(1,21))

    shuffle(people)
    chicken = sample(people, 1)
    people.remove(chicken[0])
    coffee = sample(people, 3)
    print("-- 당첨자 발표 --")
    print("치킨 당첨자 : {}".format(chicken[0]))
    print("커피 당첨자 : {}".format(coffee))
    print("-- 축하합니다. --")

def if_study():
    print("if문 시작")
    print("test")


if __name__ == '__main__':
   from random import *
   #print_hi('PyCharm')
   #  url_pw_Creat("http://naver.com")
   #list_study()
   #dictionary_sutdy()
   #tuple_study()
   #set_study()
   # struct_cast()
   #exam_1()
   if_study()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
