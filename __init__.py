from va import MycroftSkill, intent_handler
from va.adapt.intent import IntentBuilder
from va.skills.context import adds_context, removes_context

class Emergencycall(MycroftSkill):
    #def __init__(self):
        #MycroftSkill.__init__(self)

    #@intent_file_handler('emergencycall.intent')
    #def handle_emergencycall(self, message):
        #self.speak_dialog('emergencycall')

    @intent_handler(IntentBuilder("EmergencyCall").require("call").require("help"))
    @adds_context("EmergencyContext")
    def handle_call(self, message, websocket):
        self.speak("Wen soll ich rufen?", websocket, expect_response=True)

    @intent_handler(IntentBuilder("RespoEmergencyCall").require("awo").require("EmergencyContext").build())
    #@removes_context("EmergencyContext")
    def handle_response(self, message, websocket):
        self.speak("Ich rufe die AWO", websocket)

def create_skill():
    return Emergencycall()

