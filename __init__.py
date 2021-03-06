# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
#This code is written by Rahul Kumar Shandilya
from os.path import dirname

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger


import requests

__author__ = 'Rahul Kumar Shandilya'

LOGGER = getLogger(__name__)


class ItsmUserSkill4(MycroftSkill):
    def __init__(self):
        super(ItsmUserSkill4, self).__init__(name="ItsmUserSkill4")

    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        
        itsm_user_intent4 = IntentBuilder("itsmuserintent4"). \
            require("ItsmUserKeyword4").build()
        self.register_intent(itsm_user_intent4, self.handle_itsm_user_intent4)

    def handle_itsm_user_intent4(self, message):
        url = 'https://dev22921.service-now.com/api/now/table/incident?sysparm_query=assigned_to%3D66e1f49edb5d13006b72712ebf9619c2&sysparm_display_value=true&sysparm_exclude_reference_link=true&sysparm_fields=number%2Ccaller_id%2Cshort_description%2Cpriority'
        user = '531834'
        pwd = 'Welcome!2345'
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        # Do the HTTP request
        response = requests.get(url, auth=(user, pwd), headers=headers )
        # Check for HTTP codes other than 200
        if response.status_code != 200: 
            print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            exit()
        # Decode the JSON response into a dictionary and use the data
        data = response.json()
        length = len(data['result'])
        x = 0
        r = data['result']
        detail = ""
        while x<length:
            detail += "Your Incident {}".format(x+1) +" is "+ r[x]['number'] + " having caller as "+r[x]['caller_id']+ " with Short Description "+ r[x]['short_description'] + " and priority as "+r[x]['priority']+"."
            x += 1
        self.speak("Hello")
        self.speak(detail)        

    def stop(self):
        pass


def create_skill():
    return ItsmUserSkill4()
