function verif() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = window.document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || Number(fano.value) > ano) {
        window.alert('Tudo errado, digita certo ai')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')

        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade <=10){
                //kid
                res.innerHTML = 'KIIID'
            } else if (idade < 21){
                //jovem
                res.innerHTML = 'Jovenzada'
            } else if (idade < 60) {
                //adulto
                res.innerHTML = 'Adulto'
            } else {
                //idoso
                res.innerHTML = 'Idoso'
            }


        } else {
            genero = 'Mulher'
            if (idade >= 0 && idade <=10){
                //kid
                res.innerHTML = 'KIIID'
            } else if (idade < 21){
                //jovem
                res.innerHTML = 'Jovenzada'
            } else if (idade < 60) {
                //adulto
                res.innerHTML = 'Adulta'
            } else {
                //idoso
                res.innerHTML = 'Idosa'
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML += `Voce é ${genero} com ${idade} anos de idade`
        res.appendChild(img)



    }


    

}