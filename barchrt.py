import matplotlib.pyplot as plt
mark=[88,50,77,33,44,22,98,92,25,34]
gd=[0,35,70,100]
plt.title("Student Grade")
plt.hist(mark,gd,histtype="bar",rwidth=0.5,facecolor="blue")
#plt.hist(mark,gd,histtype="step",rwidth=0.5,facecolor="blue")
#plt.hist(mark,gd,histtype="stepfilled",rwidth=0.5,facecolor="blue")
plt.xticks([0,35,70,100])
plt.xlabel("Percentage")
plt.ylabel("No. Of Student")
plt.show()
