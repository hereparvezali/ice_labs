
sex <-c("Male","Male","Female","Female","Female","Female","Male","Female","Female","Female","Female","Male","Male","Female","Female","Male","Female","Male","Male","Female")
religion<-c("Muslim","Hindu","Muslim","Muslim","Buddhist","Muslim","Muslim","Hindu","Muslim","Muslim","Hindu","Muslim","Muslim","Muslim","Muslim","Muslim","Muslim","Hindu","Muslim","Muslim")
edu<-c("BTech","BEng","MSc","BSc","Hons","Primary","Primary","Primary","HSC","HSC","HSC","HSC","SSC","SSC","SSC","SSC","SSC","SSC","SSC","SSC")
blood<-c("A","A","A","A","A","B","B","B","B","B","B","B","B","B","O","O","O","AB","AB","AB")

sex_frequency<-table(sex)
rel_frequency<-table(religion)
edu_frequency<-table(edu)
blood_frequency<-table(blood)

####### I ########
# Frequency distributions for the variables Sex, Religion, Fathers level of Education and Blood group
data.frame(sex_frequency)
data.frame(rel_frequency)
data.frame(edu_frequency)
data.frame(blood_frequency)

####### II ########
# Pie diagram for the variable sex and religion
pie(sex_frequency,main = "Pie chart for Sex",col = c("red","green"))
pie(rel_frequency, main = "Pie chart for religions",col = c("red","green","yellow"))

####### III ###########
# Bar diagram for the level of education and blood
barplot(edu_frequency,main = "Father's level of Education", xlab = "Degree",ylab = "Number of Fathers",col = c("red","green","yellow","black","gray","green","red","yellow"))
barplot(blood_frequency,main = "Blood Distribution of Students",xlab = "Blood Groups",ylab = "Number of Students", col = c("red","green","yellow","black"))
