
import subprocess
from opendis import root
import os
import time
import sys
from pathlib import Path

def test_dis_sender_and_receiver():
    os.chdir(Path(root).parent)
    
    # Need -u so the stdout is immediately sent to pipe
    receive_proc = subprocess.Popen(['python', '-u', 'examples/dis_receiver.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)    
    send_proc = subprocess.Popen(['python', '-u', 'examples/dis_sender.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Run for about 3 seconds
    for i in range(3):
        print(f"Iteration {i+1}: Waiting for processes to complete...")

        if receive_proc.poll() is not None:
            if receive_proc.returncode != 0:
                print('Receive failure! ', receive_proc.returncode)
                stdout, stderr = receive_proc.communicate()
                raise ValueError(f"Receive process failed. \n STDOUT: {stdout} \n STDERR: {stderr}")
        if send_proc.poll() is not None:
                if send_proc.returncode != 0: 
                    print('Send failure!', send_proc.returncode)
                    stdout, stderr = send_proc.communicate()
                    raise ValueError(f"Send process failed. \n STDOUT: {stdout} \n STDERR: {stderr}")
        
        time.sleep(1)

    receive_proc.terminate()
    send_proc.terminate()

    receive_stdout, _ = receive_proc.communicate()
    print('Reciver stdout is:', receive_stdout)

    send_stdout, _ = send_proc.communicate()
    print('Sender stdout is:', send_stdout)

    assert receive_stdout.find("Received EntityStatePdu") != -1, "Did not receive expected PDU type in receiver output"

if __name__ == "__main__":
    test_dis_sender_and_receiver()
