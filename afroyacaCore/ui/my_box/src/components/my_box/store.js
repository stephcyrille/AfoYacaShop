import { createAction, createReducer } from "redux-act";

const initialState = {
	initial_values:{},
  box: [],
  loading: false,
};

const actions = { name: "myBoxCStoreActions" };
const store = createReducer({}, initialState); // stores are called reducers


actions.setInitialValues = createAction("MYBOX__SET_INITIAL_VALUES");
store.on(actions.setInitialValues, (state, value) => ({
	...state,
	initial_values: value
}));

actions.setBox = createAction("MYBOX__SET_ORDERS");
store.on(actions.setBox, (state, value) => ({
  ...state, box: value
}));

actions.setLoading = createAction("MYBOX__SET_LOADING");
store.on(actions.setLoading, (state, value) => ({
  ...state, loading: value
}));

export { store as myBoxCStore, actions as myBoxCStoreActions };
