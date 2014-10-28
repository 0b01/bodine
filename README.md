Bodine
-----
![Bodine](https://raw.githubusercontent.com/Yoyodyne/bodine/master/blatant.png)
### What is Bodine?
Bodine is a writing tool. Select a phrase, Press a hotkey and it does the following:
- searches selection on Google Books for correctness
- finds synonyms in context and gets their respective correctness using Google books
- matches wildcard in context (i.e. "what you see is what you *")
- returns examples of selected text
- shows historical usage of selected text
- :+1: more to come


### Development
This is in early beta with a minimal GUI(zenity really). If you like shabby softwares, you should consider playing with it and contributing. 

  #### Todo
  - [ ] GUI
  - [ ] Select Google Books API by subject/genre
  - [ ] Google N-grams View
  - [x] Incorporate Google Web API
  - [x] Synonyms using Textblob library
  - [ ] Stemming & POS tagging and other NLP: it's -> it is
  - [x] POS Tagging

### Requirements
As for now Bodine only runs on Ubuntu with X11 Windows System but can be trivially ported to other dist or windoes systems including Mac OS X.

``` bash
# on Ubuntu 14.04
sudo apt-get install xsel
sudo pip install -r requirements.txt```
