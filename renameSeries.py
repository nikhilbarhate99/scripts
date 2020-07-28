"""
1. The episodes wil be formatted as :
    series_name season_num epidode_num episode_name

2. Change the file_format, file_directory, series_name, season_num variables

3. To automatically extract episode names from the wikipedia page paste the
   wiki link in the url variable (requires urllib and BeautifulSoup libraries)

   OR

   Manually input episode names in ep_list (commented code section)

4. All NON alpha numeric characters will be removed from episode name
"""

import os
from glob import glob

file_format = "." + "mkv"
file_directory = "./The Spy/"
series_name = "The Spy"
season_num = 1

# Get episode names from wikipedia url
import urllib
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/The_Spy_(TV_series)"

ep_list = []
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, features="lxml")
for lel in soup.select('td[class="summary"]'):
  # print(lel.text.replace('"',''))
   ep_list.append(str(lel.text.replace('"','')))


# Manually add episode names (in order of episode numbers)
# ep_list = [
#         "The Immigrant",
#         "What's New, Buenos Aires?",
#         "Alone in Damascus",
#         "The Odd Couples",
#         "Fish Gotta Swim",
#         "Home",
#         ]

# keep only alpha numeric characters in episode namespace
for i in range(len(ep_list)):
    st = ""
    for ch in ep_list[i]:
        if ch.isalnum() or ch == ' ':
            st += ch
    ep_list[i] = st


# print seperators in between
seperator = "-"*100

dirs = glob( file_directory + "*" + file_format)

# check if directories contains files
if len(dirs) == 0:
        print(seperator)
        print("No file of given file format!")
        print(seperator)
        print("Format Cancelled!")
        print(seperator)

else:
    if len(dirs) != len(ep_list):
        print(seperator)
        print("Length of episode name list [ep_list] should be equal to length of files in directories [dirs]")
        print(seperator)
        print("Format Cancelled!")
        print(seperator)

    else:
        dirs_formated = []

        # iterate episodes
        for i in range(len(dirs)):

            # add series name
            st = series_name + " "

            # add series number
            if season_num < 10:
                st += "S0" + str(season_num)
            else:
                st += "S" + str(season_num)

            # add episode number
            if i+1 < 10:
                st += "E0" + str(i+1)
            else:
                st += "E" + str(i+1)

            # add episode name
            st += " " + ep_list[i]

            # add file format
            st += file_format

            dirs_formated.append(st)

        # sort directories (according to episode number)
        dirs.sort()
        dirs_formated.sort()
        # print formatted strings
        print(seperator)
        for i in range(len(dirs)):
            print(dirs[i].replace(file_directory, "") + "\t -> \t" + dirs_formated[i])

        # confirmation
        print(seperator)
        ch = input("To confirm changes, ENTER 'y' : ")
        print(seperator)

        # if confirmed then rename episodes
        if ch.lower() == 'y':
            for i in range(len(dirs)):
                os.rename(dirs[i], file_directory + dirs_formated[i])
                print("Formatted Episode " + str(i+1))

        else:
            print("Format Cancelled!")

        print(seperator)
