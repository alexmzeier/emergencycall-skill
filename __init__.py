from mycroft import MycroftSkill, intent_file_handler


class Emergencycall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('emergencycall.intent')
    def handle_emergencycall(self, message):
        self.speak_dialog('emergencycall')


def create_skill():
    return Emergencycall()

