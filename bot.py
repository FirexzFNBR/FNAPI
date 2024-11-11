import os
import requests
import tweepy
import PIL
import colorama
import datetime
import json
import sys
import time
import shutil
from PIL import Image, ImageFont, ImageDraw
from datetime import date
from datetime import datetime
from colorama import *

#====== CONFIG ======#
filepath = 'put_your_exports_path' # IT'S NECESSARY TO EXPORT NEW AND ALL COSMETICS.
language = 'en'
#=========================#
#     # V1 Tweepy
# auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
# auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
# api = tweepy.API(auth, wait_on_rate_limit=True)
#     # V2 Tweepy
# client = tweepy.Client(
#  access_token=twitAccessToken,
#  access_token_secret=twitAccessTokenSecret,
#  consumer_key=twitAPIKey,
#  consumer_secret=twitAPISecretKey,
#  wait_on_rate_limit=True
#  )
#========================#
# PULL CURRENT FORTNITE VERSION
response = requests.get('https://fortnitecentral.genxgames.gg/api/v1/aes')
version = response.json()['version']
#=================================#
def clean():
    if os.name == 'nt':
        os.system('cls')
def menu():
    while True:
        print(Fore.GREEN + '-- Welcome to FNAPI 1.0 (BETA) --')
        print('-- This program was made by @SpireFNBR and @FirexFNBR_ --')
        print('-- If have issues, Join FN-API server "https://discord.gg/ZwxMpEbgJX" for help --')
        print(f'-- Current Fortnite Version: {version} --')
        print(Fore.WHITE + '\nChoose a option:')
        print("")
        print(Fore.CYAN + 'Map Generation:')
        print(Fore.WHITE + "(1) Export map with POIs names (API takes too long to update)")
        print("(2) Export map without POIs names (NOT WORKING ON v32.00!)")
        print("(3) Export CLYDE map image (Temporary Option)")
        print("")
        print(Fore.CYAN + 'Paks Grabber')
        print(Fore.WHITE + f'(4) Export paks info from {version}')
        print(f'(5) Exports a list of files related to the pak entered.')
        print("")
        print(Fore.CYAN + 'API and Trackers')
        print(Fore.WHITE + '(6) Use mnemonic for view playlists')
        print("(7) Download the mapping for the version you want")
        print("(8) Download current lobby background")
        print("")
        print(Fore.CYAN + 'Generate cosmetics')
        print(Fore.WHITE + f'(9) Generate new cosmetics from {version}')
        print(Fore.WHITE + f'(10) Generate all cosmetics')
        print("")
        print(Fore.RED + 'Exit')
        print(Fore.WHITE + "Press '0' to close FNAPI")
        print(Fore.YELLOW)
        
        option_choice = input(">> ")

        time.sleep(2) 

        if option_choice == "1":
            mapwithPOI()
        elif option_choice == "2":
            mapwithoutPOI()
        elif option_choice == "3":
            clydemap()
        elif option_choice == "4":
            pakgrabber()
        elif option_choice == "5":
            pakarchives()
        elif option_choice == "6":
            mnemonic()
        elif option_choice == "7":
            mappings()  
        elif option_choice == "8":
            lobby()
        elif option_choice == "9":
            newcosmetics()
        elif option_choice == "10":
            allcosmetics(filepath)                     
        elif option_choice == "0":
            print("Closing the program...")
            break 
        else:
            print("Invalid option, try again.")
            

def mapwithPOI():  # MAP WITH POI NAMES GENERATOR
    url = 'https://media.fortniteapi.io/images/map.png?showPOI=true'
    r = requests.get(url, allow_redirects=True)
    open('map.png', 'wb').write(r.content)
    print(Fore.YELLOW + "Generating image with POIs names...")
    img = Image.open('map.png')
    img = img.resize((1200, 1200), PIL.Image.LANCZOS)
    img.save('Maps/map_poi.png')
    os.remove('map.png')
    time.sleep(1)
    print(Fore.GREEN + "Generated!")
    close()

def mapwithoutPOI():  # MAP WITHOUT NAME GENERATOR
    url2 = 'https://fortnitecentral.genxgames.gg/api/v1/export?path=FortniteGame%2FContent%2FAthena%2FApollo%2FMaps%2FUI%2FApollo_Terrain_Minimap&raw=false'
    r = requests.get(url2, allow_redirects=True)
    open('map.png', 'wb').write(r.content)
    print(Fore.YELLOW + "Generating image without POIs names...")
    img = Image.open('map.png')
    img = img.resize((1200, 1200), PIL.Image.LANCZOS)
    img.save('Maps/map.png')
    os.remove('map.png')
    time.sleep(1)
    print(Fore.GREEN + "Generated!")
    close()

def clydemap(): # CLYDE MAP GENERATOR
 url3 = 'https://fortnitecentral.genxgames.gg/api/v1/export?path=FortniteGame%2FContent%2FAthena%2FApollo%2FMaps%2FClyde%2FTextures%2FWeek2_Adjusted&raw=false'
 r = requests.get(url3, allow_redirects=True)
 open('map.png', 'wb').write(r.content)
 print(Fore.YELLOW + "Generating CLYDE map image...")
 img = Image.open('map.png')
 img = img.resize((1200, 1200), PIL.Image.LANCZOS)
 img.save('Maps/Week2_Adjusted.png')
 os.remove('map.png')
 time.sleep(1)
 print(Fore.GREEN + "Generated!")
 close()

def pakgrabber():  # PAK GRABBER
    try:
        url4 = f"https://fortnitecentral.genxgames.gg/api/v1/aes?version={version}"
        response = requests.get(url4)
        if response.status_code == 200:
            data = response.json()
            with open(f"Paks/{version} Paks.json", "w", encoding="utf-8") as archives:
                json.dump(data, archives, indent=2)
                print(f"Saved paks info in '{version} Paks.json'.")
        else:
            print(f"Request error. Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        time.sleep(2)
        close()

def pakarchives(): # PAK ARCHIVES GRABBER
    pakNumber = input("Type the pak (example: '1010'): ")
    while not pakNumber.strip():
        pakNumber = input("Please type the pak: ")
    url5 = f"https://fortnitecentral.genxgames.gg/api/v1/assets/dynamic/{pakNumber}"
    response = requests.get(url5)
    response.raise_for_status()
    try:
        conteudo = response.json() 
        conteudo_formatado = json.dumps(conteudo, indent=4, ensure_ascii=False)
    except ValueError:
        conteudo_formatado = response.text
    with open("Paks/PakList.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_formatado)
    
    print(Fore.GREEN + "List saved in PakList.json")
    time.sleep(1)
    close()

def mnemonic(): # MNEMONIC
    mnemonic = input("Type the playlist (example: 'playlist_defaultsolo'): ")
    while not mnemonic.strip():
        mnemonic = input("Please enter your playlist: ")
    # namespace = input("Type the namespace (example: 'fn'): ")    
    # while not namespace.strip():
    #     namespace = input("Please enter your namespace: ")
    url6 = f"https://fljpapi.onrender.com/api/links/fn/mnemonic/{mnemonic}"
    response = requests.get(url6)
    response.raise_for_status()
    try:
        conteudo = response.json() 
        conteudo_formatado = json.dumps(conteudo, indent=4, ensure_ascii=False)
    except ValueError:
        conteudo_formatado = response.text
    with open(f"Mnemonic/{mnemonic}.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_formatado)
    
    print(Fore.GREEN + f"List saved in {mnemonic}.json")
    time.sleep(1)
    close()  

def mappings(): # DOWNLOAD THE MAPPING ON ANY VERSION
    mapping = input("Which version you want to download: ")
    url7 = f'https://fortnitecentral.genxgames.gg/api/v1/mappings?version={mapping}'
    response = requests.get(url7)
    response.raise_for_status()
    data = response.json()
    mapping_url = data[0].get("url")
    if mapping_url:
        file_response = requests.get(mapping_url, stream=True)
        file_response.raise_for_status()
        folder_path = "Mappings"
        os.makedirs(folder_path, exist_ok=True)
        mapping_v = os.path.join(folder_path, mapping_url.split("/")[-1])
        with open(mapping_v, "wb") as file:
            for chunk in file_response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"The mapping '{mapping_v}' has been downloaded successfully!")
    else:
        print("This version was not found.")
        time.sleep(1)
    close()
 
def lobby(): # LOBBY BACKGROUND DOWNLOADER
    url8 = 'https://fljpapi.onrender.com/api/lobby'
    response = requests.get(url8)
    response.raise_for_status()
    data = response.json()
    backgrounds = data.get("backgrounds", {}).get("backgrounds", [])
    if backgrounds:
        lobby_img_url = backgrounds[0].get("backgroundimage")
        if lobby_img_url:
            response = requests.get(lobby_img_url, stream=True)
            response.raise_for_status()
            file_name = os.path.basename(lobby_img_url)
            save_path = os.path.join("Lobby", file_name)
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"The lobby background has been downloaded successfully!")
        time.sleep(1)
    close()

def newcosmetics():
    print('\nStarting bot...\n')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics/new?lang={language}')
    data = response.json()
    if 'items' in data['data'] and 'br' in data['data']['items']:
        items = data['data']['items']['br']
        for item in items:
            print(f'{item["name"]}:')
            if 'icon' in item['images']:
                icon_url = item["images"]["icon"]
                print(Fore.GREEN + f"Downloading image: {item['name']}")
                r = requests.get(icon_url, allow_redirects=True)
                try:
                    os.makedirs(f'{filepath}/New Cosmetics', exist_ok=True)
                    open(f'{filepath}/New Cosmetics/{item["id"]}_icon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save icon image: {e}')
            if 'smallIcon' in item['images']:
                small_icon_url = item["images"]["smallIcon"]
                print(Fore.GREEN + f"Downloading image: {item['name']}")
                r = requests.get(small_icon_url, allow_redirects=True)
                try:
                    open(f'{filepath}/New Cosmetics/{item["id"]}_smallIcon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save smallIcon image: {e}')
    print(Fore.GREEN + '\nExported successfully!')
    time.sleep(2)
    close()

def allcosmetics(filepath):
    print('\nStarting bot...\n')
    response = requests.get(f'https://fortnite-api.com/v2/cosmetics')
    data = response.json()
    if 'data' in data and 'br' in data['data']:
        items = data['data']['br']
        for item in items:
            print(Fore.YELLOW + f'{item["name"]}:')
            if 'icon' in item['images']:
                icon_url = item["images"]["icon"]
                print(Fore.WHITE + f"Downloading image:{item['name']}")
                r = requests.get(icon_url, allow_redirects=True)
                try:
                    os.makedirs(f'{filepath}/All Cosmetics', exist_ok=True)
                    open(f'{filepath}/All Cosmetics/{item["id"]}_icon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save icon image: {e}')
            if 'smallIcon' in item['images']:
                small_icon_url = item["images"]["smallIcon"]
                print(Fore.WHITE + f"Downloading image: {item['name']}")
                r = requests.get(small_icon_url, allow_redirects=True)
                try:
                    open(f'{filepath}/All Cosmetics/{item["id"]}_smallIcon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save smallIcon image: {e}')
    print(Fore.GREEN + '\nExported successfully!')
    time.sleep(2)
    close()       

def close():
    while True:
        user_input = input(Fore.CYAN + "Do you want to go back to the menu? (y/n): ").lower()
        if user_input == 'y':
            print('Sure! Returning to the menu...')
            time.sleep(2)
            clean() 
            menu()
            break
        elif user_input == 'n':
            print("Sure! Closing the program...")
            time.sleep(2)
            exit()
        else:
            print("Invalid option. Y to return to the menu or N to exit the program.")     

if __name__ == "__main__":
    menu()
