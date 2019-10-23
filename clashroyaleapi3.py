import requests
import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from requests.exceptions import ConnectionError

##########Defining variables to open various files
myfile1 = open("apipage1.html", "w")
#w allows the code to write on the various pages
myfile2 = open("apipage2.html", "w")
myfile3 = open("apipage3.html", "w")
myfile4 = open("apipage4.html", "w")

############Wifi Testing
try: #Tries to access google.com. If it works continue with code
    x = requests.get("http://google.com")
except ConnectionError as e: #if google.com cannot be accessed, the code displays a message saying there was a wifi error
    messagebox.showinfo("WiFi Error", "Please Connect with WiFi to continue")
    exit() #crashes code "kill all"
    
############Creates a function for the button##############
def processBtn():
        headers = { 
#This is the api access key. This changes based on ones location.
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjkyZTQ4ZDg3LTdjMjAtNDViOC1iMTIzLWQ4ODJkZTBiNWQ0MyIsImlhdCI6MTU3MDU1MDE0NSwic3ViIjoiZGV2ZWxvcGVyL2MyYjY1NmYzLWE4MGMtOWU4Mi03MTdmLTcwY2I2YWYwZjY3YSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2OS43Ny4xNjAuMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.1GXCZ9eJ3FS76aUN8ENMCCIexq6h6jhlu6fZkwoER3qXChnZ3tu8yw1JuoVUmg3QbdsyWonafetxFw0L32oIOQ'}
        
#Contains the data retrieved by "requests" from the api site.
        response = requests.get("https://api.clashroyale.com/v1/players/%23" + str(enterTag.get().upper()), headers = headers)
        response2 = requests.get("https://api.clashroyale.com/v1/players/%23" + str(enterTag.get().upper()) + "/upcomingchests", headers = headers) #Retrieves data from the same site, adding a /upcomingchests which retrieves different data
        
#Defines userdata as the json data
        userdata = response.json()
        userdata2 = response2.json()
        
#If the clan is not found, clan is defined as "No Clan"
        try: 
            clan = str(userdata['clan']['name'])
            role = str(userdata['role'])
        except:
            clan = "No Clan"
            role = "No Role"

#Only works if the status_code response is 200
        if (response.status_code == 200):
            winrate = str(((userdata['wins'])/((userdata['wins']) + (userdata['losses']))*100))
            
            #Write on website
            #Different file's on computer
            filename1 = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apipage1.html'
            
            #opens new tab with the first file
            webbrowser.open_new_tab(filename1)
            
            #writes code onto the first file
            myfile1.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a  class = "active" href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Clash Royale Statistics</h1>
            <table>
              <tr>
                <th>Individual Information:  - """+str(userdata['name'])+"""</th>
                <th></th>
              </tr>
              <tr>
                <td>Player Tag</td>
                <td>""" + enterTag.get().upper() + """</td>
              </tr>
              <tr>
                <td>King Tower Level</td>
                <td>Level """ + str(userdata['expLevel']) + """</td>
              </tr>
              <tr>
                <td>Player Trophies</td>
                <td>"""+ str(userdata['trophies']) +""" trophies</td>
              </tr>
              <tr>
                <td>Best Trophies</td>
                <td>"""+ str(userdata['bestTrophies']) + """ trophies</td>
              </tr>
              <tr>
                <td>Player Wins</td>
                <td>"""+str(userdata['wins'])+""" games won</td>
              </tr>
              <tr>
                <td>Player Losses</td>
                <td>"""+str(userdata['losses'])+""" games lost</td>
              </tr>
              <tr>
                <td>Win %</td>
                <td>""" + str(winrate) +"""%</td>
              </tr>
              <tr>
                <td>Clan Name</td>
                <td>""" + clan + """ - """+role+"""</td>
              </tr>
            </table>
            """)
#data above is parsed from the json
            myfile1.write("</table></body>")
            myfile1.close()
            myfile2.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a class = "active" href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Cards and Decks</h1>
            <h2>Cards and Deck Information - """+str(userdata['name'])+"""</h2>
            <h3>The last 8 cards form your deck!</h3>
            <table>
              <tr>
                <th>Card Name</th>
                <th>Card Level</th>
                <th>Card Icon</th>
                <th>Number of Cards</th>
              </tr>
            """)
            #for loop finds the number of data points when parsing
            #continues creating new rows until all the cards are displayed
            for i in range(len(userdata['cards'])):
                myfile2.write("""
                <tr>
                  <th>Card Name: """+ str(userdata['cards'][i]['name']) + """</th>
                  <th>Lvl """+ str(userdata['cards'][i]['level'])+ """</th>
                  <th><img src = """+ userdata['cards'][i]['iconUrls']['medium'] +""" width = "100"></th>
                  <th>Number of Cards: """+ str(userdata['cards'][i]['count']) + """</th>
                </tr>
                """)
            myfile2.write("""
            </table></body>
            """)
            myfile2.close()
            #finishes writing on myfile2 and opens myfile3
            myfile3.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a class = "active" href="apipage3.html">Achievements</a>
                <a href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h1>"""+str(userdata['name'])+ """'s Clash Royale Achievements & Badges </h1>
            <h2>Achievements & Badges - """+str(userdata['name'])+"""</h2>
            <h3>Congratulations on all of these amazing badges!</h3>
            <table>
              <tr>
                <th>Badges</th>
                <th>Progress</th>
              </tr>
            """)
            #this for loop finds the number of badges and repeats
            #continues producing rows until there are no more badges
            for i in range(len(userdata['badges'])):
                myfile3.write("""
                <tr>
                  <th>Badge: """+ str(userdata['badges'][i]['name']) + """</th>
                  <th>Progress: """+ str(userdata['badges'][i]['progress'])+ """</th>
                </tr>
                """) 
            myfile3.write(
            """
            </table>
            <h3>Congratulations! These are all of the achievements you have unlocked.</h3>
            <table>
              <tr>
                <th>Achievement</th>
                <th>Description</th>
                <th>Value</th>
                <th>Stars</th>
              </tr>
            """)
            
            #loops until the number of achievements are on the page
            for i in range(len(userdata['achievements'])):
                myfile3.write("""
                <tr>
                  <th>Name: """+ str(userdata['achievements'][i]['name']) + """</th>
                  <th>Info: """+ str(userdata['achievements'][i]['info'])+ """</th>
                  <th>Value: """+ str(userdata['achievements'][i]['value']) + """</th>
                  <th>Stars: """+ str(userdata['achievements'][i]['stars']) + """</th>
                </tr>
                """)
            myfile3.write("</table></body>")
            myfile3.close()
            #closes the third file and begins to write on myfile4
            myfile4.write("""
            <head> <link rel = "stylesheet" type = "text/css" href = "clashroyale.css" /></head>
            <body>
            <div class="topnav">
                <a href="apipage1.html">Personal Statistics</a>
                <a href="apipage2.html">Cards & Decks</a>
                <a href="apipage3.html">Achievements</a>
                <a class = "active" href = "apipage4.html">Upcoming Chests</a>
            </div>
            <img src = """"banner.jpg"""" width = 100%>
            <h3>Here are your upcoming chests. Chest ranking: Silver, Gold, Magical, Giant, Mega Lightning, Epic, Legendary Chest.</h3>
            <table>
              <tr>
                <th>Order Number</th>
                <th>Type</th>
                <th>Image</th>
                <th>Chest Description</th>
              </tr>
            """)
            #the images found below are retrieved from the internet
            for i in range(len(userdata2['items'])):
                chest_name = userdata2['items'][i]['name']
                image_file = chest_name + ".png"
                myfile4.write("""
                <tr>
                  <th>"""+ str(userdata2['items'][i]['index']) + """</th>
                  <th>"""+str(userdata2['items'][i]['name'])+"""</th>
                """)
                #the if and elif statements compare the chest name and outputs a certain photo based on the result
                
                #only one of the following outputs can occur due to the elif and ifs
                if (userdata2['items'][i]['name'] == "Silver Chest"):
                    myfile4.write("""<th><img src = http://clashroyalers.weebly.com/uploads/7/9/8/4/79848022/http-2f-2fvignette4-wikia-nocookie-net-2fclashroyale-2fimages-2f0-2f07-2fsilverchest_1.png?603 width = "150"></th>
                    <th>Silver Chests guarantee a few Common Cards as well as a Rare if the player is in Spell Valley or above (two Rares in Spooky Town or above). Silver Chests take 3 hours or 18 gems to unlock.</th>
                    </tr>
                    """)
                #if the chest name is gold it outputs a certain photo and message
                elif (userdata2['items'][i]['name'] == "Golden Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/8/8b/GoldenChest.png/revision/latest/scale-to-width-down/160?cb=20160209231105 width = "150"></th>
                    <th>Golden chests guarantee 2 or more Rare Cards depending on the player's arena as well as a few Common Cards. Golden chests take 8 hours or 48 gems to unlock.</th>
                    </tr>
                    """)
                #if the chest name is magical it outputs a certain photo and message
                elif (userdata2['items'][i]['name'] == "Magical Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/9/93/MagicalChest.png/revision/latest/scale-to-width-down/150?cb=20160312171354 width = "100"></th>
                    <th>Magical Chests guarantee 2 or more Epic Cards, depending the player's Arena, as well as a few Rare Cards and Common Cards. Magical Chests take 12 hours or 72 gems to unlock.</th>
                    </tr>
                    """)
                #if the chest name is giant it outputs a certain photo and message
                elif (userdata2['items'][i]['name'] == "Giant Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/d/da/Giant_chest.png/revision/latest/scale-to-width-down/120?cb=20160306083332 width = "100"></th>
                    <th>Giant Chests guarantee a large number of Rare Cards and Common Cards and have a high chance of containing an Epic Card. Giant Chests take 12 hours or 72 gems to unlock.</th>
                    </tr>
                    """)
                #if the chest name is mega lightning a certain photo is outputted and a message
                elif (userdata2['items'][i]['name'] == "Mega Lightning Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/3/3a/MegaLightningChest.png/revision/latest/scale-to-width-down/120?cb=20181205194051 width = "100"></th>
                    <th>The Mega Lightning Chests are one of the 3 rarest chests won through battles, tied with Epic and Legendary Chests. It can also be unlocked in Quests. Mega Lightning Chests are not part of the regular chest cycle (see Chest Cycle). Mega Lightning Chests have a high chance of containing a Legendary given the chest is from P.E.K.K.A.'s Playhouse or above, and even guarantee one from Spooky Town or above. Mega Lightning Chests take 24 hours or 144 gems to unlock.</th>
                    </tr>
                    """)
                #if the chest name is epic there is a photo and message
                elif (userdata2['items'][i]['name'] == "Epic Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/f/f5/EpicChest.png/revision/latest/scale-to-width-down/120?cb=20160923080038 width = "100"></th>
                    <th>Epic Chests guarantee Epic Cards only and do not contain cards of any other rarity. Epic Chests take 12 hours or 72 gems to unlock. Epic Chests can be bought in special offers in the Shop for 3,000 to 10,000 gold depending on the your Arena with higher Arenas having the higher costs. Consequently, cards from Epic Chests from higher Arenas contain more Epic Cards, ranging from 6 to 20. The special offer appears every couple of weeks and last 24 hours.</th>
                    </tr>
                    """)
                #if the chest is legendary there is a photo and message
                elif (userdata2['items'][i]['name'] == "Legendary Chest"):
                    myfile4.write("""<th><img src = https://vignette.wikia.nocookie.net/clashroyale/images/a/a1/LegendChest.png/revision/latest/scale-to-width-down/120?cb=20161002204147 width = "100"></th>
                    <th>Legendary Chests contain one Legendary Card from any Arena, allowing one to obtain Cards in higher Arenas. Legendary Chests take 24 hours or 144 gems to unlock. Legendary Chests can be bought from special offers that appear in the shop every couple of weeks once a player reaches Arena 4 (P.E.K.K.A's Playhouse) or above for 500 gems. The offer appears less often than Epic Chest offers. The offers last for 24 hours.</th>
                    </tr>
                    """)
            myfile4.write("</table></body>")
            myfile4.close()
            #closes file
        elif (response.status_code == 400):
        #this error message can occur if the status code is 400. the message below will appear in a pop-up
            messagebox.showinfo("Error 400", "Error 400 has occured. Client provided incorrect parameters for the request.")
        elif (response.status_code == 403):
         #this error message can occur if the status code is 403. the message below will appear in a pop-up
            messagebox.showinfo("Error 403", "Error 403 has occured. Access denied, either because of missing/incorrect credentials or used API token does not grant access to the requested resource.")
        elif (response.status_code == 404):
         #this error message can occur if the status code is 404. the message below will appear in a pop-up
            messagebox.showinfo("Error 404", "Error 404 has occured. Resource was not found.")
        elif (response.status_code == 429):
         #this error message can occur if the status code is 429. the message below will appear in a pop-up
            messagebox.showinfo("Error 429", "Error 429 has occured. Request was throttled, because amount of requests was above the threshold defined for the used API token.")
        elif (response.status_code == 500):
         #this error message can occur if the status code is 500. the message below will appear in a pop-up
            messagebox.showinfo("Error 500", "Error 500 has occured. Unknown error happened when handeling the requests.")
        elif (reponse.status_code == 503):
         #this error message can occur if the status code is 503. the message below will appear in a pop-up
            messagebox.showinfo("Error 503", "Error 503 has occured. Service is temporarily unavailable because of maintenance.")
####### Window 
root = Tk()
root.title("Clash Royale Statistics") #declares window title as Clash Royale Statistics
root.geometry("650x500")
root.configure(background = '#aec6cf') #colour is chosen

#label
label = Label(root, text = "Find out your clash royale statistics!")
label.grid(row = 1, column = 1)
label.configure(background = '#aec6cf')

#entry space
enterTag = Entry(root)
enterTag.grid(row = 1, column = 2)

#button
btnName = Button(text = "Find My Stats", command = processBtn, height = 10, width = 20)
btnName.grid(row = 2, column = 1, columnspan = 2)

#image 1
img = ImageTk.PhotoImage(Image.open("banner2.png"))
panel = Label(root, image = img, borderwidth=0)
panel.grid(row = 0, column = 0, columnspan = 4)

#image 2
img2 = ImageTk.PhotoImage(Image.open("king.png"))
panel2 = Label(root, image = img2, borderwidth = 0)
panel2.grid(row = 1, column = 0, rowspan = 2)



root.mainloop()