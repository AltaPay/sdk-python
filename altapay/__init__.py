__title__ = 'altapay'
__version__ = '1.5.4'
__author__ = 'Coolshop.com'
__license__ = 'MIT'
__github_url__ = 'https://github.com/coolshop-com/AltaPay'
__api_base_url__ = {
    'test': 'https://testgateway.altapaysecure.com/merchant/',
    'production': 'https://{shop_name}.altapaysecure.com/merchant/'
}

from altapay.api import API  # NOQA
from altapay.callback import Callback  # NOQA
from altapay.chargeback import ChargebackEvent  # NOQA
from altapay.funding import CustomReport, Funding, FundingList  # NOQA
from altapay.invoice import Invoice  # NOQA
from altapay.payment import Payment  # NOQA
from altapay.reservation import Reservation  # NOQA
from altapay.resource import Resource  # NOQA
from altapay.transaction import Transaction  # NOQA
from altapay.update_order import UpdateOrder  # NOQA
