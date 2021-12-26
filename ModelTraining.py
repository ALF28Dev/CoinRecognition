from detecto import core, utils, visualize
import matplotlib.pyplot as plt

dataset = core.Dataset('Train/')
val_dataset = core.Dataset('Validation/')
model = core.Model(['1','0.10','0.20','0.50','0.01','0.05','0.02'])
losses = model.fit(dataset, val_dataset, epochs=10)

plt.plot(losses)
plt.show()
