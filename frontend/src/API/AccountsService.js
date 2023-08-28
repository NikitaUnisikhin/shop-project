import { instance } from "./instance";

export default class AccountsService {
    static async register(user) {
        await instance.post('/api/accounts/register/', user);
    }

    static async login(user) {
        let response = await instance.post('/api/token/', user);
        localStorage.setItem("token", response.data['access']);
    }

    static async profile() {
        return await instance.get('/api/accounts/profile/');
    }
}