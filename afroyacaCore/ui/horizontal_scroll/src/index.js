import React, { Suspense } from 'react';
import ReactDOM from 'react-dom';
import { ConnectedRouter } from "connected-react-router";
import { Provider } from "react-redux";

import configureStore, { history } from "./stores/index";

import App from "./App";




const store = configureStore();
window.dispatch = store.dispatch;


if (document.getElementById('horizontal_scroll')) {
  ReactDOM.render(
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <Suspense fallback={null}>
          <App />
        </Suspense>
      </ConnectedRouter>
    </Provider>,

    document.getElementById("horizontal_scroll")
  );
}

