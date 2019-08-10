# The following RTTTL tunes were extracted from the following:
# https://github.com/onebeartoe/media-players/blob/master/pi-ezo/src/main/java/org/onebeartoe/media/piezo/ports/rtttl/BuiltInSongs.java
# most of which originated from here:
# http://www.picaxe.com/RTTTL-Ringtones-for-Tune-Command/
#

import machine

SONGS = [
    "Imperial:d=4,o=5,b=112:8g,16p,8g,16p,8g,16p,16d#.,32p,32a#.,8g,16p,16d#.,32p,32a#.,g,8p,32p,8d6,16p,8d6,16p,8d6,16p,16d#.6,32p,32a#.,8f#,16p,16d#.,32p,32a#.,g,8p,32p,8g6,16p,16g.,32p,32g.,8g6,16p,16f#.6,32p,32f.6,32e.6,32d#.6,16e6,8p,16g#,32p,8c#6,16p,16c.6,32p,32b.,32a#.,32a.,16a#,8p,16d#,32p,8f#,16p,16d#.,32p,32g.,8a#,16p,16g.,32p,32a#.,d6,8p,32p,8g6,16p,16g.,32p,32g.,8g6,16p,16f#.6,32p,32f.6,32e.6,32d#.6,16e6,8p,16g#,32p,8c#6,16p,16c.6,32p,32b.,32a#.,32a.,16a#,8p,16d#,32p,8f#,16p,16d#.,32p,32g.,8g,16p,16d#.,32p,32a#.,g",
    "Pinocchio:d=4,o=6,b=160:d5,d,c,b5,g#5,a5,2e,f#5,f#,e,d,c#,d,2g,a,g,f#,e,d,c,b5,a5,2e,2f#5,1d",
    "SmallWorld:d=4,o=6,b=180:8e5,8f5,g5,e,c,8d,8c,c,b5,b5,8d5,8e5,f5,d,b5,8c,8b5,a5,g5,g5,8e5,8f5,g5,8c,8d,e,8d,8c,a5,8d,8e,f,8e,8d,g5,f,e,d,2c,2c.7,d7,2e7,2c7,2d.7,d7,1d7,2d.7",
     "Macarena:d=16,o=5,b=180:4f6,8f6,8f6,4f6,8f6,8f6,8f6,8f6,8f6,8f6,8f6,8a6,8c6,8c6,4f6,8f6,8f6,4f6,8f6,8f6,8f6,8f6,8f6,8f6,8d6,8c6,4p,4f6,8f6,8f6,4f6,8f6,8f6,8f6,8f6,8f6,8f6,8f6,8a6,4p,2c.7,4a6,8c7,8a6,8f6,4p,2p",
    "FurElise:d=8,o=5,b=125:32p,e6,d#6,e6,d#6,e6,b,d6,c6,4a.,32p,c,e,a,4b.,32p,e,g#,b,4c.6,32p,e,e6,d#6,e6,d#6,e6,b,d6,c6,4a.,32p,c,e,a,4b.,32p,d,c6,b,2a",
    "SMBtheme:d=4,o=5,b=100:16e6,16e6,32p,8e6,16c6,8e6,8g6,8p,8g,8p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,16p,8c6,16p,8g,16p,8e,16p,8a,8b,16a#,8a,16g.,16e6,16g6,8a6,16f6,8g6,8e6,16c6,16d6,8b,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16c7,16p,16c7,16c7,p,16g6,16f#6,16f6,16d#6,16p,16e6,16p,16g#,16a,16c6,16p,16a,16c6,16d6,8p,16d#6,8p,16d6,8p,16c6",
    "20thCenFox:d=16,o=5,b=140:b,8p,b,b,2b,p,c6,32p,b,32p,c6,32p,b,32p,c6,32p,b,8p,b,b,b,32p,b,32p,b,32p,b,32p,b,32p,b,32p,b,32p,g#,32p,a,32p,b,8p,b,b,2b,4p,8e,8g#,8b,1c#6,8f#,8a,8c#6,1e6,8a,8c#6,8e6,1e6,8b,8g#,8a,2b",
    "MissionImp:d=16,o=6,b=95:32d,32d#,32d,32d#,32d,32d#,32d,32d#,32d,32d,32d#,32e,32f,32f#,32g,g,8p,g,8p,a#,p,c7,p,g,8p,g,8p,f,p,f#,p,g,8p,g,8p,a#,p,c7,p,g,8p,g,8p,f,p,f#,p,a#,g,2d,32p,a#,g,2c#,32p,a#,g,2c,a#5,8c,2p,32p,a#5,g5,2f#,32p,a#5,g5,2f,32p,a#5,g5,2e,d#,8d",
    "Careless:d=4,o=5,b=80:8c6,8b6,16a6,8e6,8c.6,8b6,16a6,8e6,8c.6,8g6,16f6,8c6,8a,8g.6,16f6,8c.6,8f6,16e6,8c6,8a,2f,8e,8f,8g,8a,8b,8c6,8d6,8e6,8b6,16a6,8e6,8c.6,8b6,16a6,8e6,8c.6,8g6,16f6,8c6,8a,8g.6,16f6,8c.6,8f6,16e6,8c6,8a,2f",
    "Chicken:d=32,o=5,b=50:g#,g#,a#,a#,f,f,16g#,g#,g#,a#,a#,f,f,16g#,g#,g#,a#,a#,c#6,c#6,16c6,16c6,16a#,16g#,16f#,f#,f#,g#,g#,d#,d#,16f#,f#,f#,g#,g#,d#,d#,16f#,f#,f#,g#,g#,a#,c6,16c#6,16a#,16g#,16f,16c#",
    "Picaxe:d=4,o=6,b=101:g5,c,8c,c,e,d,8c,d,8e,8d,c,8c,e,g,2a,a,g,8e,e,c,d,8c,d,8e,8d,c,8a5,a5,g5,2c",
    "Indiana:d=4,o=5,b=250:e,8p,8f,8g,8p,1c6,8p.,d,8p,8e,1f,p.,g,8p,8a,8b,8p,1f6,p,a,8p,8b,2c6,2d6,2e6,e,8p,8f,8g,8p,1c6,p,d6,8p,8e6,1f.6,g,8p,8g,e.6,8p,d6,8p,8g,e.6,8p,d6,8p,8g,f.6,8p,e6,8p,8d6,2c6",
    "TakeOnMe:d=4,o=4,b=160:8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5,8f#5,8e5,8f#5,8f#5,8f#5,8d5,8p,8b,8p,8e5,8p,8e5,8p,8e5,8g#5,8g#5,8a5,8b5,8a5,8a5,8a5,8e5,8p,8d5,8p,8f#5,8p,8f#5,8p,8f#5,8e5,8e5",
    "Xfiles:d=4,o=5,b=125:e,b,a,b,d6,2b.,1p,e,b,a,b,e6,2b.,1p,g6,f#6,e6,d6,e6,2b.,1p,g6,f#6,e6,d6,f#6,2b.,1p,e,b,a,b,d6,2b.,1p,e,b,a,b,e6,2b.,1p,e6,2b.",
    "StarWars:d=4,o=5,b=45:32p,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#.6,32f#,32f#,32f#,8b.,8f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32c#6,8b.6,16f#.6,32e6,32d#6,32e6,8c#6",
    "GoodBad:d=4,o=5,b=56:32p,32a#,32d#6,32a#,32d#6,8a#.,16f#.,16g#.,d#,32a#,32d#6,32a#,32d#6,8a#.,16f#.,16g#.,c#6,32a#,32d#6,32a#,32d#6,8a#.,16f#.,32f.,32d#.,c#,32a#,32d#6,32a#,32d#6,8a#.,16g#.,d#",
    "Flinstones:d=4,o=5,b=40:32p,16f6,16a#,16a#6,32g6,16f6,16a#.,16f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c6,d6,16f6,16a#.,16a#6,32g6,16f6,16a#.,32f6,32f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c6,a#,16a6,16d.6,16a#6,32a6,32a6,32g6,32f#6,32a6,8g6,16g6,16c.6,32a6,32a6,32g6,32g6,32f6,32e6,32g6,8f6,16f6,16a#.,16a#6,32g6,16f6,16a#.,16f6,32d#6,32d6,32d6,32d#6,32f6,16a#,16c.6,32d6,32d#6,32f6,16a#,16c.6,32d6,32d#6,32f6,16a#6,16c7,8a#.6",
    "Jeopardy:d=4,o=6,b=125:c,f,c,f5,c,f,2c,c,f,c,f,a.,8g,8f,8e,8d,8c#,c,f,c,f5,c,f,2c,f.,8d,c,a#5,a5,g5,f5,p,d#,g#,d#,g#5,d#,g#,2d#,d#,g#,d#,g#,c.7,8a#,8g#,8g,8f,8e,d#,g#,d#,g#5,d#,g#,2d#,g#.,8f,d#,c#,c,p,a#5,p,g#.5,d#,g#",
    "Gadget:d=16,o=5,b=50:32d#,32f,32f#,32g#,a#,f#,a,f,g#,f#,32d#,32f,32f#,32g#,a#,d#6,4d6,32d#,32f,32f#,32g#,a#,f#,a,f,g#,f#,8d#",
    "Smurfs:d=32,o=5,b=200:4c#6,16p,4f#6,p,16c#6,p,8d#6,p,8b,p,4g#,16p,4c#6,p,16a#,p,8f#,p,8a#,p,4g#,4p,g#,p,a#,p,b,p,c6,p,4c#6,16p,4f#6,p,16c#6,p,8d#6,p,8b,p,4g#,16p,4c#6,p,16a#,p,8b,p,8f,p,4f#",
    "MahnaMahna:d=16,o=6,b=125:c#,c.,b5,8a#.5,8f.,4g#,a#,g.,4d#,8p,c#,c.,b5,8a#.5,8f.,g#.,8a#.,4g,8p,c#,c.,b5,8a#.5,8f.,4g#,f,g.,8d#.,f,g.,8d#.,f,8g,8d#.,f,8g,d#,8c,a#5,8d#.,8d#.,4d#,8d#.",
    "Overworld:d=16,o=6,b=125:4g#5,g#.5,d#5,g#.5,4f#5,f#.5,g#5,a#.5,4b5,b.5,g#5,b.5,4a#5,a#.5,b5,c#.,2d#.,c#.,c#,c#.,2d#.,c#.,c,a#.5,4g#5,4d#.5,g#.5,g#.5,a#5,c,c#,1d#,d#.,d#.,e,f#.,1g#,g#.,g#.,f#,e.,4f#,e.,2d#,d#.,e,d#.,8c#,c#,d#,2e,8d#,8c#,8b5,b5,c#,2d#,8c#,8b5,8a#5,a#5,c,2d,4f,4d#",
    "Super Mario Main:d=4,o=5,b=125:a,8f.,16c,16d,16f,16p,f,16d,16c,16p,16f,16p,16f,16p,8c6,8a.,g,16c,a,8f.,16c,16d,16f,16p,f,16d,16c,16p,16f,16p,16a#,16a,16g,2f,16p,8a.,8f.,8c,8a.,f,16g#,16f,16c,16p,8g#.,2g,8a.,8f.,8c,8a.,f,16g#,16f,8c,2c6",
    "Bohemian:d=4,o=5,b=80:16e,2e.,16p,8c,8d,16e,2e,16p,8p,16d,16e,8f,16g,16f,16p,8e,d,16p,8d,8e,8f,16g,16f,16p,8e,2d,16p,16e,2e,16p,8p,8e,8g,8b.,16a,2a,8p,8c6,8c6,8c6,8c6,8c6,8c.6,16a,8f.,8e.,2d.,8p,16a,2a,16p,8p,8g,16a,16a#,2a.,8p,16a,16a,8a#.,16a#,8a#,8a,g.,16p,16c,8c,8g,8g,8a,8a,8a#,8a#,8c6,16a#,a,16p,16g,16a,c.6,16g,16a,2f,16c#,8d#,8c#.,16d#,2c",
    "5thSymph:d=4,o=5,b=180:8f,8f,8f,1c#,8p,8d#,8d#,8d#,1c,8p,8f,8f,8f,8c#,8f#,8f#,8f#,8f,8c#6,8c#6,8c#6,2a#,8p,8f,8f,8f,8c,8f#,8f#,8f#,8f,8d#6,8d#6,8d#6,1c6,8f6,8f6,8d#6,8c#6,8c#,8c#,8d#,8f,8f6,8f6,8d#6,8c#6,8c#,8c#,8d#,8f,8f6,8f6,8d#6,c#6,p,a#,p,2f6",
     "YellowSub:d=4,o=5,b=125:8a#5,8b5,2c#6,8a#5,8g#5,8a#5,2f#5,8a#5,8a#5,8g#5,8f#5,2d#5,8a#5,8a#5,1g#5,4c#6,4c#6,4c#6,8c#6,8d#6,8g#5,8g#5,8g#5,8g#5,2g#5,8g#5,8g#5,4g#5,2g#5,8f#5,8f#5,8f#5,8f#5,2f#5,4c#6,4c#6,4c#6,8c#6,8d#6,8g#5,8g#5,8g#5,8g#5,2g#5,8g#5,8g#5,4g#5,2g#5,8f#5,8f#5",
    "GrimGrin:d=4,o=5,b=225:8e,8e,a,a,e6,8e6,8e6,d#6,d#6,2b,a,a,c6,8c6,8c6,d6,a#,2a#,e6,8e6,e6.,e6,f,8f,2f,8p,a.,8a,a,a,d#,d#,2d#,e6,8a,8a,e6,8p,8a,e6,d6,c6,b,1a.,e,e,2a.,a,2e6,e6,e6,2d#6,2d#6,2b,b,b,2a,2a,2c6,c6,c6,2d6,2a#,1a#,2e6.,e6,2e6,2e,2f,2f,1f,2a.,a,2a,2a,2d#,2d#,1d#,e6,8a,8a,e6,8p,8a,e6,d6,c6,b,1a.",
    "Arabian:d=16,o=6,b=63:8a#5,a#.5,c.,c#,4f.,32e,32f,8e,c#,c,c#.,c.,a#5,4f.,c#,c#.,c.,a#5,8f.,f,g#.,f.,d#,8f.,32c#,32f,e.,c#.,e,2f",
    "Blue:d=4,o=6,b=63:16b,16d#,16g#,16b,16c#7,16f#,16a#,8b,16g#,16b,16d#7,16e7,16g#,16d#7,16c#7,16b,16d#,16g#,16b,16c#7,16f#,16a#,8b,16g#,16b,16d#7,16e7,16g#,16d#7,16c#7,16b,16d#,16g#,16b,16c#7,16f#,16a#,8b,16g#,16b,16d#7,16e7,16g#,16d#7,16c#7,16b,16d#,16g#,16b,16a#,16c#,16f#,8g#,16b5,16f#,8g#,16f#,16g#,16a#,16b,16d#,16g#,16b,16c#7,16f#,16a#,8b,16g#",
    "SMBwater:d=8,o=6,b=225:4d5,4e5,4f#5,4g5,4a5,4a#5,b5,b5,b5,p,b5,p,2b5,p,g5,2e.,2d#.,2e.,p,g5,a5,b5,c,d,2e.,2d#,4f,2e.,2p,p,g5,2d.,2c#.,2d.,p,g5,a5,b5,c,c#,2d.,2g5,4f,2e.,2p,p,g5,2g.,2g.,2g.,4g,4a,p,g,2f.,2f.,2f.,4f,4g,p,f,2e.,4a5,4b5,4f,e,e,4e.,b5,2c.",
    "SMBunderground:d=16,o=6,b=100:c,c5,a5,a,a#5,a#,2p,8p,c,c5,a5,a,a#5,a#,2p,8p,f5,f,d5,d,d#5,d#,2p,8p,f5,f,d5,d,d#5,d#,2p,32d#,d,32c#,c,p,d#,p,d,p,g#5,p,g5,p,c#,p,32c,f#,32f,32e,a#,32a,g#,32p,d#,b5,32p,a#5,32p,a5,g#5",
    "OneMore:d=16,o=5,b=125:4e,4e,4e,4e,4e,4e,8p,4d#.,4e,4e,4e,4e,4e,4e,8p,4d#.,4e,4e,4e,4e,4e,4e,8p,4d#.,4f#,4f#,4f#,4f#,4f#,4f#,8f#,4d#.,4e,4e,4e,4e,4e,4e,8p,4d#.,4e,4e,4e,4e,4e,4e,8p,4d#.,1f#,2f#",
    "Digital<3:d=16,o=5,b=125:4d6,4c#.6,8a,8b,8a,8b,8a,4c#6,8b,4a,8c#.6,8e.6,4f#.6,8a,8b,8a,8b,8a,4c#6,8b,4a,8c#6,8e6,4f#6,4p,8a,8b,8a,8b,8a,8b,8a,4c#.6,8a,8a,8a,8a,4a,8f#,8a,8a,4a,4f#,4e",
    "Scatman:d=4,o=5,b=200:32p,8b,16b,32p,8b,16b,32p,8b,2d6,16p,16c#.6,16p.,8d6,16p,16c#6,8b,16p,8f#,2p.,16c#6,8p,16d.6,16p.,16c#6,16b,8p,8f#,2p,32p,2d6,16p,16c#6,8p,16d.6,16p.,16c#6,16a.,16p.,8e,2p.,16c#6,8p,16d.6,16p.,16c#6,16b,8p,8b,16b,32p,8b,16b,32p,8b,2d6,16p,16c#.6,16p.,8d6,16p,16c#6,8b,16p,8f#,2p.,16c#6,8p,16d.6,16p.,16c#6,16b,8p,8f#,2p,32p,2d6,16p,16c#6,8p,16d.6,16p.,16c#6,16a.,16p.,8e,2p.,16c#6,8p,16d.6,16p.,16c#6,16a,8p,8e,2p,32p,16f#.6,16p.,16b.,16p.",
    "The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6",
    "Entertainer:d=4,o=5,b=140:8d,8d#,8e,c6,8e,c6,8e,2c.6,8c6,8d6,8d#6,8e6,8c6,8d6,e6,8b,d6,2c6,p,8d,8d#,8e,c6,8e,c6,8e,2c.6,8p,8a,8g,8f#,8a,8c6,e6,8d6,8c6,8a,2d6",
    "Muppets:d=4,o=5,b=250:c6,c6,a,b,8a,b,g,p,c6,c6,a,8b,8a,8p,g.,p,e,e,g,f,8e,f,8c6,8c,8d,e,8e,8e,8p,8e,g,2p,c6,c6,a,b,8a,b,g,p,c6,c6,a,8b,a,g.,p,e,e,g,f,8e,f,8c6,8c,8d,e,8e,d,8d,c",
    "Looney:d=4,o=5,b=140:32p,c6,8f6,8e6,8d6,8c6,a.,8c6,8f6,8e6,8d6,8d#6,e.6,8e6,8e6,8c6,8d6,8c6,8e6,8c6,8d6,8a,8c6,8g,8a#,8a,8f",
    "Bond:d=4,o=5,b=80:32p,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d#6,16d#6,16c#6,32d#6,32d#6,16d#6,8d#6,16c#6,16c#6,16c#6,16c#6,32e6,32e6,16e6,8e6,16d#6,16d6,16c#6,16c#7,c.7,16g#6,16f#6,g#.6",
    "MASH:d=8,o=5,b=140:4a,4g,f#,g,p,f#,p,g,p,f#,p,2e.,p,f#,e,4f#,e,f#,p,e,p,4d.,p,f#,4e,d,e,p,d,p,e,p,d,p,2c#.,p,d,c#,4d,c#,d,p,e,p,4f#,p,a,p,4b,a,b,p,a,p,b,p,2a.,4p,a,b,a,4b,a,b,p,2a.,a,4f#,a,b,p,d6,p,4e.6,d6,b,p,a,p,2b",
    "TopGun:d=4,o=4,b=31:32p,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,16f,d#,16c#,16g#,16g#,32f#,32f,32f#,32f,16d#,16d#,32c#,32d#,16f,32d#,32f,16f#,32f,32c#,g#",
    "A-Team:d=8,o=5,b=125:4d#6,a#,2d#6,16p,g#,4a#,4d#.,p,16g,16a#,d#6,a#,f6,2d#6,16p,c#.6,16c6,16a#,g#.,2a#",
    "LeisureSuit:d=16,o=6,b=56:f.5,f#.5,g.5,g#5,32a#5,f5,g#.5,a#.5,32f5,g#5,32a#5,g#5,8c#.,a#5,32c#,a5,a#.5,c#.,32a5,a#5,32c#,d#,8e,c#.,f.,f.,f.,f.,f,32e,d#,8d,a#.5,e,32f,e,32f,c#,d#.,c#",
    "UnderPre:d=8,o=5,b=112:f,f,f,16f,16f,f,16c,4p,f,f,f,16f,16f,f,16c,4p,f,f,f,16f,16f,f,16c,4p,a,a,2p,a,a,a,g,g,g,4p,g,g,g,f,f,f,p,f,f,d,c",
    "Phantom:d=4,o=5,b=225:d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,d#.,f#.,8e.,2e.,c#.,f#.,8c#.,1d#.,d#.,g#.,b.,d#.6,8c#.6,2c#.6,c#.6,f#.6,8c#.6,1d#.6,d#.6,1g#.6,8f#.6,8e.6,8d#.6,8c#.6,8b.,8a#.,8g#.,1g.,e.,e.,8d#.,1d#.",
    "Dallas:d=4,o=5,b=100:8f#6,16p,16c#6,8c#7,16p,16f#6,8a#6,16g#6,16a#6,8f#6,8c#6,8f#6,8d#7,16a#6,16a#6,8c#7",
    "Super Mario Title:d=4,o=5,b=125:8d7,8d7,8d7,8d6,8d7,8d7,8d7,8d6,2d#7,8d7,p,32p,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,16b6,16c7,b6,8a6,8d6,8a6,8a6,8a6,8d6,8a6,8a6,8a6,8d6,8a6,8a6,8a6,16a6,16b6,a6,8g6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,8d6,8b6,8b6,8b6,16a6,16b6,c7,e7,8d7,8d7,8d7,8d6,8c7,8c7,8c7,8f#6,2g6"
]


def find_song(name):
    for song in SONGS:
        song_name = song.split(":")[0]
        if song_name == name:
            return song


def random_song():
    return SONGS[machine.random(0, len(SONGS) - 1)]


def song_num(num):
    return SONGS[num % len(SONGS)]
