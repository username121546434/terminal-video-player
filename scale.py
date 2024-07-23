import shutil
from PIL.Image import Image

def resize(image: Image):
    t_size = shutil.get_terminal_size()

    image.thumbnail((t_size.columns, t_size.lines * 2 - 4))
