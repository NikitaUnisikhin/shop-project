import axios from "axios";
import AccountsService from "./AccountsService";
import Cookies from 'universal-cookie';

const cookies = new Cookies(null, { path: '/' });

let isRetryRefresh = false;

export const instance = axios.create({
    baseURL: "http://localhost:8000",
    withCredentials: true,
});

instance.interceptors.request.use((config) => {
    config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
    return config;
})

instance.interceptors.response.use((config) => {
    return config;
}, async (error) => {
    const originalRequest = error.config;
    if (
        error.response.status === 401 &&
        originalRequest &&
        !isRetryRefresh
    ) {
        isRetryRefresh = true;
        try {
            const response = await AccountsService.refresh(cookies.get("refresh"));
            localStorage.setItem("token", response.data['access']);
            return instance.request(originalRequest);
        } catch (e) {
            console.log('NO AUTH');
        }
    }
    throw error;
})