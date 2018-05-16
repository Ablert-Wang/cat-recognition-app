class Image:
    """
    Common base class for every uploaded image
    """
    num_images = 0


    def __init__(self, file_name, file_path, prob):
        self.file_name = file_name
        self.file_path = file_path
        self.prob = prob
        self.cat_prob = float('{:.1f}'.format(prob * 100))
        self.dog_prob = float('{:.1f}'.format((1 - prob) * 100))
        Image.num_images += 1


print(Image('sdf', 'sdfssss', 0.5).num_images)


