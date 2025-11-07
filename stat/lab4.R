stu1<-c(2.5,2.5,3.0,3.5,3.5,4.0,3.5,3.5)
stu2<-c(2.5,3.0,4.0,4.0,4.0,2.0,2.5,4.0)

###### Average #######

stu1_avg<-mean(stu1)
stu2_avg<-mean(stu2)

stu1_avg    #3.25
stu2_avg    #3.25

## as their mean is equal then we should consider their coefficient of variance to compare results

stu1_coefvar<-sd(stu1)/mean(stu1)
stu2_coefvar<-sd(stu2)/mean(stu2)
stu1_coefvar    #0.1644
stu2_coefvar    #0.2600
## as the coefficient of variance is lesser of student 1 so the student one is better in this case
