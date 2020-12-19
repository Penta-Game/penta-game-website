# Pentagame Website

The content & assets used for pentagame.cobalt.rocks

Before using this in any other project please contact the pentagame software team

> The website at `pentagame.cobalt.rocks` is hosted by [Cobalt](https:/cobalt.rocks) and isn't associated with the pentagame brand.

## Running locally

_Warning: You will need a system with bash and [GNU make](https://www.gnu.org/software/make/). For Windows I recommend [WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10)_

You need [python 3](https://www.python.org/) with [python3-pip](https://pypi.org/project/pip/) and [npm](https://www.npmjs.com/).

I recommend this installation guide for python and pip: [Stackoverflow - How to install pip with python3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3).

For npm [this guide](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) will work well too.

Just descend into `theme/static/`and run `npm i`.

> Executing `npm i` installs all JS dependencies including [Bootstrap 5](https://blog.getbootstrap.com/2020/06/16/bootstrap-5-alpha/) and all packaging utilities

> Before continuing I recommend [setting up a virtual environment](https://docs.python.org/3/library/venv.html) to keep your python installation clean

Continue with ascending back and running `python3 -m pip install -r requirements.txt`

> Executing `python3 -m pip install -r requirements.txt` will install all python dependencies including [pelican](https://blog.getpelican.com/)

> Please ensure [GNU Make](https://www.gnu.org/software/make/) is installed, before continuing. [Similar Question & Answer on StackExchange](https://askubuntu.com/questions/161104/how-do-i-install-make)

Now you can either start a local development server (under `https://localhost:8000`) with `make devserver` or create publish ready html files and assets with `make publish`.
