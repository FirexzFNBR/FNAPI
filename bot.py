"""
MIT License

Copyright (c) 2024 FirexFNBR and SpireFNBR

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import requests
import json
import time
import warnings
import PIL
import shutil
import datetime
import tweepy
from yt_dlp import YoutubeDL
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from PIL import Image
from urllib.parse import urlparse
from colorama import init
from colorama import Fore
from datetime import datetime

warnings.filterwarnings("ignore", category=InsecureRequestWarning)
#====== CONFIG ======#
init(autoreset=True)
filepath = 'Exports' # COSMETICS GENERATOR PATH
language = 'pt-BR' # PUT YOUR LANGUAGE
apikey = 'a1c0a3b4-3cb6abc4-ca5d0d97-3ac8a5f6'
#=========AUTH===========#
apiKey = 'put_your_key'
apiSecret = 'puy_your_key'
accessToken = 'put_your_token'
accessTokenSecret = 'put_your_token'
#=== PULL CURRENT FORTNITE VERSION ===#
response = requests.get('https://fortnitecentral.genxgames.gg/api/v1/aes')
version = response.json()['version']
fversion = '1.2.0'
#=================================#
def clear():
    if os.name == 'nt':
        os.system('cls')
def menu():
    while True:
        clear()
        print(Fore.GREEN + f'-- Welcome to FNAPI (BETA) --')
        print(Fore.GREEN + f'-- Current Program Version: {fversion} --')
        print(Fore.GREEN + '-- This program was made by @SpireFNBR and @FirexFNBR_ --')
        print(Fore.GREEN + '-- If have issues, Join FN-API server "https://discord.gg/ZwxMpEbgJX" for help --')
        print(Fore.GREEN + f'-- Current Fortnite Version: {version} --')
        print(Fore.WHITE + '\nChoose a option:')
        print("")
        print(Fore.CYAN + 'Map Generation:')
        print(Fore.WHITE + "(1) Export map with POIs names (API takes too long to update)")
        print("(2) Export map without POIs names (NOT WORKING ON v32.10 and 32.11!)")
        print("(3) Export CLYDE map image (Temporary Option)")
        print("")
        print(Fore.CYAN + 'Paks Grabber:')
        print(Fore.WHITE + f'(4) Export paks info from {version}')
        print(f'(5) Exports a list of files related to the pak entered.')
        print("")
        print(Fore.CYAN + 'API:')
        print(Fore.WHITE + '(6) Use mnemonic for view playlists')
        print("(7) Download the mapping for the version you want")
        print("(8) Download current lobby background")
        print("(9) Export all news images")
        print("(10) Export all Fortnite Crew")
        print("(11) Export all Fortnite Seasons")
        print("(12) Export all Maps")
        print("(13) Export current Battle Pass")
        print("(14) Export current Fortnite status")
        print("")
        print(Fore.CYAN + 'Generate cosmetics:')
        print(Fore.WHITE + f'(15) Generate new cosmetics from {version}')
        print("(16) Generate all cosmetics")
        print(Fore.GREEN + "(17) Generate any cosmetic by name - (NEW)")
        print("")
        print(Fore.CYAN + 'Trackers:')
        print(Fore.GREEN + f'(18) Tweet encrypted paks on {version} - (NEW)')
        print("")
        print(Fore.CYAN + 'Others:')
        print(Fore.WHITE + '(19) Download youtube video')
        print(Fore.GREEN + '(20) Download twitter video - (NEW)')
        print("")
        print(Fore.YELLOW + 'About:')
        print(Fore.WHITE + f'(About) View credits ')
        print("")
        print(Fore.RED + 'Exit:')
        print(Fore.WHITE + "(Exit) to close FNAPI")
        print(Fore.YELLOW)
        
        option_choice = input(Fore.YELLOW + ">> ")
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
            exportnews()
        elif option_choice == "10":
            crewexporter()
        elif option_choice == "11":
            seasonsexporter()
        elif option_choice == "12":
            mapslists()
        elif option_choice == "13":
            battlepass()
        elif option_choice == "14":
            fnstatus()    
        elif option_choice == "15":
            newcosmetics() 
        elif option_choice == "16":
            allcosmetics(filepath) 
        elif option_choice == "17":
            cosmeticname()          
        elif option_choice == "18":
            encryptedpaks(apiKey, apiSecret, accessToken, accessTokenSecret)        
        elif option_choice == "19":
            ytvideo()   
        elif option_choice == "20":
            twvideo()                                                                         
        elif option_choice == "Exit":
            print("Closing the program...")
            break
        elif option_choice == "About":
            about() 
        else:
            print("Invalid option, try again.")
            
def mapwithPOI():  # MAP WITH POI NAMES GENERATOR
    api = f'https://fortnite-api.com/images/map_{language}.png'
    r = requests.get(api, allow_redirects=True)
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
    api2 = 'https://fortnitecentral.genxgames.gg/api/v1/export?path=FortniteGame%2FContent%2FAthena%2FApollo%2FMaps%2FUI%2FApollo_Terrain_Minimap&raw=false'
    r = requests.get(api2, allow_redirects=True)
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
 api3 = 'https://fortnitecentral.genxgames.gg/api/v1/export?path=FortniteGame%2FContent%2FAthena%2FApollo%2FMaps%2FClyde%2FTextures%2FWeek3_Adjusted&raw=false'
 r = requests.get(api3, allow_redirects=True)
 open('map.png', 'wb').write(r.content)
 print(Fore.YELLOW + "Generating CLYDE map image...")
 img = Image.open('map.png')
 img = img.resize((1200, 1200), PIL.Image.LANCZOS)
 img.save('Maps/Week3_Adjusted.png')
 os.remove('map.png')
 time.sleep(1)
 print(Fore.GREEN + "Generated!")
 close()

def pakgrabber():  # PAK GRABBER
    try:
        api4 = f"https://fortnitecentral.genxgames.gg/api/v1/aes?version={version}"
        response = requests.get(api4)
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
    pakNumber = input("Put the pak (example: '1010'): ")
    while not pakNumber.strip():
        pakNumber = input("Please type the pak: ")
    api5 = f"https://fortnitecentral.genxgames.gg/api/v1/assets/dynamic/{pakNumber}"
    response = requests.get(api5)
    response.raise_for_status()
    try:
        bruh1 = response.json() 
        bruh2 = json.dumps(bruh1, indent=4, ensure_ascii=False)
    except ValueError:
        bruh2 = response.text
    with open("Paks/PakList.json", "w", encoding="utf-8") as arquivo:
        arquivo.write(bruh2)
    
    print(Fore.GREEN + "List saved in PakList.json")
    time.sleep(1)
    close()

def mnemonic(): # MNEMONIC
    mnemonic = input("Put the playlist (example: 'playlist_defaultsolo'): ")
    while not mnemonic.strip():
        mnemonic = input("Please enter your playlist: ")
    # namespace = input("Type the namespace (example: 'fn'): ")    
    # while not namespace.strip():
    #     namespace = input("Please enter your namespace: ")
    api6 = f"https://fljpapi.onrender.com/api/links/fn/mnemonic/{mnemonic}"
    response = requests.get(api6)
    response.raise_for_status()
    try:
        bruh = response.json() 
        r = json.dumps(bruh, indent=4, ensure_ascii=False)
    except ValueError:
        r = response.text
    with open(f"Mnemonic/{mnemonic}.json", "w", encoding="utf-8") as b:
        b.write(r)
    
    print(Fore.GREEN + f"List saved in {mnemonic}.json")
    time.sleep(1)
    close()  

def mappings(): # DOWNLOAD THE MAPPING ON ANY VERSION
    mapping = input("Which version you want to download: ")
    api7 = f'https://fortnitecentral.genxgames.gg/api/v1/mappings?version={mapping}'
    response = requests.get(api7)
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
    api8 = 'https://fljpapi.onrender.com/api/lobby'
    response = requests.get(api8)
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
    cosmetics_folder = f'{filepath}/New Cosmetics'
    if os.path.exists(cosmetics_folder):
        for filename in os.listdir(cosmetics_folder):
            file_path = os.path.join(cosmetics_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(Fore.RED + f'Erro ao excluir {file_path}: {e}')
    else:
        os.makedirs(cosmetics_folder)
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
                    open(f'{cosmetics_folder}/{item["id"]}_icon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save image: {e}')
            if 'smallIcon' in item['images']:
                small_icon_url = item["images"]["smallIcon"]
                print(Fore.GREEN + f"Downloading image: {item['name']}")
                r = requests.get(small_icon_url, allow_redirects=True)
                try:
                    open(f'{cosmetics_folder}/{item["id"]}_smallIcon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save image: {e}')
    
    print(Fore.GREEN + '\nExported successfully!')
    time.sleep(2)
    close()

def allcosmetics(filepath): # ALL COSMETICS GENERATOR
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
                    print(Fore.RED + f'Could not save image: {e}')
            if 'smallIcon' in item['images']:
                small_icon_url = item["images"]["smallIcon"]
                print(Fore.WHITE + f"Downloading image: {item['name']}")
                r = requests.get(small_icon_url, allow_redirects=True)
                try:
                    open(f'{filepath}/All Cosmetics/{item["id"]}_smallIcon.png', 'wb').write(r.content)
                    print(Fore.GREEN + 'Saved Image!\n')
                except Exception as e:
                    print(Fore.RED + f'Could not save image: {e}')
    print(Fore.GREEN + '\nExported successfully!')
    time.sleep(2)
    close()       

def exportnews(): # NEWS IMAGES EXPORTER (BATTLE ROYALE)
    # language2 = input("Type your language: ")
    # while not language2.strip():
    #     language2 = input("Please enter your language: ")
    api9 = f"https://fortnite-api.com/v2/news/br"
    folder = "News"
    os.makedirs(folder, exist_ok=True)
    try:
        response = requests.get(api9, verify=False)
        response.raise_for_status()
        data = response.json()
        motds = data.get("data", {}).get("motds", [])
        for index, item in enumerate(motds):
            if isinstance(item, dict):
                image_url = item.get("image")
                if image_url:
                    image_name = os.path.basename(urlparse(image_url).path)
                    img_data = requests.get(image_url).content
                    image_path = os.path.join(folder, image_name)
                    with open(image_path, "wb") as img_file:
                        img_file.write(img_data)
                    print(Fore.GREEN + f"News image saved: {image_path}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def crewexporter(): # ALL FORTNITE CREW EXPORTER
 api10 = f"https://fortniteapi.io/v2/crew/history"
 headers = {"Authorization": apikey}
 response = requests.get(api10, headers=headers)
 if response.status_code == 200:
    with open("FortniteCrew.json", "w") as f:
     json.dump(response.json(), f, indent=4)
    print(Fore.GREEN + "Exported Fortnite Crew history.")
 time.sleep(2)
 close()
def seasonsexporter(): #ALL SEASONS EXPORTER
 api11 = f"https://fortniteapi.io/v1/seasons/list"
 headers = {"Authorization": apikey}
 response = requests.get(api11, headers=headers)
 if response.status_code == 200:
    with open("FortniteSeasons.json", "w") as f:
     json.dump(response.json(), f, indent=4)
    print(Fore.GREEN + "Exported Fortnite Seasons.")
 time.sleep(2)
 close()

def mapslists(): # ALL MAPS EXPORTER
 api12 = f"https://fortniteapi.io/v1/maps/list?language={language}"
 headers = {"Authorization": apikey}
 response = requests.get(api12, headers=headers)
 if response.status_code == 200:
    with open("FortniteMaps.json", "w") as f:
     json.dump(response.json(), f, indent=4)
    print(Fore.GREEN + "Exported Fortnite Maps Lists.")
 time.sleep(2)
 close()

def battlepass(): # CURRENT BATTLE PASS EXPORTER
 api13 = f"https://fortniteapi.io/v2/battlepass?language={language}&season=current"
 headers = {"Authorization": apikey}
 response = requests.get(api13, headers=headers)
 if response.status_code == 200:
    with open("FortniteBP.json", "w") as f:
     json.dump(response.json(), f, indent=4)
    print(Fore.GREEN + "Exported current Fortnite Battle Passe.")
 time.sleep(2)
 close() 

def fnstatus(): # EXPORT CURRENT EPIC GAMES/FORTNITE STATUS
    print(Fore.CYAN + 'Starting Fortnite Status Exporter...')
    status1 = "https://status.epicgames.com/api/v2/components.json"
    status2 = "https://status.epicgames.com/api/v2/scheduled-maintenances/upcoming.json"
    status3 = "https://status.epicgames.com/api/v2/incidents.json"
    response_components = requests.get(url1)
    response_maintenance = requests.get(url2)
    response_incidents = requests.get(url3)
    fndt = {}
    if response_components.status_code == 200:
        components_data = response_components.json()
        fnmcp = [
            {
                'id': component['id'],
                'name': component['name'],
                'status': component['status'],
                'created_at': component['created_at'],
                'updated_at': component['updated_at']
            }
            for component in components_data['components'] if 'Fortnite' in component['name']
        ]
        fndt['components'] = fnmcp
        
    if response_maintenance.status_code == 200:
        maintenance_info = response_maintenance.json()
        scheduled_maintenances = []
        current_time = datetime.utcnow()
        if 'scheduled_maintenances' in maintenance_info and maintenance_info['scheduled_maintenances']:
            for maintenance in maintenance_info['scheduled_maintenances']:
                maintenance_time = datetime.strptime(maintenance['scheduled_for'], "%Y-%m-%dT%H:%M:%S.%fZ")
                
                if maintenance_time > current_time and maintenance['incident_updates']:
                    updates = [update['body'] for update in maintenance['incident_updates']]
                    combined_message = "\n\n".join(updates) if updates else "no maintenances."
                    
                    maintenance_details = {
                        'name': maintenance['name'],
                        'status': maintenance['status'],
                        'scheduled_start': maintenance['scheduled_for'],
                        'scheduled_end': maintenance['scheduled_until'],
                        'description': combined_message
                    }
                    scheduled_maintenances.append(maintenance_details)
            fndt['scheduled_maintenance'] = scheduled_maintenances or [{
                'name': 'Scheduled Maintenance',
                'status': 'none',
                'description': 'No scheduled maintenances.'
            }]
        else:
            fndt['scheduled_maintenance'] = [{
                'name': 'Scheduled Maintenance',
                'status': 'none',
                'description': 'No scheduled maintenances.'
            }]
    if response_incidents.status_code == 200:
        incidents_data = response_incidents.json()
        
        active_incidents = [
            {
                'name': incident['name'],
                'updates': [
                    {
                        'status': update['status'],
                        'body': update['body'],
                        'created_at': update['created_at']
                    }
                    for update in incident['incident_updates']
                ]
            }
            for incident in incidents_data['incidents'] 
            if 'Fortnite' in incident['name'] and incident['status'] in ['investigating', 'identified', 'monitoring']
        ]
        if active_incidents:
            fndt['current_incident'] = active_incidents[0]
    with open('FNStatus.json', 'w') as json_file:
        json.dump(fndt, json_file, indent=4)
    
    print(Fore.GREEN + "Exported status in: 'FNStatus.json'.")
    time.sleep(2)
    close()
    fnstatus()
    
def ytvideo(): # YOUTUBE VIDEO DOWNLOADER
    link = input("Type youtube video link: ")
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            print(f"Download completed: {info['title']}")
    except Exception as e:
        print("An error has been occurred:", e)
    close()        
    ytvideo()  

def encryptedpaks(apiKey, apiSecret, accessToken, accessTokenSecret): # ENCRYPTED PAKS TWEET
    print(Fore.YELLOW + "Starting bot...")
    time.sleep(1)
    
    api14 = "https://fortnitecentral.genxgames.gg/api/v1/aes"
    response = requests.get(api14)
    data = response.json()['unloaded']

    print(Fore.YELLOW + "Loading API...")
    time.sleep(1)
    post = f"All encrypted paks on {version}:\n\n"
    for item in data:
        name = item['name']
        name = name.replace("-WindowsClient.utoc", "")
        name = name.replace("chunk", "")
        bruh1 = item['fileCount']
        bruh2 = item['size']['formatted']
        bruh3 = "Yes" if item['hasHighResTextures'] else "No"
        post += f"{name} | Files: {bruh1} | Size: {bruh2} | HD Textures: {bruh3}\n"
    post += "\n#Fortnite"
    print(Fore.GREEN + "Loaded API!")
    time.sleep(1)

    print(Fore.YELLOW + "Authenticating Twitter...")
    time.sleep(1)
    twitter_client = tweepy.Client(
        consumer_key=apiKey,
        consumer_secret=apiSecret,
        access_token=accessToken,
        access_token_secret=accessTokenSecret
    )
    print(Fore.GREEN + "Twitter client authenticated!")

    print(Fore.YELLOW + "Creating tweet...")
    time.sleep(1)
    twitter_client.create_tweet(text=post)
    print(Fore.GREEN + "Tweet created!")
    print(Fore.RED + "Stopping the bot...")
    close()
    encryptedpaks(apiKey, apiSecret, accessToken, accessTokenSecret)

def twvideo():  # TWITTER VIDEO DOWNLOADER
    link = input(Fore.CYAN + "Type Twitter video link: ")
    if "x.com" not in link and "twitter.com" not in link:
        print(Fore.RED + "This link is not valid.")
        return
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'cookiefile': 'cookies.txt',
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print(Fore.YELLOW + "Downloading video...")
            ydl.download([link])
            print(Fore.GREEN + "Downloaded!")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")
        print(Fore.YELLOW + "Try updating yt-dlp or checking the link validity.")
        twvideo()
        close()
        time.sleep(2)

def cosmeticname():  # EXPORT COSMETIC BY ID OR NAME
 clear()
 print(Fore.CYAN + "How do you want to export? (name or id)")
 choice = input(Fore.YELLOW + ">> ")

 if choice == "name": # EXPORT BY NAME
    path = "Exports"
    os.makedirs(path, exist_ok=True)
    name = input("Enter cosmetic name: ")
    api15 = f"https://fortnite-api.com/v2/cosmetics/br/search?name={name}&language=en"
    try:
        response = requests.get(api15).json()
        if response.get("status") == 200 and "data" in response:
            cosmetic_id = response["data"].get("id", "unknown")

            def bruh(obj):
                if isinstance(obj, str) and obj.startswith("https://fortnite-api.com/images/cosmetics/br/"):
                    file_path = os.path.join(path, f"{cosmetic_id}_{os.path.basename(obj)}")
                    with open(file_path, "wb") as f:
                        f.write(requests.get(obj).content)
                    print(Fore.GREEN + f"Exported: {file_path}")
                elif isinstance(obj, (list, dict)):
                    for v in (obj.values() if isinstance(obj, dict) else obj):
                        bruh(v)
            bruh(response["data"])
        else:
            print(Fore.RED + "No data found for the provided name.")            
    except Exception as e:
        print(f"An error occurred: {e}")
    close()     

 if choice == "id": # EXPORT BY ID
    path = "Exports"
    os.makedirs(path, exist_ok=True)
    id = input("Enter cosmetic id (all in small caps): ")
    api16 = f"https://fortnite-api.com/v2/cosmetics/br/search?id={id}&language=en"
    try:
        response = requests.get(api16).json()
        if response.get("status") == 200 and "data" in response:
            cosmetic_id = response["data"].get("id", "unknown")

            def bruh(obj):
                if isinstance(obj, str) and obj.startswith("https://fortnite-api.com/images/cosmetics/br/"):
                    file_path = os.path.join(path, f"{cosmetic_id}_{os.path.basename(obj)}")
                    with open(file_path, "wb") as f:
                        f.write(requests.get(obj).content)
                    print(Fore.GREEN + f"Exported: {file_path}")
                elif isinstance(obj, (list, dict)):
                    for v in (obj.values() if isinstance(obj, dict) else obj):
                        bruh(v)
            bruh(response["data"])
        else:
            print(Fore.RED + "No data found for the provided name.")
    except Exception as e:
        print(f"An error occurred: {e}")
    close()     

def about():
    clear()
    print(Fore.CYAN + f'Current program version: {fversion}')
    print("")
    print(Fore.WHITE + 'FNAPI is a tool to easy leaks.')
    print("")
    print('This program uses api from "GMATRIXGAMES ( @GMatrixGames ), FLJP ( @LeakPlayer ), Fortnite-API ( https://fortnite-api.com ) and FortniteAPI.io ( https://fortniteapi.io )"')
    print("")
    print('This program was inspired (design) in AutoLeak, by Fevers .')
    print("")
    print('Credits to FirexFNBR and SpireFNBR, developers and owners of this program.')
    print("")
    print('New functions will be added in future versions.')
    print("")
    time.sleep(7)
    close()

def close():
    while True:
        option = input(Fore.CYAN + "Do you want to go back to menu? (y/n): ").lower()
        if option == 'y':
            print('Sure! Returning to the menu...')
            time.sleep(1)
            clear()
            time.sleep(1)
            menu()
            break
        elif option == 'n':
            print("Sure! Closing the program...")
            time.sleep(2)
            exit()
        else:
            print("Invalid option. Type 'y' to return to menu or 'n' to exit.")

if __name__ == "__main__":
    menu()
