#!/bin/bash

echo "sh1106 OLED�f�B�X�v���C�̃W�����p�����ȉ��̂悤�Ɍ������Ă��邱�Ƃ��m�F���Ă��������B"
echo "VCC -> 3.3v"
echo "GND -> GND"
echo "SCL -> GPIO9"
echo "SDA -> GPIO8"

sudo apt-get install -y python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential
sudo -H pip3 install --upgrade luma.oled
echo "�v���O���������s����ɂ́A[python3 sh1106_rss.py]�Ɠ��͂��Ă��������B"