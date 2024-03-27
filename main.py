import time
import requests
import playaudio
from bs4 import BeautifulSoup

fail_dir = r"C:\Users\Piotr Szkudlarek\Downloads\fail.mp3"
trumpet_dir = r"C:\Users\Piotr Szkudlarek\Downloads\effect.mp3"
prosperity_dir = r"C:\Users\Piotr Szkudlarek\Downloads\pomyslnosc.mp3"
all_laureates = []

def check_idub_resuts():
    global fail_dir, trumpet_dir
    idub_page = "https://inicjatywadoskonalosci.uw.edu.pl/dzialania/iv-4-1/rozprawy2/"
    req = requests.get(idub_page)
    all_laureates = []
    website_got = False
    if req.status_code == 200:
        website_got = True
    if website_got:
        soup = BeautifulSoup(req.text, features="lxml")
        all_h3s = soup.findAll("h3")
        headers_texts = []
        for header in all_h3s:
            headers_texts.append(header.text)
        print(headers_texts)
        if "POB II" in headers_texts:
            playaudio.playaudio(prosperity_dir)
            time.sleep(30)
        all_lis = soup.findAll("li")
        for li in all_lis:
            if "Szkoła Doktorska Nauk" in li.text and "mgr " not in li.text:
                all_laureates.append(li.text)
    else:
        playaudio.playaudio(fail_dir)
    if len(all_laureates) > 57:
        playaudio.playaudio(trumpet_dir)
        print("Pojawili Się nowi laureaci!")
        print(len(all_laureates))
        for i in all_laureates:
            print(i)

while True:
    check_idub_resuts()
    time.sleep(60)
