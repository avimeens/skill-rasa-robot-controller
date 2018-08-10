from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class RasaRobotControllerSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.utterance = None

    def initialize(self):
        self.register_rasa_intent('move.json', self.handle_robot_move)
        self.register_rasa_intent('stop.json', self.handle_robot_stop)
        self.register_rasa_intent('turn.json', self.handle_robot_turn)
        self.register_rasa_intent('error.json', self.handle_intent_error)

    def handle_intent_error(self, message):
        if self.utterance is None:
            self.speak_dialog("This is embarrassing, I could not find the previous utterance")
            return
        resp = {'utt': self.utterance, 'intents': "move or turn or fetch"}
        intent = self.get_response(dialog='robot.query.user', data=resp)
        if intent is None:
            intent = self.get_response(dialog='robot.repeat.prompt')
        resp = {'utt': self.utterance, 'intent' : intent}
        self.speak_dialog('robot.confirm.intent', data=resp)

    def handle_robot_move(self, message):
        self.utterance = message.data.get("utterance");
        print "Utterance = " + self.utterance
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
        self.utterance = message.data.get("utterance");
        print "Utterance = " + self.utterance
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

    def stop(self):
        self.speak_dialog('robot.stop')
        pass
        
def create_skill():
    return RasaRobotControllerSkill()

