# SpaceNinjaMF - a pygame

### Development Setup

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install --upgrade pip
# if on macos with m1 chip:
ARCHFLAGS="-arch arm64" pip3 install pygame  --compile --force-reinstall --no-cache-dir
# else:
# pip3 install pygame
python main.py # to run the game
```

### Organization

- register all colors, events, & groups in the assets/utils/<colors, events, groups>.py files
- assets/utils/helpers is for classless functions, currently we blit all the things to the window and check for collisions here
- assets/utils/settings is a heavyweight class that basically abstracts away all the boilerplate, including initializing pygame itself

- image assets go in assets/images

- assets/classes is for enemies, players, items classes


### Adding a feature

A few things need to happen to add something to the game, generally speaking - mileage may vary.
1. Add a class, the class should have an update() function that kills the object as it leaves the screen, you could definitely mess with the direction the thing moves here. These classes are really just surfaces that move.
2. Register a group for your class - see assets/utils/groups
3. Register an event - see assets/utils/events
4. Import your event and group to main
5. Set a timer for your event in main
6. Create an event handler for your event in the game loop, for this game it usually just creates a new object and adds that object to its own custom group and the all_sprites group.
7. Add some sort of funcitonality on a collision - see assets/utils/helpers - check_collisions()

