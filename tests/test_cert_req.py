import re
from lib.IssueCmd import IssueCmd
from lib.FileUtils import FileUtils

ic = IssueCmd()
fl = FileUtils()
host = "example.com"
_, data = fl.read_file("cert_cmds.txt")
cmds = data.split("\n")


def cert_req():
    cmd1 = cmds[0]
    rc, stdout, _ = ic.run_cmd(cmd1, host)
    assert "success" in stdout
    return stdout


def sign_cert():
    stdout = cert_req()
    req_id = re.findall(r'\d+', stdout)
    cmd2 = cmds[1].replace("req_id", req_id[0])
    rc, stdout, _ = ic.run_cmd(cmd2, host)
    return stdout


def test_cert_req(benchmark):
    benchmark.pedantic(cert_req, rounds=1)


def test_sign_cert(benchmark):
    benchmark.pedantic(sign_cert, rounds=1)

