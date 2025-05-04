# mem_access_nisq

**Memory Access Patterns of NISQ Applications**

## Overview

This repository explores the memory access patterns of applications designed for Noisy Intermediate-Scale Quantum (NISQ) devices. Understanding these patterns is crucial for improving compiler efficiency, enhancing the performance of quantum software on current and near-future quantum hardware and uncover potential security vulnerabilities.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Jupyter Notebook

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/teotro/mem_access_nisq.git
   cd mem_access_nisq

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt


Navigate to the src/ directory and open the desired notebook.

## Usage

The notebooks in this repository analyze memory access patterns in NISQ applications. By running these notebooks, you can:

    Visualize memory reference timestamps over time.

    Identify algorithms based on that memory references.

    Explore optimization strategies for memory management in quantum applications.