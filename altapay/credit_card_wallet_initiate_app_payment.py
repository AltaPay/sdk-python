from __future__ import absolute_import, unicode_literals

from altapay.resource import Resource


class CreditCardWalletInitiateAppPayment(Resource):
    def create(self, appUrl, **kwargs):
        """
        Create a payment request.

        :arg appUrl: appURL returned in the response from the createPaymentRequest in the case of MobilePay or Vipps payment.
        :arg kwargs: used for remaining, optional, payment request
            parameters, see the AltaPay documentation for a full list.
            Note that you will need to use lists and dictionaries to map the
            URL structures from the AltaPay documentation into these kwargs.

        :rtype: :samp:`True` if a payment was created, otherwise :samp:`False`.
        """

        response = self.api.get(
            resource=appUrl, parameters=kwargs, isResourceUrl=True)
        self.merge_response(response)
        return response['APIResponse']['Body']

