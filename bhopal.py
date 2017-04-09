def jump_a_wall (wallHeight, jumpHeight,offset):
	required_jumps = 0
	while wallHeight > 0:
		wallHeight = wallHeight-jumpHeight
		required_jumps+=1
		if(wallHeight>0):
			wallHeight+=offset

	return required_jumps


def GetJumpCount(input1,input2,input3):
	required_jumps = 0
	for wall in input3:
		required_jumps += jump_a_wall(wall,input1,input2)
		

	return required_jumps







ip1 = int(input());
ip2 = int(input());
ip3_cnt = 0
ip3_cnt = int(input())
ip3_i=0
ip3 = []
while ip3_i < ip3_cnt:
    ip3_item = int(input());
    ip3.append(ip3_item)
    ip3_i+=1
output = GetJumpCount(ip1,ip2,ip3)
print(str(output))