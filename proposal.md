# Song Generator

## Repository Link
  [Link](https://github.com/emnetdar/Song-Generator)

## Description
  This program will take and ask for user input and compile all inputs to output a song
  for the user. If the user does not like the song, or would simply like another, the 
  program will be able to looped until the user quits.

## Features
  - Customizable background color
    - A guaranteed question for input is the user's favorite color, which will then be used to
      change the background color of the window. The program will then ask the user if they
      like the color, and if not, the color will be set back to black. Pygame will be
      utilized throughout the entirety of this program, but especially here for the screen color.
  - External link for song output
    - When a song is given to the user, a YouTube link for the song will be output as well
    for easy access. I assume that this can be done within PyGame, or with a separate output
    that the user can copy
  - Album output for song
    - Along with the song and link, an image of the song's respective album cover will be given
    as well. The image will be compressed and pixelated using Image/ImageFilter.
  - Randomized text blurbs
    - The program will have small, separate pieces of text from the input inquiries, and to
    avoid repetitive text, the program will pull from a list of text options. The randomizing
    will be done by the random module, specifically randrange.

## Challenges
  - Being able to properly add a clickable link to the program is something I'd have to learn,
  if possible at all.
  - I'd have to research to see if I can even pixelate the image with ImageFilter, or if it'd
  be added in as already pixelated.

## Outcomes
  - Ideal Outcome:
    - The ideal program would have every feature listed before, along with a possible way to
    resize the window so it isn't only set to windowed/fullscreen.

  - Minimal Viable Outcome:
    - At the bare minimum, the program should be able to take a few user inputs and output a song
    and album image in order to serve its base purpose. It should also have the randomized text
    at least, since that feature may be easier to implement than others.


## Milestones

- Week 1
  1. Research/learn adding link and ImageFilter capabilities
  2. Start on the base for user input questions

- Week 2
  1. Finish choosing and implementing user input questions
  2. Begin adding randomized song/image output and randomized text blurbs

- Week 3 (Final)
  1. Finalize custom features (link and background color change)
  2. Verify looping and quitting functions work before final submission
