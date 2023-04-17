from datetime import datetime
#生成一个变量dob ，gettime的对象，存自己的生日
#



now = datetime.now()

print ("当前时间：", now.strftime("%Y-%m-%d %H:%M:%S"))

dob = datetime(2004,2,1)

print("My date of birth is:", dob.strftime("%Y-%m-%d"))