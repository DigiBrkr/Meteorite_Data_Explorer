# Meteorite Data Explorer
## A Tool to Analyze Data from NASA's Meteorite Landing Dataset

### Some Background
This project consists of a set of tools to analyze the data from the [NASA Meteorite Landing Dataset](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh]). I created this to test my skills with Python and Data Science. I plan on updating the project on a reasonably regular basis. I encourage anyone who is willing, able and interested to contribute to the project. The programs(s) are primary written in Python with a bit of SQLite 3, HTML, and JavaScript as needed. The only things needed to run the program are Python 3 and an Internet connection.  
### Usage
To download the raw data from NASA type:
  For all Unix based Linux, Mac, BSD, etc.
  ```
  python3 DataGrab.py
    Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

    This is free software, and you are welcome to redistribute it under certain conditions.

    See LICENSE.md for details.

    Downloading data. This may take some time depending on your Internet connection.
    Data is 21098708 bytes long
    Data sanitisation in progress please wait
    Data successfully written to disk
  ```
  For the devil that is Microsoft Windows:
  ```
  DataGrab.py
    Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

    This is free software, and you are welcome to redistribute it under certain conditions.

    See LICENSE.md for details.

    Downloading data. This may take some time depending on your Internet connection.
    Data is 21098708 bytes long
    Data sanitisation in progress please wait
    Data successfully written to disk
    ```
To processes the raw data into a format that the analysis and visualization programs can understand type:
  For all Unix based Linux, Mac, BSD, etc.
  ```
    python3 DataOrganiser.py
      Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

      This is free software, and you are welcome to redistribute it under certain conditions.

      See LICENSE.md for details.

      Sanitizing Data. This may take a while depending on the speed of your computer.

      Data sanitisation complete. This Program will now exit.

    ```
    For Microsoft Windows:
    ```
    DataOrganiser.py
      Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

      This is free software, and you are welcome to redistribute it under certain conditions.

      See LICENSE.md for details.

      Sanitizing Data. This may take a while depending on the speed of your computer.

      Data sanitisation complete. This Program will now exit
    ```
To load the data into a format that can be displayed on a map type:
  For all Unix based Linux, Mac, BSD, etc.
  ```
  python3 DataMaper.py
    Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

    This is free software, and you are welcome to redistribute it under certain conditions.

    See LICENSE.md for details.

    Processing data please wait momentarily.
    17099 Locations sucesfully written to disk.

    Please open locations.html in your web browser to view the data.
  ```
  For Microsoft Windows:

  ```
  DataMapper.py
    Meteorite Data Explorer Copyright (C) 2018 DigiBrkr This program comes with ABSOLUTELY NO WARRANTY;

    This is free software, and you are welcome to redistribute it under certain conditions.

    See LICENSE.md for details.

    Processing data please wait momentarily.
    17099 Locations sucesfully written to disk.

    Please open locations.html in your web browser to view the data.
  ```

Finally before opening `locations.html` it is **recommended** but not required that you edit `locations.html` to add a Google Maps API key. The steps are as follows:

    1. Open `locations.html` in your text editor of choice.

    2. Go to: https://developers.google.com/maps/documentation/javascript/get-api-key sign in to your Google acount and click "Get A Key".

    3. Look for the line `<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key="</script>` in `locations.html` and paste your API
     key after the equals sign. The line should now look something like this:
      `<script src="https://maps.googleapis.com/maps/api/js?v=3.exp&key=D3fin1ty4R3414PIK3yH3r3Y3P!"</script>`

    4. Open `locations.html` in your browser of choice and you should see a map, if not check the JavaScript console of your browser.

### TO-DO

This is a list of features I plan to implement over the following months.

- [ ] Tool-tips with detailed information about each meteorite on the map.
- [ ] Dynamic display scaling on the map.  
- [ ] Map filters i.e. only show landings between the years of 1963 - 1974.
- [ ] A method for hiding API keys so the interactive web pages could be put on a web server.
- [ ] Configurable charts and graphs for all the data.
- [ ] Export to spreadsheet i.e. Microsoft Excel / LibreOffice Calc.  
