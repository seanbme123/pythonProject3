def nl_first_half(self):
    question1 = input("Does your team's state begin with a letter from A-M? (y/n): ")
    while not (question1.lower().startswith('y') or question1.lower().startswith('n')):
        print("Please answer 'yes' or 'no'.")
        question1 = input("Does your team's state begin with a letter from A-M? (y/n): ")
    if question1.lower().startswith('y'):
        self.nl_teams = self.nl_teams[:8]  # remove the last half
        print(self.nl_teams)
        question2 = input("Does your team's logo have a lot of red? (y/n): ")
        while not (question2.lower().startswith('y') or question2.lower().startswith('n')):
            print("Please answer 'yes' or 'no'.")
            question2 = input("Does your team's logo have a lot of red? (y/n): ")
        if question2.lower().startswith('y'):
            self.nl_teams = self.nl_teams[:4]  # remove the last half of the remaining
            print(self.nl_teams)
            question3 = input("Does your team's state start with the letter 'A'? (y/n): ")
            while not (question3.lower().startswith('y') or question3.lower().startswith('n')):
                print("Please answer 'yes' or 'no'.")
                question3 = input("Does your team's state start with the letter 'A'? (y/n): ")
            if question3.lower().startswith('y'):
                self.nl_teams = self.nl_teams[:2]  # remove the last half of the remaining teams
                print(self.nl_teams)
                question4 = input("Is your team the Braves? (y/n): ")
                while not (question4.lower().startswith('y') or question4.lower().startswith('n')):
                    print("Please answer 'yes' or 'no'.")
                    question4 = input("Is your team the Braves? (y/n): ")
                if question4.lower().startswith('y'):
                    self.nl_teams = self.nl_teams[-1:]  # keep the braves
                    print("your team is the braves")
                    print(self.nl_teams)
                else:
                    self.nl_teams = self.nl_teams[:1]  # keep the diamondbacks
                    print("your team is the Diamondbacks!")
                    print(self.nl_teams)
            else:  # if it doesn't begin with 'A'
                self.nl_teams = self.nl_teams[-2:]
                print(self.nl_teams)
                print(self.nl_teams)
                question5 = input("is your team the Cubs? (y/n): ")
                while not (question5.lower().startswith('y') or question5.lower().startswith('n')):
                    print("Please answer 'yes' or 'no'.")
                    question5 = input("is your team the Cubs? (y/n): ")
                if question5.lower().startswith('y'):
                    self.nl_teams = self.nl_teams[:1]
                    print("your team is the cubs")
                    print(self.nl_teams)
                else:
                    self.nl_teams = self.nl_teams[-1:]
                    print("your team is the reds")
                    print(self.nl_teams)
        else:
            self.nl_teams = self.nl_teams[-4:]
            print(self.nl_teams)
            question6 = input("Does your team's state start with the latter 'M'? (y/n): ")
            while not (question6.lower().startswith('y') or question6.lower().startswith('n'))
