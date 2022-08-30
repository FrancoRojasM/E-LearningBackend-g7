import {usuarioModel} from '../models/usuarios.js';
import { direccionRequesDTO } from '../dtos/direcciones.js';

export const crearDireccion= async(req,res)=>{
    try {
        console.log(req.user);
        const data=direccionRequesDTO(req.body);
        req.user.direcciones.push(data)
        await req.user.save() //sirve para guardar los cambio realizados de una instancia de cualquier coleccion de la BD
        return res.status(201).json({
            message:'Direccion agregada exitosamente',
            result: req.user.direcciones,
        })
    } catch (error) {
        return res.status(400).json({
            message:error.message,
            result:null,
        });
    }
}

export const listarDirecciones=async(req,res)=>{
    return res.json({
        message:null,
        result:req.user.direcciones,        
    })
}