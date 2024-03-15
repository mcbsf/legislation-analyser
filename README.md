## Summary
* [Introduction](#introduction)
* [Design Patterns](#architecture)
* [Dependencies](#dependencies)
* [How to execute](#how-to-execute)
* [Write up](#write-up)


## Introduction
This repository is an simple full stack solution that analyse bills and legislators.

Given 4 input files(bills.csv, legislators.csv, vote_results.csv and votes.csv) through UI, the code generates 2 tables

## Design Pattern

I choosed django and TailwindCSS as tech stacks, django due to the sugestion of the exam and Tailwind to save develop time(better explained in questions.md file)
Since it's 2 simple analysis, I choosed to keep the folder structure simple as well. I basically kept the django default structure, creating a templates folder at 'my_project/templates' and the TailwindCSS folder at 'theme'. As the code grows(not expected), the architecture may change as well.


The my_app folder, inside my_project, is separated in 3 main classes: parsers, analysers and models. parsers and analysers are in folders, models(since very simple) are in a single file called "models.py" Outside the folders there's only config and documentation files.

## Dependencies
The OS is ubuntu 20.04, the Python version is 3.10. The Node version is 18.14

## How to execute
1. Clone the repository

```
git clone git@github.com:mcbsf/legislation-analyser.git
```

2. Create environment

```
pip install virtualenv
cd legislation-bills-analyser
virtualenv venv
```

3. Activate environment
```
source venv/bin/activate
```

4. Install depedencies

```
pip install -r requirements.txt
```

5. Install tailwind dependencies

```
python manage.py tailwind install

```

6. Start tailwind server(dont close the terminal window)

```
python manage.py tailwind start

```

7. In other terminal window, start the django server
```
cd my_project
python manage.py runserver
```

6. Access the UI Interface

Go to localhost:8000 on your web browser(currently using chrome so far)
