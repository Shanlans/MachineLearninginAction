# -*- coding: utf-8 -*-
import tensorflow as tf

x = tf.constant([[1., 1.], [2., 2.],[3,3]])

print(x.get_shape())
a = tf.reduce_mean(x)  # 1.5
b =tf.reduce_mean(x, 0)  # [1.5, 1.5]
c =tf.reduce_mean(x, 1)  # [1.,  2.]

with tf.Session() as sess:
    m,n,h,=sess.run([a,b,c])
    print(m,n,h)