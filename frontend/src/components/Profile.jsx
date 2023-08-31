import React, {useContext, useEffect, useState} from 'react';
import AccountsService from "../API/AccountsService";
import {AuthContext} from '../context/AuthContext';

const Profile = () => {
    const [user, setUser] = useState({
        username: "",
        email: ""
    });

    const {setIsAuth} = useContext(AuthContext);

    useEffect(() => {
        async function fetchProfile() {
            const user = await AccountsService.profile();
            setUser(user.data);
        }
        fetchProfile();
    }, []);

    const logout = async (e) => {
        e.preventDefault();
        setIsAuth(false);
        localStorage.removeItem('isAuth');
        await AccountsService.logout();
    }

    return (
        <div className="profile">
            <div>
                <div>Имя: {user.username}</div>
                <div>Email: {user.email}</div>
                <button onClick={logout}>Выйти из профиля</button>
            </div>
        </div>
    )
}

export default Profile;