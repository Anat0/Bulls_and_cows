import os
from PIL import Image
from rembg import remove
from multiprocessing import Pool


def process_frame(args):
    frame, output_dir, i = args
    frame = remove(frame).resize((350, 320))
    frame.save(f"{output_dir}/bull_{i}.png", "PNG")
    print(i)


def split_gif(gif_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    gif = Image.open(gif_path)
    frames = []

    try:
        while True:
            frames.append(gif.copy())
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    with Pool() as pool:
        pool.map(process_frame, [(frame, output_dir, i) for i, frame in enumerate(frames)])


if __name__ == "__main__":
    gif_path = "bull.gif"
    output_dir = "../Новая папка/bulls"
    split_gif(gif_path, output_dir)
