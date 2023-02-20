# Network-Science
For lab 2: 
1. Firstly upload whichever dataset you want from Data folder.
2. Uncomment the line reading that dataset in the code and uncomment the line about positioning of the same dataset. e.g.: for GrQc, uncomment the following lines:
GrQc = nx.read_edgelist("/content/CA-GrQc.txt", create_using=nx.Graph())
pos_GrQc = nx.spring_layout(GrQc, seed=23)
3. After doing so, copy the path of the dataset you want to work with and paste it in quotation marks. I use GoogleColab so my file paths look like /content/... but if you don't use GoogleColab, the code should work fine but the file path would be different. 
4. After loading dataset, go to the section addressing the dataset. There is one section for each dataset and by running that section you should get the same figures and result as I did. For some datasets it might take a few minutes to get output.
NOTE 1: the youtube dataset takes long so to check the results you could check them without youtube dataset.
NOTE 2: it seems that gpmetis and mlrmcl have problems in their results.