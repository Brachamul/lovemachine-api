import time
import uuid



def random_suffix():

	''' Returns a random string in the format of ' [u45e]', used to differentiate dummy strings in tests '''
	
	return ' [{}]'.format(str(uuid.uuid4())[:4])



def timeit(f):

	''' A decorator, @timeit, used to print the amount of time taken by a given function '''

	def timed(*args, **kw):

		ts = time.time()
		result = f(*args, **kw)
		te = time.time()

		print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
		return result

	return timed


import base64
from io import BytesIO
from PIL import Image
def convert_to_b64(source_file):
	''' Returns a tiny thumbnail of the image as a base64 string '''
	img = Image.open(source_file)
	resized_img = img.resize((60,40), Image.ANTIALIAS)
	buffered = BytesIO()
	resized_img.save(buffered, format="JPEG", optimize=True, quality=90)
	return base64.b64encode(buffered.getvalue()).decode('UTF-8')



def lorem_ipsum():
	return '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque aliquam suscipit pulvinar. Vivamus porttitor odio accumsan velit fringilla euismod.

Ut ac laoreet odio, in aliquam quam. Donec convallis facilisis vestibulum. Sed laoreet ac nibh ac dictum. Maecenas id eleifend sapien, ut auctor dolor.

Vivamus varius auctor massa consectetur scelerisque. Sed ultricies feugiat gravida.

Duis faucibus interdum est quis finibus. Proin ultrices semper vulputate. Nulla lorem lorem, iaculis sit amet lacinia eu, efficitur eu metus. Pellentesque imperdiet ex convallis mi suscipit dapibus.

Fusce rutrum sem id consequat sodales. Donec finibus tortor vitae nibh pellentesque sagittis. Nulla nunc ante, rutrum eu tellus non, blandit hendrerit purus. Duis sit amet tellus quis lacus mollis laoreet eget sed sem.'''