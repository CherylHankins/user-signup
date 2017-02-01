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

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
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
                    <input name = "username" type = "text" value required>
                </td>
                <td>
                    <div style="color: red">%(error)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "password">Password</label>
                </td>
                <td>
                    <input name = "password" type = "password" required>
                </td>
                <td>
                    <div style="color: red">%(error)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "verify">Verify Password</label>
                </td>
                <td>
                    <input name = "verify" type = "password" required>
                </td>
                <td>
                    <div style="color: red">%(error)s</div>
                </td>
            </tr>
            <tr>
                <td>
                    <label for = "email">Email (optional)</label>
                </td>
                <td>

                    <input name = "email" type = "email" value>
                </td>
                <td>
                    <div style="color: red">%(error)s</div>
                </td>
            </tr>
        </tbody>
    </table>
    <input type = "submit">
</form>
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
    def get(self):
        content = page_header + form + page_footer
        self.response.write(content)

    def write_form(self, error=""):
        self.response.out.write(form % {"error":error})

    def post(self):
        have_error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")
        welcome_sentence = "<h2>"'Welcome, ' + username + '!'"</h2>"
        #params = dict('username'=username, 'email'=email)



        if not valid_username(username):
            self.write_form("That's not a valid user name.")
        if not valid_password(password):
            self.write_form("That wasn't a valid password.")
        elif password != verify:

            self.write_form ("Your passwords didn't match.")
        if not valid_email(email):

            self.write_form ("That's not a valid email.")
        #if have_error:
            #self.write_form(**params)

        else:
            self.response.out.write(welcome_sentence)










app = webapp2.WSGIApplication([
    ('/', Signup),


], debug=True)
