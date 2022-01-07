# MIT LICENSE
# Mycroft Skill: Internet Storm Center Status Report
# Copyright (C)2022 Justin Warwick (justin.warwick@gmail.com)

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""Mycroft skill for ascertaining and reporting the current Internet Storm Center global threat condition."""
from mycroft import MycroftSkill, intent_file_handler
import requests

class InternetStormCenterStatusReport(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('report.status.center.storm.internet.intent')
    def handle_report_status_center_storm_internet(self, message):
        r = requests.get('https://isc.sans.edu/infocon.txt')
        self.log.info("isc.sans.edu HTTP GET was " + str(r.status_code))
        self.log.info("isc.sans.edu HTTP GET was " + r.text)
        #gui stuff is just crashing the display right now.
        #self.gui.clear()
        #self.gui.show_text(r.text, "Internet Storm Center condition")
        self.speak_dialog('report.status.center.storm.internet',{'isc_status': r.text})


def create_skill():
    return InternetStormCenterStatusReport()

