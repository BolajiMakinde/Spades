# # Bolaji Makinde Odusola
# SPADES

# currently working on adding cheat detection

# fixing logic



# assinged

# AI- Plays spades last - Plays lowest card unless best in stack

# Plays in order, winner goes first

# Export to CSV

# Comment everything out


# ?????????????????????????????????????? . ######################################
# ?????????????????????????????????????  %  #####################################
# ????????????????????????????????????  %*:  ####################################
# ???????????????????????????????????  %#*?:  ###################################
# ?????????????????????????????????  ,%##*??:.  #################################
# ???????????????????????????????  ,%##*?*#*??:.  ###############################
# ?????????????????????????????  ,%###*??*##*???:.  #############################
# ???????????????????????????  ,%####*???*###*????:.  ###########################
# ?????????????????????????  ,%####**????*####**????:.  #########################
# ???????????????????????  ,%#####**?????*#####**?????:.  #######################
# ??????????????????????  %######**??????*######**??????:  ######################
# ?????????????????????  %######**???????*#######**??????:  #####################
# ????????????????????  %######***???????*#######***??????:  ####################
# ????????????????????  %######***???????*#######***??????:  ####################
# ????????????????????  %######***???????*#######***??????:  ####################
# ?????????????????????  %######**??????***######**??????:  #####################
# ??????????????????????  '%######****:^%*:^%****??????:'  ######################
# ????????????????????????   '%####*:'  %*:  '%*????:'   ########################
# ??????????????????????????           %#*?:           ##########################
# ?????????????????????????????????  ,%##*??:.  #################################
# ???????????????????????????????  .%###***???:.  ###############################
# ??????????????????????????????                   ##############################
# ???????????????????????????????????????*#######################################

#   "Spades"     Jamie T Doran

#Anu is here

import random
import Lowest_Card_First as lcf

card_number = {
    "2" : 1,
    "3" : 2,
    "4" : 3,
    "5" : 4,
    "6" : 5,
    "7" : 6,
    "8" : 7,
    "9" : 8,
    "10" : 9,
    "Jack" : 10,
    "Queen" : 11,
    "King" : 12,
    "Ace" : 13,
}

suite = {
    "Clubs" : 1,
    "Diamonds" : 2,
    "Hearts" : 3,
    "Spades" : 4,
}

class player:

    def __init__(self, name, id, deck, current_bid, tricks_won, bags, _type):
        self.name = name
        self.id = id
        self.deck = deck
        self.current_bid = current_bid
        self.tricks_won = tricks_won
        self.bags = bags
        self._type = _type
    def print_player(self):
        print("Name: " + self.name + ", ID: " + str(self.id) + ", Deck: ")
        for a in range(len(self.deck)):
            self.deck[a].print_card()
        print("Current Bid: " + str(self.current_bid) + " Current Tricks Won: " + str(self.tricks_won) + " Current Bags: " + str(self.bags))
    def print_cards(self):
        for a in range(len(self.deck)):
            self.deck[a].print_card()
    def print_cards_select(self):
        for a in range(len(self.deck)):
            self.deck[a].print_cardID_select()

class card:

    def __init__(self, mynumber, mysuite, id, select_id):
        self.mynumber = list(card_number.keys())[mynumber]
        self.mysuite = list(suite.keys())[mysuite]
        self.id = id
        self.select_id = select_id
    def print_card(self):
        print(self.mynumber +" of "+ self.mysuite)
    def print_cardID(self):
        print("Card ID: "+ self.id)
    def print_cardID_select(self):
        print(self.mynumber +" of "+ self.mysuite +" (" + str(self.select_id) + ")")

player_count = 0

current_trick = 0

current_round = 1

num_of_rounds = 0

mode = "free4all" #Modes: "free4all" & "classical"

winner = []

players = []

all_cards = []

decks = []

best_of_table = None

best_player_of_table = None

def create_cards():
    global cards
    cards = []
    global all_cards
    all_cards = []
    i = 0
    for x in range(0,13):
        for y in range(0,4):
            a = card(x, y, i, 0)
            all_cards.append(a)
            i+=1

def divide_cards():
    temp_cards = all_cards
    global decks
    decks = []
    for a in range(1, player_count+1):
        deck = []
        for c in range(1, int(52/player_count)+1):
            a = random.choice(temp_cards)
            temp_cards.remove(a)
            a.select_id = c
            deck.append(a)
        decks.append(deck)
def assign_cards(numofplayers):
    for a in range(0, numofplayers):
        players[a].deck = decks[a]

def create_player(name, id, player_type):
    x = player(name, id, [], 0, 0, 0, player_type)
    x.print_player()
    players.append(x)

def place_bid(player_id):
    bid = 0
    global players
    if players[player_id]._type == "HUMAN":
        while True:
            print(players[player_id].name + ", please place your bid (0-9): ")
            try:
                bid = int(input())
            except ValueError:  # gets thrown on any input except an integer value
                continue
            if 0 <= bid <= 9:
                break
    else:
        print(players[player_id].name + ", please place your bid (0-9): ")
        k = random.randint(0,10)
        print(k)
        bid = k
    players[player_id].current_bid = bid

def request_card(player_id):
    selected_card = 0
    if players[player_id]._type == "HUMAN":
        while True:
            print(players[player_id].name + ", please place your card: ")
            players[player_id].print_cards_select()
            try:
                selected_card = int(input())
            except ValueError:  # gets thrown on any input except an integer value
                continue
            if 1 <= selected_card <= len(players[player_id].deck):
                break
    else:
        print(players[player_id].name + ", please place your card: ")
        players[player_id].print_cards_select()
        #k = random.randint(1,len(players[player_id].deck)) #insert engine here
        k = lcf.choose_Card(players[player_id].deck)
        print(k)
        selected_card = k
    score_trick(players[player_id].deck[selected_card-1], player_id)
    players[player_id].deck.pop(selected_card-1)
    # reasign cards
    for a in range(selected_card-1, len(players[player_id].deck)):
        players[player_id].deck[a].select_id -=1

def score_trick(c, players_id):
    global best_of_table
    global best_player_of_table
    if best_of_table == None:
        best_of_table = c
        best_player_of_table = players[players_id]
    elif best_of_table.mysuite == "Spades":
        if c.mysuite == "Spades" and c.mynumber > best_of_table.mynumber:
            best_of_table = c
            best_player_of_table = players[players_id]
    elif c.mysuite == "Spades":
        best_of_table = c
        best_player_of_table = players[players_id]
    elif c.mynumber > best_of_table.mynumber:
        best_of_table = c #whoever goes last in event of tie wins
        best_player_of_table = players[players_id]

def give_bags():
    global players
    for a in range(len(players)):
        if players[a].tricks_won >= players[a].current_bid:
            players[a].bags += players[a].current_bid
        else:
            players[a].bags += players[a].tricks_won - players[a].current_bid

#Game Logic
def game():
    global player_count
    global current_trick
    global best_player_of_table
    global best_of_table
    global num_of_rounds
    global winner
    global players
    global mode
    player_count = 0
    current_trick = 0

    print()
    print("Welcome to SPADES!")
    print()
    y = ""
    while(y.lower() != "free4all" and y.lower() != "classical"):
        if mode == "free4all":
            print('Please select a mode ("classical" or "free4all"):')
            y = input().lower()
    mode = y
    print()
    while True:
        print("How many rounds do you want?")
        try:
            num_of_rounds = int(input())
        except ValueError:  # gets thrown on any input except an integer value
            print("Please input a number (0-9)")
            continue
        if 1 <= num_of_rounds <= 1000:
            break
    cpu_counter = 0
    if(player_count == 0):
        x = ""
        while(x == ""):
            if mode == "free4all":
                print('Type AI to add a computer or Type a name to add a player (Type Name):')
                x = input()
            elif mode == "classical":
                print('Type AI to add a computer or Type a name to add a player [NORTH](Type Name):')
                x = input()
        if(x.upper() == "AI"):
            create_player("CPU " + str(cpu_counter), player_count, "AI")
            cpu_counter += 1
            print('Hello, ' + "CPU " + str(cpu_counter))
        else:
            create_player(x, player_count, "HUMAN")
            print('Hello, ' + x)
        if mode == "classical":
            print("You are NORTH")
        player_count +=1

    while(player_count < 4):
        if(player_count > 0 and player_count < 4):
            if mode == "free4all":
                if player_count > 1:
                    print('Type START to begin,Type AI to add a computer, or Type a name to add a player')
                    x = input()
                else:
                    print('Type AI to add a computer or Type a name to add a player (Type Name):')
                    x = input()
            elif mode == "classical" and player_count == 1:
                print('Type AI to add a computer or Type a name to add a player [EAST](Type Name):')
                x = input()
            elif mode == "classical" and player_count == 2:
                print('Type AI to add a computer or Type a name to add a player [SOUTH](Type Name):')
                x = input()
            elif mode == "classical" and player_count == 3:
                print('Type AI to add a computer or Type a name to add a player [WEST](Type Name):')
                x = input()
            if(x.upper() == "START" and mode == "free4all" and player_count > 1):
                break
            elif(x.upper() == "AI"):
                create_player("CPU " + str(cpu_counter), player_count, "AI")
                cpu_counter += 1
                player_count +=1
                print('Hello, ' + "CPU" + str(cpu_counter))
            else:
                player_count +=1
                create_player(x, player_count, "HUMAN")
                print('Hello, ' + x)
            if mode == "classical":
                if player_count == 2:
                    print("You are EAST")
                elif player_count == 3:
                    print("You are SOUTH")
                else:
                    print("You are WEST")
        else:
            break
    for a in range(num_of_rounds):
        create_cards()
        divide_cards()
        assign_cards(player_count)
        for a in range(0,player_count):
            place_bid(a)
        while len(players[0].deck) != 0:
            for a in range(player_count):
                request_card(a)
            best_player_of_table.tricks_won+=1
            z = ""
            if best_of_table == players[0] and mode == "classical":
                z == "[North]"
            elif best_of_table == players[1] and mode == "classical":
                z == "[East]"
            elif best_of_table == players[2] and mode == "classical":
                z == "[South]"
            elif best_of_table == players[3] and mode == "classical":
                z == "[West]"
            print(z+best_player_of_table.name + " wins the trick!")
            best_player_of_table.print_player()
            best_of_table = None
            best_player_of_table = None
            current_trick += 1
        give_bags()
        for a in range(len(players)):
            z = ""
            if a == 0 and mode == "classical":
                z == "[North]"
            elif a == 1 and mode == "classical":
                z == "[East]"
            elif a == 2 and mode == "classical":
                z == "[South]"
            elif a == 3 and mode == "classical":
                z == "[West]"
            print(z+players[a].name + " now has " + str(players[a].bags) + " bags.")
            players[a].tricks_won = 0
            players[a].current_bid = 0
        current_trick = 0
    # Decide Winner
    if mode == "free4all":
        winner.append(players[0])
        for a in range(1, len(players)):
            if(players[a].bags > winner[0].bags):
                winner = []
                winner.append(players[a])
            elif(players[a].bags == winner[0].bags):
                winner.append(players[a])
        for a in range(len(winner)):
            print("Winner is: " + str(winner[a].name) + " with " + str(winner[a].bags) + " bags!")
    else:
        if(players[0].bags + players[2].bags > players[1].bags + players[3].bags):
            print("Game is over. Winners are North and South: " + players[0].name + " and " + players[2].name + " with " + str(players[0].bags+players[2].bags) + " bags!")
        elif(players[0].bags + players[2].bags < players[1].bags + players[3].bags):
            print("Game is over. Winners are East and West: " + players[1].name + " and " + players[3].name + " with " + str(players[1].bags+players[3].bags) + " bags!")
        else:
            print("Game is over. It is a Draw!")


game()
