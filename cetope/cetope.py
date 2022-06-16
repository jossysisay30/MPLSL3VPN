from nornir import InitNornir
from nornir.core.task import Result, Task
from nornir_jinja2.plugins.tasks import template_file
from nornir_utils.plugins.functions import print_result
from nornir_scrapli.tasks import send_configs
import  ipdb
nr = InitNornir(config_file="config.yaml")
def basicconf(task):
    #r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def basicrip(task):
    #r=task.run(task=template_file,template="inter.j2",path=f"templates/")
    r=task.run(task=template_file,template="rip.j2",path=f"templates/")
    output=r.result
    send=output.splitlines()
    task.run(task=send_configs, configs=send)
def main():
        yaml_results = nr.run(task=basicconf)
        rip_results = nr.run(task=basicrip)
        print_result(yaml_results)
        print_result(rip_results)
if __name__ == '__main__':
        main()
