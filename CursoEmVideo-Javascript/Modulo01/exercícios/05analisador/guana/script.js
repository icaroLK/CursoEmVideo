var num = document.getElementById('txtn')
var msg = document.getElementById('msg')
var tab = document.getElementById('tab')
var but = document.getElementById('but')
var final = document.getElementById('final')
var qtd = 0
var menor = 0
var maior = 0
var tot = 0

function adicionar(){
    var n = Number(num.value)
    if(num.value.length == 0){
        window.alert('Digite dados válidos')
    } else {
        msg.style.display = 'none'
        tab.style.display = 'block'
        but.style.display = 'block'
    
        var item = document.createElement('option')
        item.text = `Valor ${n} adicionado`
        tab.appendChild(item)

        qtd ++
        if (qtd == 1){
            menor = n
            maior = n
        } else{

            if(n >= maior){
                maior = n
            }
            if(n <= menor){
                menor = n
            }
        }

        tot += n

    }
}

function finalizar(){
    final.innerHTML = `Ao todo temos ${qtd} números cadastrados. <br> O maior valor informado foi ${maior} <br> O menor valor informado foi ${menor}<br>Somando todos os valores temos ${tot}<br>A média dos valores é ${tot/qtd}`




}