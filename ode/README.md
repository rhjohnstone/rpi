# Play _Ode to Joy_ on a Raspberry Pi

The ultimate plan, which I might never get around to: connect the 5 notes in OtJ to individual buttons, connected to the RPi in parallel.
In particular, I wanted to use jelly babies as in the classic [burping jelly baby project](https://projects.raspberrypi.org/en/projects/burping-jelly-baby/).
However, after completing that project (video [here](https://youtu.be/byJUbMDrTLQ)), I decided never to use sweets again.
So I'll probably just make normal buttons out of tinfoil or something.

Currently, it just plays the notes in the correct order, with no thought given to speed or lengths or rests.
But once the notes are connected to buttons, it will be easier to play each note for its correct length.

I originally wanted to use `pygame.midi` to play the notes, but I couldn't get that to work.
So instead, I just downloaded recordings of a piano playing each note from [here](https://freesound.org/people/pinkyfinger/packs/4409/), and play the relevant files when needed.
Even though I could download them for free, I had to register an account there, so I'm not sure if I can share the files in this repo.
Therefore, to be safe, I have removed them from the repo.
