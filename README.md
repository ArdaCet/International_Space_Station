# International Space Station Position Finder
Want to know where is the International Space Station (ISS) currently or are you a space enthusiast who enjoys any activity related with it? Here I've created a basic python script which will enable you to see the exact location of ISS.

Due to the gravitational forces, the space station and all other space stuff rotates around the earth (orbit) with an incredible speed. The International Space Station is moving at close to 28,000 km/h so its location changes really fast! So fast that it just takes 90 minutes to orbits the earth. Soo where is it right now? To find it try the [script](#Here_is_a_small_Python_Script) or the [executable](#Here_is_a_small_Python_Script).

To learn the dependencies to run the [script](#Here_is_a_small_Python_Script) (This part is not for the ones who just want to start the "whereisISS.exe"!)

## What is ISS
Even though space stations are awsome and magnificant, for me, it was difficult to find appropriate words to describe them. Here, I leave a paragraph below to provide some understanding and brief history of international space station which I believe one of the most rare and fabolous instance representing the solidarity of humanity. I feel that citing a part of text from the [wikipedia](https://en.wikipedia.org/wiki/International_Space_Station) would be concise and explanotory for specifying its significance for all of us.

>The International Space Station (ISS) is a modular space station (habitable artificial satellite) in low Earth orbit. It is a multinational collaborative project involving five participating space agencies: NASA (United States), Roscosmos (Russia), JAXA (Japan), ESA (Europe), and CSA (Canada) <sup>[1, 2](#References)</sup>. The ownership and use of the space station is established by intergovernmental treaties and agreements <sup>[3](#References)</sup>. The station serves as a microgravity and space environment research laboratory in which scientific research is conducted in astrobiology, astronomy, meteorology, physics, and other fields <sup>[4, 5, 6](#References)</sup>. The ISS is suited for testing the spacecraft systems and equipment required for possible future long-duration missions to the Moon and Mars <sup>[7](#References)</sup>.

## To acquire the API file for ISS coordinates
The API retrieve the location points from the NASA's database.

[API Doc](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)

Here is a small demonstration of how it looks once code is run.
![newplot](https://user-images.githubusercontent.com/57831340/110324997-d163f180-8027-11eb-84ad-a859031e9cb1.png)

The blue dot indicates where currently the international space station is.
To adjust the color or size of the marker on the world map, visit ```plt.basemap()``` [documantation](https://matplotlib.org/basemap/).

## Here is a small Python Script
In the code, some popular libraries are utilized so you most likely will not need to download anything special for running the "exe." file. However if you need to run the script in any interpreter:
In case you do not any of them, below you can find the adresses to download.

- [download pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

- [download numpy](https://numpy.org/install/)

- [download IPython](https://ipython.org/install.html)

- [download Matplotlib](https://matplotlib.org/downloads.html)

- [download Basemap](https://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap/)
    -Depending on your python version and operating system bit (32 or 64) select the correct wheel file. It's setup instructions [here](https://github.com/ArdaCet/International_Space_Station/tree/main/Script/BaseMap_download.md)

To reach the pipeline:
[click](https://github.com/ArdaCet/International_Space_Station/tree/main/Script/whereisISS.py)

## You are not in a mood of struggling with a command prompt?

You can find the executable file below

[Click](https://github.com/ArdaCet/International_Space_Station/blob/main/Executable/HereforDownload.md) to download the executable file on your system without needing any pre-set dependencies or programming language(s).

> Note: Other operating systems must download the script to run it. So, you may want to check the above [section](#Here_is_a_small_Python_Script)

## Licenses
The project is under the MIT licese so it can be used freely but it is not recommended to be used as a scientific purposes because of the possible sensitivity and specificity of the ISS locations data.

## References

1. Gary Kitmacher (2006). Reference Guide to the International Space Station. Apogee Books Space Series. Canada: Apogee Books. pp. 71–80. ISBN 978-1-894959-34-6. ISSN 1496-6921.
2. "Human Spaceflight and Exploration—European Participating States". European Space Agency (ESA). 2009. Retrieved 17 January 2009.
3. "International Space Station legal framework". European Space Agency (ESA). 19 November 2013. Retrieved 21 February 2015.
4. "International Space Station Overview". ShuttlePressKit.com. 3 June 1999. Retrieved 17 February 2009.
5. "Fields of Research". NASA. 26 June 2007. Archived from the original on 23 January 2008.
6. "Getting on Board". NASA. 26 June 2007. Archived from the original on 8 December 2007.  This article incorporates text from this source, which is in the public domain.
7. "ISS Research Program". NASA. Archived from the original on 13 February 2009. Retrieved 27 February 2009.
