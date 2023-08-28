import { instance } from "./instance";
import Cookies from 'universal-cookie';

const cookies = new Cookies(null, { path: '/' });

export default class AccountsService {
    static async register(user) {
        await instance.post('/api/accounts/register/', user);
    }

    static async login(user) {
        let response = await instance.post('/api/token/', user);
        localStorage.setItem("token", response.data['access']);
        cookies.set("refresh", response.data['refresh'])
    }

    static async refresh() {
        return await instance.post('/api/token/refresh/', {
            "refresh": cookies.get("refresh")
        });
    }

    static async profile() {
        return await instance.get('/api/accounts/profile/');
    }
}