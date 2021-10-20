import React, { Component } from "react";
import { connect } from "react-redux";

import MyOrders from './components/my_orders/index'
import { clearUser, initAxios, getUser } from "./utils/auth_utils";
import { StylesProvider, createGenerateClassName } from '@material-ui/core/styles';


const generateClassName = createGenerateClassName({
  seed: 'products',
});

initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
    <StylesProvider generateClassName={generateClassName}>
        <div>
          <MyOrders />
        </div>
    </StylesProvider>

    );
  }

}
