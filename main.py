from flask import Flask
import random 
app = Flask(__name__)

gercekler = [
"Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
"Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
"2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."
]

para = ["yazı","tura"]

# http://127.0.0.1:5000/rast_gercek



durum =["iyiyim.","kötüyüm."]


@app.route("/rast_gercek")
def rastgele_gercek():
    return f'<p>{random.choice(gercekler)}</p>'

@app.route("/nasılsın")
def rastgele_durum():
    return f'<p>{random.choice(durum)}</p>'

@app.route("/para")
def paraat():
    return f'<p>{random.choice(para)}</p>'

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1><a href="/rast_gercek"> Rastgele gerçek sayfasına  götür beni.<a href="/para"> Yazı Tura at.'



app.run(debug=True)