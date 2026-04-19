from __future__ import absolute_import, unicode_literals

from altapay.resource import Resource


class CheckoutSession(Resource):
    def create(self, terminals, shop_orderid, amount, currency, **kwargs):
        """
        Create a checkout session.

        Creates a checkout session for the current customer's basket grouping
        all available payment methods. The session should be reused for
        different payment methods until the payment is not finalized.

        Checkout session is used to improve fraud detection and help maximize
        conversion rate.

        :arg terminals: list of terminal names available for the user based on
            the checkout parameters. Can also be a single terminal name string.
        :arg shop_orderid: your order ID to be attached to the checkout session
        :arg amount: order amount in floating point
        :arg currency: currency for the checkout session
        :arg kwargs: used for remaining, optional, parameters, see the AltaPay
            documentation for a full list. Note that you will need to use
            lists and dictionaries to map the URL structures from the AltaPay
            documentation into these kwargs.

        :rtype: :samp:`True` if a checkout session was created, otherwise
            :samp:`False`.
        """
        if isinstance(terminals, str):
            terminals = [terminals]

        parameters = {
            'terminals': terminals,
            'shop_orderid': shop_orderid,
            'amount': amount,
            'currency': currency,
        }

        parameters.update(kwargs)

        response = self.api.post(
            self.get_post_url(), data=parameters)
        self.merge_response(response)
        return self.success

    def get_post_url(self):
        return 'API/checkoutSession'
