from lib.IssueCmd import IssueCmd
from lib.FileUtils import FileUtils


def test_ca():
    ic = IssueCmd()
    fl = FileUtils()
    host = 'example.com'
    file, _ = fl.read_file("ca.cfg")
    cmd = f"pkispawn -v -f {file} -s CA"
    rc, stdout, _ = ic.run_cmd(cmd, host)
    assert rc == 0

