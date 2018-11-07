import os
import pandas as pd

# Path to gdelt dataset
base_path = os.path.expanduser("~/Downloads/GDELT-ID/")

# List all file in directory
file_list = os.listdir(base_path)
file_list.sort()

# Create a variable to store all dataframe
df_list = []

# Check "ID0000.tsv" for dataframe header
if file_list[0] == "ID0000.tsv":
	# Create a header for other dataframe
	df1 = pd.read_csv(base_path + file_list[0], delimiter='\t', encoding="utf8")
	header = list(df1.columns.values)

	# Delete "ID0000.tsv" from file_list
	del(file_list[0])

	# Insert the first dataframe
	df_list.append(df1)

	for filename in file_list:
		# Check if the files are the targeted one or not
		if filename.endswith(".tsv"):
			# Insert all
			df_list.append(pd.read_csv(base_path + filename, delimiter='\t', 
										encoding="utf=8",
										header=None, names=header))

	# Join all dataframe
	df = pd.concat(df_list)

else:
	import sys
	sys.exit("Please check ID0000.tsv.")

###############################################################################
# Insert your code from here -------------------------------------------------#
###############################################################################

# Define target path
target_path = os.expanduser("~/")
target_filename = "%s.%s"

# Filter dataframe
df = df[(df['Year'] > 2012) & (df['Year'] < 2015)]

# Export dataframe
df.to_csv(target_path + target_filename, sep=",", encoding="utf-8")