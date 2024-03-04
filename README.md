# Intersector-Crawler

# Efficiently Assigning Numerical Values from Multiple Intersecting Polygons to Overlapping Areas: A Case Study of Austin Council Districts

This project aims to assign numerical values from multiple intersecting polygons to overlapping areas efficiently, focusing on a case study of Austin Council Districts. It solves one-to-many cardinality issues commonly encountered in Geographic Information Systems (GIS) analysis.

## Overview

The project addresses the challenge of assigning numerical codes to polygons based on the council districts in which they intersect. Traditional spatial join methods suffer from one-to-one cardinality limitations, leading to incomplete data representation. This project offers a solution to overcome these limitations by accurately identifying and assigning multiple council districts to intersecting polygons.

## Features

- **Efficient Algorithm**: Utilizes ArcPy in ArcGIS Pro to implement an efficient algorithm for identifying intersecting polygons and assigning corresponding council districts.
  
- **One-to-Many Handling**: Handles one-to-many cardinality issues by populating a new TEXT field with comma-separated lists of council district numbers for each polygon.

- **Documentation**: Provides detailed documentation on the workflow, solution components, and potential optimizations.

  ## Problem to be solved!
  ![image](https://github.com/Milad84/Intersector-Crawl/assets/38597478/62cea75a-1aa6-4398-885a-93f3db70c5d1)

--The highlighted polygon with a yellow outline is actually intersected by two council districts in purple and orange. However, in the attribute table, only one number is assigned, coming from whichever district was reached by the code in the background of Add Spatial Join. This is the famous case of one-to-one cardinality in GIS. What I need is a one-to-many handling mentioning both Council Districts as a value (e.g., 9, 3)

## Getting Started

To use the script in your ArcGIS Pro environment, follow these steps:

1. Create a new TEXT field in the polygon layer to store the Council District numbers.

2. Open the Field Calculator in ArcGIS Pro and set the expression to:

get_council_districts(!Shape!)

Adjust the name of the fields based on your needs and run the calculation to populate the new field with the Council District numbers for each polygon.

## Result
![image](https://github.com/Milad84/Intersector-Crawl/assets/38597478/e1fb87f4-197f-4433-a386-9fc641bfe783)

--In front of the field called “District” there are two numbers separated by comma (4,7) standing for the two Council Districts intersecting the highlighted polygon.

![image](https://github.com/Milad84/Intersector-Crawl/assets/38597478/186184a9-8d87-4d54-942e-28cac38e8eec)

## Slowness Optimization and improvements!

The project discusses potential factors contributing to slow performance, such as data size, complexity of geometries, intersect analysis, and spatial indexing. It offers insights into optimizing the code and improving processing efficiency. I hope to improve the speed.

## Contributing

Contributions to the project are welcome! Feel free to open an issue or submit a pull request if you have suggestions for improvements, optimizations, or new features.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the [City of Austin](https://austintexas.gov/) for providing the dataset used in this case study.
- Inspired by the need for efficient spatial analysis in GIS applications.

## Contact

For questions, feedback, or inquiries about the project, please contact [Milad Korde](mailto:milad.kordeh@gmail.com).

