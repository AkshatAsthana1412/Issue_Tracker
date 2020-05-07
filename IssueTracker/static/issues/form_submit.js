
console.log('script loaded')

close_btns = document.querySelectorAll('.close-button')
// console.log(`anchor selected ${close_btn}`)
for(var i = 0; i < close_btns.length; i++){
  close_btns[i].addEventListener('click', function(){
    console.log('button located')
    close_btns[i].style.class = 'btn btn-success'
    close_btns[i].innerText = 'Closed!'
  })
}
