from dearpygui.core import *
from dearpygui.simple import *
from PIL import Image
import image_functions

class ImageReducerApp:

    # Initial values
    def __init__(self):
        # App info
        self.appName = "EB Image Reducer"
        self.appVersion = "v0.1"

        # App settings
        self.singleImage = None
        self.imageDiretory = None
        self.allowedExts = ["png","jpg"]

        self.resizeMode = False
        self.previewImage = True

    # DONE: Select single file function
    def __select_single_file(self):
        open_file_dialog(self.__set_single_image)

    # DONE: Select directory function
    def __select_directory(self):
        select_directory_dialog(self.__set_image_directory)

    # Resize single image
    def __resize_single_image(self, source, persentage):
        if self.singleImage == None:
            self.__set_label_value("Please select an image file")
        else:
            extension = source.split(".")[-1]
            allowed = bool()
            for ext in self.allowedExts:
                if extension == ext:
                    allowed = True
            
            if allowed:
                image_functions.resize_image(source, persentage, self.previewImage)
            else:
                self.__set_label_value("Please select an image file")

    # TODO: Implement resize bulk images function
    def __resize_bulk_images(self, sender, data):
        pass

    # TODO: Implement bulk resize
    def __resize(self, sender):
        
        if self.resizeMode == True:
            print("Bulk resize")
        else:
            self.__resize_single_image(self.singleImage, 50)

    # Sets resize mode to either single image or directory
    def __set_resize_mode(self, sender):
        self.resizeMode = get_value(sender)

        if self.resizeMode == True:
            hide_item("Select File")
            show_item("Select Directory")

            set_value("Preview image after resize", False)
            self.previewImage = False
        else:
            show_item("Select File")
            hide_item("Select Directory")

            set_value("Preview image after resize", True)
            self.previewImage = True

    # DONE: Implement set single image function
    def __set_single_image(self, sender, data):
        source = data[0] + "\\" + data[1]
        self.__set_label_value(source)
        self.singleImage = source

    # DONE: Implement set image directory function
    def __set_image_directory(self, sender, data):
        source = data[0] + "\\" + data[1]
        self.imageDiretory = source
        self.__set_label_value(source)

    def __set_label_value(self, value):
        item = "Text Label"
        show_item(item)
        set_value(item, value)

    def __preview_after_resized(self, sender):
        value = get_value("Preview image after resize")
        self.previewImage = value

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
            add_button("Select File", callback=self.__select_single_file)
            add_button("Select Directory", callback=self.__select_directory, show=False)
            add_label_text("Text Label", label=" ", show=False)
            add_separator()
            add_checkbox('Resize bulk images', label="Resize bulk images", callback=self.__set_resize_mode)
            add_checkbox("Preview image after resize", callback=self.__preview_after_resized, default_value=True)
            add_separator()
            add_button("Resize", callback=self.__resize)
            add_separator()
            # add_progress_bar("Resize Progress", overlay="Resize Progress")
        # End Gui

        # show_documentation()
        start_dearpygui(primary_window="MainWindow")

# Run app on script execution
if __name__ == "__main__":
    app = ImageReducerApp()
    app.run()