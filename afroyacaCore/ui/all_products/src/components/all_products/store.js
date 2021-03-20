import { createAction, createReducer } from "redux-act";

const initialState = {
	initial_values:{},
    products: [],
    filtered_products: [],
    loading: false,
    filter: false
};

const actions = { name: "allProductsCStoreActions" };
const store = createReducer({}, initialState); // stores are called reducers


actions.setInitialValues = createAction("ALL_PRODUCTS__SET_INITIAL_VALUES");
store.on(actions.setInitialValues, (state, value) => ({
	...state,
	initial_values: value
}));

actions.setProducts = createAction("ALL_PRODUCTS__SET_PRODUCTS");
store.on(actions.setProducts, (state, value) => ({
  ...state, products: value
}));

actions.setLoading = createAction("ALL_PRODUCTS__SET_LOADING");
store.on(actions.setLoading, (state, value) => ({
  ...state, loading: value
}));

actions.unSetFilter = createAction("ALL_PRODUCTS__UNSET_FILTER");
store.on(actions.unSetFilter, (state) => ({
  ...state, filter: false
}));

actions.setFilter = createAction("ALL_PRODUCTS__SET_FILTER");
store.on(actions.setFilter, (state, value) => ({
  ...state, filter: true, filtered_products: value
}));

export { store as allProductsCStore, actions as allProductsCStoreActions };
