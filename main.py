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

</head>
<body>
    <h1>
        Signup
    </h1>
"""

form = """
<form method = "post">
    <table>
        <tbody>
            <tr>
                <td>
                    <label for = "username">User name</label>
                </td>
                <td>
                    <input name = "username" type = "text" value = "%(username)s">
                </td>
                <td>
                    <div style="color: red">%(e1)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "password">Password</label>
                </td>
                <td>
                    <input name = "password" type = "password" >
                </td>
                <td>
                    <div style="color: red">%(e2)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "verify">Verify Password</label>
                </td>
                <td>
                    <input name = "verify" type = "password" >
                </td>
                <td>
                    <div style="color: red">%(e3)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "email">Email (optional)</label>
                </td>
                <td>

                    <input name = "email" type = "email" value = "%(email)s">
                </td>
                <td>
                    <div style="color: red">%(e4)s</div>
                </td>
            </tr>
        </tbody>
    </table>
    <input type = "submit">
</form>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return not email or EMAIL_RE.match(email)



class Signup(webapp2.RequestHandler):
    def write_form(self,error = dict(),username = "", password = "", verify = "", email = ""):
        response = {"username":username, "email":email,"e1":error.get("e1", ""), "e2":error.get("e2",""), "e3":error.get("e3",""), "e4":error.get("e4","")}
        self.response.out.write(form % response)

    def get(self):
        response = {"username":"", "email":"", "e1":"", "e2":"", "e3":"", "e4":""}
        content = page_header + form % response + page_footer
        self.response.write(content)

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        welcome_sentence = "<h2>"'Welcome, ' + username + '!'"</h2>"

        e1 = "That's not a valid username"
        e2 = "That wasn't a valid password."
        e3 = "Your passwords didn't match."
        e4 = "That's not a valid email."

        errors = dict()

        if not valid_username(username):
            errors ["e1"] = e1
        if not valid_password(password):
            errors ["e2"] = e2
        elif password != verify:
            errors ["e3"] = e3
        if not valid_email(email):
            errors ["e4"] = e4
        if errors:
            self.write_form(errors, username = username, email = email)

        else:
            self.response.out.write(welcome_sentence)


app = webapp2.WSGIApplication([
    ('/', Signup)

], debug=True)
