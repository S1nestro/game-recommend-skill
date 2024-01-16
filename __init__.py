from mycroft import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder

class GameRecommend(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('recommend.game.intent')
    def handle_recommend_game(self, message):
        self.speak_dialog('recommend.game')

    @intent_handler(IntentBuilder('HowToUseIntent').require('HowToUseKeyword').require('SkillKeyword'))
    def handle_how_to_use(self, message):
        self.speak("You can use this skill by asking me to recommend a game.")

    @intent_handler(IntentBuilder('WhatCanDoIntent').require('FunctionalityKeyword').require('SkillKeyword'))
    def handle_what_can_do(self, message):
        self.speak("I can recommend a random game from a predefined list.")

def create_skill():
    return GameRecommend()
