import requests

from clips import Clips


class KipptAPI:
    """KipptAPI Base class.

    This class should be used to instantiate the wrapper and authenticate.

    We can authenticate with either a user/pass or user/api token combination.
    Upon authentication with a password, we will grab the API token and use
    that for all future requests.
    """
    def __init__(self, username, **args):
        # Save our username and api_token (If given) for later use.
        self.username = username
        if 'api_token' in args:
            self.api_token = args['api_token']

        # Kippt API Docs ask that you set header information in every request.
        self.header = {'X-Kippt-Username': username,
                       'X-Kippt-Client': 'Kippt-Python-Wrapper,me@ThomasBiddle.com,https://github.com/thomasbiddle/Kippt-Projects',
                       'Content-Type': 'application/json'}

        # If given a password, let's make a request and get the api_token to use for future requests.
        if 'password' in args:
            r = requests.get(
                "https://%s:%s@kippt.com/api/account/?include_data=api_token" % (username, args['password']),
                headers=self.header)
            if r.status_code is 200:
                self.api_token = r.json()['api_token']
            else:
                raise RuntimeError("Incorrect username/password combination.")

        self.header['X-Kippt-API-Token'] = self.api_token

    def clips(self):
        return Clips(self)
