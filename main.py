#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt
import cgi

page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>caesar</title>
    <style type="text/css">
        .error {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">caesar</a>

    </h1>
"""
# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class Index(webapp2.RequestHandler):
   def get(self):

        edit_header = "<h3>Caesar</h3>"

        # a form for adding text
        rot_form = """
        <form action="/rotate" method="post">

            <label>
            rotate by
                <input type="int" name="rotation"/>
                <br>
                <textarea input type="text" name="text" style="height: 100px; width: 400px;"></textarea>
                <br>
            </label>
            <input type="submit" value="Submit"/>
        </form>

        """

        response = page_header + "<p>" + rot_form + "</p>" + page_footer
        self.response.write(response)

class Rotate(webapp2.RequestHandler):
#rotates text based user input
#requests coming into /rotate
    def post(self):
        # look inside the request to figure out what the user typed
        rot_form = self.request.get("text")
        rot_num = self.request.get("rotation")
        en = encrypt(str(rot_form), int(rot_num))

        if rot_form != "":
            error = "You have entered no text. Please enter some text. %s" % (en)
            error_escaped = cgi.escape(error, quote=True)
            #self.redirect("/?error= {}".format(error))
            #self.redirect("/?error=" + error_escaped)


#encrypt on new page
            #self.response.write(en)
            #self.response.write('''<textarea input type="text" name="text" style="height: 100px; width: 400px;">'''(self.response.write(en))'''</textarea>''')
            #self.response.write(<p><body><html>(en)</p></body></html>)

#testing encrypt on same page

#escape html
#escape so html doesnt get translated rot13
        new_rot_element= "<strong>" + cgi.escape(en) + "</strong>"
        new_rot2_element= "<strong>" + cgi.escape(rot_form) + "</strong>"
        #sentence = new_movie_element + " has been added to your Watchlist!"
        #response = page_header + "<p>" + en + "</p>" + page_footer
        response = page_header + "<textarea>" + en + "</textarea>" + page_footer
        self.response.write(response)



app = webapp2.WSGIApplication([
    ('/', Index),
    ('/rotate', Rotate)
], debug=True)
