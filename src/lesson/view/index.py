# lesson/view/index.py
#
# This file is part of LESSON.  LESSON is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2 or later.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright (C) 2012 Jonathan Dieter <jdieter@lesbg.com>

uuid = u'7bb2302a-a003-11e1-9b06-00163e9a5f9b'

from render import Page

class IndexPage(Page):
    url = "/"
    url_absolute = True

    def get(self):
        return {u'user': self.user.Username, u'firstname': self.user.FirstName, u'surname': self.user.Surname}
