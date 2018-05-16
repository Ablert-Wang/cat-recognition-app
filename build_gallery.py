import os
import glob
from predict import Predictor
from settings import TEST_DIR

def main():
    """Build gallery using test set
    """
    img_files = glob.glob(os.path.join(TEST_DIR, '*.jpg'))
    for i, img in enumerate(img_files):
        if i > 10: break
        print(img)
        # query application


if __name__ == '__main__':
    main()