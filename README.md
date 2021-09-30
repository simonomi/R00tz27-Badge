# R00tz27 Badge Hack
This is my hack of the badge from the r00tz village at defcon 27, which replaces the party mode with a music player. More songs can be added to src/songs.py in rttl format [examples](http://www.picaxe.com/RTTTL-Ringtones-for-Tune-Command/).


## Installation
To install this hack, first get the original code from [here](https://github.com/badg3rs-labs/r00tz27) and configure it to where _./flash_ properly works. Then, replace the _/src_ directory with the one provided here, and run _./flash_ again. If configured correctly, that should send the files in the _/src_ directory to the badge, enabling the hack

## Usage
Using this hack is simple, the _party mode_ button (top right) will now enter _song selection mode_ when pressed. In that mode, use the left two buttons to scroll through available songs (some included) and the bottom right to play the selected song. The top right button will exit _song selection mode_ and the rest of the badge is untouched.

## Notes
* Currently, there is no feedback indicating the selected song
* If buttons are pressed too quickly, they may not be registered
