import React, { Suspense } from 'react';
import ReactDOM from 'react-dom';
import { ConnectedRouter } from "connected-react-router";
import { Provider } from "react-redux";

import configureStore, { history } from "./stores/index";
import './i18n/index'
import 'antd/dist/antd.css';

import App from "./App";




const store = configureStore();
window.dispatch = store.dispatch;


if (document.getElementById('single_product')) {
  ReactDOM.render(
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <Suspense fallback={null}>
          <App />
        </Suspense>
      </ConnectedRouter>
    </Provider>,

    document.getElementById("single_product")
  );
}

