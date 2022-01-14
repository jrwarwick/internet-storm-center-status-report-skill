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
        self.display_condition(r.text)
        self.speak_dialog('report.status.center.storm.internet',{'isc_status': r.text})

    @intent_file_handler('watch.status.center.storm.internet.intent')
    def handle_watch_status_center_storm_internet(self, message):
        self.schedule_repeating_event(self.handle_nongreen_status_center_storm_internet, None, 60 * int(self.settings.get('polling_frequency',60)))
        self.speak("Very well, I will notify you if I notice that the I S C global threat condition changes to a non-green condition.")
        self.speak("I will be checking every " + self.settings.get('polling_frequency',60) + " minutes.")

    def handle_nongreen_status_center_storm_internet(self):
        r = requests.get('https://isc.sans.edu/infocon.txt')
        self.log.info("(scheduled polling) isc.sans.edu HTTP GET was " + str(r.status_code))
        self.log.info("(scheduled polling) isc.sans.edu HTTP GET was " + r.text)
        #TODO: keep track of consecutive failures to GET. 
        #      If it exceeds reasonable threshold, notify user and offer to UNschedule
        if not green in r.text:
            self.speak_dialog('report.status.center.storm.internet',{'isc_status': r.text})
            #TODO: more urgent/alerty version of the dialog file for these notifications.
            self.display_condition(r.text)

    def display_condition(self, condition):
        self.log.info("invocation success........" + condition)
        htmlsrc = f"""<!DOCTYPE html><html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>SANS ISC Global Threat Condition</title>
		<style>
			body{{
				background-color:black;
				margin:.25em;
				padding: 2em;
			}}
			div{{
				background-color:{condition};
				margin:.25em;
				padding: 2em;
				border-radius: 2em;
			}}
			h1{{
				text-align:center;
				text-transform:capitalize;
			}}
			#condition{{
				font-size:6em;
			}}
		</style>
	</head>
	<body> <div><h1>ISC Global Threat Condition:</h1><h1 id="condition"> {condition} </h1></div></body>
	</html>
""" 
        self.gui.show_html(htmlsrc)

def create_skill():
    return InternetStormCenterStatusReport()

