import requests
from bs4 import BeautifulSoup as bs

class Kompas:
	def GetHeadlines(self, url, jawaban=0):
		page = requests.get(url)
		soup = bs(page.content, 'html.parser')
		results = soup.find('h1', class_="read__title")
		print(results.text)

if __name__ == '__main__':
    Kompas = Kompas()
	# Kompas.GetHeadlines('https://regional.kompas.com/read/2020/06/19/09280071/setelah-diisolasi-3-bulan-dan-14-kali-swab-test-pria-ini-dinyatakan-sembuh')
    Kompas.GetHeadlines('https://regional.kompas.com/read/2020/06/19/09300041/upaya-damai-kasus-sopir-anggota-dprd-jabar-pukul-staf-hotel-bertepuk-sebelah')