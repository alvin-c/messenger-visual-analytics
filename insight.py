#!/usr/bin/env python

from yaml import load, dump
from collections import OrderedDict
import time, os

from visualize import visualize

DIV = '\n'+ '='*64 + '\n'

start_time = time.time()

def usage():
	pass
	 
# Iterate over all conversation threads
def summarize():

	print 'Opening file... ',
	file = open('messages_jacob.yaml', 'r')
	print 'successful!'

	print 'Parsing file... ',
	messages = load(file)
	print 'successful!' + DIV
	x = 1

	for thread in messages:
		message_contribution = {'Jacob Ziontz': 0}

		# Iterate over all messages in a thread
		for message in thread['messages']:
			try:
				message_contribution[message['sender']] += 1
			except KeyError:
				message_contribution[message['sender']] = 1

	# Print outputs
		print 'Thread', x
		print len(message_contribution), 'participants, ',
		print len(thread['messages']    ), 'messages'

		for participant, count in message_contribution.iteritems():
			print '\t', participant.encode('utf-8').strip(), ' - ', count

		print '\n'
		x += 1
	print 'Total number of conversations:', x

def conversation_separator():

	print 'Opening file... ',
	file = open('messages_jacob.yaml', 'r')
	print 'successful!'

	print 'Parsing file... ',
	messages = load(file)
	print 'successful!' + DIV

	count = 1
	for thread in messages:
		filename = 'conversations_jacob/%d.yaml' % count
		if not os.path.exists('conversations_jacob'):
			print 'Creating directory conversations_jacob'
			try:
				os.makedirs('conversations_jacob')
			except OSError as exc: # Guard against race condition
				raise
		print 'Writing', filename
		conversation_file = open(filename, 'w')
		dump(thread, conversation_file)
		count += 1

	print '(%s seconds)' % round((time.time() - start_time), 2)

# Generates insight data on a single conversation thread
def insight():
	print 'Opening thread... ',
	file = open('conversations_test/440.yaml', 'r')
	print 'successful!'

	print 'Loading thread... ',
	thread = load(file)
	print 'successful!' + DIV

#	1. Pie chart showing contribution of messages by each person

	message_contribution = {'Alvin Cao': 0}
	
	for message in thread['messages']:
		try:
			message_contribution[message['sender']] += 1
		except KeyError:
			message_contribution[message['sender']] = 1
	print message_contribution

#	2. Line chart showing messages per month

	messages_over_time = {}

	for message in thread['messages']:
		try:
			messages_over_time[message['date'].partition('T')[0][:7]] += 1
		except KeyError:
			messages_over_time[message['date'].partition('T')[0][:7]] = 1

	for elem in OrderedDict(sorted(messages_over_time.items(), key=lambda t: t[0])).items():
		messages_over_time[elem[0]] = elem[1]

	def break_message(message):
		if message == '': return '(sticker/emoji)'

		if len(message) <= 56: return message

		accumulate = 0
		broken_message = ''
		for word in message.split(' '):
			if len(word) >= 56:
				return word[:56] + '<br>' + word[56:]
			accumulate += len(word) + 1
			print accumulate
			broken_message += word + ' '
			if accumulate >= 56: 
				broken_message += '<br>'
				accumulate = 0

		return broken_message

#   3. Get first message
	
	for message in thread['messages']:
		first_message = message['sender'] + ', '
		first_message += message['date'].partition('T')[0][:10]
		first_message += '<br>' + break_message(message['message'])
		break

	print first_message

	visualize(message_contribution, messages_over_time, first_message)


# Execute one at a time in order

#summarize()
#conversation_separator()
insight()
