import sys
sys.path.append('./')
from email_bot import EmailBot
import time
import random

class ElonMusk() :
    player_details = {}
    world_issue = ""

    def __init__(self, number_of_players) :
        if not isinstance(number_of_players, int) :
            raise Exception(f"{number_of_players} must be int.")
        else :
            self.number_of_players = number_of_players
            self.play()
    
    def get_player_info(self) :
        verified = False
        while not verified :
            name = input("Name: ")
            email = input("Email address: ")
            verification_response = input(f"\nPlease confirm that the following details are correct:\nName: {name}. Email address: {email}\nY/n?")
            if verification_response.lower().replace(' ', '') != 'y' :
                print("Please reenter your details:")
                continue
            else :
                print("Confirmed")
                self.player_details[name.lower().replace(' ', '')] = email.lower().replace(' ', '')
                verified=True
        print("")

    def get_players_info(self) :
        for i in range(self.number_of_players) :
            print(f"Player {i+1} please insert your details.")
            self.get_player_info()

    def print_players_summary(self) :
        i=1
        for name, email in self.player_details.items() :
            print(f"Player {i}: {name}, {email}")
            i+=1

    def print_rules(self) :
        print("Welcome to your game of Elon Musk.\n")

    def get_world_issue(self) :
        self.world_issue = "Climate change"

    def launch_emailbot(self) :
        self.emailbot = EmailBot(self.world_issue, self.elon)

    def send_email(self, email, name) :
        self.emailbot.send_email(email, name)

    def select_elon(self) :
        self.elon = random.choice(list(self.player_details.keys()))

    def send_emails(self) :
        self.launch_emailbot()
        for name, email in self.player_details.items() :
            self.send_email(email, name)

    def play(self) :
        self.print_rules()
        time.sleep(5)
        self.get_players_info()
        self.print_players_summary()
        self.get_world_issue()
        self.select_elon()
        self.send_emails()

ElonMusk(3)