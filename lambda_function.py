###
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

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    '''A simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    '''
    print("Received event: " + json.dumps(event, indent=2))

    operation = event['httpMethod']
    if operation == "GET":
        payload = event['queryStringParameters']

        response = {}
        response['output'] = spellchecker.check_spelling(payload)

        return respond(None, json.loads(response))

    elif operation == "POST":
        payload = json.loads(event['body'])
        print("payload: " + str(payload))
    
        response = {}
        response['output'] = spellchecker.check_spelling(payload['text'])

        return respond(None, response)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
