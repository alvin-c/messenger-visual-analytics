from pathlib import Path
from tkinter import filedialog
from tkinter import *
from os import walk


def select_convo():

    """
    Selects the conversation folder to analyze
    TODO: make this a nice scrollable list for the user to select via GUI
    :return: convo_folder_filepath
    """

    # Create local tmp directory
    Path("tmp").mkdir(parents=True, exist_ok=True)

    root = Tk()
    root.withdraw()
    convo_dir = filedialog.askdirectory(parent=root,
                                        title="Select the conversation folder you wish to analyze")
    return convo_dir


def validate_convo(convo_folder_filepath):

    """
    Validates that the selected folder is a conversation
    :param convo_folder_filepath: path to conversation folder to analyze
    :return: convo_folder_filepath, filelist, dirlist
    """

    # Verify folder is valid and contains at least one messages file
    filelist = []
    dirlist = []
    for (dirpath, dirnames, filenames) in walk(convo_folder_filepath):
        filelist.extend(filenames)
        dirlist.extend(dirnames)
        break

    assert "message_1.json" in filelist, "No message files detected! \nCheck that the folder you selected contains at " \
                                         "least one messages file - for example 'message_1.json"

    print(filelist)
    print(dirlist)

    return convo_folder_filepath, filelist, dirlist


if __name__ == "__main__":
    convo_folder_filepath = select_convo()
    validate_convo(convo_folder_filepath)
