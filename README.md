# Programista

Kod źródłowy skryptów prezentowanych w wydaniu 3/2022 (102) czasopisma Programista.

## Wywołanie poszczególnych skryptów

Shodan:
$ python shodan_tools.py API_KEY search_results.json product:"Cobalt Strike Beacon"
$ python parse_search_results.py search_results.json

$ python shodan_tools.py API_KEY cobalt_search_pl.json product:"Cobalt Strike Beacon" country:PL
$ python parse_search_results.py search_results_pl.json

AlienVault OTX:

$ python alienvaultotx_tools.py 5.181.86.243 alienvault_results.json API_KEY
$ python parse_avotx_search_results.py alienvault_results.json

VirusTotal:
$ python virustotal_tools.py 5.181.86.243 vt_results.json API_KEY
$ python parse_vt_search_results.py vt_results.json collections_vt_results.json

STIX:
$ python stix_generator.py
