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

page_header = """
<!DOCTYPE html>
<html>
<head>

    </style>
</head>
<body>
    <h1>
        Signup
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""



class MainHandler(webapp2.RequestHandler):
    def get(self):
        #form for username
        user_name_form = """
        <form action = "/username" method = "post">
            <label>
                User name <input type = "text" name = "username">
            </label>
            <input type = "submit">
        </form>
        <br>
        """
        #form for password
        password_form = """
        <form action = "/password" method = "post">
            <label>
                Password <input type = "password" name = "password">
            </label>
            <input type = "submit">
            </form>
        <br>
        """
        #form for password verification
        verify_form = """
        <form action = "/verify" method = "post">
            <label>
                Verify Password <input type = "password" name = "verify">
            </label>
            <input type = "submit">
        </form>
        <br>
        """
        #form for e-mail
        email_form = """
        <form action = "/email" method = "post">
            <label>
                E-mail (optional) <input type = "text" name = "email">
            </label>
            <input type = "submit">
        </form>
        """
        #self.response.write(form)
        #sentence = 'Hello world'
        content = page_header + user_name_form + password_form + verify_form + email_form + page_footer
        self.response.write(content)

def valid_username(username):
    if username and username.isalpha():
        return username

class Username(webapp2.RequestHandler):
    def post(self):
        user_name = valid_username(self.request.get("username"))
        if not (user_name):
            self.response.write('INVALID user name')
        else:
            self.response.write('VALID user name')

class Password(webapp2.RequestHandler):
    def post(self):
        sentence = 'Valid password'
        self.response.write(sentence)

class Verify(webapp2.RequestHandler):
    def post(self):
        sentence = 'It matches'
        self.response.write(sentence)

class Email(webapp2.RequestHandler):
    def post(self):
        sentence = 'Thank you'
        self.response.write(sentence)



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/username', Username),
    ('/password', Password),
    ('/verify', Verify),
    ('/email', Email),
], debug=True)
