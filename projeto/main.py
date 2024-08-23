from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.google.com"

browser = webdriver.Edge()
browser.get(url + "/robots.txt")

time.sleep(2)

# /html/body/pre/text()
pre = browser.find_element(By.TAG_NAME, "pre")
# print(pre)
pre_text = pre.text
print(pre_text)

permitidas = []
bloqueadas = []

for i in pre_text.splitlines():
    if i.startswith("Disallow"):
        bloqueadas.append(url + i.split(": ")[1])
    elif i.startswith("Allow"):
        permitidas.append(url + i.split(": ")[1])

# print(permitidas)

with open("links.txt", "w") as arq:
    arq.write("Links Bloqueados:\n")
    for link in bloqueadas:
        arq.write(link + "\n")

    arq.write("\nLinks Permitidos:\n")
    for link in permitidas:
        arq.write(link + "\n")

browser.close()
