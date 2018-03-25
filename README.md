# pylily-music
Python code to generate music patterns (generally exercises in all keys) with output in lilypond.

The python "package" is lilypy which consists of the functions pattern() accidental(), scale(), mode(), and chord().    They could be turned into methods of a class (a Pattern class), but that's a task for another day.

Examples of sample output are in pat1.pdf, pat2.pdf, and pat3.pdf. The "driver" or "client" code is in pat1.py, pat2.py, and pat3.py, espectively. These files contain the actual patterns used (expressed in scale degrees) with a list of keys to transpose the patterns to.

TODO:

- Make it so less expertise is needed to construct the driver files.
- Explore the potential advantage of turning the functions into methods of a class.
