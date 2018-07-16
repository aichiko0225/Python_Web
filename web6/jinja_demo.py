from jinja2 import Environment, FileSystemLoader
import os.path

path = '{}/templates/'.format(os.path.dirname(__file__))

loader = FileSystemLoader(path)

env = Environment(loader=loader)

template = env.get_template('demo.html')

ns = list(range(3))
ns = [
    {
        "name": 'ash',
        "id": 1
    },
    {
        "name": 'ash66',
        "id": 2
    },
    {
        "name": 'ash77',
        "id": 3
    }
]

t = template.render(name='ash', numbers=ns, users=ns)

print(t)
