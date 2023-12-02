#funcao no R
source('https://git.io/JJ7jE')
avaliacao1(2149966) #coloque o RA nessa funcao.

# questao a

ggplot(Thales,aes(x=empresa)) +geom_bar() +labs(title='Quantidade de Empresas') + theme_bw()

# questao b

ggplot(Thales,aes(x=empresa, y=resistencia)) +geom_boxplot() +labs(title='Resistencia de Produto') + theme_bw()

# questao c

res_media=as.data.frame(tapply(Thales$resistencia,Thales$empresa,mean))
res_media$empresas=labels(res_media)[[1]]
names(res_media)[1]='media'
ggplot(res_media,aes(x=empresas))  +geom_bar(stat="identity",aes(y=media)) +labs(title='Resistencia Media por Empresa') + theme_bw()

# questao d

ggplot(Thales,aes(x=tempo,y=resistencia,col=empresa)) +geom_point() +labs(title='Resistencia x Tempo x Empresa') + theme_bw()

# questao e

ggplot(res_media,aes(area=media,fill=empresas)) +geom_treemap() +labs(title='Resistencia Media por Empresa (TreeMap)') + theme_bw()

# questao f

grafico=ggplot(Thales, aes(empresa,resistencia)) +geom_point() +labs(title = 'Tempo: {frame_time}', x = 'empresa', y = 'resistencia') + theme_bw() +transition_time(tempo)
animate(grafico, renderer = gifski_renderer())
