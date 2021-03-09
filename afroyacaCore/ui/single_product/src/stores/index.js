import { combineReducers } from "redux";
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";

// Stores in app
import { connectRouter } from "connected-react-router";
import { createBrowserHistory } from "history";
import { routerMiddleware } from "connected-react-router";
import { reducer as formReducer } from "redux-form";
import { singleProductCStore } from '../components/single_product/store'


export const history = createBrowserHistory();

const cstore = history =>
  combineReducers({
    router: connectRouter(history),
    form: formReducer,

    singleProductCStore: singleProductCStore,
  });

export default function configureStore(preloadedState) {
  const store = createStore(
    cstore(history), // root reducer with router state
    preloadedState,
    compose(
      applyMiddleware(
        routerMiddleware(history), // for dispatching history actions
        thunk
        // ... other middlewares ...
      )
    )
  );

  return store;
}
