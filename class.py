class cat:
	def __init__(self,arms, legs, eyes, tail, furry):
		self.arm_length = float(arms)
		self.leg_length = float(legs)
		self.eye_number = int(eyes)
		self.is_tail = bool(tail)
		self.is_furry = bool(furry)

	def animal(self):
		print(f"arm length is {self.arm_length}\nleg length is {self.leg_length}\n{self.eye_number} eyes\ntail = {self.is_tail}\nfurry = {self.is_furry}")

sample_animal = cat(arms=20.0,legs=20.0,eyes=2,tail=True,furry=True)
sample_animal.animal()
