from lib.IssueCmd import IssueCmd
from lib.FileUtils import FileUtils


def test_ldap():
    ic = IssueCmd()
    fl = FileUtils()
    host = 'example.com'
    _, data = fl.read_file("ldap.txt")
    cmd = data.replace("hostname", host)
    rc, stdout, _ = ic.run_cmd(cmd, host)
    assert rc == 0
