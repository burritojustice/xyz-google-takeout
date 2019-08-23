# xyz-json

Converts a [Google Takeout](https://takeout.google.com) location history `json` file to geojson and uploads to a HERE XYZ space. 

## Prerequsites

Requires Python3 (and a command line, aka Terminal). On the Mac, you'll probably have Python2 installed. `python --version` and `python3 --verison` will let you know. 

If you only have python2, `brew install python3` is your friend. (If you don't have `brew` installed, do it. There are good [instructions are here](https://wsvincent.com/install-python3-mac/). It's not that hard, I promise.)

Re Windows, don't know -- um, look at https://www.python.org/downloads/ I guess.

To get this on a mao, you'll  want to download the [HERE CLI] and sign up for a free (really!) [HERE](https://explore.xyz.here.com/) account.

## How to use it

This script assumes you run it in the Location History Google directory you get from https://takeout.google.com (though you can specify the full file path of the `.json` file with `-f`).

  python3 parse_google_takeout_location.py

then follow the HERE XYZ CLI prompts. It will upload, and you'll see an XYZ space ID, something like:

  xyzspace 'a1B2c34D' created successfully

Copy your space ID.

To see how much Google has on you, type 

  here xyz show [spaceID] -v
  
to see it in XYZ Space Invader. 

The script generates some convenient tags based on time and date that you can use as filters. You can color things by choosing the properties in the popups and controls on the left side.

There are some options which you probably won't need:

- `-f` specify the json file to parse (as noted, the script defaults to `Location History.json` if you don't use it)
- `-s` just save the geojson as a file and don't upload
- `-p` pipe the data to stdout (this broken right now because I don't know what I'm doing with stdout)

You'll probably be shocked as to what you can see and the patterns you can figure out. You'll probably not want to distribute the map of the raw location data. If you do, HERE XYZ has pretty good [token management](https://xyz.api.here.com/token-ui/tokenmatrixui.html), including temporary tokens.

To generate hexbins for a little more privacy and something safer to share, type `here xyz hexbin [spaceID] -z 3-13` -- this will generate hexbins and their centroids in a new XYZ space, sized to look good at the zoom levels specified. Open it in Space Invader using the `here xyz show [spaceID] -v` option.


