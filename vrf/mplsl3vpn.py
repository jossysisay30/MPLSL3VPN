from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import  ipdb
nr = InitNornir(config_file="config.yaml")
def vrf(task):
    r=task.run(task=template_file,template="vrf.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def basicconf(task):
    r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def bgpvpn4(task):
    r=task.run(task=template_file,template="bgp.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def ripba(task):
    r=task.run(task=template_file,template="rip.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def main():
        vrf_results = nr.run(task=vrf)
        vrfint_results = nr.run(task=basicconf)
        bgpvpn4_results = nr.run(task=bgpvpn4)
        ripba_results = nr.run(task=ripba)
        print_result(vrf_results)
        print_result(vrfint_results)
        print_result(bgpvpn4_results)
        print_result(ripba_results)
if __name__ == '__main__':
        main()
