let amigo = {nome:'Ícaro',
            sexo:'M',
            peso:80,
            engordar(p){
                console.log('Engordou')
                this.peso += p
            }
}

console.log(`${amigo.nome} pesa ${amigo.peso}kg`)
amigo.engordar(2)
console.log(`${amigo.nome} pesa ${amigo.peso}kg`)