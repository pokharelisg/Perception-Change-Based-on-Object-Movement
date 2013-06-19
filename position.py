import math
from main_class import*
import pickle
import autopy
class position():
  # def __init__(self):
	# # 	self.prev_x = 0
	# # 	self.prev_y = 0
	# 	self.direction ="Current Slide"
		
	def getLength(self,x1,y1,x2,y2):
		length= math.sqrt((x2-x1)**2+(y2-y1)**2)
		return length

	def getDirection(self,x1,y1,x2,y2,length):
		if length>100 and x1+y1 !=0:
			if(x2>x1):
				direction = "Right Slide"
				autopy.key.tap(autopy.key.K_RIGHT)
			else:
				direction = "Left Slide"
				# call here event Left
				autopy.key.tap(autopy.key.K_LEFT)
		else:
			direction = "Current Slide"
		return direction

	def compute_position(self,current_x,current_y,frame=0):

		self.direction ="Current Slide"          
		try:
			self.Vars = pickle.load(open(".config", "r"))        
			self.prev_x = self.Vars["prevX"]
			self.prev_y = self.Vars["prevY"] 
			self.Vars["noCnt"] =0
		except:
			self.Vars["prevX"] =0
			self.Vars["prevY"] =0
		if (frame%10==0):
			self.Vars["prevX"] = current_x
			self.Vars["prevY"] = current_y
			self.current_x = current_x
			self.current_y = current_y
			# self.direction =[]
			length = position().getLength(self.prev_x,self.prev_y,self.current_x,self.current_y)
			self.direction = position().getDirection(self.prev_x,self.prev_y,self.current_x,self.current_y,length)
			pickle.dump(self.Vars, open(".config", "w"))
			return self.direction
		else:
			return self.direction
