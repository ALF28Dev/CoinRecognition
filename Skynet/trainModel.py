import matplotlib.pyplot as plt
from detecto.core import Model, Dataset
from detecto.utils import read_image
from detecto.visualize import show_labeled_image

labels = ['0.01 EU','0.02 EU', '0.05 EU', '0.10 EU', '0.20 EU', '0.50 EU', '1.00 EU', '2.00 EU']
training_data = Dataset('Train EU coins/Training data2')
val_data = Dataset('Train EU coins/Validation data2')
model = Model(labels)
model.load("Train EU coins/model.pth", labels)

losses = model.fit(training_data, val_data)
plt.plot(losses)
plt.show()
model.save('Train EU coins/model.pth')