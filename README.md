# Sparrow Loader example

This example shows how to prepare basic data for Sparrow import.
You will need a Python installation (version `3.9` or above)
and an environment to run Jupyter notebooks (e.g., the `jupyter` CLI,
JupyterLab, or Visual Studio Code).

Before running the notebook, you need to install the `sparrow-loader`
Python module, as such:

```
pip install sparrow-loader
```

You can test that everything installed correctly by running the
`sparrow-loader` command.

## Loader schemas

"Loader schemas" are the basic recipes for building JSON objects to
feed to Sparrow.

You can run this command to show loader schemas. It's a bit overwhelming, but we're working on it.

```
sparrow-loader show-schemas
```

You can show a specific schema by running

```
sparrow-loader show-schema sample
```

## Validating data

Validating complex data is easier in Python, so head over to the
notebook!

## Importing data into Sparrow's database

Right now, to easily import data into Sparrow, you must be running it on
your own machine. The [Sparrow installation guide](https://sparrow-data.org/docs/getting-started)
can help with this, but briefly, the steps are:

1. Install [Docker](https://docker.com) and download the Sparrow executable.
   The easiest way is to use the following Terminal command:
   ```
   bash -c "$(curl -fsSL https://sparrow-data.org/get-sparrow.sh)"
   ```
2. Enter the `loader-test-lab` directory to enter the lab context. Running the `sparrow` command should show the name "Loader test lab"
3. You can then run `sparrow up` to start Sparrow (this command can be exited with `Ctrl+C` after the server starts).
4. In order to import data, you must run the `sparrow create-user` command to create an admin user.
5. Finally, navigate to `http://localhost:5002` to load the Sparrow web application.

## Building more serious lab workflows

Most labs have sophisticated processes to manage legacy data and the collection and reduction of new data.
Integration with these pipelines requires the development and maintenance of ingestion pipelines
that work with different types of geochemical data. Typically, these import tools are written in Python.
Lab configurations are often version-controlled and stored on GitHub, which facilitates development within
the lab and sharing within the community.

Here are some example pipelines:

- [**WiscAr** lab configuration](https://github.com/EarthCubeGeochron/Sparrow-WiscAr), which runs
  the [**WiscAr** argon lab's Sparrow website](https://wiscar-sparrow.geoscience.wisc.edu/).
