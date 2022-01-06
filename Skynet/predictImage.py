from detecto.utils import read_image
from detecto.core import Model
from detecto.visualize import show_labeled_image
image = read_image('Train EU coins/Test/IMG_3162.JPG')
predictions = model.predict_top(image)
labels, boxes, scores = predictions
show_labeled_image(image, boxes, labels)
for i in range(len(labels)):
  print(labels[i], scores[i])