const RUTABACK='http://127.0.0.1:5000'
fetch(RUTABACK+'/estado',{method: 'GET'}).then((respuesta)=>{
    return respuesta.json();
})
.then((data)=>{
    console.log(data);
})
.catch((error)=>{
    console.error(error);
})


fetch(RUTABACK + "/producto", {
    method: "POST",
    body: JSON.stringify({
      nombre: "Zanahoria",
      precio: 4.5,
    }),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((respuesta) => {
      return respuesta.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(error);
    });

    // hacer un button que cuando se haga click se mande a llamar el endpoint para devolver-productos