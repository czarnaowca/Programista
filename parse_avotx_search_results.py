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
    print(f"[+] Whois link: {results['general']['whois']}")
    print(f"[+] Reputation: "
          f"{results['general']['reputation']}")
    print(f"[+] Number of pulses: "
          f"{results['general']['pulse_info']['count']}")

    for pulse_no, pulse in enumerate(
            results['general']['pulse_info']['pulses']):
        print(f"\tPulse {pulse_no+1}:")
        print(f"\t\tName: {pulse['name']}")
        print(f"\t\tDescription: {pulse['description']}")
        print(f"\t\tTags: {pulse['tags']}")
        print(f"\t\tAdversary: {pulse['adversary']}")
        print(f"\t\tTargeted countries: "
              f"{pulse['targeted_countries']}")
        print(f"\t\tMalware families: "
              f"{pulse['malware_families']}")
        print(f"\t\tAttack ids: {pulse['attack_ids']}")
        print(f"\t\tIndustries: {pulse['industries']}")
        print(f"\t\tTLP: {pulse['TLP']}")
        print(f"\t\tAuthor: {pulse['author']['username']}")


if __name__ == "__main__":
    json_content = load_results(sys.argv[1])
    parse_results(json_content)