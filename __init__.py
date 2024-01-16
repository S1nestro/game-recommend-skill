from mycroft import MycroftSkill, intent_handler
from mycroft.skills.intent_file_handler import intent_file_handler
from adapt.intent import IntentBuilder
from random import choice


class GameRecommend(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.games_list = ["The Witcher 3", "Stardew Valley", "Celeste", "Hollow Knight", "Minecraft"]
        
    # Adapt
    
    @intent_handler('recommend.game.intent')
    def handle_recommend_game(self, message):
        recommended_game = choice(self.games_list)
        self.speak_dialog('recommend.game', {'game': recommended_game})

    @intent_handler(IntentBuilder('HowToUseIntent').require('HowToUseKeyword').require('SkillKeyword'))
    def handle_how_to_use(self, message):
        self.speak("You can use this skill by asking me to recommend a game.")

    @intent_handler(IntentBuilder('WhatCanDoIntent').require('FunctionalityKeyword').require('SkillKeyword'))
    def handle_what_can_do(self, message):
        self.speak("I can recommend a random game from a predefined list.")

    # Padatious
    
    @intent_file_handler('how_to_use.intent')
    def handle_how_to_use_padatious(self, message):
        self.speak("You can use this skill by asking me to recommend a game.")

    @intent_file_handler('what_can_do.intent')
    def handle_what_can_do_padatious(self, message):
        self.speak("I can recommend a random game from a predefined list.")

def create_skill():
    return GameRecommend()
