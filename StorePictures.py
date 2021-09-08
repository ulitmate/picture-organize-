import time
import os
import tkinter as tk
import shutil

# directory of pictures
directory_path = "E:\\My Digital Camera Pictures\\"

# directory of camera drive
picture_directory_path = "I:\\DCIM\\100MSDCF\\"


# Creates a GUI window to be able to enter the name of the new folder of pictures.
class StorePictures(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("File")
        self.label = tk.Label(self, text="Name")
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Done", command=self.on_button_click)
        self.label.pack(side=tk.LEFT)
        self.button.pack(side=tk.BOTTOM)
        self.entry.pack(side=tk.RIGHT)

    def on_button_click(self):
        pictures = os.listdir(picture_directory_path)

        date_string = get_date_string(pictures[0]) + self.entry.get() + "\\"
        path = get_year_directory_path(directory_path)
        path = get_date_directory_path(path, date_string)

        count = get_number_of_jpg(pictures)

        index = 0
        for picture in pictures:
            filename, file_extension = os.path.splitext(picture_directory_path + picture)
            if file_extension == ".JPG":
                index += 1
                picture_date_created = get_date_string(picture) + self.entry.get() + " #"
                temp_picture_name = picture_date_created + str(index) + " of " + str(count) + ".JPG"
                picture_directory = path + temp_picture_name
                shutil.copy(picture_directory_path + picture, picture_directory)

        self.quit()


# creates year folder path (EX: 2016 Pictures, 2015 Pictures, etc.) if it does
# not already exist
def get_year_directory_path(path):
    temp_directory = path + "20" + time.strftime("%y") + " Pictures\\"
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)
    path = temp_directory
    return path


# creates date folder path (EX: 2016 Pictures / 2016-04-06 - [Some event here]) if it
# does not already exist
def get_date_directory_path(path, date_string):
    temp_directory = path + date_string
    if not os.path.exists(temp_directory):
        os.makedirs(temp_directory)
    path = temp_directory
    return path


# returns the appropriate time stamp to attach to the folder name
def get_date_string(picture):
    return "20" + time.strftime("%y") + " - " + time.strftime("%m-%d-%y", time.localtime(os.path.getctime(picture_directory_path + picture))) + " - "


# returns the amount of jpg pictures in the camera folder
def get_number_of_jpg(pictures):
    count = 0;
    for picture in pictures:
        filename, file_extension = os.path.splitext(picture_directory_path + picture)
        if file_extension == ".JPG":
            count += 1
    return count

app = StorePictures()
app.mainloop()