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
