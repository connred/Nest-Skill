# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.


# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

class NestSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(NestSkill, self).__init__(name="NestSkill")

        # Initialize working variables used within the skill.
        self.count = 0

    @intent_handler(IntentBuilder("").require("Temperature").require("At").require("Currently"))
    def handle_temp_question_intent(self, message):

        # retrive data thru api there
        currentTemp = 67; #change to get temp thru api
        self.speak_dialog("current.temp", data={"currentTemp": currentTemp})

    @intent_handler(IntentBuilder("").require("Temperature").require("Set"))
    def handle_count_intent(self, message):
        # num = message.data
        num = 70
        # get number spoken
        # set nest device to number {{num}}

        self.speak_dialog("temp.set", data={'num': num})

    @intent_handler(IntentBuilder("").require("Camera").require("Status"))
    def handle_count_intent(self, message):
        #
        #use nest to get status
        nest = true # true on false off
        status = "ON"
        if (nest != true){
            status = "OFF"
        } else {
            status = "ON"
        }
        self.speak_dialog("status.cam", data={'status': status})






    ######
        #if message.data["Dir"] == "up":
        #    self.count += 1
        #else:  # assume "down"
        #    self.count -= 1
        #self.speak_dialog("count.is.now", data={"count": self.count})

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return NestSkill()
