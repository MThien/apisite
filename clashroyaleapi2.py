import requests
import webbrowser
from tkinter import *

def processBtn():
        headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjkyZTQ4ZDg3LTdjMjAtNDViOC1iMTIzLWQ4ODJkZTBiNWQ0MyIsImlhdCI6MTU3MDU1MDE0NSwic3ViIjoiZGV2ZWxvcGVyL2MyYjY1NmYzLWE4MGMtOWU4Mi03MTdmLTcwY2I2YWYwZjY3YSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI2OS43Ny4xNjAuMiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.1GXCZ9eJ3FS76aUN8ENMCCIexq6h6jhlu6fZkwoER3qXChnZ3tu8yw1JuoVUmg3QbdsyWonafetxFw0L32oIOQ'
}
        response = requests.get("https://api.clashroyale.com/v1/players/%23" + str(enterTag.get().upper()))
        #Retrieving Data From API
        userdata = response.json()
        print(str(userdata))
        king_tower = str(userdata['expLevel'])
        player_name = str(userdata['name'])
        player_trophies = str(userdata['trophies'])
        player_best_trophies = str(userdata['bestTrophies'])
        player_wins = str(userdata['wins'])
        player_losses = str(userdata['losses'])
        #Write on website
        filename = 'file:///Users/mikey.thien/Desktop/Year-10/Design/apisite.html'
        webbrowser.open_new_tab(filename)
        myfile.write("""<html>
        <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
        body {margin:0;}
        * {
          box-sizing: border-box;
          }

        .column {
          float: left;
          width: 100%;
          padding: 10px;
          margin: px;
          }

        .row:after {
          content: "";
          display: table;
          clear: both;
          }
        </style>
        </head>""")

        myfile.write("""
        <body>
        <div class="row">
          <div class="column" style="background-color:#aaa;">
            <h2>""" + player_name + """</h2>
            <p>"""+tag.upper()+"""</p>
          </div><div class="row">
          <div class="column" style="background-color:#aaa;">
            <h2>King Tower Level:</h2>
            <p>"""+king_tower+"""</p>
          </div><div class="row">
          <div class="column" style="background-color:#aaa;">
            <h2>Player Trophies: </h2>
            <p>"""+player_trophies+"""</p>
          </div><div class="row">
          <div class="column" style="background-color:#aaa;">
            <h2>Best Trophies: </h2>
            <p>"""+player_best_trophies+"""</p>
          </div>
        </body>
        """)
        myfile.close()

window = Tk()
window.title("Clash Royale Statistics")
label = Label(window, text = "Find out your clash royale statistics!")
enterTag = Entry(window)
btnName = Button(text = "Find My Stats", command = processBtn)
label.grid(row = 1, column = 1)
enterTag.grid(row = 1, column = 2)
btnName.grid(row = 1, column = 3)
mainloop()