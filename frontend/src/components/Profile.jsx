import React, {useEffect, useState} from 'react';
import AccountsService from "../API/AccountsService";

const Profile = () => {
    const [user, setUser] = useState({
        username: "",
        email: ""
    });

    useEffect(() => {
        async function fetchProfile() {
            const user = await AccountsService.profile();
            setUser(user.data);
        }
        fetchProfile();
    }, []);

    const logout = async (e) => {
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