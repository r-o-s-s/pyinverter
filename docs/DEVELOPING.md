# Developing on pyinverter

The pyinverter project is manged using [Poetry](https://python-poetry.org/). You will need to have it installed before you can work on this project. I would also recommend using the [VSCode](https://code.visualstudio.com/) IDE.

## Getting the source code

The source code can be downloaded from [GitHub](https://github.com/r-o-s-s/pyinverter).

```bash
git clone https://github.com/r-o-s-s/pyinverter.git
```

## Setting up the environment

The devlopment environment can be created by using the `poetry install` command from the command line. You will have to be in the pyinverter project directory for it to work. Optionally you can also create a `poetry.toml` file to contain any local project settings.

Once you have run the `poetry install` command, which can take a few seconds to run, you should have everything you need to work on the pyinverter project!

# Code styles

## Naming conventions

The protocols are named after their response to the 'ID' command.