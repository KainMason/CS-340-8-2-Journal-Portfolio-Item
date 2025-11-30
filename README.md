

# CS-340 Grazioso Salvare Rescue Dashboard – Enhanced Version  
**Author:** Kain Mason  
**Course:** CS 340 – Client/Server Development  
**Project:** Full Stack Dashboard Application (Enhanced for CS-499 Capstone)

---

## Project Overview
This project implements a functional, full-stack dashboard application for **Grazioso Salvare**, a company specializing in identifying and training rescue dogs. The dashboard connects to a **MongoDB Atlas** database using a custom Python CRUD module (`animal_Shelter.py`) and presents data interactively using **Dash by Plotly**.

As part of my CS-499 capstone, I enhanced this artifact by improving query structure, strengthening input validation, standardizing return values, and expanding documentation so the system behaves more reliably and professionally.

Users can filter dogs by rescue category, review key attributes through a searchable data table, visualize outcome metrics, and view geographic locations using integrated map components.

---

## Technologies Used
- **Python 3.x**
- **Dash / JupyterDash** – interactive web dashboard  
- **Dash Leaflet** – map rendering for latitude/longitude points  
- **Pandas & Plotly Express** – data manipulation and visualization  
- **MongoDB Atlas + PyMongo** – cloud database and query engine  

---

## Authentication Setup
The dashboard authenticates with MongoDB using the user credentials created during CS-340.

Connection example (inside CRUD module):

```python
self.client = MongoClient(
    f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
)
```


-----------------------------------------------------------------------------------------------------------------------------
## Enhanced CRUD Module Overview

The animal_Shelter.py file defines the AnimalShelter class used to interact with MongoDB.

Core Methods

create(data) – Inserts new animal documents

read(query) – Retrieves records based on filtering criteria

update(query, new_values) – Modifies existing documents

delete(query) – Removes matching documents

### Enhancements Made in CS-499

✔ Refactored query structures using consistent MongoDB operators ($and, $regex, $in)
✔ Added input validation to prevent malformed queries
✔ Improved error handling to avoid dashboard crashes
✔ Standardized return formats for cleaner Dash integrations
✔ Expanded inline documentation to describe each operation clearly

## Dashboard Functionality
### Filter Options

Water Rescue

Mountain/Wilderness Rescue

Disaster / Individual Tracking

Reset (clear filters)

### Data Table

Displays live records from MongoDB

Supports sorting, filtering, and row selection

Includes a custom computed rescue_type column

Handles missing or unexpected values consistently (enhancement)

### Map Visualization

Uses Dash Leaflet to pinpoint selected animal locations

Centers automatically on the latitude/longitude from the dataset

Improved handling for missing or malformed coordinates (enhancement)

Outcome Chart

Bar chart visualizing outcome types (Adopted, Transferred, etc.)

Updated to handle new return formats from the enhanced CRUD functions

### Branding & Layout

Includes the Grazioso Salvare logo

Includes student identification (Kain Mason)

Layout formatting improved for consistency

## Enhancements Completed for CS-499
### Database & Query Enhancements

Cleaned and standardized MongoDB query logic

Removed redundant or inconsistent filtering patterns

Added safer handling of empty queries and invalid inputs

### Security & Validation Improvements

Validated search parameters before executing queries

Added safeguards against malformed input

Ensured predictable outputs even when data is missing

### Documentation & Clarity

Expanded README with setup, usage, and schema overview

Added better comments in CRUD module explaining operations

Clarified expected return structures for Dash callbacks

### Stability Fixes

Prevented callback failures due to inconsistent data

Improved table/map/chart synchronization

These enhancements significantly improve the reliability, professional quality, and clarity of the artifact.



File Structure
├── Project2.ipynb               # Dashboard UI + callbacks
├── animal_Shelter.py            # Enhanced CRUD module
├── photo.png                    # Grazioso Salvare branding
└── README.md                    # Project documentation (this file)

## How to Run the Dashboard

Ensure your MongoDB Atlas cluster contains the AAC dataset

Open Project2.ipynb in Jupyter Notebook or Apporto

Run all cells to launch the Dashboard

The Dash application will open in a browser tab or inline depending on the environment.
