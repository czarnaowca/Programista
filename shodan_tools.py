import shodan
import sys
import json


def search_shodan(query, api_key):
    """
    Search Shodan by query
    :param query: Search query
    :param api_key: Shodan API key
    :return: dict
    """
    try:
        api = shodan.Shodan(api_key)

        return api.search(query)
    except Exception as ex:
        print(f"[-] Error occurs: {ex}")
        sys.exit(1)


def save_results(search_results, file_name):
    """
    Save search results as JSON file
    :param search_results: Shodan search results
    :param file_name: File name
    :return: None
    """
    with open(file_name, "w") as save_file:
        json.dump(search_results, save_file)


if __name__ == "__main__":
    # Join all query parameters
    query_search = " ".join(sys.argv[3:])

    # Invoke search by query parameter and API key
    results = search_shodan(query_search, sys.argv[1])

    # Save returned results as JSON file
    save_results(results, sys.argv[2])

