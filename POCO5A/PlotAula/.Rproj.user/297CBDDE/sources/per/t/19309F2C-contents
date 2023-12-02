data=read.csv('dados_plot.csv')

head(data)

table(data$company)

# Questao a
ggplot(data,aes(x=company)) +geom_bar() +labs(title='Quantidade de Empresas') + theme_bw()

#questao b

ggplot(data,aes(x=company, y=yield)) +geom_boxplot() +theme_bw()

#questao c

res_mean=as.data.frame(tapply(data$yield,data$company,mean))
res_mean$companys=labels(res_mean)[[1]]
names(res_mean)[1]='mean'
ggplot(res_mean,aes(x=companys))  +geom_bar(stat="identity",aes(y=mean)) +labs(title='Resistencia Media por Empresa')

#questao d

ggplot(data,aes(x=yield)) +geom_histogram()

install.packages('devtools')
install.packages('gifski')
install.packages('png')
