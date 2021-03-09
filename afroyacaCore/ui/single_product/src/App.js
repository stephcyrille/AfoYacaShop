import React, { Component } from "react";
import { connect } from "react-redux";

import SingleProduct from './components/single_product/index'
import { clearUser, initAxios, getUser } from "./utils/auth_utils";


initAxios()
export default
@connect((state, props) => ({
}))
class App extends Component {

  render() {

    return (
        <div>
          <SingleProduct />
        </div>

    );
  }

}
