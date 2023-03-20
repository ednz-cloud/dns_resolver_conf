"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_resolv_conf_file(host):
    """Validate resolv.conf file."""
    tmp_resolv_conf = host.file("/tmp/resolv.conf")
    assert tmp_resolv_conf.exists
    assert tmp_resolv_conf.user == "root"
    assert tmp_resolv_conf.group == "root"
    assert tmp_resolv_conf.mode == 0o644
    assert tmp_resolv_conf.contains("search local.lan")
    assert tmp_resolv_conf.contains("nameserver 1.1.1.1")
    assert tmp_resolv_conf.contains("nameserver 8.8.8.8")
