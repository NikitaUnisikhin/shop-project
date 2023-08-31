import {Route, Routes} from "react-router-dom";
import React from "react";
import {privateRoutes, publicRoutes} from "../router/routes";

export const AppRouter = () => {
    const isAuth = localStorage.getItem('isAuth');

    console.log(isAuth);

    let routes;
    if (isAuth) {
        routes = publicRoutes.concat(privateRoutes);
    } else {
        routes = publicRoutes;
    }

    return (
        <Routes>
            {routes.map(route => (
                <Route
                    path={route.path}
                    element={route.element}
                    key={route.path}
                    exact
                />
            ))}
        </Routes>
    )
}
