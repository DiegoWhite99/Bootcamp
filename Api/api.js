/*fetch('https://randomuser.me/api/?results=5',{

})

.then(respuesta =>respuesta.json())
.then(data =>{
    console.log(data)
    let contenedorApi=document.getElementById("contenedorjson")
    
    
})
*/

fetch('https://pokeapi.co/api/v2/pokemon/', {

})
  .then(respuesta => respuesta.json())
  .then(data => {
    console.log(data);
    let contenedorApi = document.getElementById("contenedorjson");

    if (contenedorApi) {
        for (let pokemon of data.results) {
            contenedorApi.innerHTML += `<div id=pokemon>${pokemon.name} </div> <div id=d1> ${pokemon.url} </div>`


        }
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });