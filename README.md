# xyz-json

Converts a Google Takeout json file to geojson and uploads to a HERE XYZ space. 

You'll want to download  the [HERE CLI] and sign up for a HERE Freemium account.

First version focused on [Google Takeout](https://takeout.google.com) location data. This script assumes you run this inside the Google Takeout directory you get from https://takeout.google.com though you 

options:

- `-f` specify the json file to parse (defaults to `Location History.json` for now)
- `-s` just save the geojson as a file and don't upload
- `-p` pipe the data to stdout (broken right now as I don't know what I'm doing)

To see how much Google has on you, type `here xyz show [spaceID] -v` to see it in XYZ Space Invader. It makes some convenient tags based on time and date.

You'll probably be shocked as to what you can see and the patterns you can figure out. You'll probably not want to distribute the map of the raw location data. If you do, HERE XYZ has pretty good [token management](https://xyz.api.here.com/token-ui/tokenmatrixui.html), including temporary tokens.

To generate hexbins for a little more privacy and something safer to share, type `here xyz hexbin [spaceID] -z 3-13` -- this will generate hexbins and their centroids in a new XYZ space, sized to look good at the zoom levels specified. Open it in Space Invader using the `here xyz show [spaceID] -v` option.


