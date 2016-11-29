import tensorflow as tf
#from tensorflow.nn import rnn, rnn_cell #deprecated
import numpy as np
#char_rdic = ['h','e','l','o', 'i', ' ', 't', 's', 'm', 'e'] # id -> char
char_rdic = ['h','e','l','o'] # id -> char
char_dic = {w: i for i, w in enumerate(char_rdic)} # char -> id
sample = [char_dic[c] for c in "hello"] # to index
x_data = np.array([ [1,0,0,0], #h
					[0,1,0,0], #e
					[0,0,1,0], #l
					[0,0,0,1]], #l					
					dtype='f')

# CONFIGURE:
batch_size = 1 
rnn_size = len(char_dic)  #char_vocab_size #1 hot coding so 1 of 4
time_step_size = 4  # 'hell' -> predict 'ello'
buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]


# RNN MODEL:
rnn_cell = tf.nn.rnn_cell.BasicRNNCell(rnn_size)
state = tf.zeros([batch_size, rnn_cell.state_size])
X_split = tf.split(split_dim=0, num_split=time_step_size, value=x_data)
outputs, state = tf.nn.seq2seq.rnn_decoder(
	decoder_inputs = X_split,
 	initial_state=state, 
 	cell=rnn_cell)
print(state)
print(outputs)

# logits: list of 2D Tensors of shape [batch_size x num_decoder_symbols].
# targets: list of 1D batch-sized int32 Tensors of the same length as logits.
# weights: list of 1D batch-sized float-Tensors of the same length as logits.
logits = tf.reshape(tf.concat(1, outputs), [-1, rnn_size])
targets = tf.reshape(sample[1:], [-1])
weights = tf.ones([time_step_size * batch_size])
loss = tf.nn.seq2seq.sequence_loss_by_example([logits], [targets], [weights])
cost = tf.reduce_sum(loss) / batch_size
train_op = tf.train.RMSPropOptimizer(0.01, 0.9).minimize(cost)

# LAUNCH THE GRAPH:
with tf.Session() as sess:	
	tf.initialize_all_variables().run()
	for i in range(100):
		sess.run(train_op)
		result = sess.run(tf.arg_max(logits, 1))
		print (result, [char_rdic[t] for t in result])