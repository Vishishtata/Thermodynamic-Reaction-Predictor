# Feature Breakdown – Thermodynamic Reaction Predictor

 Feature 1: Reaction Input & Parsing

    What it does:

    * Accepts a chemical reaction string (e.g., `2H2 + O2 -> 2H2O`)
    * Extracts reactants, products, and stoichiometric coefficients
    * Matches compounds to **thermodynamic data** (ΔH°, S°) from CSV/JSON

    Skills Needed:

    * Python: string parsing, regex, dictionaries
    * File handling: reading CSV/JSON
    * Optional: basic data validation
    * Modular coding: `parser.py` module

    Files / Modules:

    * `parser.py` → functions to parse reaction strings
    * `data_handler.py` → loads thermodynamic constants
    * `thermo_data.csv` → contains ΔH° and S° for compounds

    What to Implement:

    1. Function to split reactants and products
    2. Extract coefficients (default = 1 if none)
    3. Map compounds to thermodynamic values
    4. Error handling: unknown compounds, invalid syntax


 Feature 2: ΔG Calculation (C++ Engine)

    What it does:

    * Computes Gibbs free energy:
    ΔG = Σ(ΔG_products) – Σ(ΔG_reactants), where ΔG = ΔH – TΔS
    * Supports **single temperature** and **temperature sweep**
    * Handles multiple reactions if needed

    Skills Needed:

    * C++: functions, arrays/vectors, loops, basic I/O
    * C++: modular design (`dg_calculator.cpp/h`)
    * Multi-language integration: pybind11 bindings to call C++ from Python
    * Algorithmic thinking: iterate over reactants/products, handle stoichiometry

    Files / Modules:

    * `cpp_engine/dg_calculator.cpp` → core ΔG functions
    * `cpp_engine/dg_calculator.h` → function declarations
    * `cpp_engine/bindings.cpp` → pybind11 bindings
    * `tests/test_calculator.cpp` → unit tests

    What to Implement:

    1. Function to compute ΔG for given reaction
    2. Function for ΔG vs temperature sweep
    3. Function to return spontaneity prediction (ΔG <0 → spontaneous)


Feature 3: Python Integration & Visualization

    What it does:

    * Receives reaction input from frontend or terminal
    * Sends thermodynamic data to C++ engine via bindings
    * Gets ΔG results and displays:

    * Table of ΔG and spontaneity
    * Plot ΔG vs Temperature (optional interactive plot)

    Skills Needed:

    * Python: calling C++ module (pybind11)
    * Python: Matplotlib/Plotly for plots
    * Python: Pandas for data handling
    * Modular coding: `main.py` and `plotter.py`

    Files / Modules:

    * `backend/main.py` → orchestrates workflow
    * `backend/plotter.py` → generates plots
    * `backend/data_handler.py` → CSV reading
    * `cpp_engine/` → called via bindings

    What to Implement:

    1. Function to call C++ ΔG calculation
    2. Function to generate plot of ΔG vs Temperature
    3. Display ΔG table and spontaneity prediction


Feature 4: Frontend Interaction (Web)

    What it does:

    * HTML/CSS/JS interface for users
    * Input reaction, temperature, and optional multiple reactions
    * Display ΔG table and prediction
    * Display interactive ΔG vs Temperature plot
    * Optional: slider for temperature, multi-reaction comparison

    Skills Needed:

    * HTML/CSS for forms and layout
    * JS for dynamic interaction (fetch API)
    * Python: Flask/FastAPI to serve frontend & API endpoints
    * Optional: Plotly.js for interactive web plots

    Files / Modules:

    * `frontend/index.html` → main page with input form
    * `frontend/style.css` → layout, styling
    * `frontend/script.js` → calls backend API and updates plots
    * `backend/main.py` → Flask routes serving API and HTML

    What to Implement:

    1. Input form for reaction and temperature
    2. JS fetch call to backend for ΔG calculation
    3. Display prediction and ΔG table
    4. Plot ΔG vs Temperature interactively


