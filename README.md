# Parking Lot

### Requirements
Python 3.5+, pip3

### Usage

1.  Move to ```<project-dir>```, create virtual environment and then activate it as


```sh
$ cd <project-dir>
$ virtualenv -p python3 .env
$ source .env/bin/activate
```

2. Add project to ```PYTHONPATH``` as 

```sh 
$ export PYTHONPATH="$PYTHONPATH:." # . corresponds to current directory(project-dir)
```

3. Then run test cases as  

```sh
$ python -m unittest discover -s 'tests' -p '*.py'
```

4. Then run the application ```run.py``` as  
 
```sh
$ python run.py                         # Interactive mode
$ python run.py input_file_path.txt     # File mode
```

### Assumptions

 1. If `create_parking_lot` command will be executed more than once, it will overwrite/remove 
 the existing/previous information, and an empty parking lot will be created.
 
 2. Make sure `python` points to `python3` on target machine, or else make appropriate changes in bash
 scripts(available under `/bin`) .