# PyIdea - Command Line Notes

PyIdea is a Python implementation of the original app [Idea](https://github.com/IonicaBizau/idea). Like Idea before it, PyIdea lets the user jot down short notes when inspiration strikes, and remove them when no longer needed.

This project was originally created for personal use, when I wanted to use the original app Idea but didn't want to install the dependencies. Since I already had a working Python environment, I decided to write a minimal interpretation of the app, but for Python.

Modules used are Click for easy command line arguments and argument testing, and PeeWee for a simpler absctraction from SQLite. 

### Installing

Installation is best done by Pip after cloning this repo. In addition, I always suggest installing inside a virtual environment, to avoid a cluttered system.

```
$ mkdir pyidea && cd pyidea/
$ git clone https://github.com/madelyneriksen/pyidea .
$ python setup.py install
```

We can check if it's working as intended now:

```
$ pyidea --help
$ pyidea --new "My Awesome Idea"
$ pyidea --show
```

All ideas are stored in the user's home folder, as '.ideas.db'. On most *nix systems, that will be ~/.ideas.db.

## Testing

Testing is done with py.test. After cloning the repo, run the following commands in the project root:

```
$ pip install pytest
$ pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Idea App by [IonicaBizau](https://github.com/IonicaBizau/idea)


