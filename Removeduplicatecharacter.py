s=input("Enter the string with duplicate character:")
output=''
for x in s:
	if x not in output:
		output+=x
print(output)