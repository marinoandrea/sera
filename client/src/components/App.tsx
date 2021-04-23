import React from "react";
import { Route, Switch } from "react-router-dom";
import useStateSelector from "../utils/useStateSelector";
import Feed from "./Feed";
import Login from "./Login";
import Registration from "./Registration";

function App() {
  const { isAuthenticated } = useStateSelector((state) => state.auth);
  return (
    <>
      {isAuthenticated ? (
        <Switch>
          <Route path='/' component={Feed} />
        </Switch>
      ) : (
        <Switch>
          <Route path='/login' component={Login} />
          <Route path='/registration' component={Registration} />
          <Route path='/' component={Login} />
        </Switch>
      )}
    </>
  );
}

export default App;
