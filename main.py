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
    weather = input("오늘 날씨는 어때요? ")
    if weather == "비" or weather == "눈":
        print("우산을 챙기세요")
    elif weather == "미세먼지":
        print("마스크를 챙기세요")
    else:
        print("준비없이 나가도 돼요")

    temp  = int(input("기온은 어때요? "))
    if 30 <= temp:
        print("너무 더워요. 나가지 마세요")
    elif 10<= temp and temp <30:
        print("괜찮은 날씨에요")
    elif 0<=temp and temp <10:
        print("외투를 챙기세요")
    else:
        print("너무 추워요. 나가지 마세요")

def for_study():
    # print("for구문 시작")
    # print("대기번호 : 1")
    # print("대기번호 : 2")
    # print("대기번호 : 3")
    # print("대기번호 : 4")

    for waiting_num in [1,2,3,4,5]:
        print("대기번호 : {0}".format(waiting_num))

    for waiting_num in range(5):
        print("대기번호 : {0}".format(waiting_num))

    starbucks = ["아이언맨", "토르", "아이엠그루트"]
    for customer in starbucks:
        print("{0}, 커피가 준비되었습니다.".format(customer))

def while_study():
    print("while문 스터디 시작")
    customer = "토르"
    index = 5
    while index>=1:
        print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer,index))
        index -= 1
        if index == 0:
            print("커피는 폐기처분되었습니다.")

    customer ="아이언맨"
    index = 1
    while True:
        print("{0}, 커피가 준비 되었습니다. 호출 {1}".format(customer,index))
        index +=1
        if index >= 100000:
            break

    customer = "토르"
    person = "Unknown"

    while person != customer:
        print("{0}, 커피가 준비 되었습니다.".format(customer))
        person =input("이름이 어떻게 되세요 ? ")

def continue_break():
    print("continue%break 스터디 시작")
    absent = [2,5]
    no_book = [7]
    for student in range(1,11):
        if student in absent:
            continue
        elif student in no_book:
            print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
            break
        print("{0}, 책을 읽어봐".format(student))

    students =[1,2,3,4,5]
    print(students)
    students = [i+100 for i in students]
    print(students)

    students = ["Iron man", "Thor", "I am groot"]
    #students = [len(i) for i in students]
    #print(students)

    students = [i.upper() for i in students]
    print(students)

def exam_5():
   import random

   print("exam 5 시작")
   customer =[]
   for i in range(50):
       customer.append(0)

   for i in range(0,50):
       customer[i] = random.randint(5,51)

   count = 0
   for i in range(0,50):  

    if(customer[i] >= 5 and customer[i] <= 15):
       count +=1
       print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i + 1, customer[i]))
    else:
       print("[] {0}번째 손님 (소요시간 : {1}분)".format(i + 1, customer[i]))

   print("총 탑승 승객 : {0} 분".format(count))

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
   #if_study()
   #for_study()
   #while_study()
   #continue_break()
   exam_5()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
