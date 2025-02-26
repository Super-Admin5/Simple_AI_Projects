<<<<<<< HEAD
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
print("GPU devices:", tf.config.list_physical_devices('GPU'))
print("Is CUDA available:", tf.test.is_built_with_cuda())
=======
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf
print("GPU devices:", tf.config.list_physical_devices('GPU'))
print("Is CUDA available:", tf.test.is_built_with_cuda())
>>>>>>> a6cd6acd (Reinitialized repository and added changes)
