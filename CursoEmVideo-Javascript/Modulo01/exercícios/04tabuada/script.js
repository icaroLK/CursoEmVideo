function gerar(){
    var num = document.getElementById('txtnum')
    var tab = document.getElementById('seltab')
    var res = document.getElementById('res')


    if (num.value.length == 0){
        window.alert('Digite um número')
    } else{
        var n = Number(num.value)

        // res.innerHTML = null
        tab.innerHTML = null

        
        tab.style.display = 'block'
        

        for(var c=1; c<=100; c++){
        // res.innerHTML += `${num} x ${c} = ${num*c}<br>`
        var item = document.createElement('option')
        item.text = `${n} x ${c} = ${n*c}`
        tab.appendChild(item)
       }


    }


}