data_s =  open('input.txt', 'r')
a = data_s.read()

if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
    ans = 'YES'
else:
    ans = "NO"

output_data = open('output.txt', 'w')
output_data.write(ans)
#запись

data_s.close()
output_data.close()
#ОБЯЗАТЕЛЬНО не забывать