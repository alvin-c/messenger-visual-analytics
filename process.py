from select import *
from utilities import *
import json


def basic_stats(convo_folder_path, filelist, dirlist):

    participants = get_participants(convo_folder_path, 'message_1.json')
    message_count = {k: 0 for k in participants}

    print('Found ' + str(len(filelist)) + ' message files.')
    for message_file in filelist:
        partial_message_count = process_one(convo_folder_path, message_file)
        print(message_file)
        print(partial_message_count)
        for participant in partial_message_count.keys():
            message_count[participant] += partial_message_count[participant]

    print(message_count)

    return message_count


def get_participants(convo_folder_path, file):

    """
    Returns the set of participants in a messages json file
    :param convo_folder_path: path to conversation folder
    :param file: filename (not path) of messages json file
    :return: set of participants ('participant1', 'participant2', ..)
    """

    filepath = convo_folder_path + '/' + file
    with open(filepath) as json_file:
        data = json.load(json_file)

    participants = set([elem['name'] for elem in data['participants']])

    return participants

def get_first_message(convo_folder_path):
    pass

def get_last_message(convo_folder_path):
    pass

def process_one(convo_folder_path, file):

    """
    Processes one messages.json file
    :param convo_folder_path: path to conversation folder
    :param file: filename (not path) of messages json file
    :return:
    """

    filepath = convo_folder_path + '/' + file
    with open(filepath) as json_file:
        data = json.load(json_file)

    # Set of participants ('participant1', 'participant2' ,..)
    participants = get_participants(convo_folder_path, file)

    # message_count: number of messages per participant
    # {participant1: int, participant2: int}

    message_count = {k: 0 for k in participants}

    for message in data['messages']:
        if message['sender_name'] in participants:
            message_count[message['sender_name']] += 1

    return message_count



if __name__ == "__main__":
    convo_folder_path = select_convo()
    convo_folder_path, filelist, dirlist = validate_convo(convo_folder_path)

    #process_one(convo_folder_path, 'message_1.json')
    basic_stats(convo_folder_path, filelist, dirlist)