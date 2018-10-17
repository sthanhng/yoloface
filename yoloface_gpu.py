import argparse

from PIL import Image
from YOLO import YOLO


#####################################################################
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='model-weights/YOLO_Face.h5',
                        help='path to model weights file')
    parser.add_argument('--anchors', type=str, default='cfg/yolo_anchors.txt',
                        help='path to anchor definitions')
    parser.add_argument('--classes', type=str, default='cfg/face_classes.txt',
                        help='path to class definitions')
    parser.add_argument('--score', type=float, default=0.5,
                        help='the score threshold')
    parser.add_argument('--iou', type=float, default=0.45,
                        help='the iou threshold')
    parser.add_argument('--img-size', type=list, action='store',
                        default=(416, 416), help='input image size')
    parser.add_argument('--image', default=False, action="store_true",
                        help='image detection mode')
    parser.add_argument('--output', type=str,
                        default='', help='image/video output path')
    args = parser.parse_args()
    return args


def detect_img(yolo):
    while True:
        img = input('[i] ==> Input image filename: ')
        try:
            image = Image.open(img)
        except:
            print('[!] ==> Open Error! Try again!')
            continue
        else:
            res_image = yolo.detect_image(image)
            res_image.show()

    yolo.close_session()


def _main():
    # Get the arguments
    args = get_args()

    if args.image:
        # Image detection mode
        print('[i] ==> Image detection mode\n')
        detect_img(YOLO(args))
    else:
        print('[i] ==> Video detection mode\n')
        # Call the detect_video method here

    print('Well done!!!')


if __name__ == "__main__":
    _main()
