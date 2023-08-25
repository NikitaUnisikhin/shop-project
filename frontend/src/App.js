import './styles/App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home'
import ProductCart from './pages/ProductCart';
import React from "react";
import Register from "./pages/Register";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/home" element={<Home/>}/>
                <Route path="/products/:id" element={<ProductCart/>}/>
                <Route path="/register" element={<Register/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
