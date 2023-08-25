import React, {useState} from "react";
import AccountsService from "../API/AccountsService";

const RegisterForm = () => {
    const [user, setUser] = useState({
        username: "",
        email: "",
        password1: "",
        password2: ""
    });

    const registerUser = async () => {
        await AccountsService.register(user);
    }

    return (
        <form className="register_form">
            <h1>Окно регистрации</h1>
            <input
                value={user.username}
                onChange={e => setUser({...user, username: e.target.value})}
                type="text"
                placeholder="Имя"
            /><br/>
            <input
                value={user.email}
                onChange={e => setUser({...user, email: e.target.value})}
                type="email"
                placeholder="Email"
            /><br/>
            <input
                value={user.password1}
                onChange={e => setUser({...user, password1: e.target.value})}
                type="text"
                placeholder="Пароль"
            /><br/>
            <input
                value={user.password2}
                onChange={e => setUser({...user, password2: e.target.value})}
                type="text"
                placeholder="Повтор пароля"
            /><br/>
            <button onClick={registerUser}>Зарегистрироваться</button>
        </form>
    )
}

export default RegisterForm;