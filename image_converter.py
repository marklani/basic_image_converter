from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pathlib import Path

IMAGE_FORMAT_TO_EXTENSION={
    'jpeg' : 'jpeg',
    'png' : 'png',
    'jpeg2000' : 'jp2',
    'gif' : 'GIF',
    'bmp' : 'BMP',
    'tiff' : 'TIF',
    'ico' : 'ICO',
    'dib' : 'DIB'
}

def convert_image_to_grayscale(filepath, image_format, save_dir, result_path_label_text_variable):
    try:
        file_extension = Path(filepath).suffix
        if str(file_extension).lower() == '.eps':
            raise Exception(f'Image conversion failed: {file_extension} images cannot be opened.')
        jpeg_image = Image.open(open(filepath,'rb')).convert('L')
        filename_without_extension = Path(filepath).stem
        new_filename = f'{filename_without_extension}.{IMAGE_FORMAT_TO_EXTENSION[image_format.lower()]}'
        new_filepath = Path(save_dir, new_filename)
        jpeg_image.save(new_filepath, image_format)
        result_path_label_text_variable.set(f'Image successfully converted at: {new_filepath}')
    except Exception as e:
        result_path_label_text_variable.set(f'Error: {e}')

def select_file_dialog(selected_file_label_text_variable):
    filepath = filedialog.askopenfilename()
    if filepath:
        selected_file_label_text_variable.set(filepath)

def select_save_dir_dialog(selected_save_dir_label_text_variable):
    save_dir = filedialog.askdirectory()
    if save_dir:
        selected_save_dir_label_text_variable.set(save_dir)

class CustomFrame(tk.Frame):
    def __init__(self, master, pack_side):
        super().__init__(master)
        super().pack(side=pack_side)

class CustomLabel(tk.Label):
    def __init__(self, master, pack_side, default_text=''):
        self.text_variable = tk.StringVar(value=default_text)
        super().__init__(master, textvariable=self.text_variable)
        super().pack(side=pack_side)

class CustomButton(tk.Button):
    def __init__(self, master, pack_side, default_text='', command=None):
        self.text_variable = tk.StringVar(value=default_text)
        super().__init__(master, textvariable=self.text_variable, command=command)
        super().pack(side=pack_side)

class CustomCombobox(ttk.Combobox):
    def __init__(self, master, pack_side, values, default_text=''):
        self.text_variable = tk.StringVar(value=default_text)
        super().__init__(master, textvariable=self.text_variable, values=values, state='readonly')
        super().pack(side=pack_side)

def main_window():
    window = tk.Tk()
    window.title("Image Converter")

    file_selection_frame = CustomFrame(window, tk.TOP)
    selected_file_label = CustomLabel(file_selection_frame, tk.LEFT, "Choose an image to convert")
    select_file_button = CustomButton(file_selection_frame, tk.LEFT, "Open", lambda: select_file_dialog(selected_file_label.text_variable))

    type_selection_frame = CustomFrame(window, tk.TOP)
    selected_image_type_label = CustomLabel(type_selection_frame, tk.LEFT, "Choose image type to convert to.")
    image_type_combobox = CustomCombobox(type_selection_frame, tk.LEFT, list(IMAGE_FORMAT_TO_EXTENSION.keys()), "Image type")

    save_dir_selection_frame = CustomFrame(window, tk.TOP)
    selected_save_dir_label = CustomLabel(save_dir_selection_frame, tk.LEFT, "Select a path to save the converted image.")
    select_save_dir_button = CustomButton(save_dir_selection_frame, tk.LEFT, "Save to...", lambda: select_save_dir_dialog(selected_save_dir_label.text_variable))

    convert_image_frame = CustomFrame(window, tk.TOP)
    result_path_label = CustomLabel(convert_image_frame, tk.BOTTOM)
    convert_image_button = CustomButton(convert_image_frame, tk.TOP, 'Convert!', lambda: convert_image_to_grayscale(selected_file_label.text_variable.get(), image_type_combobox.get(), selected_save_dir_label.text_variable.get(), result_path_label.text_variable))

    return window

if __name__ == "__main__":
    window = main_window()
    window.mainloop()
