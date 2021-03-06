# Readme

[![Build Status](https://travis-ci.org/alexanderjulo/triptan.svg?branch=master)](https://travis-ci.org/alexanderjulo/triptan)

You need migrations that are not bound to an SQL database? You distribute code to multiple separate environments and want to run migrations at certain points? triptan is for you! It supports multiple datastores out of the box and you can easily add your own, if it is not supported yet.

Supported datastores:

- redis
- file based

## Applications

### Distributed development environment
If you i.e. distribute development environments amongst your engineers and change something about this environment, i.e. modify a config file format, where the config file is not checked in, you can easily add a migration to triptan that will convert the config files of all your engineers. No asking for directions anymore.

### Non-SQL Persistent storage
You store data but it is not in SQL but instead in elasticsearch, mongo, redis or anywhere else? You modified the way something is stored or need to re-run some initialization? No problem. Just add a new revision to triptan! You can add `triptan migrate head` to your deploy script and whenever there are new migrations, triptan will run all the new revisions for you in the correct order so that nothing gets lost.

## Setup
Simply install triptan via pip or your setup.py.

Go to your project directory and run:

```bash
triptan init # initialize revisions directory & config
triptan revision # create first revision
cat revisions/revision-000.py # show empty first revision
```

Then modify `revisions/revision-000.py` to contain your code in the up and down functions. Afterwards run `triptan migrate head`, which will run the code contained in the `up` function of the migration.

## Roadmap

- [ ] Add support for elasticsearch as a storage
- [ ] Write documentation
- [x] Add tests
- [ ] increase test coverage
- [ ] Clean up code
- [x] Publish to PyPi
- [ ] Switch to proper versioning instead of fixed numbers (and allow merges)
