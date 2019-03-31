# Install Apache and PHP

install_ap:
  pkg.installed:
    - pkgs:
      - apache2
      - libapache2-mod-php
      - php-mysql

# Apache php conf edit to enable users to use php in their home directory

/etc/apache2/mods-available/php7.0.conf:
  file.managed:
    - source: salt://apachephp/php7.0.conf

# Make sure the mod is enabled

/etc/apache2/mods-enabled/php7.0.conf:
  file.symlink:
    - target: ../mods-available/php7.0.conf

# Enable mods

/etc/apache2/mods-enabled/userdir.load:
  file.symlink:
    - target: ../mods-available/userdir.load

/etc/apache2/mods-enabled/rewrite.load:
  file.symlink:
    - target: ../mods-available/rewrite.load

# Get rid of Apache starting page

/var/www/html/index.html:
  file.managed:
    - source: salt://apachephp/index.html

# Restart Apache to apply the mods

apacherestart:
  service.running:
    - name: apache2
    - watch:
       - file: /etc/apache2/mods-enabled/rewrite.load
       - file: /etc/apache2/mods-enabled/userdir.load
