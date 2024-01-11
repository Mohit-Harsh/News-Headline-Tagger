# News-Headline-Tagger

https://github.com/Mohit-Harsh/News-Headline-Tagger/assets/111693866/4366b251-8dd8-42e0-bc74-0616757b7150

# How to Build

### 1. News Headlines Scrape

* Scrape News Headlines data from `Google News` using `BeautifulSoup`.
* Process and Store the data into a Dataframe and save it. Here is my dataset - [google_news_dataset.json](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/google_news_dataset.json).
* Refer [Google News Scraper.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/Google%20News%20Scraper.ipynb) file for the python code.

### 2. Build DL Model

* Load the scraped data as a Pandas DataFrame.
* Create a Tokenizer using keras to tokenize News Headlines.
* Create a Tokenizer using keras to tokenize Tags.
* Fit both the Tokenizers on respective texts.
* Use the Tokenizers to convert Texts to Sequences.
* One-Hot-Encode the Tags.
* Create a Sequential model with the following layers :-
  
  * Input Layer
  * Embedding Layer of 128 dimension.
  * LSTM layer with 100 units, input dimension - (,128)
  * Dropout Layer
  * Dense Layer with 'Softmax' activation.
 
* Train the model.
* Save the model.
* Refer [News Headline Tagger.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/News%20Headlines%20Tagger.ipynb) file for the python code.

### 3. Build Tkingter GUI
You can also build a Tkinter GUI for inference.
Refer [News Headline Tagger GUI.ipynb](https://github.com/Mohit-Harsh/News-Headline-Tagger/blob/main/New%20Headline%20Tagger%20GUI.ipynb) file for python code.
