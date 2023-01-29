from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyttsx3

engine = pyttsx3.init()
q = "https://www.theatlantic.com/newsletters/archive/2023/01/tech-layoff-contagion-economy/672826/?utm_source=pocket-newtab-intl-en"
qq = "https://www.inverse.com/mind-body/spices-microbiome-detox?utm_source=pocket-newtab-intl-en"

a = urlopen(qq)
o = BeautifulSoup(a,"html.parser")
n = 0


p_tags =  o.find_all("p")
for i in p_tags: 
    x = str(i.get_text())
    print(f"{n}) {x}")
    engine.say(x)
    engine.runAndWait()
    if n == 6:
        break    
    n += 1