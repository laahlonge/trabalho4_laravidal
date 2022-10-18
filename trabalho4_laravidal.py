# Lara Franco Chaves Vidal

import requests
from bs4 import BeautifulSoup

# SITE 1
page1 = "https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html"
html = requests.get(page1).text
soup1 = BeautifulSoup(html, "html.parser")
 
text_array1 = []
get = soup1.find_all('p')
text_dir1 = list(get)

for text in text_dir1:
    text_array1.append(text.get_text())

print(text_array1)

# SITE 2
page2 = "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"
html = requests.get(page2).text
soup2 = BeautifulSoup(html, "html.parser")
 
text_array2 = []
get = soup2.find_all('p')
text_dir2 = list(get)

for text in text_dir2:
    text_array2.append(text.get_text())

print(text_array2)

# SITE 3
page3 = "https://hbr.org/2022/04/the-power-of-natural-language-processing"
html = requests.get(page3).text
soup3 = BeautifulSoup(html, "html.parser")
 
text_array3 = []
get = soup3.find_all('p')
text_dir3 = list(get)

for text in text_dir3:
    text_array3.append(text.get_text())

print(text_array3)

# SITE 4
page4 = "https://monkeylearn.com/natural-language-processing/"
html = requests.get(page4).text
soup4 = BeautifulSoup(html, "html.parser")
 
text_array4 = []
get = soup4.find_all('p')
text_dir4 = list(get)

for text in text_dir4:
    text_array4.append(text.get_text())

print(text_array4)

# SITE 5
page5 = "https://www.tableau.com/learn/articles/natural-language-processing-examples"
html = requests.get(page5).text
soup5 = BeautifulSoup(html, "html.parser")
 
text_array5 = []
get = soup5.find_all('p')
text_dir5 = list(get)

for text in text_dir5:
    text_array5.append(text.get_text())

print(text_array5)
