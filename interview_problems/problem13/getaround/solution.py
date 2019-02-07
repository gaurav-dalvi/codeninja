import requests
import shutil

PATTERN = r'class="lolcat"'
STORAGE_DIR = './images/'
ROOT_WEB_PAGE = 'http://www.lolcats.com'

def get_file_name(url):
	if url is None:
		raise Exception('Invalid image URL')

	return (url.split('/')[-1])

def download_images(images):

	for image in images:
		final_url = ROOT_WEB_PAGE + image
		print final_url
		response = requests.get(final_url, stream=True)
		if response.status_code == 200:
			filename = STORAGE_DIR + get_file_name(final_url)
			print(filename)
			with open(filename, 'wb') as out_file:
				shutil.copyfileobj(response.raw, out_file)

def extract_images(text):
	
	images = []
	lines = text.split('\n')
	for line in lines:
		if PATTERN in line:
			# split using ' '
			temp = line.split(' ')
			for item in temp:
				if 'src' in item:
					extract = item.split('=')
					image_src = extract[1].replace('"', '')
					images.append(image_src)
	return images

def get_page_data(url):
	if url is None:
		raise Exception('Invalid URL')

	raw_data = requests.get(url)
	return raw_data.text

for i in xrange(1, 11):
	webpage = 'http://www.lolcats.com/page-%s.html' %i
	images = extract_images(get_page_data(webpage))
	download_images(images)

