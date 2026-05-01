from __future__ import absolute_import, unicode_literals

import responses

from altapay import API, CheckoutSession

from .test_cases import TestCase


class CheckoutSessionTest(TestCase):
    def setUp(self):
        self.api = API(mode='test', auto_login=False)

    @responses.activate
    def test_create_simple_checkout_session(self):
        session = CheckoutSession(api=self.api)
        responses.add(
            responses.POST, self.get_api_url('API/checkoutSession'),
            body=self.load_xml_response('200_checkout_session.xml'),
            status=200, content_type='application/xml')
        parameters = {
            'terminals': ['Test Terminal'],
            'shop_orderid': 1234567,
            'amount': 9.95,
            'currency': 'EUR'
        }
        self.assertEqual(session.create(**parameters), True)
        self.assertIn('session', session)
        self.assertEqual(len(session.session['id']) > 0, True)
