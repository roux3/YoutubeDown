from pytube import YouTube,Playlist
import os
from moviepy import *
from moviepy.editor import *

path = "downloads"
regex = [",","|","/",";","\"","?","!","."]

def DownVideo():
    url = input("Digite a url do video: ")
    try:
        video = YouTube(url)
        titulo = video.title

        for r in regex:
            titulo = titulo.replace(r,"")


        print(video.streams.get_by_itag("140").download(filename=f"%s.mp4" %(titulo),output_path=path))
        Convert(titulo)

    except (KeyError):
        print("video privado")
    
    

def DownPlaylist():
    url = input("Digite a url da playlist: ")
    try:
        p = Playlist(url)
        for video in p.videos:
            try:
                titulo = video.title
                for r in regex:
                    titulo = titulo.replace(r,"")

                print(titulo)
                print(video.streams.get_by_itag("140").download(filename=f"%s.mp4" %(titulo),output_path=path))
                Convert(titulo)
            except:
                print("video privado")
    except:
        pass


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


