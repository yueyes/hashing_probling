temp=[]

def find_position_dh(num,lis):
	count=0
	n=(((num%11)+(1+num%10)*count)%11)
	while n not in lis:
		print(n)
		count+=1
		n = (((num%11)+(1+num%10)*count)%11)
	print(n)

def find_position_qh(num,lis):
	count=0
	n=((num%11)+count*count)%11
	while n not in lis:
		print(n)
		count+=1
		n=((num%11)+count*count)%11
	print(n)

def search_position_lh(num,lis):
	print("a)linear probing: Start searching {} in {}".format(num,lis))
	count=0
	n = (num % 11 + count) % 11
	if num not in lis:
		print("number {} not in the list!".format(num))
		print("###########End of Searching#############\n")
		return
	while lis[n] != num:
		print("position {} is not equal to {}".format(n,num))
		count+=1
		n = (num % 11 + count) % 11
	print("Found position: {} which is equal to {}".format(n,lis[n]))
	print("###########End of Searching#############\n")

def search_position_dh(num,lis):
	print("c)double hashingStart searching {} in {}".format(num,lis))
	count=0
	n = (((num%11)+(1+num%10)*count)%11)
	if num not in lis:
		print("number {} not in the list!".format(num))
		print("###########End of Searching#############\n")
		return
	while lis[n] != num:
		print("position {} is not equal to {}".format(n,num))
		count+=1
		n = (((num%11)+(1+num%10)*count)%11)
	print("Found position: {} which is equal to {}".format(n,lis[n]))
	print("###########End of Searching#############\n")

def search_position_qh(num,lis):
	print("b)quadratic probing Start searching {} in {}".format(num,lis))
	count=0
	n = ((num%11)+count*count)%11
	if num not in lis:
		print("number {} not in the list!".format(num))
		print("###########End of Searching#############\n")
		return
	while lis[n] != num:
		print("position {} is not equal to {}".format(n,num))
		count+=1
		n = ((num%11)+count*count)%11
	print("Found position: {} which is equal to {}".format(n,lis[n]))
	print("###########End of Searching#############\n")


# search_position_lh(4,[22,88,None,None,4,15,59,17,None,31,10])
# search_position_lh(37,[22,88,None,None,4,15,59,17,None,31,10])
# search_position_lh(59,[22,88,None,None,4,15,59,17,None,31,10])
# search_position_lh(28,[22,88,None,None,4,15,59,17,None,31,10])

# search_position_qh(4,[22,88,None,None,4,15,"Deleted",17,59,31,10])
# search_position_qh(37,[22,88,None,None,4,15,"Deleted",17,59,31,10])
# search_position_qh(59,[22,88,None,None,4,15,"Deleted",17,59,31,10])
# search_position_qh(28,[22,88,None,None,4,15,"Deleted",17,59,31,10])

# search_position_dh(4,[22,15,59,17,4,None,"Deleted",88,None,31,10])
# search_position_dh(37,[22,15,59,17,4,None,"Deleted",88,None,31,10])
# search_position_dh(59,[22,15,59,17,4,None,"Deleted",88,None,31,10])
# search_position_dh(28,[22,15,59,17,4,None,"Deleted",88,None,31,10])



find_position_dh(59,[2,5,6,8])
# print("################")
# find_position_qh(59,[2,3,6,8])
