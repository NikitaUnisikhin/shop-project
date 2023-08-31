import {AuthContext} from "../context/AuthContext";
import {useContext} from "react";
import {privateRoutes, publicRoutes} from "../router/routes";
import {Route} from "react-router-dom";

export const AppRouter = () => {
    const {isAuth} = useContext(AuthContext);

    return (
        isAuth
        ?
        <AppRouter>
            {privateRoutes.concat(publicRoutes).map(route => (
                <Route
                    path={route.path}
                    element={route.element}
                    key={route.path}
                    exact
                />
            ))}
        </AppRouter>
            :
        <AppRouter>
            {publicRoutes.map(route => (
                <Route
                    path={route.path}
                    element={route.element}
                    key={route.path}
                    exact
                />
            ))}
        </AppRouter>
    )
}