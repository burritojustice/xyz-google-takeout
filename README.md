# xyz-json

Converts a json file to geojson and uploads to a HERE XYZ space. 

You'll need the HERE CLI.

First version focused on Google Takeout location data.

options:

`-f` specify the json file to parse (defaults to `Location History.json` for now)
`-s` just save the geojson
`-p` pipe the data to stdout (broken right now as I don't know what I'm doing)

To see how much Google has on you, type `here xyz show [spaceID] -v` to see it in XYZ Space Invader. It makes some convenient tags based on time and date.

To generate hexbins for a little more privacy and something safer to share, type `here xyz hexbin [spaceID] -z 3-13` -- this will generate hexbins and centroids in a new XYZ space. Open it in Space Invader using the `here xyz show [spaceID] -v` option.
