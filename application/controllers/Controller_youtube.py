from re import I
from application import app
from flask import Flask,request,render_template,redirect,url_for,flash
import youtube_dl

#Ruta Index- Inicio
@app.get('/')
def index(): 
    return render_template('index.html')

@app.post('/')
def descarga():
   # links = [line.strip() for line in open('input.txt')]

    #tmpdir = "output"
    tipo_descarga = request.form.get('tipo')
    link = request.form.get('Dlink')
    print(link)
    #Opciones de video
    #                  1080p                    720p                    480p 
    if tipo_descarga == "398" or tipo_descarga == "136" or tipo_descarga=="135":
        ydl_opts = {
        'format': tipo_descarga,
        'outtmpl': '/output/%(title)s.%(ext)s',
        'noplaylist ': True,
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.cache.remove()
                ydl.download([link])
            flash('Video descargado en directorio',"badge bg-success")
        except Exception:
            flash('Direccion no valida, o calidad no existe',"badge bg-danger")
            return redirect(url_for('index')) 
    elif tipo_descarga == "128" or tipo_descarga =="192" or tipo_descarga=="320":
        #Opciones de Musica
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': tipo_descarga,
        }],
        'outtmpl': './output/%(title)s.%(ext)s',
        }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            flash('Cancion descargada en directorio',"badge bg-success")
        except Exception:
            flash('Direccion no valida, o calidad no existe',"badge bg-danger")
            return redirect(url_for('index')) 
    else:
        flash('El valor no es correcto ',"badge bg-danger")  
    return redirect(url_for('index'))

