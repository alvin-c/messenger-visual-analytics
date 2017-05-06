#!/usr/bin/python

import plotly
import plotly.graph_objs as go
from plotly import tools

import Tkinter      as tk
import tkFileDialog as filedialog
import tkMessageBox as messagebox

import time, sys

class Visualizer(object):

	"""Uses Plotly to graph two columns of csv data """

	def __init__(self, data1, data2, first_message):
		self.filepath  = ''
		self.data1 = data1
		self.data2 = data2
		self.first_message = first_message

	# Opens dialog to allow user to select thread file
	def selectFile(self):
		tkWithdraw()
		self.filepath = filedialog.askopenfilename(message = 'Select the conversation')
		if not self.filepath: 
			sys.exit('No file selected')
		if not self.filepath.endswith('.yaml'):
			sys.exit('Invalid file type - only yaml')

	# Plots data
	def plot(self):

		layout = {
			'title': 'Facebook Messenger Thread Insight',
			  'titlefont': {
		      'size': 30,
		      'family': 'Arial'
		      },
			'margin': {
			  'r': 200, 
		      't': 50, 
		      'b': 100, 
		      'l': 200
		    },
		    'xaxis': {
		      'anchor': 'x', 
		      'title': 'Date',
		      'type': 'date',
		      'domain': [0, 1]
		    }, 
		  'yaxis': {
		    'anchor': 'y', 
		    'title': 'Number of messages',
		    'type' : '-',
		    'domain': [0, 0.4]
		  },
		  'legend':{
		    'x': 0.85,
		    'y': 0.9
		  }
		}


		annotations = [# Bar graph title
		               {'text'     : '<b>Messages over time, per month</b>',
		                'font':{
		                  'family' : 'Arial',
		                  'size'   : 16
		                },
		                'showarrow': False,
		                'xref'     : 'paper',
		                'yref'     : 'paper',
		                'x'        : 0,
		                'y'        : 0.425,
		                'align'    : 'left',
		                }, 

		               # Pie chart title
		               {'text'     : '<b>Message contribution by person</b>', 
		                'font':{
		                  'family' : 'Arial',
		                  'size'   : 16
		                },
		                'showarrow': False,
		                'xref'     : 'paper',
		                'yref'     : 'paper',
		                'x'        : 0.5, 
		                'y'        : 0.95,
		                'align'    : 'left'
		               },

		               # Quick Facts title
		               {'text'     : '<b>Quick Facts</b>', 
		                'font':{
		                  'family' : 'Arial',
		                  'size'   : 16
		                },
		                'showarrow': False,
		                'xref'     : 'paper',
		                'yref'     : 'paper',
		                'x'        : 0, 
		                'y'        : 0.95,
		                'align'    : 'left'
		               },

		               # Quick facts
		               {'text'     :
		                             '<b># Participants: </b>%d<br>'
		                             '<b># Messages: </b> %d<br>'
		                             '<br><b>First Message: </b><br>%s' 
		                             % (len(self.data1), sum(self.data1.values()), self.first_message), 
		                'font':{
		                  'family' : 'Arial',
		                  'size'   : 14
		                },
		                'showarrow': False,
		                'xref'     : 'paper',
		                'yref'     : 'paper',
		                'x'        : 0, 
		                'y'        : 0.9,
		                'align'    : 'left'
		               }]

		layout['annotations'] = annotations

 		pie = go.Pie(labels = list(self.data1.keys()),
	                 values = list(self.data1.values()),
	                 text   = list(self.data1.keys()),
	                 domain = {'x': [0.25, 0.75],
	                           'y': [0.45, 0.9]},
	                 hoverinfo = 'label+value')

		bar = go.Bar(x = list(self.data2.keys()),
	                 y = list(self.data2.values()),
	                 showlegend = False,
	                 hoverinfo = 'x+y')

		data = go.Data([bar, pie])
		fig = go.Figure(data = data, layout = layout)
		plotly.offline.plot(fig)

		print 'done!'

	# Runs visualizer
	def run(self):
		self.plot()

class EntryField(object):

	"""Helper class to create entry fields via specified Tkinter root and label"""

	def __init__(self, root, label):
		self.entrylabel   = tk.Label(root, text = label)
		self.entrycontent = tk.StringVar()
		self.entry        = tk.Entry(root, textvariable = self.entrycontent, bd = 1)
		self.entrylabel.pack()
		self.entry.pack()

# Removes tk root window
def tkWithdraw():
	root = tk.Tk()
	root.withdraw()

def visualize(data1, data2, first_message):
	visualization = Visualizer(data1, data2, first_message)
	visualization.run()

if __name__ == '__main__':
	visualize()