# Build Branches sites

## SSH

* Use your SSH config file (~/.ssh/config) to confgire all the SSH connections, for example the inventory hosts connections.
* Use SSH keys to connect to remote hosts
* Use diferent SSH keys for diffrent environments (development/stage/prod)

## Ansible
* Read how to use the **Ansible** provisioner in README.md of each role.
* To know more about Ansible: http://www.ansible.com

### Dependencies
Install the rol dependencies using Ansible Galaxy

```bash
ansible-galaxy install -r dependencies.yml
```

## Syncing content

List tasks and hosts before provision:

```bash
ansible-playbook -i inventories/local playbook.yml --list-tasks --list-hosts
```

Build brancehs sites:

```bash
ansible-playbook -i inventories/local playbook.yml
```

### Custom settings
In order to use your own custom settings, use the "settings/custom.yml" file, you can overide any varible used in the playbooks and roles.

```bash
ansible-playbook -i inventories/local playbooks.yml
```

By default the custom.yml file is ignored in git, be mindful to not add to version control your custom files or info.

### Inventory
See the `invetories` folders to know the available invetories
Use the "inventories/custom" to place your custom invetory.

## Tests
```bash
ansible-playbook -i inventories/local tests/playbook.yml
```

### Vagrant
* You can use Vagrant to set up and provision a VM in order to run tests.
* To know more about Vagrant: http://www.vagrantup.com
  And Vagrant with Ansible: http://docs.vagrantup.com/v2/provisioning/ansible.html

```bash
tests/vagrant.sh
```
### Docker
```bash
tests/docker.sh
```
