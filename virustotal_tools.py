import vt
import json
import sys


def search_vt(ip, client):
    """
    Search information about specific IP
    :param ip: IP address
    :param client: VirusTotal client object
    :return: dict
    """
    return client.get_data(f"/ip_addresses/{ip}")


def get_collections(ip, client):
    """
    Get additional information about IP address
    :param ip: IP address
    :param client: VT Client object
    :return: dict
    """
    return client.get_data(
        f"/ip_addresses/{ip}/collections")


def save_results(search_results, file_name):
    """
    Save search results as JSON file
    :param search_results: VirusTotal search results
    :param file_name: File name
    :return: None
    """
    with open(file_name, "w") as save_file:
        json.dump(search_results, save_file)


if __name__ == "__main__":
    client = vt.Client(sys.argv[3])
    details = search_vt(sys.argv[1], client)
    collections = get_collections(sys.argv[1], client)
    client.close()
    save_results(details, sys.argv[2])
    save_results(collections, "collections_" + sys.argv[2])
