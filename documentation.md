# Documentation- 

## Table of Contents 

|Description|Script|Functions| 
| ------------- | ------------- | ------------- | 
|Scrape a code script for documentation info|github_documentation\document_fxn.py|[scrape_documentation](#function-scrape_documentation)| 
|List scripts in repository and scrape documentation information.|github_documentation\document_fxn.py|[gather_scripts](#function-gather_scripts)| 
|Create Github documentation format for functions|github_documentation\document_fxn.py|[create_documentation](#function-create_documentation)| 
|Creates series of documentation for functions in a repository|github_documentation\document_fxn.py|[batch_documentation](#function-batch_documentation)| 
|brief description here (1 line)|github_documentation\document_fxn.py|[table_of_contents](#function-table_of_contents)| 
 

### End Table of Contents <br/> 
## Script: github_documentation\document_fxn.py 
 
### Function: scrape_documentation 

[Link to github_documentation\document_fxn.py Code](https://github.com/Codes-USCBiomechanicsLab/github_docu_base/blob/master/github_documentation/github_documentation\document_fxn.py) 

### **Description:** 

Scrape a code script for documentation info 

Scrape code for documentation information. Write that data into .csv file 
### Dependencies 

* pandas
* tkinter
 

### **Arguments:** 

#### *Inputs* 

* code_script: STR Code script with documentation info
* df_documentation: DF Dataframe containing documentation information


#### *Outputs* 

* df_documentation: DF Updated dataframe with additional docu information
 

### **Examples:** 

Helpful examples 

[Back to Table of Contents](#table-of-contents) 

## Script: github_documentation\document_fxn.py 
 
### Function: gather_scripts 

[Link to github_documentation\document_fxn.py Code](https://github.com/Codes-USCBiomechanicsLab/github_docu_base/blob/master/github_documentation/github_documentation\document_fxn.py) 

### **Description:** 

List scripts in repository and scrape documentation information. 

Create list of scripts in the repository that you will create documentation for, regenerate the table 
### Dependencies 

* os
* tkinter
* pandas
* glob
 

### **Arguments:** 

#### *Inputs* 

* extensions: TUPLE Specify the extensions to document in repo
* df_documentation: DF Table with the documentation information
* path: STR Path of the repository


#### *Outputs* 

* df_documentation: DF Updated documentation table
 

### **Examples:** 

Helpful examples 

[Back to Table of Contents](#table-of-contents) 
## Script: github_documentation\document_fxn.py 
 
### Function: create_documentation 

[Link to github_documentation\document_fxn.py Code](https://github.com/Codes-USCBiomechanicsLab/github_docu_base/blob/master/github_documentation/github_documentation\document_fxn.py) 

### **Description:** 

Create Github documentation format for functions 

Create Github documentation including inputs, outputs, dependencies, how to run the function etc. 
### Dependencies 

* inputs: LIST Input variable names and descriptions
* outputs: LIST Output variable names and descriptions
* Outputs
* docu_info: STR Documentation info, long string for a function
* Dependencies
 

### **Arguments:** 

#### *Inputs* 

* script_name: STR Name of the script containing the function
* function_name: STR Name of the specific function (module)
* script_website: STR Github website of the script
* describe_fxn: STR Description of the function
* depend_list: LIST Dependencies needed to run the function
* inputs: LIST Input variable names and descriptions
* outputs: LIST Output variable names and descriptions


#### *Outputs* 

* out
 

### **Examples:** 

Helpful examples 

[Back to Table of Contents](#table-of-contents) 
## Script: github_documentation\document_fxn.py 
 
### Function: batch_documentation 

[Link to github_documentation\document_fxn.py Code](https://github.com/Codes-USCBiomechanicsLab/github_docu_base/blob/master/github_documentation/github_documentation\document_fxn.py) 

### **Description:** 

Creates series of documentation for functions in a repository 

Creates series of documentation for functions in a repository 
### Dependencies 

* os
* create_documentation uscbrl labcodes
* table_of_contents uscbrl labcodes
 

### **Arguments:** 

#### *Inputs* 

* df_documentation: DF Table with documentation inforamtion


#### *Outputs* 

* documentation.md file added to the repository
 

### **Examples:** 

Helpful examples 

[Back to Table of Contents](#table-of-contents) 
## Script: github_documentation\document_fxn.py 
 
### Function: table_of_contents 

[Link to github_documentation\document_fxn.py Code](https://github.com/Codes-USCBiomechanicsLab/github_docu_base/blob/master/github_documentation/github_documentation\document_fxn.py) 

### **Description:** 

brief description here (1 line) 

Full description with details here 
### Dependencies 

 

### **Arguments:** 

#### *Inputs* 

* doc_csv_file: FILE csv file with documentation of functions


#### *Outputs* 

* tab_contents: STR Table of contents of functions in repository
 

### **Examples:** 

Helpful examples 

[Back to Table of Contents](#table-of-contents) 
