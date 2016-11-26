import numpy as np
import tensorflow as tf

accuracy = 0.

# Initializing the variables
#init = tf.initialize_all_variables()

#sess = tf.Session()  #manages the resources for graph execution
sess = tf.InteractiveSession()

#INPUTS:
#x = inputmatrix_1x3
x = tf.placeholder("float", [1,3],name='x') #placeholder(<datatype>,shape=,name=)
#w = weightsmatrix_3x3
w = tf.Variable(tf.random_normal([3,3]), name='w')  #Variable refers to a node in the graph, not the result

#PROCESSING:
y = tf.matmul(x,w)
#relu_out = outputmatrix_1x3
relu_out = tf.nn.relu(y)

relu_out = tf.nn.softmax(relu_out) #make predictions for n targets that sum to 1

#Variable is an empty node rn...
#fill in the content of a Variable node:
sess.run(tf.initialize_all_variables()) 

#sess.run(output, input feed)
print(sess.run(relu_out, feed_dict={x:np.array([[1.0,2.0,3.0]])}))

#release resources after use
sess.close()

#LD_LIBRARY_PATH="/home/nzaim/296/P3/lib/glibc/lib64/:/home/nzaim/296/P3/lib/libstdc/usr/lib/" ./lib/glibc/lib64/ld-2.17.so `which python`