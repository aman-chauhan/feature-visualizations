from keras.utils import plot_model
import sys
import os


def print_shape(model_name, dim):
    model = None
    if model_name == 'mobile-net-v1':
        from keras.applications.mobilenet import MobileNet
        model = MobileNet(weights='imagenet', include_top=False,
                          input_shape=(dim, dim, 3))
    elif model_name == 'mobile-net-v2':
        from keras.applications.mobilenet_v2 import MobileNetV2
        model = MobileNetV2(weights='imagenet', include_top=False,
                            input_shape=(dim, dim, 3))
    elif model_name == 'vgg-16':
        from keras.applications.vgg16 import VGG16
        model = VGG16(weights='imagenet', include_top=False,
                      input_shape=(dim, dim, 3))
    elif model_name == 'vgg-19':
        from keras.applications.vgg19 import VGG19
        model = VGG19(weights='imagenet', include_top=False,
                      input_shape=(dim, dim, 3))
    elif model_name == 'densenet-121':
        from keras.applications.densenet import DenseNet121
        model = DenseNet121(weights='imagenet', include_top=False,
                            input_shape=(dim, dim, 3))
    elif model_name == 'densenet-169':
        from keras.applications.densenet import DenseNet169
        model = DenseNet169(weights='imagenet', include_top=False,
                            input_shape=(dim, dim, 3))
    elif model_name == 'densenet-201':
        from keras.applications.densenet import DenseNet201
        model = DenseNet201(weights='imagenet', include_top=False,
                            input_shape=(dim, dim, 3))
    elif model_name == 'resnet-50':
        from keras.applications.resnet50 import ResNet50
        model = ResNet50(weights='imagenet', include_top=False,
                         input_shape=(dim, dim, 3))
    elif model_name == 'xception':
        from keras.applications.xception import Xception
        model = Xception(weights='imagenet', include_top=False,
                         input_shape=(dim, dim, 3))
    elif model_name == 'inception-v3':
        from keras.applications.inception_v3 import InceptionV3
        model = InceptionV3(weights='imagenet', include_top=False,
                            input_shape=(dim, dim, 3))
    elif model_name == 'inceptionresnet-v2':
        from keras.applications.inception_resnet_v2 import InceptionResNetV2
        model = InceptionResNetV2(weights='imagenet', include_top=False,
                                  input_shape=(dim, dim, 3))

    path = os.path.join('bin', os.path.join('shapes', '{}-{}.jpg'))
    plot_model(model, to_file=path.format(model_name, dim), show_shapes=True,
               show_layer_names=True, rankdir='TB')


if __name__ == '__main__':
    print_shape(sys.argv[1], int(sys.argv[2]))
