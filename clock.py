import re
import random

class Clock:
	def __init__(self):
		self.clock=0
	def tock(self, len=1):
		self.clock+=len