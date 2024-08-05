# NetBlade

## How Does This Thing Work:

For the game Blade Of Darkness, rollback last stable version from Steam. Or the specific files that I have on my PC. At least on my PC works fine.

First, run the python script on the root game directory, then, in the game you will suposed to type the IP address inside the option "Multiplayer" in the main menu. Then, whenever the map is the current specified in the server, the game trying to connect to that server will load that map.

## Done:
- Project uploaded to GitHub.
- Configured all things.
- Hide nametags when the nametag is behind the camera (Working fine)
- Check the drop and throw event (Working well)
- Find out why the start of a map is so slow. (It was a crash caused by a corrupted file. It was fixed reinstalling the base game)
- Multiplayer menu
- Inventory synchronization
- Locks and Levers synchronization

## Working on:
- 

## TODO:
- Traps synchronization
- When a player dies, what to do now?
  1. Give the player the possibility to respawn in the beginning. (Problems with continuity of the map)
  2. Give the players the possibility to revive the dying player. (Hard to implement)
  3. Restart the map for all players. (Easy to implement)
- Synch enemies (A hard task)
- When a player completes the level, what to do now?
- Inventory persistance
