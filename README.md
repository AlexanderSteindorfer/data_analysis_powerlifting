## Data analysis in Python: Open Powerlifting database

by Alexander Steindorfer
<br/><br/>

**Data source**: https://www.openpowerlifting.org/<br> 
Download from: https://openpowerlifting.gitlab.io/opl-csv/bulk-csv.html<br>
On Kaggle (data until 2019): https://www.kaggle.com/datasets/open-powerlifting/powerlifting-database

*All measurements of weight are using the unit kilograms (kg).*<br>
*Please note that this dataset is not static. At the time you will use it, it will include
more data. The results of the analysis may therefore differ, especially in outliers.*
<br/><br/>

### **Format**<br>
This data analysis comes as a **Jupyter Notebook** as well as split up into **Python files**, in which it was originally conducted. All visualisations are included in a seperate folder.<br>
In order to keep the Jupyter Notebook as clear as possible, the Python files include more detailed comments on the code. I therefore recommend consulting them in case any ambiguities should arise.<br>
Please note that due to the different natures of the formats, the variable names do sometimes differ between Jupyter Notebook and Python files. The main reason for this is that each of the Python files reads in the database, while in the Jupyter Notebook it is read only at the beginning and copies are used further on. 
<br/><br/>

### **Contents of the analysis**<br>
**1.1** Development of the numbers of male and female participants in Powerlifting competitions through time (absolute).<br>
**1.2** Development of the numbers of male and female participants in Powerlifting competitions through time (relative).<br>
**2.1** Analysis of the age of the participants in Powerlifting competitions.<br>
**2.2** Correlation of the age of participants with the total weight lifted in Powerlifting competitions.<br>
**3.1** Analysis of correlation of bodyweight with the total weight lifted in Powerlifting competitions.<br>
**3.2** Analysis of correlation of the three exercises with the total weight lifted in Powerlifting competitions.<br>
**4.1** Development of the average total weight lifted by participants in Powerlifting competitions through time.
<br/><br/>

### **Goals of this project**<br>
With this analysis I want to provide calculations and visualisations of important "demographic" developments in the sport. Furthermore, I want to show that many notions about the sport can actually be proven with statistical methods.
It is not so much about finding new correlations and uncovering developments as it is about investigating what is already known.
<br/><br/>

### **What I have learned while working on this project**<br>
This is my first data project and I fully understand now why it is so crucial to practically use the skills learned in courses. I will list only the most important insights:<br>
* Adapting common methods to a specific dataset.
* When to drop duplicates and null values (whether to use it on the full dataset, or a subset).
* Creating a percentage column for a grouped DataFrame.
* Plotting columns of a grouped DataFrame with Matplotlib, using a loop.
* Identifying and filtering out outliers with scatter plots and estimations.
<br/><br/>

### **A brief introduction to Powerlifting**<br>
In order to make this analysis easily understandable for the reader, I will give a very short overview of the sport. As I do the sport myself, the analysis is build on prior knowledge and personal experience, which proved to be fundamental.<br>
Powerlifting is weight training. It seeks to maximise the strength of an athlete, especially in the three exercises ***squat, bench press and deadlift***.<br>
In a Powerlifting competition, an athlete has several attempts at each of these exercises. The best attempt counts. *The so called ***"total"*** is the sum of the best attempts in all three exercises combined*.