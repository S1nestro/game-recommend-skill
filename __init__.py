from mycroft import MycroftSkill, intent_handler


class GameRecommend(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('recommend.game.intent')
    def handle_recommend_game(self, message):
        self.speak_dialog('recommend.game')


def create_skill():
    return GameRecommend()

