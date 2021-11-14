import sys
from pathlib import Path
from PIL import ImageFont
import feedparser
from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
import time

def make_font(name, size):
	font_path = str(Path(__file__).resolve().parent.joinpath('fonts', name))
	return ImageFont.truetype(font_path, size)

def main():
	serial = i2c(port=1, address=0x3C)
	device = sh1106(serial)
	font = make_font("code2000.ttf", 10) #フォントを指定

	rss_link = 'https://news.yahoo.co.jp/rss/topics/it.xml' #RSSのURL(お好みで)
	counter = 0
	interval = 100 #表示を繰り返したらRSSフィードをリフレッシュ

	rss_dic = feedparser.parse(rss_link)
	while 1:
		for entry in rss_dic.entries:
			title = entry.title
			with canvas(device) as draw:
				draw.rectangle(device.bounding_box, outline="white", fill="black")
				length = len(title)
				i=0
				while 1:
					if length > 12:
						draw.text((2,10+i*12), title[i*12:i*13+12], font=font, fill="white")
						i+=1
						length-=12
						time.sleep(1)
					else:
						draw.text((2,10+i*12), title[i*12:i*13+length], font=font, fill="white")
						time.sleep(1)
						break
		counter += 1
		if counter == interval:
			rss_dic = feedparser.parse(rss_link)

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		pass
