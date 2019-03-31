/home/user/public_html/index.html:
  file.managed:
    - source: salt://php-site/index.html
    - makedirs: True

/home/user/public_html/login.php:
  file.managed:
    - source: salt://php-site/login.php

/home/user/public_html/background.png:
  file.managed:
    - source: salt://php-site/background.png

/home/user/public_html/RUatWorkIcon.png:
  file.managed:
    - source: salt://php-site/RUatWorkIcon.png

/home/user/public_html/RUatWork.png:
  file.managed:
    - source: salt://php-site/RUatWork.png

