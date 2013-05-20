# Kippt for Python

Kippt for Python is an API wrapper for [Kippt](http://www.kippt.com).

The library strives to stay as close to the actual API structure by having each resource in
it's own class, and having each method return the original JSON without any modifications.

### Installation

    pip install kippt

### Usage
Browse through the [repository](kippt) to see the various methods available. All methods are
documented and should be fairly obvious - If not, please create an issue and I'll do what I can
to update it!


Setup your application to use Kippt, and authenticate! Kippt for Python takes either a
user/pass or user/token combination. If a password is given, Kippt will attempt to
authenticate immediately - And if successful, will grab the api_token and use that
for any further requests.

    from kippt import Kippt

    k = Kippt('my_username', password='my_password')
    # or..
    k = Kippt('my_username', api_token='my_crazy_long_api_token')

Checkout your profile:
    k.account()

Checkout some other user's profile:
    k.users().user(12345).profile()

Checkout your Kippt news feed:
    k.clips().feed()

How about with a larger limit?:
    k.clips().feed(limit=100)

Or offset?:
    k.clips().feed(limit=40, offset=5)

### License

[MIT](LICENSE)

### Contributing in 4 easy steps!
- Fork the project.
- Create a new feature branch.
- Hack.
- Submit a pull request.

