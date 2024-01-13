# News-Headline-Tagger

https://github.com/Mohit-Harsh/News-Headline-Tagger/assets/111693866/4366b251-8dd8-42e0-bc74-0616757b7150

News Headline Tagger is an `LSTM` based `Text Classifier` that classifies the News Headlines into different categories like - Sports, Politics, Entertainment, Environment, Technology etc.
This Project is a combination of `Web Scraping`, `AI Model Building` and `Deployment Using Tkinter GUI`.

# Libraries Required

Some important libraries required for building this project are:

  * Tensorflow
  * Keras
  * Tkinter
  * Pandas
  * Numpy
  * BeautifulSoup
    
For further details about the requirements refer the requirements.txt file.

# How to Build

### 1. News Headlines Scrape

* Scrape News Headlines data from `Google News` using `BeautifulSoup`.
* Process and Store the data into a Dataframe and save it. Here is my dataset - [google_news_dataset.json](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/google_news_dataset.json).
* Refer [Google News Scraper.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/Google%20News%20Scraper.ipynb) file for the python code.

### 2. Build DL Model

* Load the scraped data as a Pandas DataFrame.
* Load BERT Tokenizer form tensorflow hub.
* Load the BERT preprocessor from tensorflow hub.
* Label Encode the Tags using sklearn's LabelEncoder.
* One-Hot-Encode the Label Encoded Tags using sklearn's OneHotEncoder.
* Create a Funtional Keras Model with the following layers :-
 
  * Input Layer of shape - ().
  * BERT Preprocessing Layer that takes InputLayer outputs as inputs. (Max Tokens = 128)
  * BERT Tokenizer Layer that takes Preprocessed outputs as inputs. (Max Tokens = 128)
  * Dense Layer with 768 units that takes BERT Tokenizer Sequence Outputs as inputs.
  * LSTM layer with 768 units, input shape - (None,768)
  * Dropout Layer (0.3)
  * Dense Layer with 'Softmax' activation.
 
* Train the model.
* Save the model.
* Refer [News Headline Tagger.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/News%20Headlines%20Tagger.ipynb) file for the python code.

### 3. Build Tkingter GUI

You can also build a Tkinter GUI for inference.
Refer [News Headline Tagger GUI.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/New%20Headline%20Tagger%20GUI.ipynb) file for python code.
