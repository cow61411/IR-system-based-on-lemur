from nltk.corpus import stopwords
stop = stopwords.words('english')

parameter = open("stopword_parameter" , "w")

for word in stop:
	parameter.write("		<word>" + word + "</word>\n")


