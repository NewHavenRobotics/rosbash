#!/bin/bash
chmod +x rosbash.sh
sudo chown root:root rosbash.py
sudo chmod u+s rosbash.py
#find and replace 'REPLACEME' with username
sed -i "s/REPLACEME/$USER/g" rosbash.service
sudo mv rosbash.py /services
sudo mv rosbash.sh /services
sudo mv rosbash.service /etc/systemd/system
sudo systemctl enable rosbash.service
