from mycroft import MycroftSkill, intent_file_handler


class InternetStormCenterStatusReport(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('report.status.center.storm.internet.intent')
    def handle_report_status_center_storm_internet(self, message):
        self.speak_dialog('report.status.center.storm.internet')


def create_skill():
    return InternetStormCenterStatusReport()

