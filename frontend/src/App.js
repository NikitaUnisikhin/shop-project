import './styles/App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Home from './pages/Home'
import ProductCart from './pages/ProductCart';
import React from "react";
import Register from "./pages/Register";
import Login from "./pages/Login";
import ProfileCart from "./pages/ProfileCart";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route exact path="/home" element={<Home/>}/>
                <Route exact path="/products/:id" element={<ProductCart/>}/>
                <Route exact path="/register" element={<Register/>}/>
                <Route exact path="/login" element={<Login/>}/>
                <Route exact path="/profile" element={<ProfileCart/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
