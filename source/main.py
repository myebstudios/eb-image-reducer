from dearpygui.core import *
from dearpygui.simple import *
from PIL import Image
import image_functions

class ImageReducerApp:

    # Initial values
    def __init__(self):
        self.appName = "EB Image Reducer"
        self.appVersion = "v0.1"

        self.preview_image = True

    # DONE: Select single file function
    def __select_single_file(self):
        open_file_dialog(self.__resize_single_image)

    # DONE: Select directory function
    def __select_directory(self):
        select_directory_dialog(self.__resize_bulk_images)

    # Resize single image
    def __resize_single_image(self, sender, data):
        print("Source Data: ", data)
        source = data[0] + "\\" + data[1]
        print("Source File: ", source)
        image_functions.resize_image(source, 50, self.preview_image)

    # TODO: Implement resize bulk images function
    def __resize_bulk_images(self, sender, data):
        pass

    def __preview_after_resized(self, sender):
        value = get_value("Preview image after resize?")
        self.preview_image = value

    # Debug Output
    def __out(self, sender, data):
        print("Print Out Data: ", data)

    # App run function
    def run(self):

        set_main_window_size(550, 650)
        set_main_window_resizable(False)
        set_main_window_title("EB Image Reducer")
        add_additional_font("./assets/fonts/Roboto-Regular.ttf", 20)

        # Start Gui
        with window("MainWindow"):

            add_text(self.appName)
            add_separator()
            add_spacing()
            add_spacing()
            add_spacing()
            add_spacing()
            add_button("Select File", callback=self.__select_single_file)
            add_same_line()
            add_button("Select Directory", callback=self.__select_directory)
            add_separator()
            add_spacing()
            add_spacing()
            add_spacing()
            add_spacing()
            add_checkbox("Preview image after resize?", callback=self.__preview_after_resized, default_value=True)
        # End Gui

        # Start dearpygui
        start_dearpygui(primary_window="MainWindow")

# Run app on script execution
if __name__ == "__main__":
    app = ImageReducerApp()
    app.run()