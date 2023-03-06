from pytube import YouTube,Playlist
import os
from moviepy import *
from moviepy.editor import *

path = "downloads"

def DownVideo():
    url = input("Digite a url do video: ")
    video = YouTube(url)
    titulo = video.title.replace("/","")
    titulo = titulo.replace("|","")
    titulo = titulo.replace(",","")
    titulo = titulo.replace(";","")
    titulo = f"%s" %(titulo)
    print(titulo)

    print(video.streams.get_by_itag("140").download(filename=f"%s.mp4" %(titulo),output_path=path))
    Convert(titulo)


def DownPlaylist():
    url = input("Digite a url da playlist: ")
    p = Playlist(url)
    for video in p.videos:
        titulo = video.title.replace("/","")
        titulo = titulo.replace("|","")
        titulo = titulo.replace(",","")
        titulo = f"%s" %(path,titulo)
        print(video.streams.get_by_itag("140").download(filename=f"%s.mp4" %(titulo),output_path=path))
        Convert(titulo)


def Convert(titulo):
    videoToconvert = AudioFileClip(f"%s/%s.mp4" %(path,titulo))

    videoToconvert.write_audiofile(f"%s/%s.mp3" %(path,titulo))

    videoToconvert.close()
    os.remove(f"%s/%s.mp4" %(path,titulo))




op = int(input("Deseja baixar um video ou playlist? (1-video 2-list): "))
if(op == 1):
    DownVideo()

if(op == 2):
    DownPlaylist()


