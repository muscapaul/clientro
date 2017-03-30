import unittest

from betfairlightweight.filters import (
    market_filter,
    time_range,
    price_data,
    ex_best_offers_overrides,
    price_projection,
    place_instruction,
    limit_on_close_order,
    limit_order,
    cancel_instruction,
    market_on_close_order,
    replace_instruction,
    update_instruction,
)


class FilterTest(unittest.TestCase):

    def test_time_range(self):
        response = time_range()
        assert response == {'from': None, 'to': None}

        response = time_range(from_='123', to='456')
        assert response == {'from': '123', 'to': '456'}

    def test_market_filter(self):
        response = market_filter()
        assert response == {}

        response = market_filter(marketIds=['1.123'])
        assert response == {'marketIds': ['1.123']}

    def test_price_data(self):
        response = price_data()
        assert response == []

        response = price_data(ex_best_offers=True)
        assert response == ['EX_BEST_OFFERS']

    def test_ex_best_offers_overrides(self):
        response = ex_best_offers_overrides()
        assert response == {}

    def test_price_projection(self):
        response = price_projection()
        assert response == {
            'rolloverStakes': False, 'priceData': [], 'exBestOffersOverrides': {}, 'virtualise': True
        }

    def test_place_instruction(self):
        response = place_instruction('LIMIT', 123, 'LAY')
        assert response == {'orderType': 'LIMIT', 'selectionId': 123, 'side': 'LAY'}

    def test_limit_order(self):
        response = limit_order(1.1, 123, 'LAPSE')
        assert response == {'size': 1.1, 'price': 123, 'persistenceType': 'LAPSE'}

    def test_limit_on_close_order(self):
        response = limit_on_close_order(1.1, 2.2)
        assert response == {'liability': 1.1, 'price': 2.2}

    def test_market_on_close_order(self):
        response = market_on_close_order(1.1)
        assert response == {'liability': 1.1}

    def test_cancel_instruction(self):
        response = cancel_instruction('1.123')
        assert response == {'betId': '1.123'}

    def test_replace_instruction(self):
        response = replace_instruction('1.123', 12)
        assert response == {'betId': '1.123', 'newPrice': 12}

    def test_update_instruction(self):
        response = update_instruction('1.123', 'LAPSE')
        assert response == {'betId': '1.123', 'newPersistenceType': 'LAPSE'}
