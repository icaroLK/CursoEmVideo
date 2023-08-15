var sen = document.getElementById('sen')

function entrou(){
    sen.innerHTML = 'SA74%jF33'
    
}

function saiu(){
    sen.innerHTML = '*********'

}


// -----------------------------

var olho = document.getElementById('olho')
var sen2 = document.getElementById('sen2')
var sen3 = document.getElementById('sen3')

var lig = false

function clicadas(){
    if(lig == false){
        lig = true
        sen2.innerHTML = '7@DRT534J'
        sen3.innerHTML = 'S24G75N@T'
        olho.innerHTML = '🕶'

    } else {
        lig = false
        sen2.innerHTML = '*********'
        sen3.innerHTML = '*********'
        olho.innerHTML = '👀'
    }

}