import { ChakraProvider } from "@chakra-ui/react";
import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { BrowserRouter as Router } from "react-router-dom";
import App from "./components/App";
import { store } from "./store";
import theme from "./theme";

ReactDOM.render(
  <React.StrictMode>
    <Provider {...{ store }}>
      <Router>
        <ChakraProvider {...{ theme }}>
          <App />
        </ChakraProvider>
      </Router>
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);
