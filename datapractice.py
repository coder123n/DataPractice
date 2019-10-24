months={"Jan":"1","Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}
#print(months["Jan"])
for key in months:
	if key.startswith("M"):
	    print(months[key])
jlife={"name":"Jocelyn", "age":16, "classes":{"2nd":"DSW" ,"3rd":"Math" ,"4th":"English" ,"5th":"APES" ,"6th":"Sculpture"}}
if "6th" in jlife["classes"]:
	print("has 6th period")
else:
	print("no 6th period")
	
jolife={"name":"Joy", "age":16, "classes":{"1st":"English","2nd":"DSW" ,"3rd":"Jazz Band" ,"4th":"Math" ,"5th":"APES" ,"6th":"Marching Band"}}
if "6th" in jolife["classes"]:
	print("has 6th period")
else:
	print("no 6th period")
	
jonlife={"name":"Jonathan", "age":16, "classes":{"1st":"English","2nd":"DSW" ,"3rd":"Biology" ,"4th":"Orchestra" ,"5th":"Calculus" ,"6th":"Independent PE"}}
if "6th" in jlife["classes"]:
	print("has 6th period")
else:
	print("no 6th period")
	
