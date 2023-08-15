var h = new Date()
var m = new Date()

var hora = h.getHours()
var min = m.getMinutes()

console.log(`Agora são ${hora}:${min}`)
if (hora < 12) {
    console.log('Bom dia')
}else if (hora > 12 && hora < 18) {
    console.log('Boa tarde')
} else {
    console.log('Boa noite')
}
