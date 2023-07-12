my_ln<-function(x,u){
    #u: umbral
    y<-ifelse(x<u,u,x)
    return(log(y))
  }
  
  #Definicipon de nuevo exp
  my_exp<-function(x,u){
    #u: umbral
    y<-ifelse(x>=(-u) & x<u, x, ifelse(x<(-u),-u,u))
    return(exp(y))
  }