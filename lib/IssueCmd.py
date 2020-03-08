#!/usr/bin/env python

"""
Library to faciliate running commands
"""
import os
import socket
import yaml
from SSHLibrary import SSHLibrary
from paramiko import SSHException
from UserIdentity import UserIdentity

class IssueCmd():
    """
    Class to facilitate running commands on remote systems
    """
    def __init__(self):
        self._ssh_lib = SSHLibrary()

    def get_creds(self, host):
        """
        Get the server credentials
        """
        user = UserIdentity()
        cur_dir = os.path.dirname(os.path.abspath(__file__))
        creds_file = os.path.join(cur_dir, "../config/", host + ".yaml")
        with open(creds_file) as creds:
            try:
                data = yaml.safe_load(creds)
                user.username = data["default"]["username"]
                user.password = data["default"]["password"]
                return user
            except yaml.YAMLError as exc:
                print(exc)

    def _open_conn(self, host):
        user = self.get_creds(host)

        try:
            self._ssh_lib.open_connection(host)
            try:
                self._ssh_lib.login(user.username, user.password)
                print(f"Connected to host: {host} successfully" )
            except SSHException:
                print(f"Login to host: {host} failed")
                        
        except (socket.error, OSError, TimeoutError) as ex:
            print(f"Connection to host: {host} failed")
            raise ex

    def run_cmd(self, command, host):
        """
        Run a command remotely (using ssh)
        """
        print(f"[CMD]: {command}")
        self._open_conn(host)
        stdout, stderr, ret_cd = self._ssh_lib.execute_command(command, return_stdout=True,
                                                               return_stderr=True,
                                                               return_rc=True)
        print(f"Exit Value:[{ret_cd}]")
        print(f"[STDOUT]: {stdout}")
        if stderr:
            print(f"[STDERR]: {stderr}")
        return ret_cd, stdout, stderr


if __name__ == "__main__":
    #ic = IssueCmd()
    #rc, stdout, stderr = ic.run_cmd('ls /root/', '10.10.241.15')
    pass
