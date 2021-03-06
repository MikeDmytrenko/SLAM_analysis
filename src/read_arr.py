
# %%
import math
import std_msgs.msg as std
import numpy as np
import matplotlib.pyplot as plt

# Preprocessing
# %%
array1=np.load("array.npy")
array1=array1
array1[:,2]=array1[:,2]-array1[0][2]


array2=np.load("array2.npy")  
array2[:,2]=array2[:,2]-array2[0][2]

fig=plt.figure(figsize=(20, 20), dpi=200)
ax1 = fig.add_subplot(111)
ax1.scatter(array1[:,0],array1[:,1],s=10, c='b', marker="o", label='first')
ax1.scatter(array2[:,0],array2[:,1],s=10, c='r', marker="x", label='second')
plt.legend(loc='upper left')
plt.show()


#Plotting

# %%

smaller_array=[]
bigger_array=[[]]


if len(array1)<=len(array2):
    smaller_array=array1
    bigger_array=array2

else:
    smaller_array=array2
    bigger_array=array1

bigger_id=[]
diff_arr=[]

for eachS in smaller_array:
    smallest_time=100000.0
    for eachB in bigger_array:
        time_diff=abs(eachS[2]-eachB[2])
        if time_diff<smallest_time:
            smallest_time=time_diff
            bigger_id=eachB

    diff_arr.append([math.hypot(eachS[0]-bigger_id[0],eachS[1]-bigger_id[1]),round(eachS[2]-smaller_array[0][2],3)])

np.save("result",diff_arr)

print("mean error is", round(np.mean(np.array(diff_arr)[:,0]),3))

# %%



