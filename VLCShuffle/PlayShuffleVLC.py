import random


#Función que devuelve un boolean dependiendo de:
# Si la canción que recibimos por parámetro está en la lista --> True
# Si la canción que recibimos por parámetro NO está en la lista entonces:
## ==>  añadimos la canción a la lista selectedSongs
selectedSongs = []
def isSongselected(song):
   assert isinstance(song, str)
   assert song != '', 'el parámetro canción llega vacío'
   if song in selectedSongs:
       return True
   else:
       selectedSongs.append(song)
   assert len(selectedSongs) > 0, "La lista de canciones seleccionadas está vacía"
   return False



#Función que genera una canción utilizando random, que devuelve la key del diccionario
# trackList.

def randomSong(trackList):
   assert isinstance( trackList, dict ), "parámetro introducido no es un diccionario"
   assert bool(trackList), "La trackList que recibimos por parámetro está vacía"
   song = random.choice(list(trackList.keys()))
   assert isinstance(song, str), "no devuelve string"
   #assert isSongselected(song) == False, "Esta canción ya ha sido seleccionada"
   return song



def generatePlaylist (trackList, playList):
    song = randomSong(trackList)
    for i in range(len(trackList)):
        playList[i+1] = ''
        # Mientras la canción que generamos esté en la lista
        #==> pedimos un nuevo título de canción de forma aleatoria
        while(isSongselected(song)):
            song = randomSong(trackList)
        playList[i+1] = song
    assert len(playList) > 0
    assert isinstance(playList,dict)
    return playList



def printSongList(playList):
    assert isinstance(playList, dict)
    for songItem in sorted(playList.keys()):
        print(str(songItem) + ": " + str(playList[songItem]))


def startVLC(trackList, playList):

    # Las canciones deben estar en el directorio biblioteca (junto a la aplicacion)
    import subprocess
    import shlex
    import os

    PathVLC = "C:/Program Files/VideoLAN/VLC/vlc.exe"
    commandLineVLC = PathVLC

    for trackNumber in playList.keys():
        trackTitle = playList[trackNumber]
        try:
            pathToFile = trackList[trackTitle]["location"]
        except KeyError:
            print("la cancion " + str(trackFile) + " no esta en la biblioteca")
        else:
            if os.path.exists(str(pathToFile)):
                commandLineVLC += " " + str(pathToFile)
            else:
                pass


    arguments = shlex.split(commandLineVLC)
    try:
        commandLineVLC = subprocess.Popen(arguments)
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("VLC lanzado con exito!")
        printSongList(playList)


def playShuffle(trackList,playList):
    if isinstance(trackList,dict):
        generatePlaylist (trackList, playList)
        startVLC(trackList, playList)


# playList ={ 1: "titulo cancion", 2: "titulo cancion" ... }
playList = {1:"It's a Kind Of Magic"}

trackList = {"California_Uber_Alles.mp3":
               {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
           "Seattle_Party":
               {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
           "King_Kunta":
               {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}
           }



playShuffle(trackList,playList)



#Casos Test
#trackList no es un diccionario >> ""
#trackList = {} >> salta assertion
# Inicializamos la playlist antes de llamar a la funcion:
# playList(1:"November Rain") >> Ignora y siempre genera a partir de la tracklist que tenemos
