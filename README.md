<p>
<h4 align="center">4Geeks Academy</h4>
<h2 align="center" style="margin: 0">StarWars blog database</h2>
<h3 align="center" style="margin-top: 0">Keili Rosales</h3>
</p>

## Objective

The objective of this exercise is to create a Star Wars blog data model that allows the user to log in, add characters and planets, as well as mark the ones they want as favorites.

The project is using the Python SQLAlchemy library to generate the database and contains the following tables:

**Users table**
Contains important information about each of the users, such as a username, email and password. Additionally, in this table a column is added to store the favorites of each blog user with a one-to-many relationship with the Favorites table.

**Planet Table**
Stores the value for the selected planet.

**Character table**
Stores the value for the selected character.

**Favorites Table**
Stores the values for username, planet name or character name. 

The tables can be viewed in the src/models.py file.

## Application

1. Enter the environment `$ pipenv shell`
2. Install all dependencies `$ pipenv install`
3. Generate the diagram as many times as necessary `$ python src/models.py`
4. Open the diagram.png file to see the UML diagram.

## Technologies

- SQLAlchemy
- Flask
- Python

## Contributions

I'd love to get your appreciation or report on the code at https://github.com/keikeka/Data-Modeling-a-StarWars-Blog

Thank you so much!