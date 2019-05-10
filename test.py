﻿###
# Domain Spell Checker is an AWS Lambda interface to perform spell checks using a domain 
# specific dictionary.
# 
# Copyright (C) 2018-2019  Asurion, LLC
#
# Domain Spell Checker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Domain Spell Checker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Domain Spell Checker.  If not, see <https://www.gnu.org/licenses/>.
###

import json
import spellchecker

event = { "body": "{\"text\":\"spel checj thes.\"}",  "resource": "/{proxy+}" }

body = json.loads(event['body'])
print(str(body))
corrected = spellchecker.check_spelling(body['text'])

print(corrected)