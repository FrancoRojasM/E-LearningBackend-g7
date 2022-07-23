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
// indicamos que nuestro servidor podra aceptar y entender kla informacion enviada en formato JSON
servidor.use(express.json());
// lista de categorias
const categories=[{
    name: 'Zapatos',
    description:"Zapatos para hombres, mujeres niños y niñas"
},
];

servidor.get("/",(req,res)=>{
    res.status(200).json({
        message: "Bienvenido a mi primera API",
    });
});

servidor.get("/categories",(req,res)=>{
    return res.status(200).json({categories});
});

servidor.post("/categories",(req,res)=>{
    // declaro req.body = en una variable
    const category=req.body;

    // agreagra la nueva cateogría al listado de categorías
    categories.push(category);

    return res.status(201).json({
        message:"Category created succesfully",
        content:category,
    });
});

servidor.route('/categories/:id').get((req,res)=>{
    console.log(req.params);
    const {id}=req.params
// en base al id dado por la url buscar en la lista de categorias si existe, si no existe indicar en el message que la categoria no existe, caso contrario devolver la categoria, NOTA: usar la posicion de la lista como el ID
    
    console.log(categories[id]);
    if(categories[id]!==undefined){
        return res.json({
            message:"La categoria es",
            content:categories[id],
        });
    }else{
        return res.status(400).json({
            message:"La categoria no existe",
            content:null,
        });
    }
});

// callback =>    ()=>{}  => funcion anónima
servidor.listen(PORT,()=>{
    console.log(`servidor corriendo exitosamente en el puerto ${PORT}`);
});