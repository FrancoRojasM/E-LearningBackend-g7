// forma de usar las librerias usando ECMAScript
// Se agregó "type":"module"  en package.json
import express from "express";
import dotenv from "dotenv";
// forma de usar las librerias usando CommonJs
// const express= require("express");

// esto buscara el archivo .env t seteara las variables defiindas en ese archivo como variables de entorno
dotenv.config();

const servidor= express();
const PORT= process.env.PORT; // ESTE GENERALMENTE ES 3000 PERO puede ser cualquier valor

// callback =>    ()=>{}  => funcion anónima
servidor.listen(PORT,()=>{
    console.log(`servidor corriendo exitosamente en el puerto ${PORT}`);
});