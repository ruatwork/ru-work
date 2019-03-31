install_python:
  pkg.installed:
    - pkgs:
      - python
      - python3
      - python-pip
      - python3-pip
# Mikä tää on?      - mysql-connector-python3

install_mariaconnector:
  pip.installed:
    - name: mysql-connector-python
    - bin_env: /usr/bin/pip3
    - require:
      - pkg: install_python
