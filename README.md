# extract-exercises

Python code provided by Toby Hodges from The Carpentries ⭐ (and slightly modified by myself) to extract exercises for lessons in the Carpentries Workbench format from episode text.
The code writes the result to `stdout`.

Original code by Toby:

```python
from sys import argv, stdout

episode_files = argv[:]


for episode in episode_files:
    title = ''
    exercise = False
    with open(episode, 'r') as infh:
        for line in infh.readlines():
            if line.startswith('title: '):
                _, title = line.split(': ')
                stdout.write(f'# {title}')
            elif line.strip().endswith(':::  challenge'):
                exercise = True
            else:
                if line.strip().endswith(':::') or line.strip().endswith(':::  solution'):
                    exercise = False
                elif exercise:
                    stdout.write(line)
```

## Execution

Copy the Python script into the `episodes` folder of the lesson.

Run as: 
`$ python3 extract_exercises.py *.md > exercises.md` from the `episodes` folder.
