import json
import requests

def print_details(wut):
    print('-------------------------------------------------------------')
    print('Movie: ', wut['Title'], '\n')
    if wut['Released'] == "N/A":
        print('Released: ', wut['Year'], '\n')
    else:
        print('Released: ', wut['Released'], '\n')
    print('Genre: ', wut['Genre'], '\n')
    print('Director: ', wut['Director'], '\n')
    print('Writer: ', wut['Writer'], '\n')
    print('Actors: ', wut['Actors'], '\n')
    print('Plot: ', wut['Plot'], '\n')
    if wut['Metascore'] == 'N/A':
        print('IMDb Rating: ', wut['imdbRating'], '\n')
    else:
        print('Metascore: ', wut['Metascore'], '\n')
    print('Poster: ', wut['Poster'])
    print('-------------------------------------------------------------')

def get_information(sup):
    try:
        kek = requests.get("http://www.omdbapi.com/?t=" + sup)
        ne = json.loads(kek.text)
        print_details(ne)
    except:
        if ne['Response'] == 'False' and ne['Error'] == 'Movie not found!':
            print('Ops, movie not found.')
        else:
            print('Please, check your connection.')





out = False
while not out:
    print('If you want to exit just type EXIT!')
    moe = input('To search a movie, just type the title: \n')
    if moe == 'EXIT':
        out = True
    else:
        get_information(moe)






