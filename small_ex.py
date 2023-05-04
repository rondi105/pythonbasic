import calendar

def pigs():
    num=int(input("enter a num that will represent the bricks of the pigs: "))
    one=num%10
    two=(num//10)%10
    three=num//100
    sum=one+two+three
    print("the sum is ", sum)
    print("each pig will get ", sum//3)
    print("the remainder of the dividing : " ,sum%3)
    print("the sum is divisible without remainder :" ,sum%3==0)

def replace_with_first_letter():
    str =input("Please enter a string: ")
    first=str[0]
    replaced=str.replace(first[0],"e")
    print(first+replaced[1:])

def half_big_half_small():
    str =input("Please enter a string: ")
    print(str[:len(str)//2].lower()+str[len(str)//2:].upper())

def palindrom():
    str =input("Please enter a string: ")
    if(str==str[-1::-1]):
        print("OK")
    else:
        print("NOT")

def deegrees():
    str =input("Please enter a string: ")
    amount=float(str[:-1])
    type=str[-1]
    if(type=="C" or type=="c"):
        hamara=(9*amount+32*5)/5
        print(hamara,"F")
    elif(type=="F" or type=="f"):
        hamara=(5*amount-160)/9
        print(hamara,"C")
    else:
        print("invalid input, try again")
        deegrees()

def week_day():
    str =input("Please enter a date with dd/mm/yyyy: ")
    datelist=str.split("/")
    daynum=calendar.weekday(int(datelist[2]),int(datelist[1]),int(datelist[0]))
    print(calendar.day_name[daynum])

def last_early(my_str):
    return my_str[-1] in my_str[:-1]

def distance(num1, num2, num3):
    return ((abs(num1 - num2)==1 or abs(num1 - num3)==1) and
            ((abs(num2 - num1) >= 2 and abs(num2 - num3) >= 2) or
           (abs(num3 - num1) >= 2 and abs(num3 - num2) >= 2)))

def filter_teens(a=13, b=13, c=13):
    return  fix_age(a)+fix_age(b)+fix_age(c)
def fix_age(age):
    if(age>=13 and age<15 or age>16 and age<=19):
        return 0
    else:
        return age


def chocolate_maker(small, big, x):
    max_big = x // 5
    remaining_length = x - max_big * 5
    num_small = min(remaining_length, small)
    return num_small + max_big * 5 == x and big >= max_big


def shift_left(my_list):
    shifted_list = [my_list[1], my_list[2], my_list[0]]
    return shifted_list


def format_list(my_list):
    even_list = my_list[::2]
    even_str = ", ".join(even_list)
    last_elem = my_list[-1]
    final_str = even_str+", and "+ last_elem
    return final_str

def extend_list_x(list_x, list_y):
    newlist=list_y
    for item in list_x:
        newlist.append(item)
    list_x=newlist
    return list_x

def are_lists_equal(list1, list2):
    return sorted(list1)==sorted(list2)

def longest(my_list):
    sortedlist=sorted(my_list,key=len)
    return sortedlist[-1]

def squared_numbers(start, stop):
    list=[]
    while (start<=stop):
        list.append(start**2)
        start+=1
    return list

def is_greater(my_list, n):
    bigger=[]
    for element in my_list:
        if (element>n):
            bigger.append(element)
    return bigger
def numbers_letters_count(my_str):
    digits=0
    letters=0
    for tav in my_str:
        if(str(tav).isdigit()):
            digits+=1
        else:
            letters+=1
    return [digits,letters]
def seven_boom(end_number):
    list=[]
    for i in range(end_number+1):
        if(i%7==0 or '7' in str(i)):
            list.append('BOOM')
        else:
            list.append(i)
    return list
def sequence_del(my_str):
    new_str=" "
    last_i=0
    for tav in my_str:
        if(tav!=new_str[last_i]):
            new_str=new_str+tav
            last_i+=1
    return new_str[1:]

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

def shopping_list():
    string=input("Enter the list supperated with ',' : ")
    lst=string.split(',')
    exited=False
    while not exited:
        num=int(input("Enter a digit"))
        if(num==1): #printlist
            print(lst)
        elif (num == 2):  # print len
            print(len(lst))
        elif (num == 3):  # print is in list
            item = input("enter an item : ")
            print(item in lst)
        elif (num == 4):  # print count item in list
            item = input("enter an item : ")
            print(lst.count(item))
        elif (num == 5):  # del one item
            item = input("enter an item : ")
            lst.remove(item)
        elif (num == 6):  # add item
            item = input("enter an item : ")
            lst.append(item)
        elif (num == 7):  # print illigal
            for item in lst:
                if(len(item<3) or not item.isalpha()):
                    print(item)
        elif (num == 8):  # remove kfilut
            remove_duplicates(lst)
        elif (num == 9):  # exit
            exited=True

def arrow(my_char, max_length):
    arrow_list = []
    for i in range(1, max_length+1):
        arrow_list.append(my_char * i)
    for i in range(max_length-1, 0, -1):
        arrow_list.append(my_char * i)
    return '\n'.join(arrow_list)

def sort_prices(list_of_tuples):
    sorted_list = sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)
    return sorted_list

def mult_tuple(tuple1, tuple2):
    product = []
    for x in tuple1:
        for y in tuple2:
            product.append((x, y))
            product.append((y, x))
    return tuple(product)


def sort_anagrams(list_of_strings):
    # Create an empty dictionary to store lists of anagrams
    anagram_dict = {}

    # Iterate over each word in the list
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    sorted_anagrams = []
    for key in anagram_dict:
        sorted_anagrams.append(anagram_dict[key])

    return sorted_anagrams

def dict_ex():
    dic={}
    dic["first_name"]="Maraiah"
    dic["last_name"]="Carey"
    dic["birth_date"]="27.03.1970"
    dic["hobbies"]=["Sing","Compose","Act"]
    num=int(input("enter a num: "))
    if (num == 1):  # print last name
        print(dic["last_name"])
    elif (num == 2):  # print month
        print(dic["birth_date"].split(".")[1])
    elif (num == 3):  # print the num of hobbies
        print(len(dic["hobbies"]))
    elif (num == 4):  # print last hobbie
        print(dic["hobbies"][-1])
    elif (num == 5):  # add Cooking
        dic["hobbies"].append("Cooking")
    elif (num == 6):  # tuple date
        dic["hobbies"]= tuple(dic["hobbies"])
        print(dic["hobbies"])
    elif (num == 7):  # print illigal
        dic["age"]=53

def count_chars(my_str):
    char_count = {}
    for char in my_str:
        if char != " ":
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def inverse_dict(my_dict):
    inverse = {}
    for key, value in my_dict.items():
        if value not in inverse:
            inverse[value] = [key]
        else:
            inverse[value].append(key)
    for key in inverse:
        inverse[key].sort()
    return inverse


def are_files_equal(file1, file2):
    file1=open(file1,"r")
    file2=open(file2,"r")
    file1_text=file1.read()
    file2_text=file1.read()
    return file1_text==file2_text

def files_actions():
    path = input("enter file path")
    action = input("enter action (last ,rev or sort)")
    file=open(path,"r")
    file_text=file.read()
    if(action=="sort"):
        print(file_text.split().sort())
    elif(action=="rev"):
        print(file_text[-1::-1])
    elif(action=="last"):
       n= int(input("enter a number : "))
       words=file_text.split();
       print(words[-n:])
    file.close()

def copy_file_content(source, destination):
    file1 = open(source, "r")
    file2 = open(destination, "w")
    file1_text = file1.read()
    file2.write(file1_text)
    file1.close()
    file2.close()
def who_is_missing(file_name):
    file1 = open(file_name, "r")
    file1_text=file1.read()
    list=sorted(file1_text.split(","))
    for i in range (len(list)-1):
        if(int(list[i+1])>int(list[i])+1):
            print(int(list[i])+1)
    file1.close()

def my_mp3_playlist(file_path):
    with open(file_path, 'r') as f:
        playlist = f.read().split("\n")
    playlist = [song.strip().split(';') for song in playlist]
    longest_song = max(playlist, key=lambda x: x[2])[0]
    num_songs = len(playlist)

    performers = {}
    for song in playlist:
        performer = song[1]
        if performer in performers:
            performers[performer] += 1
        else:
            performers[performer] = 1

    most_common_performer = max(performers, key=performers.get)

    return (longest_song, num_songs, most_common_performer)

def my_mp4_playlist(file_path, new_song):
    with open(file_path, "r") as file:
        lines = file.read().split("\n")
    while len(lines) < 3:
        lines.append("\n")
    parts = lines[2].split(";")
    parts[0] = new_song
    lines[2] = ";".join(parts)

    with open(file_path, "w") as file:
        file.writelines(lines)

    with open(file_path, "r") as file:
        print(file.read())

def main():
    print(my_mp3_playlist("file.txt"))
if __name__ == "__main__":
    main()