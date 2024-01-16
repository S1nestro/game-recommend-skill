from mycroft import MycroftSkill, intent_handler


class GameRecommend(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.games_list = ["The Witcher 3", "Stardew Valley", "Celeste", "Hollow Knight", "Minecraft"]

    @intent_handler('recommend.game.intent')
    def handle_recommend_game(self, message):
        recommended_game = choice(self.games_list)
        self.speak_dialog('recommend.game', {'game': recommended_game})



def create_skill():
    return GameRecommend()

