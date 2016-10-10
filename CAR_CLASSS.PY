class Car(object):
	speed=0
	num_of_doors=4
	num_of_wheels=4

	def __init__(self, name='General',model='GM',car_type=None):
		self.name=name
		self.model=model
		self.car_type=car_type
		if self.name=='Porshe' or 'Koenigsegg':
			self.num_of_doors=2
		else:
		    self.num_of_doors=4
		if self.name=='trailer':
		    self.num_of_wheels=8
		else:
		    self.num_of_wheels=4

	def is_saloon(self):
	    pass	            
    
    def drive(self, knot):
    	self.knot=knot
        if self.model == 'trailer':
            self.speed = knot * 11
        if self.name == 'Mercedes':
            self.speed = 10**knot
        return self


		