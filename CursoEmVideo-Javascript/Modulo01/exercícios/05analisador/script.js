var num = document.getElementById('txtn')
var msg = document.getElementById('msg')
var tab = document.getElementById('tab')
var but = document.getElementById('but')
var final = document.getElementById('final')

var list = [0, 0, 0, 0]

// var qtd = 0
// var menor = 0
// var maior = 0
// var tot = 0

function isNumero(n){
    if(Number(n)> 1 && Number(n)<= 100){
        return true
    }else{
        return false
    }
}


function inLista(n, l){
    if (l.indexOf(Number(n)) != -1){
        return true
    }else {
        return false
    }
}







function adicionar(){
    var n = Number(num.value)
    if(num.value.length == 0 || isNumero(num.value) == false){
        window.alert('Valor inválido! Digite dados válidos')
    } else {
        msg.style.display = 'none'
        tab.style.display = 'block'
        but.style.display = 'block'
    
        var item = document.createElement('option')
        item.text = `Valor ${n} adicionado`
        tab.appendChild(item)

        // qtd ++
        list[0] ++
        if (list[0] == 1){
            list[1] = n
            list[2] = n
        } else{

            if(n >= list[1]){
                list[1] = n
            }
            if(n <= list[2]){
                list[2] = n
            }
        }

        list[3] += n

    }
    final.innerHTML = null
    num.value = null
    num.focus
}

function finalizar(){
    // final.innerHTML = `Ao todo temos ${list[0]} números cadastrados. <br> O maior valor informado foi ${list[1]} <br> O menor valor informado foi ${list[2]}<br>Somando todos os valores temos ${list[3]}<br>A média dos valores é ${list[3]/list[0]}`

    final.innerHTML = `Ao todo temos ${list[0]} números cadastrados.`
    final.innerHTML += `<p>O maior valor informado foi ${list[1]}.</p>`
    final.innerHTML += `<p>O menor valor informado foi ${list[2]}.</p>`
    final.innerHTML += `<p>Somando todos os valores temos ${list[3]}.</p>`
    final.innerHTML += `<p>A média dos valores é ${list[3]/list[0]}.</p>`



}