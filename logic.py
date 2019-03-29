
class Logic:
	def __init__(self, string1, string2):
		self.string1_hash = [0] * 26
		self.string2_hash = [0] * 26

		self.string1 = string1
		self.string2 = string2

		self.string1_len = len(string1)
		self.string2_len = len(string2)
		
		self.mismatch = 0
		self.string1_wildcard = 0
		self.string2_wildcard = 0

	def match(self):
		# Assigning values to the string1_hash and string2_hash based on the availability of the the alphabets 
		for char in self.string1:
			# Checking for wildcard entries
			if char != "?":
				self.string1_hash[ord(char)-97] += 1
			else:
				self.string1_wildcard += 1
		for char in self.string2:
			# Checking for wildcard entries
			if char != "?":
				self.string2_hash[ord(char)-97] += 1
			else:
				self.string2_wildcard += 1

	    # Checking for mismatches
		if self.string1_len > self.string2_len : 
			for i in range(26):
				if (self.string2_hash[i] != 0) and (self.string2_hash[i] > self.string1_hash[i]):
					self.mismatch += self.string2_hash[i] - self.string1_hash[i]
			# returning values based on wilcard entries and mismatch
			if self.mismatch <= self.string1_wildcard:
				return True
			else:
				return False
		else:
			for i in range(26):
				if (self.string1_hash[i] != 0) and (self.string1_hash[i] > self.string2_hash[i]):
					self.mismatch += self.string1_hash[i] - self.string2_hash[i] 
			# returning values based on wilcard entries and mismatch
			if self.mismatch <= self.string2_wildcard:
				return True
			else:
				return False
