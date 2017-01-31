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
import re

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
        form = """
        <form action = "/validate" method = "post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for = "username">User name</label>
                        </td>
                        <td>
                            <input name = "username" type = "text" value required>
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "password">Password</label>
                        </td>
                        <td>
                            <input name = "password" type = "password" required>
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "verify">Verify Password</label>
                        </td>
                        <td>
                            <input name = "verify" type = "password" required>
                            <span class = "error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for = "email">Email (optional)</label>
                        </td>
                        <td>
                            <input name = "email" type = "email" value>
                            <span class = "error"></span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type = "submit">
        </form>
        """

        content = page_header + form + page_footer
        self.response.write(content)


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
  def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
    def valid_password(password):
        return PASS_RE.match(password)

EMAIL_RE = re.compile(r "^[\S]+@[\S]+.[\S]+$")
    def valid_email(email):
        return not email or EMAIL_RE.match(email)


class Validate(webapp2.RequestHandler):
    def post(self):
        user_name = valid_username(self.request.get("username"))
        if not (user_name):
            self.response.write('INVALID user name')
        else:
            self.response.write('Welcome, ' + user_name + "!")





def valid_username(username):
    if len(username) > 0:
        if username and username.isalpha():
            return username

#class Username(webapp2.RequestHandler):
    #def post(self):
        #user_name = valid_username(self.request.get("username"))
        #if not (user_name):
            #self.response.write('INVALID user name')
        #else:
            #self.response.write('VALID user name')


def valid_password(password, verify):
    if len(password) > 0:
        password = (self.request.get("password"))
        verify = (self.request.get("verify"))
        if password.index == verify.index:
            return password

#class Password(webapp2.RequestHandler):
    #    sentence = 'Valid password'
        #self.response.write(sentence)

#class Verify(webapp2.RequestHandler):
    #def post(self):
        #verified = valid_password(self.request.get("password"),(self.request.get("verify")))
        #if not (verified):
            #self.response.write("Passwords do not match")
        #else:
            #self.response.write('Good Password')


#def valid_email(email):
    #email.find('@')
    #email.find(.)
    #if

#class Email(webapp2.RequestHandler):
    #def post(self):
        #sentence = 'Thank you'
        #self.response.write(sentence)



app = webapp2.WSGIApplication([
    ('/', MainHandler),

], debug=True)
