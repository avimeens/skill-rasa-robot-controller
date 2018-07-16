from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class RasaRobotControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.register_rasa_intent('move.json', self.handle_robot_move)
        self.register_rasa_intent('stop.json', self.handle_robot_stop)
        self.register_rasa_intent('turn.json', self.handle_robot_turn)

    def handle_robot_move(self, message):
        distance = message.data.get("distance")
        if distance is None:
            self.speak_dialog('robot.no.distance')
            return
        direction = message.data.get("direction")
        if direction is None:
            self.speak_dialog('robot.no.direction')
            return
        unit = message.data.get("unit")
        if unit is None:
            self.speak_dialog('robot.no.unit')
            return
        resp = {'distance' : distance, 'direction' : direction, 'unit' : unit}
        self.speak_dialog('robot.move', data=resp)

    def handle_robot_turn(self, message):
        distance = message.data.get("distance")
        if distance is None:
            self.speak_dialog('robot.no.distance')
            return
        direction = message.data.get("direction")
        if direction is None:
            self.speak_dialog('robot.no.direction')
            return
        unit = message.data.get("unit")
        if unit is None:
            self.speak_dialog('robot.no.unit')
            return
        resp = {'distance' : distance, 'direction' : direction, 'unit' : unit}
        self.speak_dialog('robot.move', data=resp)

    def handle_robot_stop(self, message):
        self.speak_dialog('robot.stop')

def create_skill():
    return RasaRobotControllerSkill()

