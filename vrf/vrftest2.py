from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_command
from nornir_scrapli.tasks import send_configs
from scrapli import Scrapli
from pprint import pprint
from nornir.core.filter import F
import ipdb
import json
import colorama
from colorama import Fore, Style
nr = InitNornir(config_file="config.yaml")
nn=nr.inventory.hosts
#ipdb.set_trace()
results = nr.run(task=send_command, command="show vrf")
ipdb.set_trace()
print(results)
