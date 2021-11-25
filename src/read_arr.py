import math
import std_msgs.msg as std
import numpy as np


array1=np.load("array.npy")
array1=array1
array1[:,2]=array1[:,2]-array1[0][2]


array2=np.load("array1.npy")  
smaller_array=[]
bigger_array=[[]]


if len(array1)<=len(array2):
    smaller_array=array1
    bigger_array=array2

else:
    smaller_array=array2
    bigger_array=array1
smallest_time=100000.0
bigger_id=[]
diff_arr=[]

for eachS in smaller_array:
    for eachB in bigger_array:
        time_diff=abs(eachS[2]-eachB[2])
        if time_diff<smallest_time:
            smallest_time=time_diff
            bigger_id=eachB

    diff_arr.append([math.hypot(eachS[0]-bigger_id[0],eachS[1]-bigger_id[1]),round(eachS[2]-smaller_array[0][2],3)])


print("done")




