import React, { Component } from "react";
import { connect } from "react-redux";

import MyOrders from './components/my_orders/index'
import { clearUser, initAxios, getUser } from "./utils/auth_utils";


initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
        <div>
          <MyOrders />
        </div>

    );
  }

}
