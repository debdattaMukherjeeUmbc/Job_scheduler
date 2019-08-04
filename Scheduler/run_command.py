#!/usr/bin/env python
def trigger_command(self):
        import subprocess
        command = ["bash","/Users/dm029579/Desktop/SAP_assingment/Scheduler/scheduler_api/bash_script2.sh"]
        try:
            process = Popen(command, stdout=PIPE, stderr=STDOUT)
            output = process.stdout.read()
            exitstatus = process.poll()
            if (exitstatus==0):
                    result = {"status": "Success", "output":str(output)}
            else:
                    result = {"status": "Failed", "output":str(output)}

        except Exception as e:
            result =  {"status": "failed", "output":str(e)}
