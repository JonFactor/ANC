import { Route, Redirect } from "react-router-dom"
import { useContext } from "react"
import AuthContext from "../context/AuthContext"

const PrivateRoute = ({ chidren, ...rest }) => {
    let { user } = useContext(AuthContext)
    return <Route {...rest}>{!user ? <Redirect to="/login" /> : chidren}</Route>
}

export default PrivateRoute