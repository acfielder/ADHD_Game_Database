# About this Project

This repository contains optional, but important, components that add on to the [ADHD Game](https://github.com/acfielder/ADHD_Game) project. This database and its related components were added to track participants progress across all of the mini-games and their trained executive functions so that experimenters and psych professionals have access to all relevant data. 

Alongside the MySql schema and the flask server that connects the game and database, there is also a Google Sheets UI that utilizes the database and Apps Script to create visuals of collected data.

[Google Sheets UI](https://docs.google.com/spreadsheets/d/1tP75X27D79ZtHo5tIW8SoxgwUMd-LQuEBdsJ6SGG81s/edit?usp=sharing)

# System Design

[UML Component Diagram](https://drive.google.com/file/d/1YOw1Kju2w-ld6_wyqusGffQ8ynLHdf1M/view?usp=sharing)

[Database Poster](DatabasePoster.pdf)

# Getting Started

The database schema can be used in a MySQL database through a tool like DBeaver. The flask server should be started to ensure connecting to game, and database credentials updated to current database. Created SQL queries in Sheets UI must be updated with current database credentials as well.
