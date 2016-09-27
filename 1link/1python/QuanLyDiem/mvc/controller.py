import os
import time
from view import *
from model import *

class control:
	def __init__(self, view, model):
		while True:
			model._calc(view.getInput(mode=1), view.getInput(mode=2), view.getInput(mode=None), view.getInput(mode='oper'))
			view.setSol(model.get_sol())
			time.sleep(1)
			if view.getInput(mode='continue') == 'n': break

if __name__ == '__main__':
    control(view(), model())
