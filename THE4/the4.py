def inheritance(Descriptions):

	def converter(Descriptions): 
		result = []
		for i in Descriptions:
			result.append(i.split())
		return result

	editedDescriptions = converter(Descriptions)

	Final_Result = []

	for i in editedDescriptions:
		if "DECEASED" in i:
			deceased_person = i[1]
			inheritance_value = float(i[2])

	def isAlive(name): 
		for i in editedDescriptions:
			if "DEPARTED" in i and name in i:
				return False
		return True	

	def spouse(name): 
		for i in editedDescriptions:
			if "MARRIED" in i and name in i:
				if i[1] == name:
					return i[2]
				elif i[2] == name:
					return i[1]
		return ""

	def children(name): 
		children_list = []
		for i in editedDescriptions:
			if "CHILD" in i and name in i:
				if name == i[1] or name == i[2]:
					for j in i[3:]:
						children_list.append(j)
		return children_list

	def parents(name): 
		for i in editedDescriptions:
			if "CHILD" in i and name in i[3:]:
				return [i[1]] + [i[2]]
		return []	

	def grandparents(name): 
		grandparents = []
		for i in editedDescriptions:
			if "CHILD" in i and parents(name):
				if parents(name)[0] in i[3:]:
					grandparents.append(i[1])
					grandparents.append(i[2])
				if parents(name)[1] in i[3:]:
					grandparents.append(i[1])
					grandparents.append(i[2])
		return grandparents

	def alive_descendants(name): 
		alives = []
		for child in children(name):
			if isAlive(child):
				alives.append(child)
			else:
				alives += alive_descendants(child)

		return alives

	def alive_parents(name): 
		alives = []
		for parent in parents(name):
			if isAlive(parent):
				alives.append(parent)
		return alives

	def descendants_share(name, share): 
		share_len = len(children(name))
		for child in children(name):
			if not alive_descendants(child) and not isAlive(child):
				share_len -= 1
		if share_len != 0:
			for child in children(name):
				if isAlive(child):
					Final_Result.append((child, share/share_len))
				else:
					descendants_share(child, share/share_len)

	def parents_share(name, share): 
		share_len = len(parents(name))
		for parent in parents(name):
			if not alive_descendants(parent) and not isAlive(parent):
				share_len -= 1
		if share_len != 0:
			for parent in parents(name):
				if isAlive(parent):
					Final_Result.append((parent, share/share_len))
				else:
					descendants_share(parent, share/share_len)	

	def grandparents_share(name, share):
		share_len = len(grandparents(deceased_person))
		for grandparent in grandparents(name):
			if not alive_descendants(grandparent) and not isAlive(grandparent):
				share_len -= 1
		if share_len != 0:
			for grandparent in grandparents(name):
				if isAlive(grandparent):
					Final_Result.append((grandparent, share/share_len))
				else:
					descendants_share(grandparent, share/share_len)	

	if alive_descendants(deceased_person): #PG1

		if spouse(deceased_person) and isAlive(spouse(deceased_person)):	
			descendants_share(deceased_person, inheritance_value*0.75)
			Final_Result.append((spouse(deceased_person), (inheritance_value)*0.25))
		
		else: 		
			descendants_share(deceased_person, inheritance_value)

	elif parents(deceased_person): #PG2

		if (alive_descendants(parents(deceased_person)[0]) + alive_descendants(parents(deceased_person)[1])) or alive_parents(deceased_person):	

			if spouse(deceased_person) and isAlive(spouse(deceased_person)):
				parents_share(deceased_person, inheritance_value*0.5)
				Final_Result.append((spouse(deceased_person), (inheritance_value)*0.5))	
			else: 
				parents_share(deceased_person, inheritance_value)

		elif grandparents(deceased_person): #PG3

			if spouse(deceased_person) and isAlive(spouse(deceased_person)):
				Final_Result.append((spouse(deceased_person), (inheritance_value)*0.75))
				grandparents_share(deceased_person, inheritance_value*0.25)

			else:
				grandparents_share(deceased_person, inheritance_value)

	if Final_Result == [] and spouse(deceased_person) and isAlive(spouse(deceased_person)):
		return [(spouse(deceased_person), inheritance_value)]

	def final_Result_Calculator(Final_Result):
		for i in Final_Result:
			for j in Final_Result[(Final_Result.index(i)+1):]:
				if i[0] == j[0]:
					Final_Result.append((i[0], i[1]+j[1]))
					Final_Result.remove(i)
					Final_Result.remove(j)
					final_Result_Calculator(Final_Result)		

	final_Result_Calculator(Final_Result)

	return Final_Result

