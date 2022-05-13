import json
import sys

def load_results(file_name):
    """
    Loads results from file to JSON object
    :param file_name: JSON file
    :return: JSON
    """
    with open(file_name, "r") as json_file:
        return json.load(json_file)


def parse_results(results):
    """
    Parse JSON results and prints defined output
    :param results: JSON object
    :return: None
    """
    print(f"[+] Shodan found {results['total']} "
          f"total results.")
    print(f"[+] File contains first {len(results['matches'])}"
          f" results.\n")

    for result in results['matches']:
        print(f"[+] {result['location']['country_name']}")
        print(f"[+] {result['location']['city']}")
        print(f"[+] {result['ip_str']}:{str(result['port'])}"
              f"\n")

        extract_c2_config(result['cobalt_strike_beacon'])

        if "ssl" in result.keys():
            get_ssl_details(result)


def extract_c2_config(result):
    """
    Extracts C2 config details
    :param result: JSON object represents each search result
    :return: None
    """
    for arch in result:
        print(f"{arch}:")
        for beacon in result[arch]:
            print(f"\t{beacon} : {result[arch][beacon]}")


def get_ssl_details(result):
    """
    Prints SSL certificate details
    :param result: JSON object represents each search result
    :return: None
    """
    print(f"[+] Certificate type: {result['tags'][0]}")
    print(f"[+] JARM signature: {result['ssl']['jarm']}")
    print(f"[+] Issued: {result['ssl']['cert']['issued']}")
    print(f"[+] Expires: {result['ssl']['cert']['expires']}")
    print("[+] Issuer:")
    print(f"\tC: {result['ssl']['cert']['issuer']['C']}")
    print(f"\tCN: {result['ssl']['cert']['issuer']['CN']}")
    print(f"\tL: {result['ssl']['cert']['issuer']['L']}")
    print(f"\tO: {result['ssl']['cert']['issuer']['O']}")
    print(f"\tST: {result['ssl']['cert']['issuer']['ST']}")
    print(f"\tOU: {result['ssl']['cert']['issuer']['OU']}")


if __name__ == "__main__":
    json_content = load_results(sys.argv[1])
    parse_results(json_content)

