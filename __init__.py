# workshop 1.3.2
# from mycroft import MycroftSkill, intent_handler
# from adapt.intent import IntentBuilder
# from random import choice
# from mycroft.skills.core import intent_file_handler


# class GameRecommend(MycroftSkill):
#     def __init__(self):
#         MycroftSkill.__init__(self)
#         self.games_list = ["The Witcher 3", "Stardew Valley", "Celeste", "Hollow Knight", "Minecraft"]
        
#     # Adapt
    
#     @intent_handler('recommend.game.intent')
#     def handle_recommend_game(self, message):
#         recommended_game = choice(self.games_list)
#         self.speak_dialog('recommend.game', {'game': recommended_game})

#     @intent_handler(IntentBuilder('HowToUseIntent').require('HowToUseKeyword').require('SkillKeyword'))
#     def handle_how_to_use(self, message):
#         self.speak("You can use this skill by asking me to recommend a game.")

#     @intent_handler(IntentBuilder('WhatCanDoIntent').require('FunctionalityKeyword').require('SkillKeyword'))
#     def handle_what_can_do(self, message):
#         self.speak("I can recommend a random game from a predefined list.")

#     # Padatious
#     @intent_file_handler('how_to_use.intent')
#     def handle_how_to_use_padatious(self, message):
#         self.speak("You can use this skill by asking me to recommend a game.")

#     @intent_file_handler('what_can_do.intent')
#     def handle_what_can_do_padatious(self, message):
#         self.speak("I can recommend a random game from a predefined list.")
        

# def create_skill():
#     return GameRecommend()

# workshop 2.2.1 
import csv
import os
from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
from random import choice
from mycroft.skills.core import intent_file_handler

class GameRecommend(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.games_list = ["The Witcher 3", "Stardew Valley", "Celeste", "Hollow Knight", "Minecraft"]
        self.played_games_file = os.path.join(self.file_system.path, 'played_games.csv')
        self.played_games = self.load_played_games()

    def load_played_games(self):
        if not os.path.exists(self.played_games_file):
            return []
        with open(self.played_games_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return [row[0] for row in reader]

    def save_played_game(self, game):
        with open(self.played_games_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([game])

    def get_unplayed_game(self):
        unplayed = [game for game in self.games_list if game not in self.played_games]
        return choice(unplayed) if unplayed else None

    @intent_handler('recommend.game.intent')
    def handle_recommend_game(self, message):
        recommended_game = self.get_unplayed_game()
        if not recommended_game:
            self.speak("It seems you have played all the games I know.")
            return
        self.speak_dialog('recommend.game', {'game': recommended_game})
        self.set_context('GameRecommended', recommended_game)

    @intent_handler(IntentBuilder('').require('Affirmative').require('GameRecommended'))
    def handle_played_game(self, message):
        game = message.data.get('GameRecommended')
        self.save_played_game(game)
        self.speak("Okay, I'll remember that. Let me recommend another game.")
        self.handle_recommend_game(None)

    @intent_handler(IntentBuilder('').require('Negative').require('GameRecommended'))
    def handle_not_played_game(self, message):
        game = message.data.get('GameRecommended')
        self.speak(f"Great! Enjoy playing {game}.")
    
    @intent_handler(IntentBuilder('HowToUseIntent').require('HowToUseKeyword').require('SkillKeyword'))
    def handle_how_to_use(self, message):
        self.speak("You can use this skill by asking me to recommend a game.")
    
    @intent_handler(IntentBuilder('WhatCanDoIntent').require('FunctionalityKeyword').require('SkillKeyword'))
    def handle_what_can_do(self, message):
        self.speak("I can recommend a random game from a predefined list. I can also remember which games you have played.")
    
    @intent_file_handler('how_to_use.intent')
    def handle_how_to_use_padatious(self, message):
        self.speak("You can use this skill by asking me to recommend a game.")
    
    @intent_file_handler('what_can_do.intent')
    def handle_what_can_do_padatious(self, message):
        self.speak("I can recommend a random game from a predefined list. I can also remember which games you have played.")

def create_skill():
    return GameRecommend()
