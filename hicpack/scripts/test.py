import tensorflow as tf


def f(x):
    return x ** 2


matrix = tf.placeholder(shape=(10, 20), dtype=tf.float32)
feed_matrix = [[i * j for j in range(20)] for i in range(1, 11)]
a = tf.placeholder(shape=[None, None], dtype=tf.float32)
# a = tf.map_fn(f, matrix)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     result = sess.run(tf.eye(None), feed_dict={matrix: feed_matrix})
#     print(result)

weight = tf.ones_like(a) - tf.eye(tf.shape(a)[0])
# tf.multiply(weight, z)
# tf.scalar_mul