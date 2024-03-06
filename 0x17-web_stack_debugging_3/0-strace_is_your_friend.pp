# Ensure the Apache module is installed

exec{'replace phpp with php using sed':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
