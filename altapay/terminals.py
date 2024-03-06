from __future__ import absolute_import, unicode_literals

from altapay import exceptions
from altapay.resource import Resource


class Terminals(Resource):
    @classmethod
    def __init__(self, api):
        """
        Initialize the Terminal object by fetching terminals data from AltaPay.

        :arg api: An API object used for AltaPay communication.
        """
        response = api.get('API/getTerminals')['APIResponse']

        try:
            terminals = response['Body']['Terminals']['Terminal']
        except KeyError:
            raise exceptions.ResourceNotFoundError('Terminals not found')
        
        if isinstance(terminals, list):
            self.terminals = terminals
        else:
            self.terminals = [terminals]
