import random

class Game:
    def __init__(self):
        self.players = []

# determines the number of players and creates new players
    def number_of_players(self):
        players = int(input("How many players? "))
        for p in range(players): 
            name = input("Enter name for Player {} : ".format(p+1)).capitalize()
            self.players.append({name:[]})
        return self.players

# prints game instructions
    def print_instruction(self):
        print('\nWelcome to the Guessing Game!')
        print("\nYou will have three chances to guess the computer's number.")
        print("\nWith each guess, you'll lose a point and receive a hint.")
        print("\n")

# turns string answers into numbers
    def switch(self, arg):
        switch = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
            'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10}
        return switch.get(arg.lower(), arg)

    def guess_number(self, player_name, score_list):
        computer_guess= random.randint(1,9)
        print("\n")
        print("It's {} turn! ".format(player_name).upper())
        # each player gets 3 tries
        for tries in range(3):
            while True:
                try:
                    user_input = int(input('Guess a number between 1 thru 9. '))
                    if user_input in range(1,10):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print('Invalid input, try again.')
            if user_input > computer_guess:
                print('Nice try {}, but your guess is too high.'.format(player_name))
            elif user_input < computer_guess:
                print('Nice try {}, but your guess is too low.'.format(player_name))
            else:
                break
        if user_input == computer_guess:
            print('Congratulations {}! YOU GUESSED RIGHT!'.format(player_name.upper()))
            score = int(3-tries)
            score_list.append(score)
        else:
            print('Sorry {}. You lost.'.format(player_name))
            score = 0
            score_list.append(score)
        print('The number was {}.'.format(computer_guess))
        print("\n{} score for this round is {}.".format(player_name ,score))

# Post end game results
    def end_game_results(self):
        print("\n__FINAL SCORE__")
        for p in self.players:
            for name in p:
                print("Total score for {} is {}! ".format(name, sum(p[name])))
        print("\n")
        print("Thanks for playing!")
        

# initates the game
    def play_game(self):
        self.print_instruction()
        rounds = int(input("How many rounds do you want to play? "))
        self.number_of_players()
        for r in range(rounds):
            print('\n')
            print("__ROUND {}__".format(r+1))
            for p in self.players:
                for name in p:
                    self.guess_number(name, p[name])
        self.end_game_results()


new = Game()
new.play_game()
