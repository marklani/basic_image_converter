from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path
from os import path


image_format_to_extension={
    'jpeg' : 'jpeg',
    'png' : 'png',
    'jpeg2000' : 'jp2',
    'gif' : 'GIF',
    'bmp' : 'BMP',
}

def convert_image_to_grayscale():
    try:
        filepath = selected_file_label['text']
        image_format = image_type_combobox.get()
        new_filedir = selected_save_path_label['text']

        jpeg_image = Image.open(open(filepath,'rb')).convert('L')
        filename_without_extension = Path(filepath).stem
        new_filename = f'{filename_without_extension}.{image_format_to_extension[image_format.lower()]}'
        new_filepath = path.join(new_filedir, new_filename)
        jpeg_image.save(new_filepath, image_format)
        result_path_label['text'] = f'Image successfully converted at: {new_filepath}'
    except Exception as e:
        print(f'Error: {e}')

def select_file_dialog():
    filepath = filedialog.askopenfilename()
    if filepath:
        selected_file_label.configure(text=filepath)

def select_save_filename_dialog():
    filepath = filedialog.askdirectory()
    if filepath:
        selected_save_path_label.configure(text=filepath)

window = tk.Tk()
window.title("Image Converter")


top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)
mid_frame = tk.Frame(window)
mid_frame.pack(side=tk.TOP)
upper_mid_frame = tk.Frame(window)
upper_mid_frame.pack(side=tk.TOP)
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.TOP)

selected_file_label = tk.Label(top_frame, text="Choose an image to convert.")
selected_file_label.pack(side=tk.LEFT)

select_file_button = tk.Button(top_frame, text="Open", command=select_file_dialog)
select_file_button.pack(side=tk.LEFT)

selected_image_type_label = tk.Label(upper_mid_frame, text="Choose image type to convert to.")
selected_image_type_label.pack(side=tk.LEFT)

default_combo_box_text = tk.StringVar(value='Image type')
combo_box_values = ['jpeg', 'png', 'jpeg2000', 'gif', 'bmp']
image_type_combobox = ttk.Combobox(upper_mid_frame, textvariable=default_combo_box_text, values=combo_box_values, state='readonly')
image_type_combobox.pack(side=tk.LEFT)

selected_save_path_label = tk.Label(mid_frame, text='Select a path to save the converted image.')
selected_save_path_label.pack(side=tk.LEFT)

select_save_path_button = tk.Button(mid_frame, text="Save to...", command=select_save_filename_dialog)
select_save_path_button.pack(side=tk.LEFT)

convert_image_button = tk.Button(bottom_frame, text='Convert!', command=convert_image_to_grayscale)
convert_image_button.pack(side=tk.TOP)

result_path_label = tk.Label(bottom_frame)
result_path_label.pack(side=tk.TOP)

window.mainloop()
