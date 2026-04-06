import requests
from bs4 import BeautifulSoup
import json

url = "https://informatika.umsida.ac.id/mata-kuliah-game-latih-mahasiswa-informatika-umsida-jadi-kreatif/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Ambil judul
judul = soup.find("h1").text.strip()

items = soup.find_all("li")

materi = [item.text.strip() for item in items]

# Struktur data
data = {
    "judul": judul,
    "materi_pembelajaran": materi
}

# Simpan ke JSON
with open("C:/Users/bimaa/Downloads/hasil_scraping.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Data berhasil disimpan!")