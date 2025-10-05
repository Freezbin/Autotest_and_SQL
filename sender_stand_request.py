import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.headers)


def get_order_by_track(track_number):
    return requests.get(
        configuration.URL_SERVICE + configuration.getting_order_by_track,
        params={"t": track_number},
        headers=data.headers
    )