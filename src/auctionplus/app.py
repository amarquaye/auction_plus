"""
A simple implementation of monopoly plus using beeware
"""
from random import randint, choice
from functools import partial
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class AuctionPlus(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN,flex=1))

        # Box to contain label
        box1 = toga.Box(style=Pack(flex=1,padding_left=10,padding_right=10,padding_top=10))
        # label to display info the game
        game_info = toga.Label("Welcome to Auction Plus with Jesse 😎", style=Pack(flex=1))
        # Adding gameinfo to box1
        box1.add(game_info)

        # Box for label and text input
        box2 = toga.Box(style=Pack(direction=ROW,flex=1,padding_left=10,padding_right=10,padding_top=10))
        # Another label to ask for the user's name
        user_name = toga.Label('Enter your name: ')
        # Text input to ask for the users name
        self.ask_user_name = toga.TextInput(style=Pack(flex=1))
        # Adding username and askusername to box1
        box2.add(user_name,self.ask_user_name)

        # Box for displaying name and welcome message
        box3 = toga.Box(style=Pack(flex=1,padding_top=10,padding_left=10,padding_right=10))
        # Creating a submit button to display name of player in dialog box
        submit_button = toga.Button("Submit",style=Pack(flex=1),on_press=partial(self.display_name))
        # Adding submitbutton to box3
        box3.add(submit_button)

        # Box for asking player bid amount
        box4 = toga.Box(style=Pack(flex=1,padding_top=10,padding_left=10,padding_right=10,direction=ROW))
        lab1 = toga.Label('Enter the amount you want to bid in USD: ')
        self.player_bid = toga.TextInput(style=Pack(flex=1))
        
        
        # Button to submit bid
        sub_player_bid = toga.Button('Submit Bid',style=Pack(flex=1, padding_left=10),on_press=partial(self.display_bid))

        # Adding items to box4
        box4.add(lab1,self.player_bid,sub_player_bid)

        # Box for displaying bid amount
        box5 = toga.Box(style=Pack(flex=1,padding_top=10,padding_left=10,padding_right=10,direction=COLUMN))
        self.lab2 = toga.Label("",style=Pack(flex=1))
        

        # Adding label for ai bid
        self.lab3 = toga.Label("", style=Pack(flex=1))
        self.lab4 = toga.Label("", style=Pack(flex=1, padding_top=10))
        self.lab5 = toga.Label("", style=Pack(flex=1, padding_top=10))

        # Adding items to box5
        box5.add(self.lab2,self.lab3,self.lab4,self.lab5)

        
        # Adding all items to mainbox
        main_box.add(box1,box2,box3,box4,box5)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # Function to display name in dialog box when submit is clicked
    def display_name(self,widget):
        """Function to display player name in dialog"""
        self.main_window.info_dialog('Welcome',message=f"Hey {self.ask_user_name.value.title()}, enjoy the game🤪🤪")

    # Function to display player bid in lab2
    def display_bid(self,widget):
        """Function to display player's bid"""
        self.lab2.text=f"The amount you are biding is ${self.player_bid.value}\n"
        avch = (float(self.player_bid.value)-randint(1,10),float(self.player_bid.value),float(self.player_bid.value)+randint(1,10))
        ai_bid = choice(avch)
        ai_bid = float(ai_bid)
        self.lab3.text = f"The AI is making it's bid ..."
        self.lab4.text = f"The AI's bid is ${ai_bid}"

        if float(self.player_bid.value) > float(ai_bid):
            self.lab5.text = f"Congrats {self.ask_user_name.value}, you won the game 🎊"
        elif float(self.player_bid.value) == float(ai_bid):
            self.lab5.text = f"Oops, it was a draw 😛"
        elif float(self.player_bid.value) < float(ai_bid):
            self.lab5.text = f"Sorry, you lost the game to the AI 😥😥\nTry again"
        elif self.player_bid.value == None:
            self.lab2.text = f"{self.ask_user_name.value}, please enter an amount to make your bid!"

def main():
    return AuctionPlus()
