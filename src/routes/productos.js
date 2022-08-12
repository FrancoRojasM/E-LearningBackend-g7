import { Router } from "express";
import { actualizarProducto, crearProducto, eliminarProducto, listarProductos } from "../controllers/productos.js";

export const productoRouter=Router();

productoRouter.route("/producto").post(crearProducto).get(listarProductos);
productoRouter.route("/producto/:id").put(actualizarProducto).delete(eliminarProducto);