#!/bin/bash

echo "sh1106 OLEDディスプレイのジャンパ線を以下のように結線していることを確認してください。"
echo "VCC -> 3.3v"
echo "GND -> GND"
echo "SCL -> GPIO9"
echo "SDA -> GPIO8"

sudo apt-get install -y python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential
sudo -H pip3 install --upgrade luma.oled
echo "プログラムを実行するには、[python3 sh1106_rss.py]と入力してください。"