# Future Value Calculator

This is a simple web-based calculator that helps you determine the future value of an investment based on the initial investment, annual contribution, number of years, and interest rate.

## How to Use

1. Open the [Future Value Calculator](https://githubnext.github.io/workspace-blank/) in your web browser.
2. Enter the initial investment amount in the "Initial Investment" field.
3. Enter the annual contribution amount in the "Annual Contribution" field.
4. Enter the number of years you plan to invest in the "Years" field.
5. Enter the expected annual interest rate (in percentage) in the "Interest Rate (%)" field.
6. Click the "Calculate" button.
7. The future value of your investment will be displayed below the button.

## Example

If you start with an initial investment of $1,000, contribute $500 annually, invest for 10 years, and expect an annual interest rate of 5%, the calculator will display the future value of your investment.

## Reverse Calculator

The reverse calculator helps you determine the monthly contribution needed to reach a desired final amount based on the initial amount and interest rate.

### How to Use

1. Open the [Future Value Calculator](https://githubnext.github.io/workspace-blank/) in your web browser.
2. Enter the desired final amount in the "Desired Final Amount" field.
3. Enter the initial amount in the "Initial Amount" field.
4. Enter the expected annual interest rate (in percentage) in the "Interest Rate (%)" field.
5. Click the "Calculate" button.
6. The monthly contribution needed to reach your desired final amount will be displayed below the button.

## Example

If you want to have a final amount of $10,000, start with an initial amount of $1,000, and expect an annual interest rate of 5%, the calculator will display the monthly contribution needed to reach your goal.

## GitHub Pages

You can access the Future Value Calculator on GitHub Pages [here](https://githubnext.github.io/workspace-blank/).

## Data Processing Script

A data processing script is provided to process data files and keep only location, year, and value. The script also calculates the mean for multiple data points per year and extrapolates missing data points for years 2000-2023.

### How to Use

1. Place your data files in the `data_files` directory.
2. Run the `data_processing.py` script.
3. The processed data files will be saved in the same directory with the prefix `processed_`.

## Example Data Format

The processed data files will have the following format:

```
location,year,value
Location1,2000,Value1
Location1,2001,Value2
...
Location1,2023,Value23
Location2,2000,Value1
Location2,2001,Value2
...
Location2,2023,Value23
```
