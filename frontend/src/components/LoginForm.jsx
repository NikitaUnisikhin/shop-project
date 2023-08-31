import React, {useState, useContext} from "react";
import AccountsService from "../API/AccountsService";
import {AuthContext} from '../context/AuthContext';

const LoginForm = () => {
    const [user, setUser] = useState({
        username: "",
        password: ""
    });

    const {setIsAuth} = useContext(AuthContext);

    const loginUser = async (e) => {
        e.preventDefault();
        setIsAuth(true);
        localStorage.setItem('isAuth', 'true');
        await AccountsService.login(user);
        setUser({username: "", password: ""});
    }

    return (
        <form className="login_form">
            <h1>Окно авторизации</h1>
            <input
                value={user.username}
                onChange={e => setUser({...user, username: e.target.value})}
                type="text" placeholder="Имя"
            /><br/>
            <input
                value={user.password}
                onChange={e => setUser({...user, password: e.target.value})}
                type="text" placeholder="Пароль"
            /><br/>
            <button onClick={loginUser}>Войти</button>
        </form>
    )
}

export default LoginForm;