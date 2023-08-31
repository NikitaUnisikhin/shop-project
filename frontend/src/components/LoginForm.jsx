import React, {useState} from "react";
import AccountsService from "../API/AccountsService";

const LoginForm = () => {
    const [user, setUser] = useState({
        username: "",
        password: ""
    });

    const loginUser = async (e) => {
        e.preventDefault();
        let response = await AccountsService.login(user);
        console.log(1);
        if (response.status === 200) {
            console.log(2);
            localStorage.setItem('isAuth', 'true');
        }
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