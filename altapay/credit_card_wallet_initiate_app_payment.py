from __future__ import absolute_import, unicode_literals

from altapay.resource import Resource


class CreditCardWalletInitiateAppPayment(Resource):
    def create(self, app_url, **kwargs):
        """
        Create a payment request.

        :arg app_url: Returned in the response from the createPaymentRequest
            in the case of credit card wallet payment e.g. MobilePay or Vipps.
        :arg kwargs: used for remaining, optional, payment request
            parameters, see the AltaPay documentation for a full list.
            Note that you will need to use lists and dictionaries to map the
            URL structures from the AltaPay documentation into these kwargs.

        :rtype: :samp:`True` if a payment was created, otherwise :samp:`False`.
        """

        response = self.api.get(
            resource=app_url, parameters=kwargs, is_resource_url=True)
        self.merge_response(response)
        return response['APIResponse']['Body']
