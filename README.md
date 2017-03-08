# Manga Mania

## What is Manga Mania

Manga-Mania is a simple desktop application for reading manga scraped from MangaFox (http://mangafox.me). It is written in `python3`, with the generous aid of `pyqt5`, `requests` and `beautiful-soup`.

Here are a few screen captures.

![Manga-Mania-1](screenshots/snapshot1.png)

![Manga-Mania-2](screenshots/snapsshot2.png)


## Features

### Supported

* Advanced search functionality of MangaFox
* Read chapters sequentially/jump to particular pages

### Planned

* Add a 'history' feature, i.e., remember where the user last left off
* Improve UI (display app status, search results & chapter info in a more appealing way)
* Provide support for other popular manga sites like KissManga, Mangahere, etc.

### Running Manga Mania

`Manga Mania` has a few dependencies:

* PyQt5
* requests
* BeautifulSoup4

You can easily install them using `pip` like so:

`# pip install pyqt5 requests beautifulsoup4`

To run the script, clone the repo and switch to the `manga-mania` directory and run `manga-mania.py`

```
$ git clone https://github.com/TheIllusionistMirage/Manga-Mania
$ cd Manga-Mania/manga-mania
$ python3 manga-mania.py
```

### Problems & Bugs

If you encounter anything out of the ordinary, just drop me a mail at `koushtav at fleptic dot eu`.

---------------

**Legal**

*I am neither affiliated to the manga sites mentioned in this application, nor do I own any kind of rights to the manga these sites contain. I merely provide a medium to access from your desktop what is already reachable using a web browser. In no event shall I be held responsible for any kinds of damages, physical or intellectual, arising from the use of `Manga-Mania`. See LICENSE for licensing info.*
