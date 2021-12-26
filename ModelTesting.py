from detecto import core, utils, visualize

image = utils.read_image('Test/IMG_3452.JPG')
predictions = model.predict_top(image)
labels, boxes, scores = predictions

hash = {}
for coin in predictions[0]:
  if coin in hash:
    hash[coin] += 1
  else:
    hash[coin] = 1
print(hash)

total = 0
for coin in hash:
  total += (float(coin)*float(hash[coin]))
print(total)

model.save('Test/model_weights.pth')

labels, boxes, scores = predictions
visualize.show_labeled_image(image, boxes, labels)
