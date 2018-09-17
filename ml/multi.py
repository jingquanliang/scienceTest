"""
Asynchronous Advantage Actor Critic (A3C) with continuous action space, Reinforcement Learning.

The Pendulum example.

View more on my tutorial page: https://morvanzhou.github.io/tutorials/

Using:
tensorflow r1.3
gym 0.8.0
"""

import multiprocessing
import threading
import tensorflow as tf
import numpy as np
import gym
import os
import shutil
import matplotlib.pyplot as plt



item_type_weights = tf.constant([1, 2, 3, 4], name='item_type_weights', dtype=tf.float32)
number_of_item_types = tf.cast(tf.count_nonzero(item_type_weights), tf.int32)

# target_item_embeddings = tf.get_variable(name='target_item_embeddings',
#                                                       shape=[2, 2],
#                                                       initializer=tf.random_uniform_initializer(minval=-0.001,
#                                                                                                 maxval=0.001),
#                                                       dtype=np.float32)

target_item_embeddings = tf.constant([[1,1],[1,1]], name='target_item_embeddings', dtype=tf.float32)

batch_behaviors_item_indices = tf.placeholder(name='batch_behaviors_item_indices',
                                                           shape=[2, 2, None],
                                                           dtype=tf.int32)

batch_behaviors_item_type_indices = tf.placeholder(name='batch_behaviors_item_type_indices',
                                                                shape=[2, 2, None],
                                                                dtype=tf.int32)

batch_behaviors_item_one_hots = tf.one_hot(name='batch_behaviors_item_one_hots',
                                                        indices=batch_behaviors_item_indices,
                                                        depth=2)

batch_behaviors_item_type_one_hots = tf.one_hot(name='batch_behaviors_item_type_one_hots',
                                                             indices=batch_behaviors_item_type_indices,
                                                             depth=number_of_item_types)


batch_behaviors_item_embeddings = tf.einsum('ijth,hd->ijtd',
                                                         batch_behaviors_item_one_hots,
                                                         target_item_embeddings)
batch_behaviors_item_weights = tf.einsum('ijth,h->ijt',
                                                      batch_behaviors_item_type_one_hots,
                                                      item_type_weights)

batch_behaviors_weighted_representations = tf.einsum('ijtd,ijt->ijtd',
                                                                  batch_behaviors_item_embeddings,
                                                                  batch_behaviors_item_weights)

batch_behaviors_matrix_inner_product = tf.matmul(batch_behaviors_weighted_representations,
                                                              batch_behaviors_weighted_representations,
                                                              transpose_a=False,
                                                              transpose_b=True)

if __name__ == "__main__":


    with tf.Session() as SESS:

        tf.global_variables_initializer().run()

        a=np.zeros((2,2,2))
        a[:,:,0]=([[0,1],[1,0]])
        a[:,:,1]=([[1,1],[1,0]])


        b=np.zeros((2,2,2))
        b[:,:,0]=([[0,2]])
        b[:,:,1]=([[1,3]])


        feed_dict = {batch_behaviors_item_indices: a,
                             batch_behaviors_item_type_indices: b,}

        SESS.run(tf.global_variables_initializer())

        h,typeh=SESS.run([batch_behaviors_item_one_hots,batch_behaviors_item_type_one_hots], feed_dict=feed_dict)

        print(h.shape)

        print(typeh.shape)

        # print(typeh)

        e,f,g,innerproduct=SESS.run([batch_behaviors_item_embeddings,batch_behaviors_item_weights,batch_behaviors_weighted_representations,batch_behaviors_matrix_inner_product], feed_dict=feed_dict)

        print(e.shape)

        print(e)

        print(f.shape)

        print(f)

        print(g.shape)

        print(g)

        print(innerproduct.shape)

        print(innerproduct)
