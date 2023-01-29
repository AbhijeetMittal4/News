import pyttsx3 as pyt
from  googlesearch import search
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from urllib.request import urlopen


# Constant variables
quit = "Quitquit"
snews = "Newsnews"
my = "Mymy"
cpref = "Cprefcpref"  


# Saved preferences
f = open("data.txt",'r')
f1 = f.read()
mylist = f1.splitlines()
f.close

engine = pyt.init()

def sands(q):
    urlo = urlopen(q)
    st= BeautifulSoup(urlo,"html.parser")
    no1 = 0
    p_tags = st.find_all('p')

    for i in p_tags:
        x = str(i.get_text())
        if len(x)>= 60:
            print(f"{no1}) {x}")
            print(len(x))
            engine.say(x)
            engine.runAndWait()
            if no1 == 6:
                break
            no1 += 1


if __name__ == "__main__":

    engine.say("Hello You fail school college life")
    engine.runAndWait()

    while True:

        print(" To search news enter n\n For News from your preference enter my\n To add or remove preferences enter cpref \n To Quit enter q")
        
        next_step = input("What would you like to do next  -->  ")
        
        if next_step in quit:
            break
        
        elif next_step in snews:
            sq = input("Pls write the news you want to search  -->  ")
            list = []

            for i in search(sq, tld="co.in", num=5, stop=1, pause=2):
                list.append(i)

            rip = list[0]
            print(rip)
            sands(rip)
        
        elif next_step in my:
            print(mylist)
            for i in mylist:
                list = []
                for j in search(i, tld="co.in", num=5, stop=1, pause=2):
                    list.append(j)
                rip = list[0]
                print(rip)
                sands(rip)

        elif next_step in cpref:
            no = 0
            a = input("Would you like to remove or add a preference \n To add enter 'a' to remove enter 'r'  -->  ")
            
            for v in mylist:
                print(f"{no}) {v}")
                no += 1
            print("These are your existing preferences")

            if a == "A" or a == "a":
                b = input("Enter the topic you would like to add to your preferences  --> ")
                mylist.append(b)
                f = open("data.txt",'a')
                f.write(f"\n{b}")
                f.close
            elif a == "R" or a == "r":
                b = input("Enter the topic ou would like to remove from your preferences as it is or its no.  --> ")
                if b.isdigit():
                    b = int(b)
                    del mylist[b]
                    print(mylist)
                else:
                    print("i am str")
                    mylist.remove(b)
                    print(mylist)
                ctxt = open("data.txt","w")
                ctxt.close
                ctxt = open("data.txt","a")
                for y in mylist:
                    if y is mylist[-1]:
                        ctxt.write(f"{y}")
                    else:
                        ctxt.write(f"{y}\n")
                ctxt.close
                    
        #except:
        #    print("Somepthing went wrong")

        else:
            print("Something went wrong pls try again")





             

