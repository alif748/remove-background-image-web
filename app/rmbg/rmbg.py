import requests

from PIL import Image
from pymatting import cutout
import pymatting
import time
from time import process_time
import random
import string

from app.rmbg.generate import generate

def rmbg(uri):
    t1_start = process_time()
    # image = io.BytesIO(req.content)

    req = requests.get(uri)
    current_time_id = str(int(time.time()))
    def generate_random_id(length=3):
        return ''.join(random.choices(string.ascii_lowercase, k=length))

    name = f'{current_time_id+generate_random_id()}'
    input_path = 'app/rmbg/input'
    output_path = 'app/rmbg/output'

    input_file = f'{input_path}/{name}.jpg'
    mask_file = f'app/rmbg/mask/{name}.png'

    with open(f'{input_path}/{name}.jpg', 'wb') as f:
        f.write(req.content)
    generate(f'{input_path}/{name}.jpg', name)
    cutout(input_file, mask_file, f'{output_path}/{name}.png')
    t1_stop = process_time()

    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
    # return Image.open(f'{output_path}/{name}.png')
    return f'{output_path}/{name}.png'