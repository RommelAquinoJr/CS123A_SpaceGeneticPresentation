# CS123A_SpaceGeneticPresentation
### Description
The purpose of this code is to analyze the RNA Contamination levels from plants and rodents once they enter outerspace. This is important in understanding the effects of outerspace on living specimens.

### Data Sources
Data was collected from the website https://osdr.nasa.gov/bio/repo/search?q=&data_source=cgene,alsda&data_type=study

### Project Structure
* Code Files
  * PlantData.py
  * RodentData.py

* Data Text Files  
  * s_OSD-467.txt
  * s_OSD-770.txt
* README File
  * README.md

### How to run program
1. Download all files from git repo.
2. Save them into your workspace
3. make sure you have python and pip installed    
   * open terminal and type the following  
```
python3 --version
```

Install pip
```
python3 -m ensurepip --upgrade
```

4. make sure you have pandas installed
   * open terminal and type the following  
     
Option 1
```
pip install pandas
```  
Option 2 (For Python 3 or higher)
```
!pip install pandas
```   
Option 3 ('pip' is not recognized error)
```
python -m pip install pandas
```
Option 4 (Jupyter Notebook)
```
conda install pandas
```
4. run the following line in the terminal  

For PlantData.py
```
python3 PlantData.py
```

For RodentData.py
```
python3 RodentData.py
```