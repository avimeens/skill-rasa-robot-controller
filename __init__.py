from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class RasaRobotControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('RasaRobotController'))
    def handle_rasa_robot_controller(self, message):
        self.speak_dialog('rasa.robot.controller')


def create_skill():
    return RasaRobotControllerSkill()

