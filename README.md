DNS resolver conf
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role configures dns resolvers on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/dns_resolver_conf.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
dns_resolv_conf_disable_resolvectl: false # by default, set to false
```
This variable determines if systemd-resolved should be kept enabled/started or not. On some systems, like dns servers, it can interfere with the actual server, and disabling it might be a good idea.

```yaml
dns_resolv_conf_path: '/etc'
```
This variable defines the path where the resolv.conf fie should be copied.

```yaml
dns_resolv_conf_nameservers: []
```
This variable is the list of nameservers to configure on the host.

```yaml
dns_resolv_conf_domain: ""
```
This variable sets the domain field in resolv.conf.

```yaml
dns_resolv_conf_search: []
```
This variable is a list of all the search domains. Ideally, only one of `dns_resolv_conf_domain` or `dns_resolv_conf_search` should be specified. The other should be left untouched.

```yaml
dns_resolv_conf_sortlist: []
```
This variable sets the sortlist option for resolv.conf. This option is a bit obsolete, and is here only for completeness of the config.

```yaml
dns_resolv_conf_options: []
```
This variable sets the options to pass in resolv.conf, like `rotate`, etc...

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.dns_resolver_conf
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.