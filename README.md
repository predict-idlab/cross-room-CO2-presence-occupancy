# 🏢 Cross-Room CO<sub>2</sub>-based Presence Detection for Occupancy Profiling

Codebase and dataset for the paper:
> **Cross-Room CO<sub>2</sub>-based Presence Detection for Occupancy Profiling**</br>
> Jelle Vanhaeverbeke, Emiel Deprost, Steven Verstockt and Sofie Van Hoecke

## Data
The repository contains data from three offices:

* `data/office/200.009.parquet` referred to as *office L1* in the paper
* `data/office/200.010.parquet` referred to as *office L2* in the paper
* `data/office/200.024.parquet` referred to as *office S3* in the paper

These parquet files can be easily loaded as Pandas dataframe and include CO<sub>2</sub> and presence data. Please note that the data from *home 1* was collected in collaboration with a private company and is not available for public distribution.

## Code
The repository includes the following notebooks for data exploration, presence detection and occupancy profiling:

* `notebooks/1-data.ipynb` explores and visualizes the dataset
* `notebooks/2-single-room.ipynb` performs and reports the results of the single-room presence detection experiments
* `notebooks/3-cross-room.ipynb` performs and reports the results of the cross-room presence detection experiments
* `notebooks/4-occupancy-profiling.ipynb` demonstrates and validates two occupancy profiling techniques

Additionally, the `src` folder contains supporting functions for data loading and processing.

## Environment Setup
To set up the environment for this codebase, follow these steps:

1. Create a new Conda environment: `conda create --name myenv`
2. Activate the environment: `conda activate myenv`
3. Install the dependencies from the YAML file: `conda env update --file environment.yml`

Remember to replace `myenv` with your preferred environment name.

## Licenses
* The data is licensed under the terms of the [CC BY-NC-SA license](LICENSE_DATA).
* The code is licensed under the terms of the [MIT license](LICENSE_CODE).
