# About CoinRecognition

<img width="1013" alt="Screenshot 2021-12-27 at 20 58 40" src="https://user-images.githubusercontent.com/87500491/147506782-d0c3d7c1-d7e9-444c-83a3-1eec921c273a.png">

During my first term at university, I spoke to a friend at a party about counting coins. He suggested it would be awesome if an app could recognise the coins and count them. I immediately told him that I could attempt to develop an object detection model capable of performing such calculations. I had done some previous projects before using object detection, so I thought it would be a great challenge to attempt.

# Data Collection

The first step of developing an object detection model is gathering training data. I had some spare change lying around, so I started taking pictures of different coins in various layouts. This was one of my first ML projects, so I wasn't sure how many images I would need. I decided to start with a few pictures and then collect more over time. I started with about 35 images. At the time, I was aware that I would probably need a lot more pictures to develop a very good model; however, as this was the first project, I was more interested in building a functioning model.

<img width="750" alt="Screenshot 2021-12-27 at 20 33 17" src="https://user-images.githubusercontent.com/87500491/147505456-2f0ed998-4ea8-4204-b0d0-c5595adeea15.png">

# Data Labeling using LabelImg

Once I had collected the images, I used some software called LabelImg. It allows users to draw bounding boxes around objects within the image and save the label into an XML file.

<img width="1173" alt="Screenshot 2021-12-27 at 20 32 00" src="https://user-images.githubusercontent.com/87500491/147505377-ec756404-5393-473a-9856-354ca47b7ea6.png">

# Model Training

Training an object detection model requires quite a lot of processing power. To make the model training process more effective, I utilised Google Colaboratory. It is ideal for me because they provide a free GPU to users. After gathering the training data and labelling the images, I placed the pictures and XML files into a folder on my google drive, and I started training the model.

<img width="642" alt="Screenshot 2021-12-26 at 21 40 01" src="https://user-images.githubusercontent.com/87500491/147420660-b41b3760-eb42-4c44-a513-2d1da3adadb6.png">

# Losses

After training the model, I examined how the accuracy of its results changed during the training process. As you can see from the chart, the accuracy gradually improves over time. This is good news; however, the results are nowhere near perfect, and there is much room for improvement.

<img width="376" alt="Screenshot 2021-12-27 at 20 43 47" src="https://user-images.githubusercontent.com/87500491/147506002-414b7679-6934-4e55-85b0-d734b3e7ed80.png">

# Model Testing

After training the model, I performed some testing. I used images not in the training dataset to prevent any bias in the results. The results were nowhere near perfect; however, it can recognise 50p coins effectively. I used a hashmap to store the number of each coin detected in the image.

<img width="542" alt="Screenshot 2021-12-27 at 20 55 37" src="https://user-images.githubusercontent.com/87500491/147506624-72dbafad-b7b9-43af-b44a-fdb4d4a89ae7.png">

# Evaluation

I thought this was an exciting first project as an introduction to object detection. By using detecto, developing a model was a lot more straightforward. I could improve the model by including more labelled images within the Training and Validation datasets. The more data the model has to learn from, the better it should perform.
