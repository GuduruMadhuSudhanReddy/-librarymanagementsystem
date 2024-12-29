
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/library_management_system/nginx/nginx.conf /etc/nginx/sites-available/library_management_system
sudo ln -s /etc/nginx/sites-available/library_management_system /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/library_management_system /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx

