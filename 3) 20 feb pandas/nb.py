# Creating Jupyter notebooks with sample content for each topic

import json

notebooks = {
    "handling_missing_values.ipynb":{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Handling Missing Values in Pandas (Detailed)\n",
                "\n",
                "Missing data can affect analysis. In this notebook, we will cover:\n",
                "- Identifying missing values\n",
                "- Removing missing values\n",
                "- Filling missing values using various strategies\n",
                "- Advanced methods like interpolation and forward fill"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "\n",
                "# Create a sample DataFrame with missing values\n",
                "data = {\n",
                "    'A': [1, 2, np.nan, 4, 5],\n",
                "    'B': [np.nan, 2, 3, np.nan, 5],\n",
                "    'C': [1, np.nan, np.nan, 4, 5]\n",
                "}\n",
                "df = pd.DataFrame(data)\n",
                "print('Original DataFrame:')\n",
                "print(df)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Identifying Missing Values\n",
                "Use `isnull()`, `sum()`, or `info()` to get an overview of missing data."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "print('\\nMissing values (isnull):')\n",
                "print(df.isnull())\n",
                "\n",
                "print('\\nCount of missing values per column:')\n",
                "print(df.isnull().sum())\n",
                "\n",
                "print('\\nDataFrame info:')\n",
                "df.info()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Removing Missing Values\n",
                "Use `dropna()` to remove rows or columns with missing values. Be cautious as this might remove useful data."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "df_dropna = df.dropna()\n",
                "print('\\nDataFrame after dropna():')\n",
                "print(df_dropna)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Filling Missing Values\n",
                "There are several strategies:\n",
                "- **Constant value:** Use `fillna(0)`\n",
                "- **Column mean:** Use `fillna(df.mean())`\n",
                "- **Forward fill:** Use `fillna(method='ffill')`\n",
                "- **Interpolation:** Use `interpolate()` for continuous data"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Fill with a constant value\n",
                "df_fill_const = df.fillna(0)\n",
                "print('\\nDataFrame after fillna(0):')\n",
                "print(df_fill_const)\n",
                "\n",
                "# Fill with the column mean\n",
                "df_fill_mean = df.fillna(df.mean())\n",
                "print('\\nDataFrame after filling with mean:')\n",
                "print(df_fill_mean)\n",
                "\n",
                "# Forward fill\n",
                "df_ffill = df.fillna(method='ffill')\n",
                "print('\\nDataFrame after forward fill:')\n",
                "print(df_ffill)\n",
                "\n",
                "# Interpolation\n",
                "df_interp = df.interpolate()\n",
                "print('\\nDataFrame after interpolation:')\n",
                "print(df_interp)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Summary\n",
                "Choose the method based on your data. Dropping data loses information; filling data preserves it but might introduce bias."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
},
    
    "filtering_data.ipynb":{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Filtering Data in Pandas (Detailed)\n",
                "\n",
                "Filtering helps select specific rows based on conditions. In this notebook, we cover:\n",
                "- Boolean indexing\n",
                "- Using `loc[]`\n",
                "- Using `query()`\n",
                "- Combining multiple conditions"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "import pandas as pd\n\n",
                "# Create a sample DataFrame\n",
                "data = {\n",
                "    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],\n",
                "    'Age': [25, 30, 35, 40, 45],\n",
                "    'Salary': [50000, 60000, 70000, 80000, 90000],\n",
                "    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance']\n",
                "}\n",
                "df = pd.DataFrame(data)\n",
                "print('Original DataFrame:')\n",
                "print(df)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Filtering Using Boolean Indexing\n",
                "Select rows where conditions are met using boolean expressions."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Filter employees older than 30\n",
                "filtered_bool = df['Age'] > 30\n",
                "filtered_df = df[filtered_bool]\n",
                "print('\\nEmployees older than 30 (Boolean Indexing):')\n",
                "print(filtered_df)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Filtering Using loc[]\n",
                "The `loc[]` function filters rows based on label conditions."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "filtered_loc = df.loc[df['Department'] == 'IT']\n",
                "print('\\nEmployees in IT Department (loc[]):')\n",
                "print(filtered_loc)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Filtering Using query()\n",
                "The `query()` method allows filtering with a string expression."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "filtered_query = df.query('Salary >= 70000')\n",
                "print('\\nEmployees with Salary >= 70000 (query()):')\n",
                "print(filtered_query)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Combining Multiple Conditions\n",
                "Combine conditions using `&` (AND) or `|` (OR). Use parentheses to group conditions."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Employees older than 30 and in IT department\n",
                "combined_filter = df[(df['Age'] > 30) & (df['Department'] == 'IT')]\n",
                "print('\\nEmployees older than 30 and in IT:')\n",
                "print(combined_filter)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Summary\n",
                "Filtering is crucial for data analysis. Use the method that offers clarity and meets your needs."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
},
    "grouping_aggregation.ipynb":{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Grouping & Aggregation in Pandas (Detailed)\n",
                "\n",
                "This notebook demonstrates how to group data by one or more keys and perform aggregations to extract insights. Topics include:\n",
                "- Grouping using `groupby()`\n",
                "- Aggregation functions (e.g., `mean`, `sum`, `count`)\n",
                "- Applying multiple and custom aggregations"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "import pandas as pd\n\n",
                "# Create a sample DataFrame\n",
                "data = {\n",
                "    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT'],\n",
                "    'Salary': [50000, 70000, 80000, 55000, 90000, 95000, 72000],\n",
                "    'Experience': [2, 5, 7, 3, 10, 12, 6]\n",
                "}\n",
                "df = pd.DataFrame(data)\n",
                "print('Original DataFrame:')\n",
                "print(df)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Grouping Data\n",
                "Group the DataFrame by the 'Department' column."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "grouped = df.groupby('Department')\n",
                "print('\\nGrouped Data:')\n",
                "for name, group in grouped:\n",
                "    print(f'\\n{name} group:')\n",
                "    print(group)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Aggregation\n",
                "Apply multiple aggregation functions using `agg()`. You can use built-in functions or custom lambda functions."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Multiple aggregations\n",
                "agg_df = grouped.agg({\n",
                "    'Salary': ['mean', 'sum', 'count'],\n",
                "    'Experience': 'mean'\n",
                "})\n",
                "print('\\nAggregated Data:')\n",
                "print(agg_df)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Custom Aggregations\n",
                "Calculate the salary range (max - min) for each department."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "salary_range = grouped['Salary'].agg(lambda x: x.max() - x.min())\n",
                "print('\\nSalary Range per Department:')\n",
                "print(salary_range)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Summary\n",
                "Grouping and aggregation simplify analysis by summarizing key metrics. Experiment with various aggregation methods to explore your data."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
},
    "merging_joining.ipynb":{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Merging & Joining Data in Pandas (Detailed)\n",
                "\n",
                "In this notebook, we cover methods to combine multiple datasets. Topics include:\n",
                "- Merging DataFrames using `merge()` with different join types\n",
                "- Concatenating DataFrames using `concat()`\n",
                "- Understanding inner, left, right, and outer joins"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "import pandas as pd\n\n",
                "# Create sample DataFrames\n",
                "df1 = pd.DataFrame({\n",
                "    'ID': [1, 2, 3, 4],\n",
                "    'Name': ['Alice', 'Bob', 'Charlie', 'David']\n",
                "})\n",
                "\n",
                "df2 = pd.DataFrame({\n",
                "    'ID': [3, 4, 5, 6],\n",
                "    'Score': [85, 90, 95, 80]\n",
                "})\n",
                "\n",
                "print('DataFrame 1:')\n",
                "print(df1)\n",
                "print('\\nDataFrame 2:')\n",
                "print(df2)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Merging DataFrames with `merge()`\n",
                "Merge DataFrames on a common key. Explore different join types."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Inner join: only matching IDs\n",
                "inner_merge = pd.merge(df1, df2, on='ID', how='inner')\n",
                "print('\\nInner Merge:')\n",
                "print(inner_merge)\n",
                "\n",
                "# Left join: all rows from df1\n",
                "left_merge = pd.merge(df1, df2, on='ID', how='left')\n",
                "print('\\nLeft Merge:')\n",
                "print(left_merge)\n",
                "\n",
                "# Outer join: all IDs from both DataFrames\n",
                "outer_merge = pd.merge(df1, df2, on='ID', how='outer')\n",
                "print('\\nOuter Merge:')\n",
                "print(outer_merge)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Concatenating DataFrames with `concat()`\n",
                "Stack DataFrames vertically or horizontally."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "source": [
                "# Concatenate vertically (axis=0)\n",
                "concat_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)\n",
                "print('\\nConcatenated DataFrame (vertical):')\n",
                "print(concat_vertical)\n",
                "\n",
                "# Concatenate horizontally (axis=1)\n",
                "concat_horizontal = pd.concat([df1, df2], axis=1)\n",
                "print('\\nConcatenated DataFrame (horizontal):')\n",
                "print(concat_horizontal)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Summary\n",
                "Merging and joining are key to combining datasets from various sources. Choose the method that fits your data structure and analysis needs."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.x"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 2
},
}

# Save each notebook as a .ipynb file
for filename, content in notebooks.items():
    with open(f"./tut-codes/-2) notebooks/1) pandas/{filename}", "w") as f:
        json.dump(content, f)
