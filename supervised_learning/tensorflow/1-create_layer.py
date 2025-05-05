#!/usr/bin/env python3
"""
Defines a function to create a layer for neural network
"""


import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """
    Creates a layer for neural network

    parameters:
        prev [tensor]: tensor output of the previous layer
        n [int]: the number of nodes in the layer to create
        activation [function]: the activation function the layer should use

    use tf.keras.initializers.VarianceScaling(mode='fan_avg')
        to implement He et. al initialization for the layer weights
    each layer is given the name "layer"

    returns:
        tensor output of the layer
    """
    weights_initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    layer = tf.layers.Dense(
        n,
        activation=activation,
        name="layer",
        kernel_initializer=weights_initializer)
    return (layer(prev))
