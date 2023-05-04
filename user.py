class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member:
            print("User already a member.")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print("You have successfully spent", amount, "gold card points.")
        else:
            print("Sorry, you do not have enough gold card points to spend", amount, "points.")
        return self
user1 = User("John", "Doe", "johndoe@example.com", 30).display_info().enroll().spend_points(100).display_info()
user2 = User("Jane", "Doe", "janedoe@example.com", 21, True, 500).display_info().spend_points(100).spend_points(450).display_info()
user3 = User("Santa", "Claus", "santaclaus@north.pole,com", 547, True, 1000000).display_info().spend_points(1000001).display_info()
