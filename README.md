# twitter-scraping-with-python

<p align="center">
    <img src="https://22570l2e793j2oo9c81ug2nh-wpengine.netdna-ssl.com/wp-content/uploads/2020/05/CRAWL-TWITTER.png">
</p>

This guide seeks to teach you how to get started using **Python** requests from the **Twitter API** using **Tweepy**, as well as store the information gained from those requests into a **csv** file. If you need additional information, **Twitter** also provides [a course](https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research) on how to use **V2** of their **API** for academic research, as well as [other resources](https://developer.twitter.com/en/use-cases/do-research/academic-research/resources).

# GETTING STARTED WITH TWITTER DEVELOPER

- Collecting Twitter data is done through the **Twitter API**. In order to use the Twitter API, you'll need to [apply for developer access](https://developer.twitter.com/en/apply-for-access):
- If you're an undergrad, you don't have access to the academic research track, so just apply for the standard developer track
- In order to apply, you'll either need to log in to your account or create one
  - It is recommended to apply using an existing **Twitter** account, in our experience they are more likely to get approved, and get approved faster

# USING TWITTER DEVELOPER TO GAIN API ACCESS

- Start at the **Twitter** [developer portal](https://twitter.com/login?redirect_after_login=https%3A%2F%2Fdeveloper.twitter.com%2Fen%2Fportal%2Fdashboard). This is how you will create a project and app in order to get the necessary access and bearer tokens you need to write code that accesses information using the **Twitter API**
- Gathering **Twitter** data to investigate trends related to toxicity, community building, platform governance and other related issues
- Create a project, then an app, and you'll be presented with your keys. [Here's the video walkthrough](https://drive.google.com/file/d/1Wva--0kS19M7yXdzhJW_65kUdPPKhjkE/view?usp=sharing)
- After initial setup, your keys can be accessed by hitting the key icon next to the app name in your project dashboard.
  - Your keys will be hidden after they're first displayed to you, so you should either take a screenshot or save them as variables in a file so you don't have to continue to regenerate them.

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873321851407970315/unknown.png">
</p>

# GETTING STARTED WITH PYTHON

- Thus far, we've been using **Python** to work with the **Twitter API**. In order to use **Python**, you'll first have to install it onto your computer. I recommend two possible tracks for getting started:
  - 1- If space on your computer isn't a concern, or you anticipate working with data science into the future, it's probably best to download **Anaconda**, which will install **Python** for you, and provide a dashboard allowing you to access **Jupyter Notebooks**, **PyCharm**, and other resources.
    - Download [**Anaconda**](https://www.anaconda.com/products/individual):
    - **Anaconda** also makes things easier by pre-installing commonly used libraries like **Pandas** so you can skip that step
    - Once you download **Anaconda**, you should open the Anaconda-Navigator and download the community version of **PyCharm** (an **IDE** made specifically for (**Python**), unless you already have a preferred **IDE** you're attached to
      - **IDE** = Integrated Development Environment -- **IDEs** are to write code/programs as word processing software (**Word**, **Google Docs**) are to writing documents. Different **IDEs** are made for different purposes-- there are some made to work for a broad scope of languages (like **Visual Studio Code** or **Aom**), others optimized for a specific language (like **PyCharm** for **Python**), and others that are designed to help with a more niche task (like **Spyder** for data science)
  - 2- If you prefer to save space, you can download [**Python**](https://www.python.org/downloads/) by itself
    - You'd then need to download an IDE to use, we recommend either [**PyCharm**](https://www.jetbrains.com/PyCharm/download/#section=mac) or [**Visual Studio Code**](https://code.visualstudio.com/). If you have windows, you should already have visual studio installed
- Once you have **Python** and an **IDE** installed, you'll want to install the necessary packages to web scraping using the **Twitter API**. You can either do this through terminal or PyCharm.
  - 1- Using terminal, enter the command `pip3 install [insert package name`
    - (ex. `pip3 install Tweepy`)
    - [video example using `pip3 install` in terminal](https://drive.google.com/file/d/1WpGRgykJr-0jzvrg7j1fhmTNN2kUyw5H/view?usp=sharing) (I already had **Tweepy** installed, so the output might look different)
  - 2- Go through **PyCharm**: in bottom menu bar, select **Python** packages, search for desired package, and click install
    - [video example installing in PyCharm](https://drive.google.com/file/d/1ocNvBiMj_V3ByNAqFzsf28Vig28mePNc/view?usp=sharing)
- Packages to install (some might already be installed if you install through **Anaconda**, but entering the command to install them won't hurt anything)
  - `Tweepy`
  - `csv`
  - `JSON`
  - `schedule`
  - `time`
  - `pandas`

# YOUR FIRST PYTHON PROGRAM

- This example will use **PyCharm**, but the steps should be essentially the same no matter what **IDE** you choose to use in [this hello world video walkthrough](https://drive.google.com/file/d/1-xySKW52zgVfXdLo7U3Zw1u8EAU4Lpab/view?usp=sharing)
- In my example, I wrote code to print hello world -- `print('hello world')` -- in order to run the program, open terminal (either in your **IDE** or a normal terminal window), and enter the command: `Python3 filename.py`
  - Common pitfall: if you are running the program outside of your **IDE**, you will get an error saying something like there is no file with that name. To fix this, you have to make sure your terminal is pointed at the right folder. For example, if I had a file called `main.py` stored in a file called `PythonProjects` which was saved onto my desktop, you would first have to enter the following command into terminal before running your code: `cd Desktop/PythonProjects`
- If you're completely new to coding, it will probably be best to use a course to learn the basic structures you'll being using (ie. loops, conditional statements)
  - **Codeacademy** is a great resource that offers both free and paid courses
  - All **SCU** students have free access to **LinkedIn Learning**, which offers some really cool classes-- you'll have to fill out [this form](https://forms.gle/VZaUtmm4Kxd44ajy5) in order to get access
  - If you prefer to read info rather than watch it, [this course](https://realpython.com/learning-paths/python3-introduction/) from **Real Python** will be very helpful
  - While **YouTube** is also a great free resource, taking a course with structure is usually a better option to avoid having a scattered experience that repeats information and leaves out other bits
- If you have experience with coding but not in **Python**, [W3Schools](https://www.w3schools.com/python/) is a great resource for understanding syntax

# MAKING YOUR FIRST REQUEST USING Tweepy

- Now that you have Python set up and your developer credentials set up, you are able to start writing programs to make requests from the **Twitter API**!
- Start by writing a statement to **import Tweepy** : `import Tweepy as tw`
  - The as tw part saves time because now when you would otherwise type out Tweepy, you can type tw instead
- Now, authorize your request and connect to the **Twitter API's** endpoint:
  - Save **API key**, **API secret**, **access token**, and **access secret** as variables.
  - Use the **Tweepy** package's `OAuthHandler` function to input your **API key** and **secret**, and the `set\_access\_token` function to input your access token and secret
  - Using the variable you've stored your keys and tokens in, use **Tweepy's API** function to connect to the **Twitter API's** endpoint

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873321894579945472/unknown.png">
</p>

- _Importing **Tweepy**, storing keys and tokens, securing access and connecting to the **Twitter API's** endpoint_

    - Now, you're ready to make a request! **Tweepy** allows you to use different functions to search in different ways, but for now, we'll just work with the search method:
    - To use a different method, check out the [list of available ones](https://docs.Tweepy.org/en/v3.5.0/api.html#timeline-methods) in **Tweepy's** documentation
    - You can filter your search results using the parameters below, as well as the tweet\_mode parameter, and limit the number of tweets by appending `.items()`

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873321918986600529/unknown.png">
</p> 

- _From **Tweepy's** documentation_

    - Example search:

    <p align="center">
        <img src="https://media.discordapp.net/attachments/778418042702528532/873321937840013342/unknown.png">
    </p> 

    - The **tweets** variable will now store an iterator - in order to access the information itself, you'll want to loop through it
    - To see what information is contained in each object, simply print the item:

    <p align="center">
        <img src="https://media.discordapp.net/attachments/778418042702528532/873321958639538236/unknown.png">
    </p> 

    - This is all the information for one **tweet**: clearly this isn't the most readable way to store data, so we'll want to store it in a better way:
      - If you want only particular pieces of information, you can use a dataframe, then store it into a **csv** file.
      - If you want to store the entire **JSON** object, you can store it directly into a **csv ** file.

# USING DATAFRAMES

- Dataframes are an aspect of the **Pandas** package that is an essential part of dealing with data in **Python** -- it essentially creates a table that organizes your information.
- When using dataframes, you'll need to include the statement: `import pandas as pd`
- In this example, let's say we're trying to collect the time a tweet is created, its author's **Twitter** handle, and the full text.
- We'll want to create three lists that will store those pieces of information.
- Then, we can loop through the iterator item returned by our search and add the information we want to those lists.
  - In order to find how to reference and grab the information you want, print out the entire **Tweepy** object and check how the information you want is labelled.

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873321979074187274/unknown.png">
</p>

- Once lists are populated with the search information, we can make it into a dataframe.
- As you can see below, when I print the data frame, the information is neatly organized.

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873322008249786398/unknown.png">
</p> 

- However, we ideally want to be storing this information into a **csv** file, rather than only being able to view it in the terminal.
- You can do this easily by using **pandas's** `to_csv()` method

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873322037408567376/unknown.png">
</p>
 
- Now, when you run this program, either a csv file will be created, or an existing one will be overwritten with the dataframe we created.

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873322037408567376/unknown.png">
</p> 

# CONVERTING A JSON OBJECT INTO A csv FILE

- In order to use this method, you'll have to import the **csv** package: `import csv`
- First, you'll need to create a list to store the **JSON** objects and iterate through the search object to populate it
- Then, open a **csv** file to write into
- Next, you'll loop through the list of **JSON** objects and write the data from the **JSON** object into the **csv** file
  - On the first iteration through the loop, you'll want to access the titles of the data contained in the **JSON** object and write them into the **csv** file so that the first line of each column indicates what information is contained in it

<p align="center">
    <img src="https://media.discordapp.net/attachments/778418042702528532/873322092504965130/unknown.png">
</p>

# MORE TOPICS YET TO INCLUDE

- Running a file continuously in the background
- Rate limits on requests
- Using **requests** library rather than **Tweepy** to grab tweets