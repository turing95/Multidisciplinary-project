# Multidisciplinary Project

Urban-path classification project developed from product/design exploration to implementation.

## Overview
This repository combines data analysis, geospatial processing, and API prototyping around tourism-oriented path recommendation.

## Main Components
- `Design Thinking/`: project report and presentation material
- `Implementation/`: notebooks, geospatial assets, scripts, and API code
- `Implementation/api/`: Swagger/Connexion-based API service
- `Implementation/shapefiles/`: geospatial layers used for path analysis

## What Is Included
- Data preparation and analysis scripts (`calc_speed.py`, `speed_calculator.py`, `sparsity_matrix.py`)
- Exploratory notebooks and map exports
- API prototype for user/path recommendation logic

## Run the API Prototype
From `Implementation/api`:

```bash
pip install -r requirements.txt
python -m swagger_server
```

Then open:
- API UI: `http://localhost:8080/api/v1/ui/`
- Swagger spec: `http://localhost:8080/api/v1/swagger.json`

## Notes
- This is a multidisciplinary academic-style project repository.
- Large data artifacts are included because they are part of the original implementation context.
