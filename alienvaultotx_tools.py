from OTXv2 import OTXv2
import IndicatorTypes
import sys
import json

OTX_SERVER = "https://otx.alienvault.com"


def search_alienvault(ip, api_key):
    """
    Search information about specific IP
    :param ip: IP address
    :param api_key: AlienVaultOTX API Key
    :return: dict
    """
    otx = OTXv2(api_key, server=OTX_SERVER)

    return otx. get_indicator_details_full(IndicatorTypes.
                                           IPv4, ip)


def save_results(search_results, file_name):
    """
    Save search results as JSON file
    :param search_results: AlienVaultOTX search results
    :param file_name: File name
    :return: None
    """
    with open(file_name, "w") as save_file:
        json.dump(search_results, save_file)


if __name__ == "__main__":
    details = search_alienvault(sys.argv[1], sys.argv[3])
    save_results(details, sys.argv[2])
