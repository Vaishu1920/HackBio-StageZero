# pandas library was imported
import pandas as pd

# Separate list was created for each piece of information
Names= ["Poornavaishnavi Chekuri","Hasiba asma","Abane Louis Ashu","Aaronie Jersha Jenyfred"]
Slack_username = ["Vaishnavi","Hasiba asma","Louis","Jersha Jenyfred"]
Country = ["USA","Pakistan","Cameroon","USA" ]
Hobby = ["Knowledge Hunter","Exploring AI","Investing","Bookreading"]
Affiliations= ["UHCL","Sepal AI","ULB","Northeastern"]
DNA_sequence= ["AGTCTCGAATACAACTTGTT","ATCATTTTTCTTCTCCGGCC","GGACTCGCGCTCGCCCGCTG","GGGGCCGGAAGTGCCGCTCC"]

# combining all lists into dictionary and keys as the column names
data = {
    "Name": Names,
    "Slack Username": Slack_username,
    "Country": Country,
    "Hobby": Hobby,
    "Affiliation": Affiliations,
    "Favorite Gene Sequence": DNA_sequence
}

# creating a pandas data frame from dictionary and printing it
team_df = pd.DataFrame(data)
print(team_df)

# Save to Excel without index
team_df.to_excel("team_info.xlsx", index=False)