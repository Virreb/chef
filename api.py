# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_restful import Resource, Api

import db_functions
import api_functions
import os


# Global constants
VERSION = '1.0'
TOKEN_LENGTH = 20
DEBUG = False

port = int(os.getenv('PORT', 5000))

# Init app to API
app = Flask(__name__)
api = Api(app, prefix=f'/api/v{VERSION}')


class Customer(Resource):

    def get(self):

        # Check token
        requester = api_functions.authenticate_token()

        # Set search key depending on company
        search_column = api_functions.get_search_column(requester)

        # Prepare to get arguments
        request_arg_specs = {
            search_column:
                {
                    'type': str,
                    'importance': 'required'
                }
        }

        # Get arguments
        args = api_functions.get_and_parse_args_from_request(request_arg_specs)

        # Values for DB2 call
        search_value = args[search_column]
        wanted_columns = READ_ACCESS_KEYS[requester]

        # Get data about customer
        customer = db_functions.read_customer(search_value, search_column, wanted_columns)

        # Create a correct json-response
        return jsonify(
            data=customer,
            message=f'Response for customer with {search_column}:{search_value}'   # TODO: REMOVE MESSAGE?
        )

    def put(self):
        import datetime

        # Check token
        requester = api_functions.authenticate_token()

        # Get column to search in depending on the requester
        search_column = api_functions.get_search_column(requester)

        # Get valid column names for the requesting company
        approved_column_names = WRITE_ACCESS_KEYS[requester]

        # Format the columns for the parser
        request_arg_specs = dict()
        for col in approved_column_names:
            request_arg_specs[col] = \
                {
                    'type': str,
                    'importance': 'optional'
                }

        # We need the column to search in to be able to upsert customer
        request_arg_specs[search_column]['importance'] = 'required'

        # Parse args
        args = api_functions.get_and_parse_args_from_request(request_arg_specs)

        # Add update time and by
        args['LAST_UPDATED'] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        args['LAST_UPDATED_BY'] = requester

        # Get value to search for
        search_value = args[search_column]

        # Create/update customer with args
        status = db_functions.create_customer(search_value, search_column, args)

        if status is True:
            return jsonify(
                message=f'Customer updated/inserted'   # TODO: Remove message?
            )

# Connect endpoints to classes
api.add_resource(Customer, '/customer')

# Run the flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=DEBUG)
