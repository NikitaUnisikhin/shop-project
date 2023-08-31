import './styles/App.css';
import React from "react";
import {AuthContext} from "./context/AuthContext";
import {AppRouter} from './components/AppRouter'
import {BrowserRouter} from "react-router-dom";
import {useState, useEffect} from "react";

function App() {
    const [isAuth, setIsAuth] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('isAuth')) {
            setIsAuth(true)
        }
    }, [])


    return (
        <AuthContext.Provider value={{
            isAuth,
            setIsAuth
        }}>
            <BrowserRouter>
                <AppRouter/>
            </BrowserRouter>
        </AuthContext.Provider>
    );
}

export default App;
