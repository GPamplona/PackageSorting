# PackageSorting
A Python function to sort packages based on size and mass</br>

The packages are sorted using using the following criteria:</br>

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.</br>
- A package is **heavy** when its mass is greater or equal to 20 kg.</br>

The method will dispatch the packages in the following stacks:</br>

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.</br>
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.</br>
- **REJECTED**: packages that are **both** heavy and bulky are rejected.</br>
- **ERROR**: there was an error with the input parameter values.</br>

## Running the code

1. Get the Python file from the GitHub repository: https://github.com/GPamplona/PackageSorting<br/>
2. Open your terminal:<br/>
   - On Windows, use Command Prompt or PowerShell.<br/>
   - On macOS or Linux, use the Terminal application.<br/>
3. Navigate to the script's directory:<br/>
   - Use the cd command to change the directory to where your sorter.py file is located.<br/>
   - For example: cd path/to/your/directory<br/>
4. Run the sort method:<br/>
   - Run the following command in the terminal using actual values for the four parameters (width, height, length, mass).<br/>
    ```python -c "from sorter import sort; print(sort(<width>, <height>, <length>, <mass>))"```<br/>
     (units are centimeters for the dimensions and kilogram for the mass). The function returns a string: the name of the stack where the package should go.</BR>
   - If you have multiple Python versions use python3 instead of python.<br/>
   - This will execute the script, including the code that calls your method.<br/>

## Sample Runs

```
python -c "from sorter import sort; print(sort(50, 50, 50, 50))"      # Results = "STANDARD"
python -c "from sorter import sort; print(sort(200, 50, 50, 50))"     # Results = "SPECIAL"
python -c "from sorter import sort; print(sort(50, 200, 50, 50))"     # Results = "SPECIAL"
python -c "from sorter import sort; print(sort(50, 50, 200, 50))"     # Results = "SPECIAL"
python -c "from sorter import sort; print(sort(50, 50, 50, 200))"     # Results = "SPECIAL"
python -c "from sorter import sort; print(sort(200, 50, 50, 200))"    # Results = "REJECTED"
python -c "from sorter import sort; print(sort(0, 0, 0, 0))"          # Results = "ERROR"
python -c "from sorter import sort; print(sort("a", "b", "c", "d"))"  # Results = "ERROR"
python -c "from sorter import sort; print(sort(-50, 50, 50, 50))"     # Results = "ERROR"
```
