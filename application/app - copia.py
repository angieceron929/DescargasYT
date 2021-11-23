from flask import Flask,request,render_template,redirect,url_for,flash
import youtube_dl

app= Flask(__name__)
app.secret_key ='YDdYb'

#Ruta de Inicio
@app.get('/')
def index(): 

    return render_template('/views/index.html')

@app.post('/')
def descarga():

    return "Desarrollo social"


links = [line.strip() for line in open('input.txt')]

tmpdir = "output"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '190',
    }],
    'outtmpl': './output/%(title)s.%(ext)s',
}

""" with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(links)"""
app.run(debug=True, port=5000)
